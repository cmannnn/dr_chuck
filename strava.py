# imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
sns.set_style('darkgrid')

# data frame read
df = pd.read_csv('strava.csv', parse_dates=True, index_col='Activity Date')

# dropping cols with no data
cols_to_drop = ['Activity Description', 'Relative Effort', 'Activity Gear', 'Athlete Weight', 'Bike Weight', 'Average Positive Grade', 'Average Negative Grade', 'Max Cadence', 'Average Cadence', 'Max Heart Rate', 'Average Heart Rate', 'Max Watts', 'Average Watts', 'Calories', 'Max Temperature', 'Average Temperature', 'Relative Effort.1', 'Total Work', 'Number of Runs', 'Uphill Time', 'Downhill Time', 'Other Time', 'translation missing: en-US.lib.export.portability_exporter.activities.horton_values.type', 'translation missing: en-US.lib.export.portability_exporter.activities.horton_values.start_time', 'Weighted Average Power', 'Power Count', 'Total Weight Lifted', 'Weather Observation Time', 'Weather Condition', 'Weather Temperature', 'Apparent Temperature', 'Dewpoint', 'Humidity', 'Weather Pressure', 'Wind Speed', 'Wind Gust', 'Wind Bearing', 'Precipitation Intensity', 'Sunrise Time', 'Sunset Time', 'Moon Phase', 'Bike', 'Gear', 'Precipitation Probability', 'Precipitation Type', 'Cloud Cover', 'Weather Visibility', 'UV Index', 'Weather Ozone', 'translation missing: en-US.lib.export.portability_exporter.activities.horton_values.jump_count', 'translation missing: en-US.lib.export.portability_exporter.activities.horton_values.total_grit', 'translation missing: en-US.lib.export.portability_exporter.activities.horton_values.avg_flow', 'Prefer Perceived Exertion']
df.drop(axis=1, columns=cols_to_drop, inplace=True)

'''_____________________________________________________________________________________________'''

# dealing with missing values:
null_val = df.isnull().sum()
#print('The columns with null values are:\n', null_val)

'''_____________________________________________________________________________________________'''

# 'Perceived Exertion' column; will use mean exertion to fill
p_exertion_null = df['Perceived Exertion'].isnull().sum()
#print('There are {} null values in the \'Perceived Exertion\' column'.format(p_exertion_null))

# taking the mean of the 'Perceived Exertion' column
p_exertion_mean = df['Perceived Exertion'].mean()
#print('The mean of the \'Perceived Exertion\' column is: {}'.format(p_exertion_mean))

# replacing the null values of 'Perceived Exertion' column with the mean
df['Perceived Exertion'].fillna(int(p_exertion_mean), inplace=True)

'''_____________________________________________________________________________________________'''

# 'Perceived Relative Effort'
p_relative_null = df['Perceived Relative Effort'].isnull().sum()
#print('There are {} null values in the \'Perceived Relative Effort\' column'.format(p_relative_null))

# taking the mean of the 'Perceived Relative Effort' column
p_relative_mean = df['Perceived Relative Effort'].mean()
#print('The mean of the \'Perceived Relative Effort\' column is: {}'.format(p_exertion_mean))

# replacing the null values of the 'Perceived Relative Effort' column with the mean 
df['Perceived Relative Effort'].fillna(int(p_relative_mean), inplace=True)

'''_____________________________________________________________________________________________'''

# 'Grade Adjusted Distance'
g_adjusted_null = df['Grade Adjusted Distance'].isnull().sum()
#print('There are {} null values in the \'Grade Adjusted Distance\' column'.format(g_adjusted_null))

# taking the mean of the 'Grade Adjusted Distance' column
g_adjusted_mean = df['Grade Adjusted Distance'].mean()
#print('The mean of the \'Grade Adjusted Distance\' column is: {}'.format(g_adjusted_mean))

# replacing the null values of the 'Grade Adjusted Distance' column with the mean
df['Grade Adjusted Distance'].fillna(int(g_adjusted_mean), inplace=True)

# no more nulls!
#print(df.isnull().sum())

'''_____________________________________________________________________________________________'''

# splitting DataFrames into 3, specific for different activities for later analysis
df_run = df[df['Activity Type'] == 'Run'].copy()
df_ride = df[df['Activity Type'] == 'Ride'].copy()
df_hike = df[df['Activity Type'] == 'Hike'].copy()

'''_____________________________________________________________________________________________'''

# how many of each activity were recorded?
act_count = df['Activity Type'].value_counts().sum()

# creating fig, ax
fig, ax = plt.subplots()
sns.countplot(df['Activity Type'])

ax.set_xlabel('Activity type')
ax.set_ylabel('# of activities recorded')
plt.title('Count of activity type', fontsize=20, fontweight=10)
sns.set_style('dark')
sns.despine(right=True)

# remove to display graph
plt.close()
plt.show()

'''_____________________________________________________________________________________________'''

# subsetting data by activity
run_df = df[df['Activity Type'] == 'Run'].copy()



# CHAINGING ACTIVITY NAME TO DATETIME NOT CONVERTING
run_df['Activity Name'] = pd.to_datetime(run_df['Activity Name'])
run_df_distance = run_df['Distance']
run_df_avg_speed = run_df['Average Speed']
run_df_p_rel_effort = run_df['Perceived Relative Effort']


fig, (ax0, ax1, ax2) = plt.subplots(3, sharex=False, figsize=(19,7))

run_df_distance.plot(ax=ax0, linestyle='none', marker='o', markersize=4)
run_df_avg_speed.plot(ax=ax1, linestyle='none', marker='o', markersize=4, color='blue')
run_df_p_rel_effort.plot(ax=ax2, linestyle='none', marker='o', markersize=4, color='green')


ax0.set_title('Run distance (km)')
ax0.set_xlabel(' ')
ax0.grid(True)
ax1.set_title('Run avg. speed (km/h)')
ax1.set_xlabel(' ')
ax1.grid(True)
ax2.set_title('Run perceived relative effort')
ax2.grid(True)

fig.tight_layout()
plt.xticks(range(min(run_df['Activity Name']), max(run_df['Activity Name'])+1))
#plt.close()
plt.show()

print(run_df.columns)

print(run_df['Activity Name'].min())
# print(run_df_p_rel_effort.describe())

#print(run_df.columns)

'''_____________________________________________________________________________________________'''
bike_df = df[df['Activity Type'] == 'Bike'].copy()
#fig, (ax1, ax2) = plt.subplots(2, sharex=True)


'''_____________________________________________________________________________________________'''
hike_df = df[df['Activity Type'] == 'Hike'].copy()
#fig, (ax1, ax2) = plt.subplots(2, sharex=True)

fig, ax = plt.subplots(3, 1)

#ax0 = plt.plot(kind='scatter', data=run_df)
#ax1 = plt.plot(kind='scatter', data=bike_df)
#ax2 = plt.plot(kind='scatter', data=hike_df)





