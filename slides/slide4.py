#!/usr/bin/env python3
"""
Slide 4: Combining Probabilities
Demonstration of probability combination rules and calculations

Copyright (c) 2025 Dr. Yoram Segal. All rights reserved.
כל הזכויות שמורות לד"ר יורם סגל
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
import itertools
from collections import Counter

def multiplication_rule():
    """
    כלל הכפל לאירועים עצמאיים
    Multiplication rule for independent events
    """
    print("=== כלל הכפל (Multiplication Rule) ===")
    print("עבור אירועים עצמאיים: P(A ∩ B) = P(A) × P(B)")
    
    # הטלת מטבע
    p_heads = Fraction(1, 2)
    print(f"\nהטלת מטבע:")
    print(f"P(H) = {p_heads} = {float(p_heads):.3f}")
    
    print(f"\nרצפי ראשים:")
    print("רצף | הסתברות | שבר | עשרוני")
    print("-" * 40)
    
    for n in range(1, 7):
        p_sequence = p_heads ** n
        sequence = 'H' * n
        print(f"{sequence:6s} | (1/2)^{n} | {p_sequence} | {float(p_sequence):.6f}")
    
    # דוגמה מעשית
    print(f"\nדוגמה מעשית:")
    print(f"מה הסיכוי לקבל 10 ראשים רצופים?")
    p_10_heads = p_heads ** 10
    print(f"P(10 ראשים) = (1/2)^10 = {p_10_heads} = {float(p_10_heads):.6f}")
    print(f"זה אומר שבממוצע זה יקרה פעם אחת מכל {2**10:,} ניסויים!")

def addition_rule():
    """
    כלל החיבור לאירועים
    Addition rule for events
    """
    print("\n=== כלל החיבור (Addition Rule) ===")
    print("P(A ∪ B) = P(A) + P(B) - P(A ∩ B)")
    
    # הטלת קובייה
    print(f"\nדוגמה: הטלת קובייה")
    print(f"מרחב המדגם: {1, 2, 3, 4, 5, 6}")
    
    # הגדרת אירועים
    even_numbers = {2, 4, 6}
    greater_than_4 = {5, 6}
    intersection = even_numbers & greater_than_4  # חיתוך
    union = even_numbers | greater_than_4  # איחוד
    
    print(f"\nאירוע A: מספר זוגי = {even_numbers}")
    print(f"אירוע B: גדול מ-4 = {greater_than_4}")
    print(f"A ∩ B (חיתוך) = {intersection}")
    print(f"A ∪ B (איחוד) = {union}")
    
    # חישוב הסתברויות
    p_even = Fraction(len(even_numbers), 6)
    p_greater_4 = Fraction(len(greater_than_4), 6)
    p_intersection = Fraction(len(intersection), 6)
    p_union_calculated = p_even + p_greater_4 - p_intersection
    p_union_direct = Fraction(len(union), 6)
    
    print(f"\nחישובי הסתברות:")
    print(f"P(A) = P(זוגי) = {p_even} = {float(p_even):.3f}")
    print(f"P(B) = P(>4) = {p_greater_4} = {float(p_greater_4):.3f}")
    print(f"P(A ∩ B) = {p_intersection} = {float(p_intersection):.3f}")
    print(f"P(A ∪ B) = P(A) + P(B) - P(A ∩ B) = {p_union_calculated} = {float(p_union_calculated):.3f}")
    print(f"בדיקה ישירה: P(A ∪ B) = {p_union_direct} = {float(p_union_direct):.3f}")

def card_deck_example():
    """
    דוגמת חפיסת קלפים
    Card deck example
    """
    print("\n=== דוגמת חפיסת קלפים ===")
    
    # הגדרת חפיסה
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    
    print(f"חפיסת קלפים: {len(deck)} קלפים")
    
    # הגדרת אירועים
    aces = [card for card in deck if card[0] == 'A']
    spades = [card for card in deck if card[1] == '♠']
    ace_of_spades = [card for card in deck if card == ('A', '♠')]
    
    print(f"\nאירוע A: משיכת אס")
    print(f"מספר אסים: {len(aces)}")
    print(f"אסים: {aces}")
    
    print(f"\nאירוע B: משיכת עלה")
    print(f"מספר עלים: {len(spades)}")
    
    print(f"\nאירוע A ∩ B: אס עלים")
    print(f"אס עלים: {ace_of_spades}")
    
    # חישוב הסתברויות
    p_ace = Fraction(len(aces), len(deck))
    p_spade = Fraction(len(spades), len(deck))
    p_ace_and_spade = Fraction(len(ace_of_spades), len(deck))
    
    print(f"\nחישובי הסתברות:")
    print(f"P(אס) = {len(aces)}/{len(deck)} = {p_ace} = {float(p_ace):.3f}")
    print(f"P(עלה) = {len(spades)}/{len(deck)} = {p_spade} = {float(p_spade):.3f}")
    print(f"P(אס ∩ עלה) = {len(ace_of_spades)}/{len(deck)} = {p_ace_and_spade} = {float(p_ace_and_spade):.3f}")
    
    # חישוב P(אס או עלה)
    p_ace_or_spade = p_ace + p_spade - p_ace_and_spade
    
    print(f"\nP(אס ∪ עלה) = P(אס) + P(עלה) - P(אס ∩ עלה)")
    print(f"             = {p_ace} + {p_spade} - {p_ace_and_spade}")
    print(f"             = {p_ace_or_spade} = {float(p_ace_or_spade):.3f}")
    
    # בדיקה ישירה
    ace_or_spade_cards = set(aces + spades)
    p_direct = Fraction(len(ace_or_spade_cards), len(deck))
    print(f"בדיקה ישירה: {len(ace_or_spade_cards)}/{len(deck)} = {p_direct} = {float(p_direct):.3f}")

def complex_combinations():
    """
    שילובים מורכבים של הסתברויות
    Complex probability combinations
    """
    print("\n=== שילובים מורכבים ===")
    
    # דוגמה 1: לפחות אחד מ-n ניסויים
    print("1. הסתברות להצלחה בלפחות אחד מ-n ניסויים:")
    print("   P(לפחות אחד) = 1 - P(כולם נכשלים)")
    
    p_success = 0.3  # הסתברות להצלחה בניסוי בודד
    p_failure = 1 - p_success
    
    print(f"\nהסתברות להצלחה בניסוי בודד: {p_success}")
    print(f"הסתברות לכישלון בניסוי בודד: {p_failure}")
    
    print(f"\nמספר ניסויים | P(כולם נכשלים) | P(לפחות אחד מצליח)")
    print("-" * 55)
    
    for n in range(1, 6):
        p_all_fail = p_failure ** n
        p_at_least_one = 1 - p_all_fail
        print(f"{n:13d} | {p_all_fail:15.4f} | {p_at_least_one:18.4f}")
    
    # דוגמה 2: שילוב של מטבע וקובייה
    print(f"\n2. שילוב מטבע וקובייה (אירועים עצמאיים):")
    p_heads = 0.5
    p_even_dice = 3/6
    p_both = p_heads * p_even_dice
    
    print(f"P(ראש במטבע) = {p_heads}")
    print(f"P(זוגי בקובייה) = {p_even_dice:.3f}")
    print(f"P(ראש וזוגי) = {p_heads} × {p_even_dice:.3f} = {p_both:.3f}")

def simulate_combinations():
    """
    סימולציה של שילובי הסתברויות
    Simulation of probability combinations
    """
    print("\n=== סימולציה ===")
    
    n_experiments = 10000
    
    # סימולציה 1: רצף של 5 ראשים
    print(f"1. סימולציה: רצף של 5 ראשים ב-{n_experiments:,} ניסויים")
    
    successes = 0
    for _ in range(n_experiments):
        # הטלת 5 מטבעות
        flips = [random.choice(['H', 'T']) for _ in range(5)]
        if all(flip == 'H' for flip in flips):
            successes += 1
    
    observed_prob = successes / n_experiments
    theoretical_prob = (0.5) ** 5
    
    print(f"תוצאות ניסיוניות: {successes} הצלחות מתוך {n_experiments:,}")
    print(f"הסתברות ניסיונית: {observed_prob:.4f}")
    print(f"הסתברות תיאורטית: {theoretical_prob:.4f}")
    print(f"הפרש: {abs(observed_prob - theoretical_prob):.4f}")
    
    # סימולציה 2: אס או עלה
    print(f"\n2. סימולציה: אס או עלה ב-{n_experiments:,} משיכות קלף")
    
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    
    ace_or_spade_count = 0
    for _ in range(n_experiments):
        card = random.choice(deck)
        if card[0] == 'A' or card[1] == '♠':
            ace_or_spade_count += 1
    
    observed_prob_cards = ace_or_spade_count / n_experiments
    theoretical_prob_cards = 16/52  # 4 אסים + 13 עלים - 1 אס עלים
    
    print(f"תוצאות ניסיוניות: {ace_or_spade_count} הצלחות מתוך {n_experiments:,}")
    print(f"הסתברות ניסיונית: {observed_prob_cards:.4f}")
    print(f"הסתברות תיאורטית: {theoretical_prob_cards:.4f}")
    print(f"הפרש: {abs(observed_prob_cards - theoretical_prob_cards):.4f}")

def visualize_combinations():
    """
    ויזואליזציה של שילובי הסתברויות
    Visualization of probability combinations
    """
    print("\n=== ויזואליזציה ===")
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. הסתברות רצפי ראשים
    sequence_lengths = range(1, 8)
    probabilities = [(0.5)**n for n in sequence_lengths]
    
    ax1.bar(sequence_lengths, probabilities, color='#0047AB', alpha=0.7)
    ax1.set_xlabel('אורך רצף ראשים')
    ax1.set_ylabel('הסתברות')
    ax1.set_title('הסתברות רצפי ראשים')
    ax1.set_yscale('log')
    ax1.grid(True, alpha=0.3)
    
    # הוספת תוויות
    for i, prob in enumerate(probabilities):
        ax1.text(i+1, prob, f'{prob:.4f}', ha='center', va='bottom', fontsize=8)
    
    # 2. השוואה: תיאורטי מול ניסיוני
    n_trials = [100, 500, 1000, 5000, 10000]
    theoretical = 0.03125  # (1/2)^5
    experimental_results = []
    
    for n in n_trials:
        successes = 0
        for _ in range(n):
            flips = [random.choice([0, 1]) for _ in range(5)]
            if all(flip == 1 for flip in flips):
                successes += 1
        experimental_results.append(successes / n)
    
    ax2.plot(n_trials, experimental_results, 'o-', label='ניסיוני', color='#3B82F6', linewidth=2, markersize=8)
    ax2.axhline(y=theoretical, color='red', linestyle='--', label='תיאורטי', linewidth=2)
    ax2.set_xlabel('מספר ניסויים')
    ax2.set_ylabel('הסתברות')
    ax2.set_title('התכנסות לערך התיאורטי')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. כלל החיבור - דיאגרמת ון
    # יצירת דיאגרמת ון פשוטה
    circle1 = plt.Circle((0.3, 0.5), 0.3, alpha=0.3, color='blue', label='A')
    circle2 = plt.Circle((0.7, 0.5), 0.3, alpha=0.3, color='red', label='B')
    
    ax3.add_patch(circle1)
    ax3.add_patch(circle2)
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.set_aspect('equal')
    ax3.set_title('דיאגרמת ון: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)')
    
    # הוספת תוויות
    ax3.text(0.2, 0.5, 'A', fontsize=14, ha='center', va='center')
    ax3.text(0.8, 0.5, 'B', fontsize=14, ha='center', va='center')
    ax3.text(0.5, 0.5, 'A∩B', fontsize=10, ha='center', va='center')
    ax3.axis('off')
    
    # 4. הסתברות "לפחות אחד" כפונקציה של מספר ניסויים
    n_trials_range = range(1, 11)
    p_success = 0.3
    p_at_least_one = [1 - (1 - p_success)**n for n in n_trials_range]
    
    ax4.plot(n_trials_range, p_at_least_one, 'o-', color='#1E3A8A', linewidth=2, markersize=8)
    ax4.set_xlabel('מספר ניסויים')
    ax4.set_ylabel('P(לפחות הצלחה אחת)')
    ax4.set_title('הסתברות להצלחה בלפחות ניסוי אחד')
    ax4.grid(True, alpha=0.3)
    ax4.set_ylim(0, 1)
    
    # הוספת תוויות נקודות
    for i, prob in enumerate(p_at_least_one):
        if i % 2 == 0:  # הצגת כל נקודה שנייה
            ax4.text(i+1, prob + 0.02, f'{prob:.2f}', ha='center', va='bottom', fontsize=8)
    
    plt.tight_layout()
    plt.show()
    
    return fig

def main():
    """
    הפונקציה הראשית
    Main function
    """
    print("שקף 4: שילוב הסתברויות")
    print("Slide 4: Combining Probabilities")
    print("=" * 60)
    
    # כללי שילוב בסיסיים
    multiplication_rule()
    addition_rule()
    
    # דוגמאות מורכבות
    card_deck_example()
    complex_combinations()
    
    # סימולציות
    simulate_combinations()
    
    # ויזואליזציה
    try:
        visualize_combinations()
    except Exception as e:
        print(f"שגיאה בויזואליזציה: {e}")
    
    print("\n" + "=" * 60)
    print("סיכום כללי השילוב:")
    print("• כלל הכפל (עצמאיים): P(A ∩ B) = P(A) × P(B)")
    print("• כלל החיבור (כללי): P(A ∪ B) = P(A) + P(B) - P(A ∩ B)")
    print("• כלל החיבור (זרים): P(A ∪ B) = P(A) + P(B)")
    print("• משלים: P(A') = 1 - P(A)")
    print("• לפחות אחד: P(≥1) = 1 - P(כולם נכשלים)")
    print("\nסיום שקף 4")

if __name__ == "__main__":
    # הגדרת זרע אקראי לשחזור תוצאות
    random.seed(42)
    np.random.seed(42)
    
    main()

