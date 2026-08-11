# README.md

```markdown
# توليد أشكال مقال "عندما يصبح الانتظام غير متوقَّع"

هذا المستودع يحتوي على الشيفرات البرمجية (Python) المستخدمة لتوليد جميع الأشكال البيانية في مقال التبسيط العلمي:

**"عندما يصبح الانتظام غير متوقَّع – رحلة في قلب الأنظمة الديناميكية والشَّوَاش"**  
(الكاتب: محمد لمين صحاري)

---

## محتويات المستودع

يحتوي المستودع على الملفات التالية (كل ملف يولد شكلاً بيانياً واحداً أو أكثر):

| الملف | الشكل المُنتَج |
|-------|----------------|
| `figure_trajectoire.py` | المسار الزمني للنموذج اللوجستي (\(r=3.9\)) |
| `figure_bifurcation.py` | مخطط التفرع للنموذج اللوجستي |
| `figure_sensibilite.py` | مقارنة مسارين من شروط ابتدائية متقاربة (\(x_0=0.400000\) و \(y_0=0.400001\)) |
| `figure_lyapunov.py` | أس ليابونوف بدلالة \(r\) للنموذج اللوجستي |
| `figure_lorenz.py` | جاذب لورنز (الفراشة) |
| `figure_attracteurs.py` | ثلاثة أنواع من الجاذبات (نقطي، دوري، غريب) |
| `figure_mandelbrot_zoom.py` | سلسلة تكبيرات على مجموعة ماندلبروت |
| `figure_koch.py` | منحنى كوخ (Flocon de Koch) من الرتبة 0 إلى 4 |
| `figure_double_pendule.py` | مساران لنواس مزدوج من شروط ابتدائية متقاربة |
| `figure_ecart.py` | تطور الفارق بين مسارين على مقياس لوغاريتمي |

---

## المتطلبات الأساسية (Prerequisites)

لتشغيل هذه الشيفرات، تحتاج إلى تثبيت :

- Python 3.7 أو أحدث
- المكتبات التالية (يمكن تثبيتها عبر `pip`):

```bash
pip install numpy scipy matplotlib
```

---

## كيفية الاستخدام

1. **انسخ المستودع** إلى جهازك:
   ```bash
   git clone https://github.com/sahariml/VulgarisationChaos.git
   cd VulgarisationChaos
   ```

2. **شغّل الملف المطلوب**، مثلاً:
   ```bash
   python figure_sensibilite.py
   ```
   سيتم إنشاء ملف PNG في نفس المجلد (مثل `figure_sensibilite.png`).

3. **جميع الملفات** تعمل بنفس الطريقة. تأكد من أن لديك صلاحية الكتابة في المجلد الحالي.

---

## ملاحظات على بعض الملفات

- **`figure_attracteurs.py`** : يولد شكلاً واحداً يحتوي على ثلاثة أجزاء (point fixe, cycle limite, attracteur de Lorenz).  
- **`figure_mandelbrot_zoom.py`** : يستغرق بضع ثوانٍ (حسب قوة الحاسوب) بسبب كثافة الحسابات.  
- **`figure_lorenz.py`** : يستخدم مكتبة `scipy.integrate.odeint` لحل المعادلات التفاضلية.  

---

## تخصيص الأشكال

يمكنك تعديل البارامترات داخل كل ملف (مثل قيمة `r`، عدد التكرارات، دقة الشبكة، إلخ) للحصول على نتائج مختلفة.

---

## الترخيص (License)

هذه الشيفرات مرخصة تحت رخصة **MIT** – يمكنك استخدامها وتعديلها بحرية مع الإشارة إلى المصدر.

---

## المراجع العلمية

الأشكال المستخدمة في المقال تستند إلى النماذج الكلاسيكية التالية :

- Lorenz, E. N. (1963). *Deterministic nonperiodic flow*.  
- May, R. M. (1976). *Simple mathematical models with very complicated dynamics*.  
- Li, T.-Y. & Yorke, J. A. (1975). *Period three implies chaos*.  
- Sharkovsky, O. M. (1964). *Coexistence of cycles of a continuous map of a line to itself*.

---

## الاتصال

للاستفسارات أو الاقتراحات، يمكنك فتح **Issue** في هذا المستودع أو الاتصال بالكاتب عبر حسابه على GitHub.

---

**رابط المستودع**: [https://github.com/sahariml/VulgarisationChaos](https://github.com/sahariml/VulgarisationChaos)

**شكراً لاهتمامك!**
```
