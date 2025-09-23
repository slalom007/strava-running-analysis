import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# The file path to your Strava CSV export
csv_path=r'C:\Users\Felhasználó\Desktop\Balogh László\python\Running_performance\strava_export\activities.csv'

# Set up the Streamlit page title
st.title("Strava Running Dashboard")

# Read the CSV file into a pandas DataFrame
try:
    df=pd.read_csv(csv_path, sep=',')
    st.success("Successfully read data from the file!")
except FileNotFoundError:
    st.error(f"Error: The file was not found at the specified path: {csv_path}")
    st.stop()

# Select the most important columns for the project
df=df[["Activity Date", "Distance", "Moving Time", "Activity Type"]]

#Rename columns for clarity
df.columns=['date', 'distance', 'moving_time', 'activity_type']

#Filter for 'Run' activities only
df=df[df['activity_type'] == 'Run']

# Convert distance to kilometers (assuming it's given in units of 100)
df['distance'] = df['distance'].str.replace('.', '', regex=False).astype(float)
df['distance'] = df['distance'] /100

# Calculate pace in minutes per kilometer
df['pace'] = (df['moving_time']/60)/df['distance']

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%b %d, %Y, %I:%M:%S %p')

# Set the date column as the DataFrame index
df.set_index('date', inplace=True)

# Resample the data on a weekly basis and calculate the total distance, average pace, and total time
weekly_distance = df['distance'].resample('W').sum()
weekly_pace = df['pace'].resample('W').mean()
weekly_time = df['moving_time'].resample('W').sum() / 60

# Display Weekly Running Distance
st.header('Weekly Running Distance')
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(weekly_distance.index, weekly_distance.values, marker='o', color='blue')
ax.set_xlabel('Date')
ax.set_ylabel('Distance (km)')
ax.grid(True)
st.pyplot(fig)

# Display Weekly Average Pace
st.header('Weekly Average Pace')
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(weekly_pace.index, weekly_pace.values, marker='o', linestyle='-', color='red')
ax.set_xlabel('Date')
ax.set_ylabel('Pace (min/km)')
ax.grid(True)
st.pyplot(fig)

# Display Weekly Running Time
st.header('Weekly Running Time')
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(weekly_time.index, weekly_time.values, color='green')
ax.set_xlabel('Date')
ax.set_ylabel('Time (minutes)')
ax.grid(axis='y')
st.pyplot(fig)



