#!/usr/bin/env python3
"""
Slide 5: Combinatorics
Demonstration of combinatorial calculations and their applications in probability

Copyright (c) 2025 Dr. Yoram Segal. All rights reserved.
כל הזכויות שמורות לד"ר יורם סגל
"""

import math
import random
import numpy as np
import matplotlib.pyplot as plt
from math import factorial
import itertools
from collections import Counter

def factorial_examples():
    """
    דוגמאות לחישוב פקטוריאל
    Examples of factorial calculations
    """
    print("=== פקטוריאל (Factorial) ===")
    print("הגדרה: n! = n × (n-1) × (n-2) × ... × 2 × 1")
    print("הגדרה מיוחדת: 0! = 1")
    
    print(f"\nדוגמאות:")
    print("n | n! | חישוב")
    print("-" * 30)
    
    for n in range(6):
        if n == 0:
            calculation = "הגדרה"
        elif n == 1:
            calculation = "1"
        else:
            factors = " × ".join(str(i) for i in range(n, 0, -1))
            calculation = factors
        
        fact_value = factorial(n)
        print(f"{n} | {fact_value:3d} | {calculation}")
    
    # דוגמאות גדולות יותר
    print(f"\nפקטוריאלים גדולים:")
    for n in [7, 8, 9, 10]:
        print(f"{n}! = {factorial(n):,}")
    
    print(f"\nצמיחה מהירה של הפקטוריאל:")
    print(f"10! = {factorial(10):,}")
    print(f"15! = {factorial(15):,}")
    print(f"20! = {factorial(20):,}")

def combinations_formula(n, k):
    """
    חישוב C(n,k) = n choose k
    Calculate combinations C(n,k)
    """
    if k > n or k < 0:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def combinations_examples():
    """
    דוגמאות לחישוב קומבינציות
    Examples of combinations calculations
    """
    print("\n=== קומבינציות (Combinations) ===")
    print("נוסחה: C(n,k) = n! / (k!(n-k)!)")
    print("משמעות: מספר הדרכים לבחור k פריטים מתוך n פריטים")
    
    # דוגמאות בסיסיות
    examples = [
        (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5),
        (4, 2), (6, 3), (10, 2)
    ]
    
    print(f"\nדוגמאות:")
    print("C(n,k) | ערך | פירוש")
    print("-" * 40)
    
    for n, k in examples:
        value = combinations_formula(n, k)
        if n <= 6:
            meaning = f"דרכים לבחור {k} מתוך {n}"
        else:
            meaning = f"בחירת {k} מתוך {n}"
        print(f"C({n},{k})  | {value:3d} | {meaning}")

def detailed_calculation_example():
    """
    דוגמה מפורטת לחישוב C(5,3)
    Detailed calculation example for C(5,3)
    """
    print("\n=== דוגמה מפורטת: C(5,3) ===")
    print("שאלה: בכמה דרכים ניתן לבחור 3 פריטים מתוך 5?")
    
    n, k = 5, 3
    
    print(f"\nחישוב שלב אחר שלב:")
    print(f"C(5,3) = 5! / (3! × (5-3)!)")
    print(f"       = 5! / (3! × 2!)")
    
    fact_5 = factorial(5)
    fact_3 = factorial(3)
    fact_2 = factorial(2)
    
    print(f"       = {fact_5} / ({fact_3} × {fact_2})")
    print(f"       = {fact_5} / {fact_3 * fact_2}")
    print(f"       = {fact_5 // (fact_3 * fact_2)}")
    
    # הצגת כל הדרכים
    items = ['A', 'B', 'C', 'D', 'E']
    all_combinations = list(itertools.combinations(items, 3))
    
    print(f"\nכל הדרכים לבחור 3 מתוך {items}:")
    for i, combo in enumerate(all_combinations, 1):
        print(f"{i:2d}. {combo}")
    
    print(f"\nסה\"כ: {len(all_combinations)} דרכים")

def coin_flip_combinatorics():
    """
    יישום קומבינטוריקה על הטלת מטבעות
    Application of combinatorics to coin flips
    """
    print("\n=== הטלת מטבעות עם קומבינטוריקה ===")
    
    n = 5  # מספר הטלות
    print(f"הטלת {n} מטבעות:")
    print(f"מספר תוצאות אפשריות: 2^{n} = {2**n}")
    
    print(f"\nמספר דרכים לקבל k ראשים:")
    print("k | C(n,k) | הסתברות | אחוז")
    print("-" * 35)
    
    total_outcomes = 2**n
    total_probability = 0
    
    for k in range(n + 1):
        ways = combinations_formula(n, k)
        probability = ways / total_outcomes
        percentage = probability * 100
        total_probability += probability
        
        print(f"{k} | {ways:5d} | {probability:8.4f} | {percentage:5.1f}%")
    
    print("-" * 35)
    print(f"סה\"כ הסתברות: {total_probability:.4f} (צריך להיות 1.0000)")

def solve_textbook_exercises():
    """
    פתרון התרגילים מהשקף
    Solve the exercises from the slide
    """
    print("\n=== פתרון תרגילים ===")
    
    # תרגיל 3: 3 ראשים ב-5 הטלות
    print("תרגיל 3: הסתברות לקבל 3 ראשים ב-5 הטלות")
    n, k = 5, 3
    ways = combinations_formula(n, k)
    total = 2**n
    probability = ways / total
    
    print(f"פתרון:")
    print(f"C(5,3) = {ways}")
    print(f"מספר תוצאות אפשריות = 2^5 = {total}")
    print(f"P(3 ראשים) = {ways}/{total} = {probability:.4f}")
    
    # תרגיל 4: יצירת פונקציה
    print(f"\nתרגיל 4: פונקציה לחישוב הסתברויות")
    
    def coinflip_prob(n, k):
        """פונקציה לחישוב הסתברות k ראשים ב-n הטלות"""
        n_choose_k = factorial(n) // (factorial(k) * factorial(n - k))
        return n_choose_k / (2**n)
    
    print(f"הסתברויות ל-5 הטלות:")
    for heads in range(6):
        prob = coinflip_prob(5, heads)
        print(f"P({heads} ראשים) = {prob:.4f}")

def pascal_triangle():
    """
    משולש פסקל וקשר לקומבינציות
    Pascal's triangle and its connection to combinations
    """
    print("\n=== משולש פסקל ===")
    print("כל מספר במשולש פסקל הוא C(n,k)")
    
    rows = 6
    print(f"משולש פסקל עד שורה {rows-1}:")
    
    for n in range(rows):
        # הדפסת רווחים למרכוז
        spaces = " " * (rows - n - 1) * 2
        row_str = spaces
        
        for k in range(n + 1):
            value = combinations_formula(n, k)
            row_str += f"{value:3d} "
        
        print(row_str)
    
    print(f"\nקשר להטלת מטבעות:")
    print(f"שורה n במשולש = התפלגות מספר ראשים ב-n הטלות")

def binomial_theorem():
    """
    המשפט הבינומי
    Binomial theorem
    """
    print("\n=== המשפט הבינומי ===")
    print("(a + b)^n = Σ C(n,k) × a^(n-k) × b^k")
    
    # דוגמה: (1/2 + 1/2)^5
    print(f"\nדוגמה: (1/2 + 1/2)^5 = 1")
    print(f"פיתוח:")
    
    n = 5
    a, b = 0.5, 0.5
    total = 0
    
    for k in range(n + 1):
        coeff = combinations_formula(n, k)
        term = coeff * (a**(n-k)) * (b**k)
        total += term
        print(f"C(5,{k}) × (1/2)^{n-k} × (1/2)^{k} = {coeff} × {term/coeff:.4f} = {term:.4f}")
    
    print(f"סה\"כ: {total:.4f}")

def simulate_combinatorics():
    """
    סימולציה לאימות חישובים קומבינטוריים
    Simulation to verify combinatorial calculations
    """
    print("\n=== סימולציה לאימות ===")
    
    n_experiments = 100000
    n_flips = 5
    
    print(f"סימולציה: {n_experiments:,} ניסויים של {n_flips} הטלות")
    
    # ספירת תוצאות
    results = []
    for _ in range(n_experiments):
        flips = [random.choice([0, 1]) for _ in range(n_flips)]  # 0=T, 1=H
        heads_count = sum(flips)
        results.append(heads_count)
    
    result_counts = Counter(results)
    
    print(f"\nהשוואה: תיאורטי מול ניסיוני")
    print("k | תיאורטי | ניסיוני | הפרש")
    print("-" * 40)
    
    for k in range(n_flips + 1):
        theoretical = combinations_formula(n_flips, k) / (2**n_flips)
        observed_count = result_counts.get(k, 0)
        experimental = observed_count / n_experiments
        difference = abs(theoretical - experimental)
        
        print(f"{k} | {theoretical:8.4f} | {experimental:8.4f} | {difference:.4f}")

def visualize_combinatorics():
    """
    ויזואליזציה של מושגים קומבינטוריים
    Visualization of combinatorial concepts
    """
    print("\n=== ויזואליזציה ===")
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. משולש פסקל
    rows = 8
    triangle_data = []
    for n in range(rows):
        row = [combinations_formula(n, k) for k in range(n + 1)]
        triangle_data.append(row)
    
    # יצירת מטריצה למשולש פסקל
    max_len = max(len(row) for row in triangle_data)
    triangle_matrix = np.zeros((rows, max_len))
    
    for i, row in enumerate(triangle_data):
        start_idx = (max_len - len(row)) // 2
        for j, val in enumerate(row):
            triangle_matrix[i, start_idx + j] = val
    
    im1 = ax1.imshow(triangle_matrix, cmap='Blues', aspect='auto')
    ax1.set_title('משולש פסקל')
    ax1.set_xlabel('k')
    ax1.set_ylabel('n')
    
    # הוספת מספרים למשולש
    for i in range(rows):
        for j in range(max_len):
            if triangle_matrix[i, j] > 0:
                ax1.text(j, i, f'{int(triangle_matrix[i, j])}', 
                        ha='center', va='center', fontsize=8)
    
    # 2. התפלגות בינומית למספרי n שונים
    n_values = [3, 5, 8, 10]
    colors = ['#0047AB', '#3B82F6', '#1E3A8A', '#60A5FA']
    
    for i, n in enumerate(n_values):
        k_vals = list(range(n + 1))
        probs = [combinations_formula(n, k) / (2**n) for k in k_vals]
        ax2.plot(k_vals, probs, 'o-', label=f'n={n}', 
                color=colors[i], linewidth=2, markersize=6)
    
    ax2.set_xlabel('מספר ראשים (k)')
    ax2.set_ylabel('הסתברות')
    ax2.set_title('התפלגות בינומית למספרי הטלות שונים')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. צמיחת הפקטוריאל
    n_vals = list(range(1, 11))
    fact_vals = [factorial(n) for n in n_vals]
    
    ax3.semilogy(n_vals, fact_vals, 'o-', color='#0047AB', linewidth=2, markersize=8)
    ax3.set_xlabel('n')
    ax3.set_ylabel('n! (סקלה לוגריתמית)')
    ax3.set_title('צמיחת הפקטוריאל')
    ax3.grid(True, alpha=0.3)
    
    # הוספת תוויות
    for i, (n, fact) in enumerate(zip(n_vals, fact_vals)):
        if i % 2 == 0:  # הצגת כל תווית שנייה
            ax3.text(n, fact, f'{fact:,}', ha='center', va='bottom', fontsize=8)
    
    # 4. השוואה תיאורטי מול ניסיוני
    n_flips = 6
    k_vals = list(range(n_flips + 1))
    
    # תיאורטי
    theoretical_probs = [combinations_formula(n_flips, k) / (2**n_flips) for k in k_vals]
    
    # ניסיוני (סימולציה)
    n_sim = 10000
    sim_results = []
    for _ in range(n_sim):
        flips = [random.choice([0, 1]) for _ in range(n_flips)]
        sim_results.append(sum(flips))
    
    sim_counts = Counter(sim_results)
    experimental_probs = [sim_counts.get(k, 0) / n_sim for k in k_vals]
    
    x = np.arange(len(k_vals))
    width = 0.35
    
    ax4.bar(x - width/2, theoretical_probs, width, label='תיאורטי', 
           color='#0047AB', alpha=0.7)
    ax4.bar(x + width/2, experimental_probs, width, label='ניסיוני', 
           color='#3B82F6', alpha=0.7)
    
    ax4.set_xlabel('מספר ראשים')
    ax4.set_ylabel('הסתברות')
    ax4.set_title(f'השוואה: {n_flips} הטלות מטבע')
    ax4.set_xticks(x)
    ax4.set_xticklabels(k_vals)
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return fig

def main():
    """
    הפונקציה הראשית
    Main function
    """
    print("שקף 5: קומבינטוריקה ותורת הספירה")
    print("Slide 5: Combinatorics")
    print("=" * 60)
    
    # מושגי יסוד
    factorial_examples()
    combinations_examples()
    
    # דוגמה מפורטת
    detailed_calculation_example()
    
    # יישום על הטלת מטבעות
    coin_flip_combinatorics()
    
    # פתרון תרגילים
    solve_textbook_exercises()
    
    # נושאים מתקדמים
    pascal_triangle()
    binomial_theorem()
    
    # סימולציה
    simulate_combinatorics()
    
    # ויזואליזציה
    try:
        visualize_combinatorics()
    except Exception as e:
        print(f"שגיאה בויזואליזציה: {e}")
    
    print("\n" + "=" * 60)
    print("סיכום קומבינטוריקה:")
    print("• פקטוריאל: n! = n × (n-1) × ... × 2 × 1")
    print("• קומבינציות: C(n,k) = n! / (k!(n-k)!)")
    print("• משולש פסקל: כל איבר הוא C(n,k)")
    print("• יישום בהסתברות: ספירת תוצאות אפשריות")
    print("• התפלגות בינומית: P(X=k) = C(n,k) × p^k × (1-p)^(n-k)")
    print("\nסיום שקף 5 - סיום המצגת!")
    print("תודה רבה!")

if __name__ == "__main__":
    # הגדרת זרע אקראי לשחזור תוצאות
    random.seed(42)
    np.random.seed(42)
    
    main()

