import pandas as pd
import matplotlib.pyplot as plt

# The file path to your Strava CSV export
# Make sure to change this to your exact file path!
csv_path=r'C:\Users\Felhasználó\Desktop\Balogh László\python\Running_performance\strava_export\activities.csv'

# Read the CSV file into a pandas DataFrame
try:
    df = pd.read_csv(csv_path, sep=',')
    print("Succesfully read data from the file!")

except FileNotFoundError:
    print(f"Error, The file was not found at the specified path: {csv_path}")
    exit()

# Select the most important columns for the project
df = df[['Activity Date', 'Distance', 'Moving Time', 'Activity Type']]

# Rename columns for clarity
df.columns=["date", "distance", "moving_time", "type"]

# Convert the 'date' column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Filter for 'Run' activities only
df=df[df["type"]=="Run"]

# Clean the 'distance' column by removing thousand separators and converting to float
df['distance'] = df['distance'].str.replace('.', '', regex=False).astype(float)

# Convert distance to kilometers (assuming it's given in units of 100)
df['distance'] = df['distance'] / 100

# Calculate pace in minutes per kilometer
df['pace']=(df['moving_time']/60)/df['distance']

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Set the date column as the DataFrame index
df.set_index('date', inplace=True)

# Resample the data on a weekly basis and calculate the total distance
weekly_distance = df['distance'].resample('W').sum()
weekly_pace = df['pace'].resample('W').mean()

print("\nWeekly ran distances:")
print(weekly_distance)

# Visualize the weekly running performance
plt.figure(figsize=(12,6))
plt.plot(weekly_distance.index, weekly_distance.values, marker='o', linestyle='-')

# Add titles and labels to the plot
plt.title("Weekly Running Performance - Data Visualisation Project", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Distance [km]", fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

## Visualize Weekly Average Pace
plt.figure(figsize=(12, 6))
plt.plot(weekly_pace.index, weekly_pace.values, marker='o', linestyle='-', color='red')

# Add titles and labels to the plot
plt.title('Weekly Average Pace', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Pace (min/km)', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()











