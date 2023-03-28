import requests
import time

# Set the API endpoint and parameters
url = "https://winni.wiki/api.php"
params = {
    "action": "query",
    "list": "allusers",
    "auprop": "count",
    "aulimit": "5000",
    "format": "json"
}

# Make the first API request
response = requests.get(url, params=params)

# Parse the JSON response
data = response.json()

# Store the user names in a list
user_names = [user['name'] for user in data['query']['allusers']]

l = 0

# Paginate through the results and retrieve all users
while 'continue' in data:
    params['aufrom'] = data['continue']['aufrom']
    response = requests.get(url, params=params)
    data = response.json()

    # Add a delay of 1 second between requests
    time.sleep(0.1)
    l += 1
    print("Sleeping " + str(l))

    # Append the user names to the list
    user_names += [user['name'] for user in data['query']['allusers']]

# Export the user names as a plaintext file
with open('user_names.txt', 'w') as f:
    f.write('\n'.join(user_names))
