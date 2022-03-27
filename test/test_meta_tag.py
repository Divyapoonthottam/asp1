import requests

url = input("Enter the URL: ")
meta_tag_name = input("Enter the meta tag name: ")

api_url = "http://localhost:8080/find-meta-tag-with-name"
api_input = {
    "url": url,
    "meta-tag-name": meta_tag_name
}

response = requests.get(api_url, params=api_input)

status_code = response.status_code

print("==========Response==========")
print(f"Response status code: {status_code}")

if status_code == 200:
    response_json = response.json()
    meta_tag_value = response_json["meta-tag-value"]
    print(f"Meta tag with name '{meta_tag_name}' was found in URL '{url}'. It's value is '{meta_tag_value}'.")
else:
    print(f"Response Text: {response.text}")

print("============================")