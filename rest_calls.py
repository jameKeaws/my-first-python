import requests

url = 'https://jsonplaceholder.typicode.com/photos'

# response = requests.get(url)

# print(response.json())

myJsonPayload = {'albumId': 1, 'title': 'test', 'url': 'nothing.com', 'thumbnailUrl':'nothing.com'}

# postResponse = requests.post(url, json=myJsonPayload)

# print(postResponse.json())

putUrl = 'https://jsonplaceholder.typicode.com/photos/100'

putResponse = requests.put(putUrl, json=myJsonPayload)

print(f'Put response {putResponse.json()}')

deleteUrl = 'https://jsonplaceholder.typicode.com/photos/100'

deleteResponse = requests.delete(deleteUrl)

print(f'Delete response : {deleteResponse.json()}')

