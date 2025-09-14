#!/usr/bin/env python3
"""
Slide 1: What Probability Theory Is
Basic Probability Concepts Demonstration

Copyright (c) 2025 Dr. Yoram Segal. All rights reserved.
כל הזכויות שמורות לד"ר יורם סגל
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def basic_probability_demo():
    """
    הדגמה בסיסית של מושגי הסתברות
    Basic demonstration of probability concepts
    """
    print("=== תורת ההסתברות - דוגמאות בסיסיות ===")
    print("=== Probability Theory - Basic Examples ===")
    
    # הטלת מטבע - Coin flip
    print("\n1. הטלת מטבע (Coin Flip):")
    coin_results = []
    for i in range(1000):
        result = random.choice(['ראש', 'עץ'])  # Heads, Tails
        coin_results.append(result)
    
    heads_count = coin_results.count('ראש')
    probability_heads = heads_count / 1000
    
    print(f"מספר 'ראש' ב-1000 הטלות: {heads_count}")
    print(f"הסתברות ניסיונית ל'ראש': {probability_heads:.3f}")
    print(f"הסתברות תיאורטית ל'ראש': 0.500")
    print(f"הפרש מהתיאוריה: {abs(probability_heads - 0.5):.3f}")
    
    # הטלת קובייה - Dice roll
    print("\n2. הטלת קובייה (Dice Roll):")
    dice_results = [random.randint(1, 6) for _ in range(1000)]
    
    print("תוצאות הטלת קובייה:")
    for number in range(1, 7):
        count = dice_results.count(number)
        probability = count / 1000
        theoretical = 1/6
        print(f"מספר {number}: {count:3d} פעמים, הסתברות: {probability:.3f}, תיאורטי: {theoretical:.3f}")
    
    return coin_results, dice_results

def probability_visualization():
    """
    ויזואליזציה של תוצאות הסתברות
    Visualization of probability results
    """
    print("\n3. ויזואליזציה של התוצאות:")
    
    # יצירת נתונים
    coin_results, dice_results = basic_probability_demo()
    
    # יצירת גרפים
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # גרף הטלת מטבע
    coin_counts = Counter(coin_results)
    ax1.bar(coin_counts.keys(), coin_counts.values(), color=['#0047AB', '#3B82F6'])
    ax1.set_title('תוצאות הטלת מטבע (1000 הטלות)', fontsize=14)
    ax1.set_ylabel('מספר הופעות')
    ax1.grid(True, alpha=0.3)
    
    # הוספת קו הסתברות תיאורטית
    ax1.axhline(y=500, color='red', linestyle='--', label='הסתברות תיאורטית (500)')
    ax1.legend()
    
    # גרף הטלת קובייה
    dice_counts = Counter(dice_results)
    numbers = list(range(1, 7))
    counts = [dice_counts[i] for i in numbers]
    
    ax2.bar(numbers, counts, color='#1E3A8A')
    ax2.set_title('תוצאות הטלת קובייה (1000 הטלות)', fontsize=14)
    ax2.set_xlabel('מספר על הקובייה')
    ax2.set_ylabel('מספר הופעות')
    ax2.grid(True, alpha=0.3)
    
    # הוספת קו הסתברות תיאורטית
    ax2.axhline(y=1000/6, color='red', linestyle='--', label=f'הסתברות תיאורטית ({1000/6:.1f})')
    ax2.legend()
    
    plt.tight_layout()
    plt.show()
    
    return fig

def theoretical_vs_experimental():
    """
    השוואה בין הסתברות תיאורטית לניסיונית
    Comparison between theoretical and experimental probability
    """
    print("\n4. השוואה: תיאורטי מול ניסיוני")
    print("=" * 50)
    
    sample_sizes = [10, 50, 100, 500, 1000, 5000]
    
    print("גודל מדגם | הסתברות ניסיונית | הפרש מתיאוריה")
    print("-" * 50)
    
    for n in sample_sizes:
        # הטלת מטבע n פעמים
        results = [random.choice([0, 1]) for _ in range(n)]  # 0=עץ, 1=ראש
        experimental_prob = sum(results) / n
        difference = abs(experimental_prob - 0.5)
        
        print(f"{n:8d} | {experimental_prob:15.3f} | {difference:13.3f}")
    
    print("\nמסקנה: ככל שגודל המדגם גדל, ההסתברות הניסיונית מתקרבת לתיאורטית")

def main():
    """
    הפונקציה הראשית
    Main function
    """
    print("שקף 1: מה היא תורת ההסתברות")
    print("Slide 1: What Probability Theory Is")
    print("=" * 60)
    
    # הרצת כל הדוגמאות
    coin_data, dice_data = basic_probability_demo()
    
    # ויזואליזציה
    try:
        probability_visualization()
    except Exception as e:
        print(f"שגיאה בויזואליזציה: {e}")
    
    # השוואה תיאורטי מול ניסיוני
    theoretical_vs_experimental()
    
    print("\n" + "=" * 60)
    print("סיום שקף 1")
    print("End of Slide 1")

if __name__ == "__main__":
    # הגדרת זרע אקראי לשחזור תוצאות
    random.seed(42)
    np.random.seed(42)
    
    main()

