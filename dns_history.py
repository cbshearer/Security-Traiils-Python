import requests
import sys
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
domain = sys.argv[1] if len(sys.argv) > 1 else input("Enter Domain: ")

api_key = "xxxxxxxx"
url = "https://api.securitytrails.com/v1/history/" + domain + "/dns/a"
headers = {
    "accept": "application/json",
    "APIKEY": api_key
}

response = requests.get(url, headers=headers, verify=False)
json_data = json.loads(response.text)

record_count = len(json_data["records"])
highest_index = record_count - 1

first_seen = json_data["records"][highest_index]["first_seen"]
last_seen = json_data["records"][0]["last_seen"]
record_type = json_data["type"]

# Print the extracted values
print()
print("First Seen:", first_seen)
print("Last Seen:", last_seen)
print("Record Count:", record_count)
print("Record Type:", record_type)
print()

# Header for the table
header = ["First Seen", "Last Seen", "Organization", "Type", "IP"]

# Print the header
print("{:<15} {:<15} {:<45} {:<5} {:<15}".format(*header))
print("="*99)

for record in json_data["records"]:
    first_seen = record["first_seen"]
    last_seen = record["last_seen"]
    org = record["organizations"][0]  # Assuming there is only one organization
    record_type = record["type"]
    ip = record["values"][0]["ip"]  # Assuming there is only one IP

    print("{:<15} {:<15} {:<45} {:<5} {:<15}".format(first_seen, last_seen, org, record_type, ip))
