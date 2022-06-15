import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://4fa588a4-0051-4cd7-9be8-1cfdda909b6d.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'TERZjBsrHzs0wjO69peb5LQcJjtL5BZB'

# Two sets of data to score, so we get two results back
data = {
    "Inputs": {
        "data": [{
		"age": 17,
		"job": "blue-collar",
		"marital": "married",
		"education": "university.degree",
		"default": "no",
		"housing": "yes",
		"loan": "yes",
		"contact": "cellular",
		"month": "may",
		"day_of_week": "mon",
		"duration": 971,
		"campaign": 1,
		"pdays": 999,
		"previous": 1,
		"poutcome": "failure",
		"emp.var.rate": -2,
		"cons.price.idx": 92,
		"cons.conf.idx": -46,
		"euribor3m": 1,
		"nr.employed": 5099,
	}, {
		"age": 87,
		"job": "blue-collar",
		"marital": "married",
		"education": "university.degree",
		"default": "no",
		"housing": "yes",
		"loan": "yes",
		"contact": "cellular",
		"month": "may",
		"day_of_week": "mon",
		"duration": 471,
		"campaign": 1,
		"pdays": 999,
		"previous": 1,
		"poutcome": "failure",
		"emp.var.rate": -2,
		"cons.price.idx": 92,
		"cons.conf.idx": -46,
		"euribor3m": 1,
		"nr.employed": 5099,
	},],
    },
    "GlobalParameters": {
        'method': "predict",
    }
}

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())