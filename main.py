import requests
import folium
import polyline
from folium.plugins import HeatMap
import config


# --- 1. AUTHENTICATION: Get a fresh Access Token using the Refresh Token ---

def get_access_token():
    """
    Uses the long-lived Refresh Token to get a short-lived Access Token.
    """
    print("Requesting a new Access Token from Strava...")

    auth_url = "https://www.strava.com/oauth/token"
    payload = {
        'client_id': config.CLIENT_ID,
        'client_secret': config.CLIENT_SECRET,
        'refresh_token': config.REFRESH_TOKEN,
        'grant_type': "refresh_token",
        'f': 'json'
    }

    response = requests.post(auth_url, data=payload)
    response.raise_for_status()

    access_token = response.json()['access_token']
    print("Successfully obtained a new Access Token!")
    return access_token


# --- 2. DATA FETCHING: Get all activities from Strava ---

def get_all_activities(access_token):
    """
    Fetches all activities page by page from the Strava API.
    """
    print("Fetching activities from Strava... This may take a while.")

    activities_url = "https://www.strava.com/api/v3/athlete/activities"
    headers = {'Authorization': f'Bearer {access_token}'}
    all_activities = []
    page = 1

    while True:
        params = {'per_page': 200, 'page': page}
        response = requests.get(activities_url, headers=headers, params=params).json()

        if not response:
            break

        all_activities.extend(response)
        print(f"Fetched page {page} with {len(response)} activities.")
        page += 1

    print(f"Finished fetching. Total activities found: {len(all_activities)}")
    return all_activities


# --- 3. DATA PROCESSING: Decode polylines to get GPS coordinates ---

def get_all_coordinates(activities):
    """
    Extracts and decodes the summary polyline from each 'Run' activity.
    """
    print("Decoding polylines for 'Run' activities to get GPS coordinates...")
    all_coords = []

    for activity in activities:
        # Check if the activity is a 'Run' AND has a summary polyline
        if activity['type'] == 'Run' and activity['map']['summary_polyline']:
            # Decode the polyline into a list of [lat, lon] coordinates
            decoded_points = polyline.decode(activity['map']['summary_polyline'])
            all_coords.extend(decoded_points)

    print(f"Successfully decoded GPS data. Total points found: {len(all_coords)}")
    return all_coords


# --- 4. MAP CREATION: Generate the heatmap ---

def create_heatmap(coordinates):
    """
    Creates a heatmap from a list of coordinates and saves it to an HTML file.
    """
    if not coordinates:
        print("No running coordinates found to create a map.")
        return

    print("Creating the heatmap...")

    map_center = coordinates[0]
    m = folium.Map(location=map_center, zoom_start=13, tiles="CartoDB dark_matter")

    HeatMap(coordinates).add_to(m)

    output_file = "strava_run_heatmap.html"  # Changed the output file name
    m.save(output_file)
    print(f"Success! Heatmap for runs saved to '{output_file}'")


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    try:
        fresh_access_token = get_access_token()
        activities = get_all_activities(fresh_access_token)
        coords = get_all_coordinates(activities)
        create_heatmap(coords)

    except Exception as e:
        print(f"\nAn error occurred during the process: {e}")