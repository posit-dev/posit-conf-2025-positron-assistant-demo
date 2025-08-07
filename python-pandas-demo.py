import pandas as pd
import seaborn as sns

# 👀 CSV file path -- update this path as needed!
csv_file_path = 'data/data.csv'

# Load CSV file into a pandas DataFrame
data = pd.read_csv(csv_file_path)

###########################################
# TBD may use plotly or matplotlib instead
###########################################

# Plot a heatmap of the data
sns.heatmap(data, annot=True, cmap='viridis')

sns.plt.close()
