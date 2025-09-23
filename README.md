# Strava Running Data Visualisation

This project is a personal data analysis and visualisation project created to track my running performance using data exported from the Strava platform. The project is built using Python and the `pandas`, `matplotlib`, and `streamlit` libraries. It includes a web-based dashboard for interactive data exploration.

## Project Goal

The main goal of this project is to process and visualise my personal running data to gain insights into my performance over time. The project demonstrates data cleaning, processing, and visual plotting skills.

## Visualisations

The project currently generates three different visualisations, all of which are available in the web dashboard:

- **Weekly Running Distance:** A line plot showing the total distance run per week.
- **Weekly Average Pace:** A line plot showing the average pace (min/km) per week.
- **Weekly Running Time:** A bar chart showing the total time spent running per week.

## Technologies Used

- **Python:** The core programming language used for the project.
- **Pandas:** A powerful data analysis library for cleaning and processing the dataset.
- **Matplotlib:** A data visualisation library used to create the plots.
- **Streamlit:** An open-source Python library used to create a web-based dashboard.

## How to Run the Project

1.  **Export Your Strava Data:** Export your activity data from your Strava profile settings. The project specifically uses the `activities.csv` file.
2.  **Set Up the Environment:**
    * Create a virtual environment: `python -m venv venv`
    * Activate the virtual environment.
    * Install the required libraries: `pip install pandas matplotlib streamlit`
3.  **Place the Data File:** Place your `activities.csv` file into a `data` folder within the project directory.
4.  **Run the Dashboard:** Run the `dashboard.py` file using the Streamlit command.

```bash
streamlit run dashboard.py