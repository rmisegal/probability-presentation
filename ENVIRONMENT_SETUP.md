# הוראות התקנה והפעלת סביבת העבודה
## Probability Presentation Environment Setup

**כל הזכויות שמורות לד"ר יורם סגל**

## דרישות מערכת
- Python 3.8 או גרסה חדשה יותר
- Git
- דפדפן Chrome/Firefox מעודכן
- מערכת הפעלה: Windows 11, macOS, או Linux

## שלב 1: הורדת הפרויקט מ-GitHub

```bash
# שכפול הרפוזיטורי
git clone [URL_OF_REPOSITORY]
cd probability_presentation

# אם הפרויקט כבר קיים אצלכם, עדכון:
git pull origin main
```

## שלב 2: יצירת סביבה וירטואלית

### ב-Windows:
```cmd
# יצירת סביבה וירטואלית
python -m venv venv

# הפעלת הסביבה
venv\Scripts\activate
```

### ב-macOS/Linux:
```bash
# יצירת סביבה וירטואלית
python3 -m venv venv

# הפעלת הסביבה
source venv/bin/activate
```

## שלב 3: התקנת החבילות הנדרושות

```bash
# התקנת כל החבילות מקובץ requirements.txt
pip install -r requirements.txt

# אימות התקנה
pip list
```

## שלב 4: הפעלת המצגת

### אופציה 1: שרת פיתוח פשוט
```bash
# הפעלת שרת HTTP פשוט
python -m http.server 8000

# פתיחת הדפדפן בכתובת:
# http://localhost:8000
```

### אופציה 2: שרת עם Live Reload (מומלץ לפיתוח)
```bash
# התקנת live-server (חד פעמי)
npm install -g live-server

# הפעלת השרת
live-server --port=8000
```

## שלב 5: צפייה במצגת

1. פתחו דפדפן Chrome או Firefox
2. נווטו לכתובת: `http://localhost:8000`
3. המצגת תיפתח אוטומטית

## פתרון בעיות נפוצות

### בעיה: Python לא מזוהה
**פתרון:** ודאו שPython מותקן ונמצא ב-PATH של המערכת

### בעיה: pip לא עובד
**פתרון:** 
```bash
python -m pip install --upgrade pip
```

### בעיה: חבילות לא מתקינות
**פתרון:**
```bash
# התקנה עם הרשאות מנהל (Windows)
pip install -r requirements.txt --user

# או ב-macOS/Linux
sudo pip3 install -r requirements.txt
```

### בעיה: הדפדפן לא פותח את המצגת
**פתרון:** ודאו שהשרת רץ ונסו לגשת ידנית לכתובת

## עדכון הפרויקט

```bash
# עצירת השרת (Ctrl+C)
# עדכון מ-GitHub
git pull origin main

# התקנת חבילות חדשות (אם יש)
pip install -r requirements.txt

# הפעלה מחדש של השרת
python -m http.server 8000
```

## מבנה הפרויקט

```
probability_presentation/
├── index.html              # דף הבית של המצגת
├── slides/                 # תיקיית השקפים
│   ├── slide1.html
│   ├── slide2.html
│   └── ...
├── data/                   # נתונים לויזואליזציות
│   ├── generate_data.py
│   └── *.json
├── js/                     # קבצי JavaScript
├── css/                    # קבצי עיצוב
├── assets/                 # תמונות ומדיה
├── requirements.txt        # חבילות Python
└── README.md              # תיעוד הפרויקט
```

## תמיכה טכנית

במקרה של בעיות טכניות, אנא פנו לד"ר יורם סגל או עיינו בתיעוד המלא ב-README.md

