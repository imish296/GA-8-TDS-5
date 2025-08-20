mport seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
data = pd.DataFrame({
    'Website_Visits': np.random.randint(50, 200, 100),
    'Email_Clicks': np.random.randint(10, 100, 100),
    'Purchases': np.random.randint(1, 50, 100),
    'App_Usage': np.random.randint(20, 150, 100),
    'Customer_Support_Calls': np.random.randint(1, 30, 100)
})

# Correlation matrix
corr = data.corr()

# Seaborn style
sns.set(style="whitegrid", font_scale=1.1)

# Exact 512x512 output
plt.figure(figsize=(8,8), dpi=64)   # 8in × 64dpi = 512px
sns.heatmap(corr, annot=True, cmap="coolwarm", cbar=True, square=True,
            linewidths=.5, fmt=".2f", annot_kws={"size":10})

plt.title("Customer Engagement Correlation Matrix", fontsize=14, pad=12)

# Tight layout but NO bbox_inches
plt.tight_layout()
plt.savefig("chart.png", dpi=64)
