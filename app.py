import requests

def get_objects(obj_id):
	url = f"https://api.service.com/objects/{obj_id}"
	response = requests.get(url)
	return response
