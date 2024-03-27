# API: An Application Programming Interface (API) is a set of commands, functions, protocols and objects that
# programmers can use to create software or interact with an external system.

import requests  # must be installed

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response by default contains the response code to our request, which can be any of these values:
# 1xx = informational, in process
# 2xx = success
# 3xx = redirection
# 4xx = client error
# 5xx = server error

response.raise_for_status()  # raise_for_status() is the method for handling request errors and error codes

data = response.json()  # response.json() contains the actual data in the form of a dictionary
print(data)

latitude = response.json()["iss_position"]["latitude"]  # we can get specific values by tapping into specific keys
longitud = response.json()["iss_position"]["longitude"]

iss_position = (latitude, longitud)
print(iss_position)
