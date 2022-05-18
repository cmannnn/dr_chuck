# The cost of a Shanghai license plate
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')
import numpy as np

# reading in the data from CSV
df = pd.read_csv('shanghai_df.csv')

# changing date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%b-%y')

# creating fig + ax subplot
fig, ax = plt.subplots(figsize=[12,7])

# plotting # of applicants on date
ax.plot(df['Date'], df['Total number of applicants'], color='darkred', marker='v', markersize=3)

# setting ax y-label 
ax.set_ylabel('Number of applicants', color='darkred', fontsize=20, fontweight='bold', labelpad=20)
ax.tick_params('y', labelcolor='darkred')
ax.grid(linestyle=':', color='darkred')

# creating second x-axis
ax2 = ax.twinx()

# plotting cost on date
ax2.plot(df['Date'], df['avg price'], color='darkblue', marker='o', markersize=3)

# setting ax2 y-label
ax2.set_ylabel('Cost (RMB)', color='darkblue', fontsize=20, fontweight='bold', labelpad=16)
ax2.tick_params('y', labelcolor='darkblue')
ax2.grid(linestyle=':', color='darkblue')

# setting graph title
ax.set_title('Cost of a Shanghai license plate', color='black', fontsize=30, fontweight='bold', pad=18)

# setting x-label
ax.set_xlabel('Year', color='black', fontsize=20, fontweight='bold', labelpad=20)

# graphing! 
plt.show()