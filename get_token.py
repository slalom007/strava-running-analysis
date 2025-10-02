# get_token.py
import requests
import webbrowser

CLIENT_ID = "179377"
CLIENT_SECRET = "2229ebce8300d35cba2f5be22f113bbf1687dd2d"

# 1. URL generalasa es megnyitasa
auth_url = (
    f"https://www.strava.com/oauth/authorize?"
    f"client_id={179377}"
    f"&response_type=code"
    f"&redirect_uri=http://localhost/exchange_token"
    f"&approval_prompt=force"
    f"&scope=read,activity:read_all"
)

print("Nyisd meg a kovetkezo URL-t a bongeszodben, es engedelyezd az alkalmazast:")
print(auth_url)
webbrowser.open(auth_url)

# 2. A kod bekerese
auth_code = input("\Masold be ide a 'code=' utan levo reszt az URL-bol, majd nyomj Entert: ")

# 3. Tokenek lekerese
token_url = "https://www.strava.com/oauth/token"
payload = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "code": auth_code.strip(),
    "grant_type": "authorization_code"
}

response = requests.post(token_url, data=payload)

if response.status_code == 200:
    tokens = response.json()
    print("\nSikeres hitelesites!")
    print("--------------------------")
    print(f"Access Token: {tokens['access_token']}")
    print(f"Refresh Token: {tokens['refresh_token']}")
    print("--------------------------")
    print("\nFONTOS: Masold be a 'Refresh Token'-t a config.py fajlodba!")
else:
    print("\nHiba a hitelesites soran:")
    print(response.json())