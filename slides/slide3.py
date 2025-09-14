#!/usr/bin/env python3
"""
Slide 3: Multiple Independent Observations
Demonstration of probability calculations for multiple independent events

Copyright (c) 2025 Dr. Yoram Segal. All rights reserved.
כל הזכויות שמורות לד"ר יורם סגל
"""

import itertools
import random
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
from collections import Counter
import math

def multiple_coin_flips(n):
    """
    חישוב כל התוצאות האפשריות ל-n הטלות מטבע
    Calculate all possible outcomes for n coin flips
    """
    print(f"=== הטלת {n} מטבעות (Flipping {n} coins) ===")
    
    # יצירת כל התוצאות האפשריות
    outcomes = list(itertools.product(['H', 'T'], repeat=n))
    print(f"מספר תוצאות אפשריות: 2^{n} = {len(outcomes)}")
    print(f"תוצאות אפשריות:")
    
    # הדפסת התוצאות בצורה מסודרת
    for i, outcome in enumerate(outcomes):
        outcome_str = ''.join(outcome)
        print(f"  {i+1:2d}. {outcome_str}")
    
    # ספירת ראשים בכל תוצאה
    heads_count = {}
    for outcome in outcomes:
        h_count = outcome.count('H')
        if h_count not in heads_count:
            heads_count[h_count] = []
        heads_count[h_count].append(''.join(outcome))
    
    print(f"\nהתפלגות מספר ראשים:")
    print("מספר ראשים | מספר דרכים | הסתברות | דוגמאות")
    print("-" * 60)
    
    for heads in sorted(heads_count.keys()):
        count = len(heads_count[heads])
        prob = count / len(outcomes)
        examples = ', '.join(heads_count[heads][:3])  # הצגת 3 דוגמאות ראשונות
        if len(heads_count[heads]) > 3:
            examples += "..."
        print(f"{heads:11d} | {count:11d} | {prob:8.3f} | {examples}")
    
    return outcomes, heads_count

def consecutive_heads_probability():
    """
    הסתברות לרצפי ראשים
    Probability of consecutive heads
    """
    print("\n=== הסתברות רצפי ראשים (Consecutive Heads Probability) ===")
    
    print("רצף | הסתברות | חישוב")
    print("-" * 35)
    
    for n in range(1, 6):
        prob = (1/2) ** n
        heads_str = 'H' * n
        calculation = f"(1/2)^{n}"
        print(f"{heads_str:4s} | {prob:8.4f} | {calculation}")
    
    # דוגמה מעשית
    print(f"\nדוגמה מעשית:")
    print(f"מה הסיכוי לקבל 5 ראשים רצופים?")
    print(f"P(HHHHH) = (1/2)^5 = {(1/2)**5:.5f} = {Fraction(1, 32)}")
    print(f"כלומר, בממוצע זה יקרה פעם אחת מכל {2**5} ניסויים")

def binomial_probability(n, k, p=0.5):
    """
    חישוב הסתברות בינומית
    Calculate binomial probability
    """
    # חישוב C(n,k)
    combinations = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    
    # חישוב ההסתברות
    probability = combinations * (p ** k) * ((1 - p) ** (n - k))
    
    return combinations, probability

def demonstrate_binomial_distribution():
    """
    הדגמת התפלגות בינומית
    Demonstrate binomial distribution
    """
    print("\n=== התפלגות בינומית (Binomial Distribution) ===")
    
    n = 5  # מספר הטלות
    p = 0.5  # הסתברות להצלחה (ראש)
    
    print(f"הטלת {n} מטבעות, הסתברות לראש = {p}")
    print(f"נוסחה: P(X = k) = C(n,k) × p^k × (1-p)^(n-k)")
    print()
    print("k | C(n,k) | הסתברות | אחוז")
    print("-" * 35)
    
    total_prob = 0
    for k in range(n + 1):
        combinations, prob = binomial_probability(n, k, p)
        percentage = prob * 100
        total_prob += prob
        print(f"{k} | {combinations:6d} | {prob:8.4f} | {percentage:5.1f}%")
    
    print("-" * 35)
    print(f"סה\"כ: {total_prob:.4f} (צריך להיות 1.000)")

def simulate_multiple_experiments(n_coins, n_experiments=1000):
    """
    סימולציה של ניסויים מרובים
    Simulate multiple experiments
    """
    print(f"\n=== סימולציה: {n_experiments} ניסויים של {n_coins} הטלות ===")
    
    results = []
    for _ in range(n_experiments):
        # הטלת n_coins מטבעות
        flips = [random.choice(['H', 'T']) for _ in range(n_coins)]
        heads_count = flips.count('H')
        results.append(heads_count)
    
    # ספירת התוצאות
    result_counts = Counter(results)
    
    print("מספר ראשים | תדירות | הסתברות ניסיונית | הסתברות תיאורטית")
    print("-" * 70)
    
    for k in range(n_coins + 1):
        observed_count = result_counts.get(k, 0)
        observed_prob = observed_count / n_experiments
        
        # חישוב הסתברות תיאורטית
        _, theoretical_prob = binomial_probability(n_coins, k)
        
        print(f"{k:11d} | {observed_count:8d} | {observed_prob:17.3f} | {theoretical_prob:18.3f}")
    
    return results

def visualize_multiple_observations():
    """
    ויזואליזציה של תצפיות מרובות
    Visualization of multiple observations
    """
    print("\n=== ויזואליזציה ===")
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. השוואת הסתברויות תיאורטיות לניסיוניות
    n_coins = 4
    n_experiments = 1000
    
    # סימולציה
    simulated_results = simulate_multiple_experiments(n_coins, n_experiments)
    result_counts = Counter(simulated_results)
    
    # נתונים לגרף
    k_values = list(range(n_coins + 1))
    observed_probs = [result_counts.get(k, 0) / n_experiments for k in k_values]
    theoretical_probs = [binomial_probability(n_coins, k)[1] for k in k_values]
    
    x = np.arange(len(k_values))
    width = 0.35
    
    ax1.bar(x - width/2, observed_probs, width, label='ניסיוני', color='#3B82F6', alpha=0.7)
    ax1.bar(x + width/2, theoretical_probs, width, label='תיאורטי', color='#1E3A8A', alpha=0.7)
    ax1.set_xlabel('מספר ראשים')
    ax1.set_ylabel('הסתברות')
    ax1.set_title(f'השוואה: {n_coins} הטלות מטבע')
    ax1.set_xticks(x)
    ax1.set_xticklabels(k_values)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. הסתברות רצפי ראשים
    sequences = range(1, 8)
    probabilities = [(1/2)**n for n in sequences]
    
    ax2.bar(sequences, probabilities, color='#0047AB')
    ax2.set_xlabel('אורך רצף ראשים')
    ax2.set_ylabel('הסתברות')
    ax2.set_title('הסתברות רצפי ראשים')
    ax2.set_yscale('log')
    ax2.grid(True, alpha=0.3)
    
    # הוספת תוויות על העמודות
    for i, prob in enumerate(probabilities):
        ax2.text(i+1, prob, f'{prob:.4f}', ha='center', va='bottom')
    
    # 3. התפלגות בינומית למספרי הטלות שונים
    n_values = [3, 5, 10]
    colors = ['#0047AB', '#3B82F6', '#1E3A8A']
    
    for i, n in enumerate(n_values):
        k_vals = list(range(n + 1))
        probs = [binomial_probability(n, k)[1] for k in k_vals]
        ax3.plot(k_vals, probs, 'o-', label=f'n={n}', color=colors[i], linewidth=2, markersize=6)
    
    ax3.set_xlabel('מספר ראשים (k)')
    ax3.set_ylabel('הסתברות')
    ax3.set_title('התפלגות בינומית למספרי הטלות שונים')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 4. התכנסות לחוק המספרים הגדולים
    sample_sizes = [10, 50, 100, 500, 1000, 5000]
    proportions = []
    
    for size in sample_sizes:
        flips = [random.choice([0, 1]) for _ in range(size)]  # 0=T, 1=H
        proportion = sum(flips) / size
        proportions.append(proportion)
    
    ax4.plot(sample_sizes, proportions, 'o-', color='#0047AB', linewidth=2, markersize=8)
    ax4.axhline(y=0.5, color='red', linestyle='--', linewidth=2, label='הסתברות תיאורטית (0.5)')
    ax4.set_xlabel('גודל מדגם')
    ax4.set_ylabel('שיעור ראשים')
    ax4.set_title('התכנסות לחוק המספרים הגדולים')
    ax4.set_xscale('log')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return fig

def independence_examples():
    """
    דוגמאות לעצמאות ואי-עצמאות
    Examples of independence and dependence
    """
    print("\n=== דוגמאות לעצמאות ואי-עצמאות ===")
    
    print("1. אירועים עצמאיים:")
    print("   • הטלות מטבע רצופות")
    print("   • הטלות קובייה רצופות")
    print("   • משיכת קלפים עם החזרה")
    print("   P(A and B) = P(A) × P(B)")
    
    print("\n2. אירועים תלויים:")
    print("   • משיכת קלפים ללא החזרה")
    print("   • בחירת כדורים מקופסה ללא החזרה")
    print("   P(A and B) = P(A) × P(B|A)")
    
    # דוגמה מספרית
    print("\nדוגמה מספרית:")
    print("משיכת 2 קלפים מחפיסה:")
    
    print("\nעם החזרה (עצמאי):")
    print("P(2 אסים) = P(אס) × P(אס) = 4/52 × 4/52 = 16/2704 ≈ 0.0059")
    
    print("\nללא החזרה (תלוי):")
    print("P(2 אסים) = P(אס ראשון) × P(אס שני|אס ראשון)")
    print("          = 4/52 × 3/51 = 12/2652 ≈ 0.0045")

def main():
    """
    הפונקציה הראשית
    Main function
    """
    print("שקף 3: תצפיות עצמאיות מרובות")
    print("Slide 3: Multiple Independent Observations")
    print("=" * 60)
    
    # דוגמאות בסיסיות
    outcomes_2, heads_count_2 = multiple_coin_flips(2)
    outcomes_3, heads_count_3 = multiple_coin_flips(3)
    
    # הסתברות רצפים
    consecutive_heads_probability()
    
    # התפלגות בינומית
    demonstrate_binomial_distribution()
    
    # סימולציה
    simulation_results = simulate_multiple_experiments(3, 1000)
    
    # דוגמאות עצמאות
    independence_examples()
    
    # ויזואליזציה
    try:
        visualize_multiple_observations()
    except Exception as e:
        print(f"שגיאה בויזואליזציה: {e}")
    
    print("\n" + "=" * 60)
    print("סיכום:")
    print("• אירועים עצמאיים: P(A ∩ B) = P(A) × P(B)")
    print("• מספר תוצאות אפשריות ל-n הטלות: 2^n")
    print("• התפלגות בינומית: P(X=k) = C(n,k) × p^k × (1-p)^(n-k)")
    print("• חוק המספרים הגדולים: התכנסות לערך הצפוי")
    print("\nסיום שקף 3")

if __name__ == "__main__":
    # הגדרת זרע אקראי לשחזור תוצאות
    random.seed(42)
    np.random.seed(42)
    
    main()

