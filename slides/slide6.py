#!/usr/bin/env python3
"""
Slide 6: Law of Large Numbers
Demonstration of the law of large numbers and gambler's fallacy

Copyright (c) 2025 Dr. Yoram Segal. All rights reserved.
כל הזכויות שמורות לד"ר יורם סגל
"""

import numpy as np
import matplotlib.pyplot as plt
import random
from collections import Counter

def law_of_large_numbers_demo():
    """
    הדגמת חוק המספרים הגדולים
    Demonstration of the law of large numbers
    """
    print("=== חוק המספרים הגדולים (Law of Large Numbers) ===")
    
    # יצירת וקטור של מספרי הטלות גדלים אקספוננציאלית
    ns = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096])
    np.random.seed(42)  # לשחזור תוצאות
    
    print(f"מספרי הטלות בניסוי: {ns}")
    
    # ביצוע ניסויים עם binomial distribution
    heads_count = [np.random.binomial(n, 0.5) for n in ns]
    proportion_heads = np.array(heads_count) / ns
    
    print(f"\nתוצאות הניסויים:")
    print("מספר הטלות | מספר ראשים | שיעור ראשים | הפרש מ-0.5")
    print("-" * 60)
    
    for i, n in enumerate(ns):
        diff_from_half = abs(proportion_heads[i] - 0.5)
        print(f"{n:11d} | {heads_count[i]:11d} | {proportion_heads[i]:12.4f} | {diff_from_half:11.4f}")
    
    print(f"\nמסקנה: ככל שמספר ההטלות גדל, השיעור מתקרב ל-0.5")
    
    return ns, heads_count, proportion_heads

def gambler_fallacy_explanation():
    """
    הסבר על כשל המהמר
    Explanation of gambler's fallacy
    """
    print("\n=== כשל המהמר (Gambler's Fallacy) ===")
    print("טעות נפוצה: חשיבה שאירועי עבר משפיעים על עתיד בניסויים עצמאיים")
    
    print(f"\nדוגמה: 5 ראשים ברצף")
    print("שאלה: האם הסיכוי לעץ בהטלה הבאה גדול יותר?")
    print("תשובה: לא! כל הטלה עצמאית - תמיד 50% לכל צד")
    
    # הדגמה מעשית
    print(f"\nהדגמה:")
    sequence = ['H', 'H', 'H', 'H', 'H']
    for i, result in enumerate(sequence):
        print(f"הטלה {i+1}: {result} - הסתברות לראש בהטלה הבאה: 50%")
    
    print(f"הטלה 6: ? - הסתברות לראש: עדיין 50%!")
    
    # דוגמה מקזינו
    print(f"\nדוגמה מקזינו:")
    print("רולטה: 5 אדומים ברצף")
    print("מהמרים חושבים: 'עכשיו בטוח יבוא שחור!'")
    print("מציאות: הסיכוי לשחור עדיין 47.4% (כמו תמיד)")

def demonstrate_independence():
    """
    הדגמת עצמאות בהטלות מטבע
    Demonstrate independence in coin flips
    """
    print("\n=== הדגמת עצמאות ===")
    
    # ניסוי: בדיקת השפעת היסטוריה על תוצאות עתידיות
    n_experiments = 10000
    sequences_after_5_heads = []
    
    print(f"ניסוי: בדיקת {n_experiments:,} רצפים של 6 הטלות")
    print("מחפשים רצפים שמתחילים ב-5 ראשים ובודקים את ההטלה השישית")
    
    count_5_heads_then_heads = 0
    count_5_heads_then_tails = 0
    
    for _ in range(n_experiments):
        # יצירת רצף של 6 הטלות
        sequence = [random.choice(['H', 'T']) for _ in range(6)]
        
        # בדיקה אם 5 הראשונות הן ראשים
        if sequence[:5] == ['H', 'H', 'H', 'H', 'H']:
            if sequence[5] == 'H':
                count_5_heads_then_heads += 1
            else:
                count_5_heads_then_tails += 1
    
    total_5_heads = count_5_heads_then_heads + count_5_heads_then_tails
    
    if total_5_heads > 0:
        prob_heads_after_5 = count_5_heads_then_heads / total_5_heads
        prob_tails_after_5 = count_5_heads_then_tails / total_5_heads
        
        print(f"\nתוצאות:")
        print(f"מספר רצפים של 5 ראשים: {total_5_heads}")
        print(f"מתוכם, ההטלה השישית:")
        print(f"  ראש: {count_5_heads_then_heads} ({prob_heads_after_5:.3f})")
        print(f"  עץ: {count_5_heads_then_tails} ({prob_tails_after_5:.3f})")
        print(f"\nמסקנה: גם אחרי 5 ראשים, ההסתברות עדיין קרובה ל-0.5!")
    else:
        print("לא נמצאו רצפים של 5 ראשים בניסוי זה")

def visualize_law_of_large_numbers():
    """
    ויזואליזציה של חוק המספרים הגדולים
    Visualization of the law of large numbers
    """
    print("\n=== ויזואליזציה ===")
    
    # נתונים מהדגמה הקודמת
    ns, heads_count, proportion_heads = law_of_large_numbers_demo()
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. התכנסות לחוק המספרים הגדולים
    ax1.semilogx(ns, proportion_heads, 'o-', color='#0047AB', linewidth=2, markersize=8)
    ax1.axhline(y=0.5, color='red', linestyle='--', linewidth=2, label='הסתברות תיאורטית (0.5)')
    ax1.set_xlabel('מספר הטלות (סקלה לוגריתמית)')
    ax1.set_ylabel('שיעור ראשים')
    ax1.set_title('חוק המספרים הגדולים')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 1)
    
    # 2. הפרש מההסתברות התיאורטית
    differences = np.abs(proportion_heads - 0.5)
    ax2.loglog(ns, differences, 'o-', color='#3B82F6', linewidth=2, markersize=8)
    ax2.set_xlabel('מספר הטלות')
    ax2.set_ylabel('הפרש מ-0.5 (ערך מוחלט)')
    ax2.set_title('התכנסות - הפרש מההסתברות התיאורטית')
    ax2.grid(True, alpha=0.3)
    
    # 3. סימולציה של כשל המהמר
    # יצירת 1000 רצפים של 10 הטלות
    n_sequences = 1000
    sequence_length = 10
    
    heads_after_streaks = []
    streak_lengths = []
    
    for _ in range(n_sequences):
        sequence = [random.choice([0, 1]) for _ in range(sequence_length)]
        
        # חיפוש רצפי ראשים
        current_streak = 0
        for i, flip in enumerate(sequence):
            if flip == 1:  # ראש
                current_streak += 1
            else:
                if current_streak >= 2 and i < sequence_length:  # רצף של לפחות 2 ראשים
                    streak_lengths.append(current_streak)
                    # בדיקה מה קרה אחרי הרצף (אם יש הטלה נוספת)
                    if i < sequence_length - 1:
                        heads_after_streaks.append(sequence[i + 1])
                current_streak = 0
    
    if heads_after_streaks:
        heads_after_count = sum(heads_after_streaks)
        total_after = len(heads_after_streaks)
        prob_heads_after_streak = heads_after_count / total_after
        
        ax3.bar(['ראש', 'עץ'], 
               [prob_heads_after_streak, 1 - prob_heads_after_streak],
               color=['#0047AB', '#3B82F6'])
        ax3.axhline(y=0.5, color='red', linestyle='--', linewidth=2, label='הסתברות תיאורטית')
        ax3.set_ylabel('הסתברות')
        ax3.set_title('תוצאות אחרי רצפי ראשים')
        ax3.legend()
        ax3.set_ylim(0, 1)
    
    # 4. התפלגות אורכי רצפים
    if streak_lengths:
        streak_counter = Counter(streak_lengths)
        lengths = list(streak_counter.keys())
        counts = list(streak_counter.values())
        
        ax4.bar(lengths, counts, color='#1E3A8A', alpha=0.7)
        ax4.set_xlabel('אורך רצף ראשים')
        ax4.set_ylabel('מספר רצפים')
        ax4.set_title('התפלגות אורכי רצפים')
        ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return fig

def main():
    """
    הפונקציה הראשית
    Main function
    """
    print("שקף 6: חוק המספרים הגדולים")
    print("Slide 6: Law of Large Numbers")
    print("=" * 60)
    
    # הדגמת חוק המספרים הגדולים
    ns, heads_count, proportion_heads = law_of_large_numbers_demo()
    
    # הסבר על כשל המהמר
    gambler_fallacy_explanation()
    
    # הדגמת עצמאות
    demonstrate_independence()
    
    # ויזואליזציה
    try:
        visualize_law_of_large_numbers()
    except Exception as e:
        print(f"שגיאה בויזואליזציה: {e}")
    
    print("\n" + "=" * 60)
    print("סיכום:")
    print("• חוק המספרים הגדולים: ככל שהמדגם גדל, התוצאות מתכנסות לערך הצפוי")
    print("• כשל המהמר: אירועי עבר לא משפיעים על עתיד בניסויים עצמאיים")
    print("• עצמאות: כל הטלת מטבע היא ניסוי עצמאי עם הסתברות קבועה")
    print("• יישום מעשי: בסיס לסטטיסטיקה ומחקר מדעי")
    print("\nסיום שקף 6")

if __name__ == "__main__":
    # הגדרת זרע אקראי לשחזור תוצאות
    random.seed(42)
    np.random.seed(42)
    
    main()

