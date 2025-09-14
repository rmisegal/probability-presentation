# מצגת אינטראקטיבית: מבוא להסתברות

מצגת זו נוצרה עבור ד"ר יורם סגל ומציגה מושגי יסוד בתורת ההסתברות. המצגת פותחה כאתר אינטרנט אינטראקטיבי עם שקפים דינמיים, אנימציות, ודוגמאות קוד בפייתון.

**קישור למצגת:** [https://rmisegal.github.io/probability-presentation/](https://rmisegal.github.io/probability-presentation/)

## תכונות עיקריות

- **עיצוב מודרני:** מבוסס על תבנית Cobalt עם אנימציות ועיצוב נקי.
- **אינטראקטיביות:** ניווט מלא באמצעות מקלדת, עכבר, ומגע.
- **תוכן דינמי:** שקפים מבוססי HTML, CSS, ו-JavaScript.
- **דוגמאות קוד:** כל שקף מלווה בקובץ פייתון להרצה והבנה מעמיקה.
- **דו-לשוני:** כותרות באנגלית והסברים בעברית.

## כיצד להריץ את המצגת מקומית

### דרישות קדם

- **Git:** להתקנת Git, עקוב אחר ההוראות [כאן](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
- **Python 3:** להתקנת פייתון, עקוב אחר ההוראות [כאן](https://www.python.org/downloads/).

### הוראות התקנה

1. **שכפול הרפוזיטורי:**
   פתח טרמינל (או Command Prompt בחלונות) והרץ את הפקודה הבאה:
   ```bash
   git clone https://github.com/rmisegal/probability-presentation.git
   ```

2. **ניווט לתיקיית הפרויקט:**
   ```bash
   cd probability-presentation
   ```

3. **הקמת סביבה וירטואלית (מומלץ):**
   ```bash
   python -m venv venv
   ```

4. **הפעלת הסביבה הווירטואלית:**
   - **בחלונות:**
     ```bash
     .\venv\Scripts\activate
     ```
   - **ב-macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

5. **התקנת החבילות הנדרשות:**
   הרץ את הפקודה הבאה כדי להתקין את כל חבילות הפייתון הנדרשות מהקובץ `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### הרצת המצגת

1. **הפעלת שרת מקומי:**
   בתיקיית הפרויקט, הרץ את הפקודה הבאה:
   ```bash
   python -m http.server 8080
   ```

2. **צפייה במצגת:**
   פתח דפדפן כרום וגלוש לכתובת הבאה:
   [http://localhost:8080](http://localhost:8080)

## כיצד לעדכן את הרפוזיטורי

אם בוצעו שינויים ברפוזיטורי המרוחק ב-GitHub, תוכל למשוך את העדכונים האחרונים באמצעות הפקודה הבאה (ודא שאתה נמצא בתיקיית הפרויקט):

```bash
git pull origin main
```

## מבנה הפרויקט

```
probability-presentation/
├── css/                    # קבצי עיצוב
│   └── cobalt-theme.css
├── data/                   # קבצי נתונים שנוצרו
│   └── ...
├── slides/                 # קבצי HTML ופייתון של השקפים
│   ├── opening.html
│   ├── slide1.html
│   ├── slide1.py
│   └── ...
├── index.html              # דף הכניסה הראשי של המצגת
├── README.md               # קובץ זה
├── requirements.txt        # רשימת חבילות פייתון
└── ENVIRONMENT_SETUP.md    # הוראות נוספות להגדרת הסביבה
```

---

© 2025, ד"ר יורם סגל. כל הזכויות שמורות.


