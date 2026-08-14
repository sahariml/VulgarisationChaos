"""
جاذب هينون (Henon Attractor)
=============================
يولّد هذا البرنامج جاذب هينون للقيم الكلاسيكية a=1.4 و b=0.3،
ثم يرسم:
  1) الجاذب كاملاً
  2) تكبيراً متتالياً (Zoom) على منطقة صغيرة منه لإظهار الطبقات
     الدقيقة المتكررة (البنية شبه المتشابهة ذاتياً - self-similar)

نظام هينون:
    x_{n+1} = 1 - a * x_n^2 + y_n
    y_{n+1} = b * x_n
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import arabic_reshaper
from bidi.algorithm import get_display

# ---------------------------------------------------------------
# 0) دعم عرض النص العربي بشكل صحيح داخل matplotlib
#    (تشكيل الحروف المتصلة + ترتيب الاتجاه من اليمين لليسار)
# ---------------------------------------------------------------
def ar(text):
    """يهيئ نصاً عربياً ليُعرض بشكل صحيح (متصل ومن اليمين لليسار) في matplotlib."""
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)


def _find_arabic_font():
    """
    يبحث عن خط يدعم العربية بعدة طرق متتالية حتى يعمل البرنامج
    على أي جهاز، بغض النظر عن الخطوط المثبتة فيه:
      1) ملف الخط المرفق مع هذا السكربت (fonts/Amiri-Regular.ttf)
      2) أي خط اسمه يحتوي على Amiri/Scheherazade/Arabic/Noto Naskh
         من بين الخطوط المثبتة على النظام
      3) في حال الفشل: يعود إلى الخط الافتراضي مع تحذير (سيظهر
         النص العربي بشكل غير متصل الحروف لكن البرنامج لن يتعطل)
    """
    # 1) الخط المرفق محلياً بجانب هذا الملف
    here = os.path.dirname(os.path.abspath(__file__))
    bundled = os.path.join(here, "fonts", "Amiri-Regular.ttf")
    if os.path.isfile(bundled):
        return fm.FontProperties(fname=bundled)

    # 2) البحث بين خطوط النظام المثبتة (نتجنب الخطوط الخاصة مثل نسخ
    #    القرآن الملونة التي لا تحتوي كل الحروف، ونفضل الخط العادي)
    candidates = ["amiri", "scheherazade", "noto naskh arabic",
                  "noto sans arabic", "traditional arabic", "tahoma", "arial"]
    avoid_words = ["quran", "colored", "bold", "italic"]
    for c in candidates:
        matches = [
            f for f in fm.fontManager.ttflist
            if c in f.name.lower()
            and not any(w in f.name.lower() for w in avoid_words)
        ]
        if matches:
            return fm.FontProperties(fname=matches[0].fname)

    # 3) لا يوجد خط عربي متاح
    print(
        "تحذير: لم يُعثر على خط يدعم العربية على هذا الجهاز.\n"
        "لعرض النصوص العربية بشكل صحيح، ثبّت خط Amiri مثلاً "
        "(https://github.com/aliftype/amiri/releases) وضع ملف\n"
        "Amiri-Regular.ttf في مجلد 'fonts' بجانب هذا السكربت،\n"
        "أو ثبّته على مستوى النظام."
    )
    return None


ARABIC_FONT = _find_arabic_font()

# ---------------------------------------------------------------
# 1) توليد المسار (Trajectory)
# ---------------------------------------------------------------
def henon_trajectory(a=1.4, b=0.3, n_iter=200_000, n_transient=1_000,
                      x0=0.0, y0=0.0):
    """
    يُرجع مصفوفتي x و y لجاذب هينون بعد إسقاط الفترة العابرة
    (transient) الأولى حتى يستقر المسار على الجاذب نفسه.
    """
    x, y = x0, y0
    xs = np.empty(n_iter)
    ys = np.empty(n_iter)

    # الفترة العابرة: نكرر الخريطة دون تسجيل النتائج
    for _ in range(n_transient):
        x, y = 1.0 - a * x**2 + y, b * x

    # الآن نسجل النقاط التي تنتمي فعلاً إلى الجاذب
    for i in range(n_iter):
        x, y = 1.0 - a * x**2 + y, b * x
        xs[i] = x
        ys[i] = y

    return xs, ys


# ---------------------------------------------------------------
# 2) الرسم: الجاذب الكامل + تكبيرات متتالية
# ---------------------------------------------------------------
def plot_henon_with_zoom(a=1.4, b=0.3, n_iter=200_000):
    xs, ys = henon_trajectory(a=a, b=b, n_iter=n_iter)

    fig = plt.figure(figsize=(13, 9))

    # --- (أ) الجاذب كاملاً ---------------------------------------------
    ax1 = fig.add_subplot(2, 2, (1, 3))  # عمود أيسر كامل الارتفاع
    ax1.scatter(xs, ys, s=0.15, c="darkblue", alpha=0.6, linewidths=0)
    ax1.set_title(ar(f"جاذب هينون الكامل  (a={a}, b={b})"),
                  fontsize=12, fontproperties=ARABIC_FONT)
    ax1.set_xlabel("$x_n$")
    ax1.set_ylabel("$y_n$")
    ax1.set_aspect("equal", adjustable="datalim")

    # نحدد إطار التكبير الأول على الجاذب (منطقة صغيرة قرب الطرف الأيمن)
    zoom1_xlim = (0.55, 0.75)
    zoom1_ylim = (0.16, 0.22)
    _draw_zoom_box(ax1, zoom1_xlim, zoom1_ylim, color="crimson")

    # --- (ب) التكبير الأول -----------------------------------------------
    ax2 = fig.add_subplot(2, 2, 2)
    mask1 = (
        (xs >= zoom1_xlim[0]) & (xs <= zoom1_xlim[1]) &
        (ys >= zoom1_ylim[0]) & (ys <= zoom1_ylim[1])
    )
    ax2.scatter(xs[mask1], ys[mask1], s=0.6, c="crimson", alpha=0.7,
                linewidths=0)
    ax2.set_xlim(zoom1_xlim)
    ax2.set_ylim(zoom1_ylim)
    ax2.set_title(ar("تكبير 1: تظهر عدة \"خيوط\" متوازية"),
                  fontsize=11, fontproperties=ARABIC_FONT)
    for spine in ax2.spines.values():
        spine.set_edgecolor("crimson")
        spine.set_linewidth(1.5)

    # نحدد إطار تكبير ثانٍ داخل التكبير الأول (تكبير على أحد الخيوط)
    zoom2_xlim = (0.60, 0.66)
    zoom2_ylim = (0.180, 0.196)
    _draw_zoom_box(ax2, zoom2_xlim, zoom2_ylim, color="darkorange")

    # --- (ج) التكبير الثاني (داخل الأول): تظهر طبقات أدق ------------------
    ax3 = fig.add_subplot(2, 2, 4)
    mask2 = (
        (xs >= zoom2_xlim[0]) & (xs <= zoom2_xlim[1]) &
        (ys >= zoom2_ylim[0]) & (ys <= zoom2_ylim[1])
    )
    ax3.scatter(xs[mask2], ys[mask2], s=1.2, c="darkorange", alpha=0.8,
                linewidths=0)
    ax3.set_xlim(zoom2_xlim)
    ax3.set_ylim(zoom2_ylim)
    ax3.set_title(ar("تكبير 2: طبقات دقيقة متكررة داخل الخيط نفسه"),
                  fontsize=11, fontproperties=ARABIC_FONT)
    for spine in ax3.spines.values():
        spine.set_edgecolor("darkorange")
        spine.set_linewidth(1.5)

    fig.suptitle(
        ar("جاذب هينون: من الصورة الكلية إلى البنية الدقيقة المتكررة"),
        fontsize=14, fontweight="bold", fontproperties=ARABIC_FONT
    )
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    return fig


def _draw_zoom_box(ax, xlim, ylim, color):
    """يرسم مستطيلاً يحدد منطقة التكبير التالية على المحور ax."""
    x0, x1 = xlim
    y0, y1 = ylim
    ax.plot([x0, x1, x1, x0, x0], [y0, y0, y1, y1, y0],
            color=color, linewidth=1.3)


# ---------------------------------------------------------------
# 3) تشغيل البرنامج
# ---------------------------------------------------------------
if __name__ == "__main__":
    fig = plot_henon_with_zoom(a=1.4, b=0.3, n_iter=200_000)
    fig.savefig("henon_attractor_zoom.png", dpi=200, bbox_inches="tight")
    print("تم حفظ الشكل في henon_attractor_zoom.png")
    plt.show()
