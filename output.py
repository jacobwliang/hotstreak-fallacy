from trials import runtrials
import pandas as pd
from matplotlib import pyplot as plt
import statistics as stat

n_trials = 10000 
probabilities = runtrials(n_trials)  

prob_series = pd.Series(probabilities) # turn the list of probabilities into a series

# descriptive statistic
q1 = prob_series.quantile(0.25)
q3 = prob_series.quantile(0.75)
print(f"min: {min(probabilities)}, median: {stat.median(probabilities)}, max: {max(probabilities)}, mean: {stat.mean(probabilities)}, Q1: {q1}, Q3: {q3}")

num_bins = 10 # bin trials for better visualization
prob_series_binned = pd.cut(prob_series, bins=num_bins, precision=2)

binned_counts = prob_series_binned.value_counts().sort_index()

plt.figure(figsize=(10, 6)) # set window
ax = binned_counts.plot(kind='bar', color='orange', edgecolor='black', alpha=0.9)
plt.title('Frequency of Hotstreak Probabilities')
plt.xlabel('Probability of Success After Streak of 2')
plt.ylabel('Count')
plt.grid(axis='y', linestyle=':', alpha=0.5)
ax.set_xticklabels([f"{interval.left:.2f} - {interval.right:.2f}" for interval in binned_counts.index], rotation=45, ha='right')

plt.show()
