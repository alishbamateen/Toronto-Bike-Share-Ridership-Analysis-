import pandas as pd
import glob

# Replace 'bike_data/' with the path to your folder if needed
file_paths = glob.glob('./*.csv')


dfs = []

for f in file_paths:
    try:
        df = pd.read_csv(f, encoding='latin1')  # specify encoding
        dfs.append(df)
    except Exception as e:
        print(f"Error reading {f}: {e}")

all_data = pd.concat(dfs, ignore_index=True)
print(all_data.shape)
print(all_data.columns)

# ---- CLEANING STEP ----

# Remove BOM column if it exists
if 'ï»¿Trip Id' in all_data.columns:
    all_data = all_data.drop(columns=['ï»¿Trip Id'])

# Standardize column names
all_data.columns = [col.strip().lower().replace(' ', '_') for col in all_data.columns]
print(all_data.columns)

# Check for missing values
print(all_data.isnull().sum())

# Convert start and end times to datetime
all_data['start_time'] = pd.to_datetime(all_data['start_time'], errors='coerce')
all_data['end_time'] = pd.to_datetime(all_data['end_time'], errors='coerce')

# Drop rows where datetime conversion failed
all_data = all_data.dropna(subset=['start_time', 'end_time'])

# Check final shape
print(all_data.shape)


# Aggregate rides per day
daily_ridership = all_data.groupby(all_data['start_time'].dt.date).size()

# Plot daily ridership
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
daily_ridership.plot(kind='line')
plt.title('Daily Bike Share Ridership (Jan–Sep 2024)')
plt.xlabel('Date')
plt.ylabel('Number of Rides')
plt.show()

# Extract hour from start_time
all_data['hour'] = all_data['start_time'].dt.hour

# Aggregate by hour
hourly_ridership = all_data.groupby('hour').size()

plt.figure(figsize=(10,5))
hourly_ridership.plot(kind='bar')
plt.title('Average Ridership by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Rides')
plt.show()


#A/B Style Analysis

# Day of the week (Monday=0, Sunday=6)
all_data['day_of_week'] = all_data['start_time'].dt.day_name()

# Label as Weekday or Weekend
all_data['day_type'] = all_data['day_of_week'].apply(lambda x: 'Weekend' if x in ['Saturday','Sunday'] else 'Weekday')

#aggregate data by day type
weekday_rides = all_data[all_data['day_type']=='Weekday']
weekend_rides = all_data[all_data['day_type']=='Weekend']

print(f"Total weekday rides: {len(weekday_rides)}")
print(f"Total weekend rides: {len(weekend_rides)}")

#perform a t-test to see if difference is significant
from scipy.stats import ttest_ind

# Count rides per day
weekday_counts = weekday_rides.groupby(weekday_rides['start_time'].dt.date).size()
weekend_counts = weekend_rides.groupby(weekend_rides['start_time'].dt.date).size()

t_stat, p_val = ttest_ind(weekday_counts, weekend_counts, equal_var=False)
print(f"T-test statistic: {t_stat}")
print(f"P-value: {p_val}")

#If p < 0.05, the difference in daily ridership between weekdays and weekends is statistically significant.


#Top Start Stations
# Count rides per start station
top_stations = all_data['start_station_name'].value_counts().head(10)

print("Top 10 Start Stations:")
print(top_stations)

# Plot top stations
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
top_stations.plot(kind='bar')
plt.title('Top 10 Bike Share Start Stations')
plt.xlabel('Station')
plt.ylabel('Number of Rides')
plt.xticks(rotation=45)
plt.show() #This shows which stations are most popular, which is great for understanding usage patterns.

#Ridership by Hour (Weekday vs Weekend)
import seaborn as sns

# Aggregate rides by hour and day type
hourly_data = all_data.groupby(['hour', 'day_type']).size().reset_index(name='ride_count')

plt.figure(figsize=(12,6))
sns.lineplot(data=hourly_data, x='hour', y='ride_count', hue='day_type', marker='o')
plt.title('Hourly Ridership: Weekday vs Weekend')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Rides')
plt.xticks(range(0,24))
plt.show() #This will show peak hours for weekdays vs weekends