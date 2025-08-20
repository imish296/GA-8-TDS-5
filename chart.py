# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data (customer engagement metrics)
np.random.seed(42)
data = pd.DataFrame({
    'Website_Visits': np.random.randint(50, 200, 100),
    'Email_Clicks': np.random.randint(10, 100, 100),
    'Purchases': np.random.randint(1, 50, 100),
    'App_Usage': np.random.randint(20, 150, 100),
    'Customer_Support_Calls': np.random.randint(1, 30, 100)
})

# Compute correlation matrix
corr = data.corr()

# Set style
sns.set(style="whitegrid", font_scale=1.1)

# Plot heatmap
plt.figure(figsize=(6,6))  # 512x512 approx
heatmap = sns.heatmap(corr, annot=True, cmap="coolwarm", cbar=True, square=True,
                      linewidths=.5, fmt=".2f", annot_kws={"size":10})

plt.title("Customer Engagement Correlation Matrix", fontsize=14, pad=12)

# Save as PNG (exact size 512x512)
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
