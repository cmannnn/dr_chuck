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
# just run data set
df_run = df[df['Activity Type'] == 'Run'].copy()

# just bike data set
df_ride = df[df['Activity Type'] == 'Ride'].copy()

# just hike data set
df_hike = df[df['Activity Type'] == 'Hike'].copy()

'''_____________________________________________________________________________________________'''

# how many of each activity were recorded?
act_count = df['Activity Type'].value_counts().sum()

# creating fig, ax
fig, ax = plt.subplots()

# countplot of activities by type
sns.countplot(df['Activity Type'])

# setting the x and y label
ax.set_xlabel('Activity type')
ax.set_ylabel('# of activities recorded')

# setting the title
plt.title('Count of activity type', fontsize=20, fontweight=10)

# changing the graph sytle
sns.set_style('dark')
sns.despine(right=True)

# remove below line to display graph!
plt.close()
plt.show()

'''_____________________________________________________________________________________________'''

# replacing one bad date
df_run.replace(to_replace='3020-10-23', value='2020-10-23', inplace=True)

# creating date time column
df_run['Activity Name'] = pd.to_datetime(df_run['Activity Name'])

# sub setting running data
# running distance IN MILES
run_df_distance = (df_run['Distance'] / (8/5))

# calculating average speed IN MILES/HOUR
run_df_avg_speed = (run_df_distance / (df_run['Moving Time'] / 3600))

# running perceived relative effort
run_df_p_rel_effort = df_run['Perceived Relative Effort']

# creating fig, ax in subplots
fig, (ax0, ax1, ax2) = plt.subplots(3, sharex=False, figsize=(19,8))

run_df_distance.plot(ax=ax0, linestyle='none', marker='o', markersize=4)
run_df_avg_speed.plot(ax=ax1, linestyle='none', marker='o', markersize=4, color='blue')
run_df_p_rel_effort.plot(ax=ax2, linestyle='none', marker='o', markersize=4, color='green')

# dates being used for x axis
dates = ['2020-06-28', '2020-07-01', '2020-07-04', '2020-07-07', '2020-07-10', '2020-07-13', '2020-07-16', '2020-07-19', '2020-07-22', '2020-07-25', '2020-07-28', '2020-07-31', '2020-08-03', '2020-08-06', '2020-08-09', '2020-08-12', '2020-08-15', '2020-08-18', '2020-08-21', '2020-08-24', '2020-08-27', '2020-08-30', '2020-09-02', '2020-09-05', '2020-09-08', '2020-09-11', '2020-09-14', '2020-09-17', '2020-09-20', '2020-09-23', '2020-09-26', '2020-09-29', '2020-10-02', '2020-10-05', '2020-10-08', '2020-10-11', '2020-10-14', '2020-10-17', '2020-10-20', '2020-10-23', '2020-10-26', '2020-10-29', '2020-11-02', '2020-11-5', '2020-11-08', '2020-11-11', '2020-11-14']

# ax0 graph params
ax0.set_title('Run distance (mi)')
ax0.set_xlabel(' ')
ax0.axhline(run_df_distance.mean(), alpha=0.3, color='black')
ax0.grid(True)
ax0.set_xlim(dates[0], dates[-1])
ax0.set_xticklabels(labels=dates, fontsize=7)
#ax0.set_ylim([4,16])


# ax1 graph params
# FININSH SETTING Y LIM'S
# FINISH TRIMMING XLABELS
ax1.set_title('Run avg. speed (mi/h)')
ax1.set_xlabel(' ')
ax1.axhline(run_df_avg_speed.mean(), alpha=0.3, color='black')
ax1.grid(True)
ax1.set_xlim(dates[0], dates[-1])
ax1.set_xticklabels(labels=dates, fontsize=7)
#ax1.set_ylim()
ax1.set_xlabel('', fontsize=1)

#print(df_run.columns)
#print(df_run['Average Speed'].describe())


# ax2 graph params
ax2.set_title('Run perceived relative effort')
ax2.axhline(run_df_p_rel_effort.mean(), alpha=0.3, color='black')
ax2.grid(True)
ax2.set_xlim(dates[0], dates[-1])
ax2.set_xticklabels(labels=dates, fontsize=7)
#ax2.set_ylim()
ax2.set_xlabel('', fontsize=1)

# figure layout
plt.setp((ax0, ax1, ax2), xticks=dates)
plt.legend('')
fig.tight_layout()

#plt.close()
plt.show()


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


