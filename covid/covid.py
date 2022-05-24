import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

covid_df = pd.read_csv('covid-data.csv')

print(covid_df.shape)
print('------------------------------------')
print(covid_df.info())
print('------------------------------------')
print(covid_df.isnull().sum())
print('------------------------------------')


# column descriptions:
# SchoolYear: year of school data is describing: dtype: int64 2020-2021: 15067
# DistrictNCES: school district code: ALL UNIQUE Length: 14375, dtype: int64
# DistrictName: school district name: NOT UNIQUE Length: 14696, dtype: int64
# Control: Public: 15038, Private: 26, Catholic: 1, dtype: int64
# PhysicalCity: US city name, Length: 7918, dtype: int64
# PhysicalState: US city state abbreviation, dtype: int64
# Enrollment: honestly not sure, Length: 5632, dtype: int64
# OpenDate: date the school opened this year, Length: 94, dtype: int64
# TeachingMethod: Hybrid, Pending, ONline Only, On Premises, Unknown, Other, dtype: int64
# SportsParticipation: Pending, Yes, No, Unknown, dtype: int64
# OnlineInstructionIncrease: Pending, Yes, Unknown, No, dtype: int64
# NetworkInvestment: Yes, Pending, Unknown, No, dtype: int64
# HardwareInvestment: Yes, Pending, Unknown, No, dtype: int64
# StaffMaskPolicy: Pending, Required for all staff, Not required, Unknown, dtype: int64
# StudentMaskPolicy: Pending, Required for all students, Not required, Unknown, Required for middle/high school students only, Required for high school students only, dtype: int64
# StudentIllnessReturnPolicy: Pending, Yes, Unknown, No, dtype: int64
# StudentIsolationArea: Pending, Yes, Unknown, No, dtype: int64
# SchoolTemporaryShutdown: Pending, Never closed, Closed indefinitely, Unknown, Closed 6-14 days, Closed 1-5 days, dtype: int64 
# ParentOptOutClassroomTeaching: Pending, Yes, No, Unknown, dtype: int64
# LastVerifiedDate: date last verified, dtype: int64

# removing NAN's from DistrictNCES and Control columns
print('------------------------------------')
covid_df.dropna(subset = ['DistrictNCES', 'Control'], inplace=True)
print(covid_df.isnull().sum())

# need to use other methods for: enrollment, OpenDate, Hardware Investment, Last Verified Date
print('------------------------------------')
# beginning with removing outliers from 'Enrollment'
def remove_outlier(col):
	sorted(col)
	Q1, Q3 = col.quantile([0.25, 0.75])
	IQR = Q3 - Q1
	lower_range = Q1 - (1.5 * IQR)
	upper_range = Q1 + (1.5 * IQR)
	return lower_range, upper_range

low_enroll, high_enroll = remove_outlier(covid_df['Enrollment'])

covid_df['Enrollment'] = np.where(covid_df['Enrollment'] > high_enroll, high_enroll, covid_df['Enrollment'])
covid_df['Enrollment'] = np.where(covid_df['Enrollment'] < low_enroll, low_enroll, covid_df['Enrollment'])

print('------------------------------------')
# removing Enrollment NAN values
enroll_median = covid_df['Enrollment'].median()
covid_df['Enrollment'].replace(np.nan, enroll_median, inplace=True)

print('------------------------------------')
# dropping 'OpenDate' due to 1/2 of values listed are null
covid_df.drop('OpenDate', axis=1, inplace=True)

print('------------------------------------')
# removing 'HardwareInvestment' NAN values
covid_df['HardwareInvestment'] = covid_df['HardwareInvestment'].fillna('Unknown')

print('------------------------------------')
# dropping 'LastVerifiedDate' due to 1/2 of values listed are null
covid_df.drop('LastVerifiedDate', axis=1, inplace=True)

# covid_df.to_excel('covid_df_clean.xlsx')

print(covid_df['Enrollment'].median())










