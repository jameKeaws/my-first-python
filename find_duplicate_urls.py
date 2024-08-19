import requests

photosUrl = 'https://jsonplaceholder.typicode.com/photos'

allPhotosResponse = requests.get(photosUrl)

# print(allPhotosResponse.json())

photoList = allPhotosResponse.json()
photoUrlList = []
photoUrlSet = set()

for anyPhoto in photoList:
    anyPhotoDictionary = anyPhoto
    for key in anyPhotoDictionary:
        # print(key)
        # print(anyPhotoDictionary[key])
        if key == 'url':
            photoUrlList.append(anyPhotoDictionary[key])
 
photoUrlListLength = len(photoUrlList)         
for anyItem in photoUrlList:
    if anyItem in photoUrlSet:
        print(anyItem)
    photoUrlSet.add(anyItem)

print(len(photoUrlSet))
    
