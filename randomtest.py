from qrng import qrng
from collections import Counter
from scipy.stats import chisquare

bits = [qrng() for _ in range(10000)]
counts = Counter(bits)
sum = sum(counts.values())
observed = [counts[0], counts[1]]

expected = [len(bits) / 2, len(bits) / 2]

chi2_stat, p_value = chisquare(f_obs=observed, f_exp=expected)

print(counts)
print("Chi-squared statistic:", chi2_stat)
print("p-value:", p_value)
