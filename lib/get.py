import requests
import json

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
location_response = requests.get(url_locations)

people_response = requests.get(url_people)


location_json_content = json.loads(people_response.text)

people_json_content = json.loads(people_response.text)

print(json.dumps(location_json_content, indent=4))
print(json.dumps(people_json_content, indent=4))
