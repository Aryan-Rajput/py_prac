# Random Number Generation
# Practice generating random numbers

import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Random floats between 0 and 1
print("--- Random Floats [0, 1) ---")
print("Single random:", np.random.rand())
print("1D array (5):", np.random.rand(5))
print("2D array (2x3):\n", np.random.rand(2, 3))

# Random floats from standard normal distribution (mean=0, std=1)
print("\n--- Standard Normal Distribution ---")
print("Single random:", np.random.randn())
print("1D array (5):", np.random.randn(5))
print("2D array (2x3):\n", np.random.randn(2, 3))

# Random integers
print("\n--- Random Integers ---")
print("Single int (0 to 10):", np.random.randint(0, 10))
print("1D array (5 ints, 0-100):", np.random.randint(0, 100, 5))
print("2D array (3x3, 1-50):\n", np.random.randint(1, 50, (3, 3)))

# Random choice from array
print("\n--- Random Choice ---")
choices = np.array(['apple', 'banana', 'cherry', 'date'])
print("Choices:", choices)
print("Single choice:", np.random.choice(choices))
print("Multiple choices (3):", np.random.choice(choices, 3))
print("With replacement (5):", np.random.choice(choices, 5, replace=True))

# Weighted random choice
print("\n--- Weighted Choice ---")
weights = [0.1, 0.5, 0.3, 0.1]  # banana has 50% probability
print("Weights:", weights)
print("Weighted choices (10):", np.random.choice(choices, 10, p=weights))

# Shuffle array (in-place)
print("\n--- Shuffle ---")
arr = np.arange(10)
print("Original:", arr)
np.random.shuffle(arr)
print("Shuffled:", arr)

# Permutation (returns new array, doesn't modify original)
print("\n--- Permutation ---")
arr = np.arange(10)
print("Original:", arr)
print("Permutation:", np.random.permutation(arr))
print("Original unchanged:", arr)

# Different distributions
print("\n--- Various Distributions ---")

# Uniform distribution
print("Uniform (low=5, high=10, size=5):", np.random.uniform(5, 10, 5))

# Normal distribution with custom mean and std
print("Normal (mean=50, std=10, size=5):", np.random.normal(50, 10, 5))

# Binomial distribution
print("Binomial (n=10, p=0.5, size=5):", np.random.binomial(10, 0.5, 5))

# Poisson distribution
print("Poisson (lambda=5, size=5):", np.random.poisson(5, 5))

# Exponential distribution
print("Exponential (scale=2, size=5):", np.random.exponential(2, 5))

# Using Generator (modern approach - NumPy 1.17+)
print("\n--- Modern Generator API ---")
rng = np.random.default_rng(seed=42)
print("Random floats:", rng.random(5))
print("Random integers:", rng.integers(0, 100, 5))
print("Random normal:", rng.normal(0, 1, 5))

# Reproducibility with seed
print("\n--- Reproducibility ---")
np.random.seed(123)
print("First run:", np.random.rand(3))
np.random.seed(123)
print("Second run (same seed):", np.random.rand(3))
