# Strava Data Analysis & Visualization Hub 🏃‍♂️🚴‍♀️

## Project Description

This repository contains a collection of Python scripts for analyzing and visualizing personal activity data from Strava, demonstrating two different approaches to data acquisition and presentation.

1.  **CSV Analysis with Streamlit Dashboard:** An interactive web dashboard (`dashboard.py`) for exploring historical running performance from an exported `activities.csv` file.
2.  **API-Powered Activity Heatmap:** A script (`main.py`) that connects directly to the Strava API to fetch all activity data and generate a comprehensive, interactive heatmap.

---

## Files in This Repository

- `main.py`: The main script that connects to the Strava API and generates the activity heatmap.
- `dashboard.py`: An interactive Streamlit dashboard for visualizing data from the exported `activities.csv` file.
- `csv_analyzer.py`: The original, script-based version for analyzing the exported Strava CSV file.
- `get_token.py`: A one-time utility script required to perform the initial Strava API authentication.

---

## Part 1: Running Performance Dashboard (from CSV)

This part of the project focuses on processing and visualizing personal running data from a Strava export to gain insights into performance over time. The results are presented in an interactive web dashboard.

### How to Run the Dashboard

1.  **Export Your Strava Data:** Export your activity data from your Strava profile settings. The project specifically uses the `activities.csv` file.
2.  **Place the Data File:** Place your `activities.csv` file into a `data` folder within the project directory.
3.  **Run the Dashboard:**
    ```bash
    streamlit run dashboard.py
    ```

---

## Part 2: Activity Heatmap (from API)

This script connects to the official Strava API to fetch a complete history of all activities (runs, rides, etc.), extracts the GPS data, and generates an interactive heatmap.

### How to Run the Heatmap Generator

1.  **Register for a Strava API Key:**
    - Go to `https://www.strava.com/settings/api` and create an application.
    - Set the **Authorization Callback Domain** to `localhost`.
    - Note your **Client ID** and **Client Secret**.

2.  **Initial Authentication (One-Time Step):**
    - Run the `get_token.py` utility script to obtain your **Refresh Token**.
    - Place your `CLIENT_ID`, `CLIENT_SECRET`, and `REFRESH_TOKEN` into the `config.py` file.

3.  **Run the Main Script:**
    ```bash
    python main.py
    ```
    - The script will generate a `strava_heatmap.html` file in the project directory.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Streamlit (for the dashboard)
- Folium (for the heatmap)
- Requests & Requests-OAuthlib (for API communication)
- Polyline