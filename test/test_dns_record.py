import requests

domain = input("Enter the domain: ")
dns_text_record = input("Enter the DNS TXT record name: ")

api_url = "http://localhost:8080/check-txt-record"
api_headers = {
    "Content-Type": "application/json"
}
api_input = {
    "domain": domain,
    "dns-txt-record": dns_text_record
}

response = requests.post(api_url, json=api_input, headers=api_headers)

status_code = response.status_code

print("==========Response==========")
print(f"Response status code: {status_code}")

if status_code == 200:
    response_json = response.json()
    api_output = response_json["dns-txt-record"]
    print(f"DNS TXT record '{api_output}' was found for domain '{domain}'.")
else:
    print(f"Response Text: {response.text}")

print("============================")