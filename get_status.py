import requests
import json

def get_server_status(ip):
    url = f"https://api.mcsrvstat.us/3/{ip}"

    try:
        # Make the request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx or 5xx)
        
        # Load the JSON data
        data = response.json()

        # Save the data to the file status.json
        with open("status.json", "w") as json_file:
            json.dump(data, json_file, indent=2)

        # Print the data
        print(json.dumps(data, indent=2))
    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")
    except json.JSONDecodeError:
        print("JSON decoding error")

def main():
    ip = "play.sunrisenetwork.eu".strip()
    
    if not ip:
        print("Please enter the server address.")
        return

    get_server_status(ip)

if __name__ == "__main__":
    main()
