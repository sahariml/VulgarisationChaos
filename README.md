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
| `generate_figure_1_2_4_9.py` | المسار الزمني للنموذج اللوجستي (\(r=3.9\)) |
| `generate_figure_1_2_4_9.py` | مخطط التفرع للنموذج اللوجستي |
| `generate_figure_3.py` | مقارنة مسارين من شروط ابتدائية متقاربة (\(x_0=0.400000\) و \(y_0=0.400001\)) |
| `generate_figure_1_2_4_9.py` | أس ليابونوف بدلالة \(r\) للنموذج اللوجستي |
| `generate_figure_1_2_4_9.py` | جاذب لورنز (الفراشة) |
| `generate_figure_5.py` | ثلاثة أنواع من الجاذبات (نقطي، دوري، غريب) |
| `generate_figure_7.py` | سلسلة تكبيرات على مجموعة ماندلبروت |
| `generate_figure_6.py` | منحنى كوخ (Flocon de Koch) من الرتبة 0 إلى 4 |
| `generate_figure_8.py` | مساران لنواس مزدوج من شروط ابتدائية متقاربة |
| `generate_figure_10.py` | تطور الفارق بين مسارين على مقياس لوغاريتمي |

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
   python generate_figure_1_2_4_9.py
   ```
   سيتم إنشاء ملف PNG في نفس المجلد (مثل `figure_sensibilite.png`).

3. **جميع الملفات** تعمل بنفس الطريقة. تأكد من أن لديك صلاحية الكتابة في المجلد الحالي.

---

## ملاحظات على بعض الملفات

- **`generate_figure_5.py`** : يولد شكلاً واحداً يحتوي على ثلاثة أجزاء (point fixe, cycle limite, attracteur de Lorenz).  
- **`generate_figure_6.py; generate_figure_7.py`** : يستغرق بضع ثوانٍ (حسب قوة الحاسوب) بسبب كثافة الحسابات.  
- **`generate_figure_1_2_4_9.py`** : يستخدم مكتبة `scipy.integrate.odeint` لحل المعادلات التفاضلية.  

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

للاستفسارات أو الاقتراحات، يمكنك فتح **Issue** في هذا المستودع أو الاتصال بالكاتب عبر بريده الالكتروني.

---

**رابط المستودع**: [https://github.com/sahariml/VulgarisationChaos](https://github.com/sahariml/VulgarisationChaos)

---

## Authors

**Mohamed Lamine Sahari**  
Department of Mathematics  
Badji Mokhtar-Annaba University, Algeria  
Email: mohamed-lamine.sahari@univ-annaba.dz

**Contributors**: The code suite was unified, extended, and documented for public release.


---

## License

This project is provided for academic and research purposes. Users are encouraged to cite the original authors in any publications arising from the use of these codes.
