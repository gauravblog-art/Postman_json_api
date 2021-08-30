

import requests

# API URL

url = "https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=0dd8208d253bfa9ef80334ac7412a2d6&user_id=193812655%40N07&format=json&nojsoncallback=1"



# Send Get Request
response = requests.get(url)

print(response.json())
print(response.status_code)