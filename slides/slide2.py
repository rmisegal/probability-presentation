#!/usr/bin/env python3
"""
Slide 2: Events and Sample Spaces
Demonstration of basic probability concepts with events and sample spaces

Copyright (c) 2025 Dr. Yoram Segal. All rights reserved.
כל הזכויות שמורות לד"ר יורם סגל
"""

import random
from fractions import Fraction
import matplotlib.pyplot as plt
import numpy as np

def coin_flip_example():
    """
    דוגמת הטלת מטבע
    Coin flip example
    """
    print("=== הטלת מטבע (Coin Flip) ===")
    sample_space = ['H', 'T']  # מרחב המדגם
    print(f"מרחב המדגם (Sample Space): Ω = {sample_space}")
    print(f"גודל מרחב המדגם: |Ω| = {len(sample_space)}")
    
    # אירוע: קבלת ראש
    event_heads = ['H']
    prob_heads = len(event_heads) / len(sample_space)
    print(f"\nאירוע A: קבלת ראש = {event_heads}")
    print(f"P(H) = |A|/|Ω| = {len(event_heads)}/{len(sample_space)} = {prob_heads}")
    
    # אירוע: קבלת עץ
    event_tails = ['T']
    prob_tails = len(event_tails) / len(sample_space)
    print(f"\nאירוע B: קבלת עץ = {event_tails}")
    print(f"P(T) = |B|/|Ω| = {len(event_tails)}/{len(sample_space)} = {prob_tails}")
    
    # בדיקה: סכום ההסתברויות
    total_prob = prob_heads + prob_tails
    print(f"\nבדיקה: P(H) + P(T) = {prob_heads} + {prob_tails} = {total_prob}")
    
    return sample_space, prob_heads, prob_tails

def card_deck_example():
    """
    דוגמת חפיסת קלפים
    Card deck example
    """
    print("\n=== חפיסת קלפים (Card Deck) ===")
    
    # יצירת חפיסה
    suits = ['♠', '♥', '♦', '♣']  # סמלים: spades, hearts, diamonds, clubs
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    deck = [(rank, suit) for suit in suits for rank in ranks]
    print(f"מרחב המדגם: חפיסת 52 קלפים")
    print(f"גודל מרחב המדגם: |Ω| = {len(deck)}")
    
    # אירועים שונים
    aces = [card for card in deck if card[0] == 'A']
    spades = [card for card in deck if card[1] == '♠']
    ace_of_spades = [card for card in deck if card == ('A', '♠')]
    
    print(f"\nאירוע A: משיכת אס")
    print(f"מספר אסים: {len(aces)}")
    print(f"P(ace) = {len(aces)}/{len(deck)} = {len(aces)/len(deck):.3f}")
    
    print(f"\nאירוע B: משיכת עלה")
    print(f"מספר עלים: {len(spades)}")
    print(f"P(spade) = {len(spades)}/{len(deck)} = {len(spades)/len(deck):.3f}")
    
    print(f"\nאירוע C: משיכת אס עלים")
    print(f"מספר אס עלים: {len(ace_of_spades)}")
    print(f"P(ace of spades) = {len(ace_of_spades)}/{len(deck)} = {len(ace_of_spades)/len(deck):.3f}")
    
    # חישוב P(ace OR spade)
    ace_or_spade = set(aces + spades)  # איחוד ללא כפילויות
    print(f"\nאירוע D: אס או עלה")
    print(f"P(ace OR spade) = {len(ace_or_spade)}/{len(deck)} = {len(ace_or_spade)/len(deck):.3f}")
    
    # בדיקה עם נוסחת האיחוד
    prob_ace = len(aces) / len(deck)
    prob_spade = len(spades) / len(deck)
    prob_ace_and_spade = len(ace_of_spades) / len(deck)
    prob_union_formula = prob_ace + prob_spade - prob_ace_and_spade
    
    print(f"\nבדיקה עם נוסחת האיחוד:")
    print(f"P(A ∪ B) = P(A) + P(B) - P(A ∩ B)")
    print(f"P(ace OR spade) = {prob_ace:.3f} + {prob_spade:.3f} - {prob_ace_and_spade:.3f} = {prob_union_formula:.3f}")
    
    return deck, aces, spades, ace_of_spades

def dice_example():
    """
    דוגמת הטלת קובייה
    Dice example
    """
    print("\n=== הטלת קובייה (Dice Roll) ===")
    sample_space = list(range(1, 7))
    print(f"מרחב המדגם: Ω = {sample_space}")
    print(f"גודל מרחב המדגם: |Ω| = {len(sample_space)}")
    
    # אירועים שונים
    even_numbers = [2, 4, 6]
    odd_numbers = [1, 3, 5]
    greater_than_4 = [5, 6]
    less_than_3 = [1, 2]
    
    print(f"\nאירוע A: מספר זוגי = {even_numbers}")
    print(f"P(זוגי) = {len(even_numbers)}/{len(sample_space)} = {len(even_numbers)/len(sample_space):.3f}")
    
    print(f"\nאירוע B: מספר אי-זוגי = {odd_numbers}")
    print(f"P(אי-זוגי) = {len(odd_numbers)}/{len(sample_space)} = {len(odd_numbers)/len(sample_space):.3f}")
    
    print(f"\nאירוע C: גדול מ-4 = {greater_than_4}")
    print(f"P(>4) = {len(greater_than_4)}/{len(sample_space)} = {len(greater_than_4)/len(sample_space):.3f}")
    
    print(f"\nאירוע D: קטן מ-3 = {less_than_3}")
    print(f"P(<3) = {len(less_than_3)}/{len(sample_space)} = {len(less_than_3)/len(sample_space):.3f}")
    
    # אירועים משלימים
    print(f"\nבדיקת אירועים משלימים:")
    print(f"P(זוגי) + P(אי-זוגי) = {len(even_numbers)/len(sample_space):.3f} + {len(odd_numbers)/len(sample_space):.3f} = {(len(even_numbers) + len(odd_numbers))/len(sample_space):.3f}")
    
    return sample_space, even_numbers, odd_numbers, greater_than_4

def impossible_and_certain_events():
    """
    אירועים בלתי אפשריים ובטוחים
    Impossible and certain events
    """
    print("\n=== אירועים מיוחדים ===")
    
    # בהטלת קובייה
    sample_space = list(range(1, 7))
    
    # אירוע בטוח
    certain_event = sample_space  # כל התוצאות
    print(f"אירוע בטוח (קבלת מספר 1-6): {certain_event}")
    print(f"P(בטוח) = {len(certain_event)}/{len(sample_space)} = {len(certain_event)/len(sample_space)}")
    
    # אירוע בלתי אפשרי
    impossible_event = []  # אין תוצאות
    print(f"\nאירוע בלתי אפשרי (קבלת 7): {impossible_event}")
    print(f"P(בלתי אפשרי) = {len(impossible_event)}/{len(sample_space)} = {len(impossible_event)/len(sample_space)}")
    
    # בחפיסת קלפים
    print(f"\nבחפיסת קלפים:")
    print(f"P(קלף) = 52/52 = 1.000 (אירוע בטוח)")
    print(f"P(תפוח) = 0/52 = 0.000 (אירוע בלתי אפשרי)")

def visualize_sample_spaces():
    """
    ויזואליזציה של מרחבי מדגם
    Visualization of sample spaces
    """
    print("\n=== ויזואליזציה ===")
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # הטלת מטבע
    coin_outcomes = ['ראש', 'עץ']
    coin_probs = [0.5, 0.5]
    ax1.bar(coin_outcomes, coin_probs, color=['#0047AB', '#3B82F6'])
    ax1.set_title('הטלת מטבע', fontsize=12)
    ax1.set_ylabel('הסתברות')
    ax1.set_ylim(0, 1)
    
    # הטלת קובייה
    dice_outcomes = list(range(1, 7))
    dice_probs = [1/6] * 6
    ax2.bar(dice_outcomes, dice_probs, color='#1E3A8A')
    ax2.set_title('הטלת קובייה', fontsize=12)
    ax2.set_xlabel('תוצאה')
    ax2.set_ylabel('הסתברות')
    ax2.set_ylim(0, 0.3)
    
    # קלפים - סוגי קלפים
    suits = ['♠', '♥', '♦', '♣']
    suit_probs = [0.25] * 4
    colors = ['black', 'red', 'red', 'black']
    ax3.bar(suits, suit_probs, color=colors)
    ax3.set_title('סוגי קלפים', fontsize=12)
    ax3.set_ylabel('הסתברות')
    ax3.set_ylim(0, 0.3)
    
    # קלפים - ערכי קלפים
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    rank_probs = [4/52] * 13
    ax4.bar(ranks, rank_probs, color='#0047AB')
    ax4.set_title('ערכי קלפים', fontsize=12)
    ax4.set_xlabel('ערך')
    ax4.set_ylabel('הסתברות')
    ax4.set_ylim(0, 0.1)
    ax4.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    return fig

def main():
    """
    הפונקציה הראשית
    Main function
    """
    print("שקף 2: אירועים ומרחב המדגם")
    print("Slide 2: Events and Sample Spaces")
    print("=" * 60)
    
    # דוגמאות בסיסיות
    coin_data = coin_flip_example()
    card_data = card_deck_example()
    dice_data = dice_example()
    
    # אירועים מיוחדים
    impossible_and_certain_events()
    
    # ויזואליזציה
    try:
        visualize_sample_spaces()
    except Exception as e:
        print(f"שגיאה בויזואליזציה: {e}")
    
    print("\n" + "=" * 60)
    print("סיכום:")
    print("• מרחב המדגם (Ω) מכיל את כל התוצאות האפשריות")
    print("• אירוע הוא תת-קבוצה של מרחב המדגם")
    print("• P(A) = |A| / |Ω|")
    print("• 0 ≤ P(A) ≤ 1 לכל אירוע A")
    print("• P(Ω) = 1, P(∅) = 0")
    print("\nסיום שקף 2")

if __name__ == "__main__":
    # הגדרת זרע אקראי לשחזור תוצאות
    random.seed(42)
    np.random.seed(42)
    
    main()

