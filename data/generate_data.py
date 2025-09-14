#!/usr/bin/env python3
"""
Data Generation Script for Probability Presentation
Generates all datasets needed for the probability theory slides

Copyright (c) 2025 Dr. Yoram Segal. All rights reserved.
כל הזכויות שמורות לד"ר יורם סגל
"""

import numpy as np
import pandas as pd
import json
import os
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

def generate_coin_flip_data():
    """Generate data for law of large numbers demonstration"""
    ns = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096])
    heads_count = [np.random.binomial(n, 0.5) for n in ns]
    proportion_heads = np.array(heads_count) / ns
    
    data = {
        'n_flips': ns.tolist(),
        'heads_count': heads_count,
        'proportion_heads': proportion_heads.tolist(),
        'expected_value': 0.5
    }
    
    with open('coin_flip_law_of_large_numbers.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    return data

def generate_probability_distribution_data():
    """Generate data for 5-coin flip probability distribution"""
    n_experiments = 1000
    heads_count = np.random.binomial(5, 0.5, n_experiments)
    
    heads, event_count = np.unique(heads_count, return_counts=True)
    event_proba = event_count / n_experiments
    
    # Theoretical probabilities
    from math import factorial
    def coinflip_prob(n, k):
        n_choose_k = factorial(n)/(factorial(k)*factorial(n-k))
        return n_choose_k/2**n
    
    theoretical_proba = [coinflip_prob(5, x) for x in range(6)]
    
    data = {
        'heads_values': heads.tolist(),
        'observed_counts': event_count.tolist(),
        'observed_probabilities': event_proba.tolist(),
        'theoretical_probabilities': theoretical_proba,
        'n_experiments': n_experiments
    }
    
    with open('probability_distribution_5_coins.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    return data

def generate_central_tendency_data():
    """Generate data for central tendency measures"""
    # Normal distribution (no skew)
    x_normal = stats.skewnorm.rvs(0, size=1000)
    
    # Skewed distribution
    x_skewed = stats.skewnorm.rvs(10, size=1000)
    
    normal_data = {
        'values': x_normal.tolist(),
        'mean': float(np.mean(x_normal)),
        'median': float(np.median(x_normal)),
        'mode': float(stats.mode(x_normal)[0]),
        'distribution_type': 'normal'
    }
    
    skewed_data = {
        'values': x_skewed.tolist(),
        'mean': float(np.mean(x_skewed)),
        'median': float(np.median(x_skewed)),
        'mode': float(stats.mode(x_skewed)[0]),
        'distribution_type': 'skewed'
    }
    
    with open('central_tendency_normal.json', 'w') as f:
        json.dump(normal_data, f, indent=2)
    
    with open('central_tendency_skewed.json', 'w') as f:
        json.dump(skewed_data, f, indent=2)
    
    return normal_data, skewed_data

def generate_quantiles_data():
    """Generate data for quantiles demonstration"""
    x = stats.skewnorm.rvs(10, size=1000)
    
    # Percentiles
    percentiles = np.percentile(x, [95, 99])
    
    # Quartiles
    quartiles = np.percentile(x, [25, 50, 75])
    
    # Deciles
    deciles = np.percentile(x, range(10, 100, 10))
    
    data = {
        'values': x.tolist(),
        'percentiles_95_99': percentiles.tolist(),
        'quartiles': quartiles.tolist(),
        'deciles': deciles.tolist(),
        'min_value': float(np.min(x)),
        'max_value': float(np.max(x))
    }
    
    with open('quantiles_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    return data

def generate_boxplot_data():
    """Generate data for box plot demonstration"""
    # Load iris dataset equivalent
    np.random.seed(42)
    
    # Generate synthetic iris-like data
    setosa_sepal_length = np.random.normal(5.0, 0.3, 50)
    versicolor_sepal_length = np.random.normal(5.9, 0.5, 50)
    virginica_sepal_length = np.random.normal(6.6, 0.6, 50)
    
    setosa_sepal_width = np.random.normal(3.4, 0.4, 50)
    versicolor_sepal_width = np.random.normal(2.8, 0.3, 50)
    virginica_sepal_width = np.random.normal(3.0, 0.3, 50)
    
    data = {
        'iris_data': {
            'setosa': {
                'sepal_length': setosa_sepal_length.tolist(),
                'sepal_width': setosa_sepal_width.tolist()
            },
            'versicolor': {
                'sepal_length': versicolor_sepal_length.tolist(),
                'sepal_width': versicolor_sepal_width.tolist()
            },
            'virginica': {
                'sepal_length': virginica_sepal_length.tolist(),
                'sepal_width': virginica_sepal_width.tolist()
            }
        }
    }
    
    # Generate tips-like data
    total_bills = np.random.exponential(15, 244) + 5
    tips = total_bills * np.random.normal(0.15, 0.05, 244)
    days = np.random.choice(['Thu', 'Fri', 'Sat', 'Sun'], 244)
    smoker = np.random.choice(['Yes', 'No'], 244)
    
    data['tips_data'] = {
        'total_bill': total_bills.tolist(),
        'tip': tips.tolist(),
        'day': days.tolist(),
        'smoker': smoker.tolist()
    }
    
    with open('boxplot_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    return data

def generate_dispersion_data():
    """Generate data for measures of dispersion"""
    x = stats.skewnorm.rvs(10, size=1000)
    
    mean_val = np.mean(x)
    variance = np.var(x)
    std_dev = np.std(x)
    
    # Calculate standard deviation bands
    std_bands = {
        'mean_minus_2std': float(mean_val - 2*std_dev),
        'mean_minus_1std': float(mean_val - std_dev),
        'mean': float(mean_val),
        'mean_plus_1std': float(mean_val + std_dev),
        'mean_plus_2std': float(mean_val + 2*std_dev)
    }
    
    data = {
        'values': x.tolist(),
        'mean': float(mean_val),
        'variance': float(variance),
        'standard_deviation': float(std_dev),
        'std_bands': std_bands
    }
    
    with open('dispersion_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    return data

def generate_advanced_visualization_data():
    """Generate complex data for D3.js visualization"""
    # Generate multi-dimensional probability data
    n_points = 500
    
    # Create correlated variables
    mean = [0, 0]
    cov = [[1, 0.7], [0.7, 1]]
    x, y = np.random.multivariate_normal(mean, cov, n_points).T
    
    # Add categorical variable
    categories = np.random.choice(['A', 'B', 'C'], n_points, p=[0.4, 0.35, 0.25])
    
    # Create probability density estimation
    from scipy.stats import gaussian_kde
    kde = gaussian_kde([x, y])
    
    # Create grid for contour plot
    xi = np.linspace(x.min(), x.max(), 50)
    yi = np.linspace(y.min(), y.max(), 50)
    Xi, Yi = np.meshgrid(xi, yi)
    zi = kde(np.vstack([Xi.ravel(), Yi.ravel()]))
    
    data = {
        'scatter_data': {
            'x': x.tolist(),
            'y': y.tolist(),
            'category': categories.tolist()
        },
        'contour_data': {
            'x_grid': Xi.tolist(),
            'y_grid': Yi.tolist(),
            'density': zi.reshape(Xi.shape).tolist()
        },
        'correlation': float(np.corrcoef(x, y)[0, 1])
    }
    
    with open('advanced_visualization_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    return data

def main():
    """Generate all datasets"""
    print("Generating probability presentation datasets...")
    
    # Change to data directory
    os.chdir('/home/ubuntu/probability_presentation/data')
    
    # Generate all datasets
    coin_data = generate_coin_flip_data()
    print("✓ Generated coin flip data")
    
    prob_dist_data = generate_probability_distribution_data()
    print("✓ Generated probability distribution data")
    
    normal_data, skewed_data = generate_central_tendency_data()
    print("✓ Generated central tendency data")
    
    quantiles_data = generate_quantiles_data()
    print("✓ Generated quantiles data")
    
    boxplot_data = generate_boxplot_data()
    print("✓ Generated boxplot data")
    
    dispersion_data = generate_dispersion_data()
    print("✓ Generated dispersion data")
    
    advanced_data = generate_advanced_visualization_data()
    print("✓ Generated advanced visualization data")
    
    print("\nAll datasets generated successfully!")
    print(f"Files created in: {os.getcwd()}")
    
    # List generated files
    files = [f for f in os.listdir('.') if f.endswith('.json')]
    print(f"Generated {len(files)} data files:")
    for file in sorted(files):
        print(f"  - {file}")

if __name__ == "__main__":
    main()

