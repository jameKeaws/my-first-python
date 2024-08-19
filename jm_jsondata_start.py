import urllib.request
import json

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    print(type(theJSON))
    print(theJSON)
    
    # Find metadata key in dictionary
    if "title" in theJSON["metadata"]:
        # Then find the title key in metadata dictionary
        print("title", theJSON["metadata"]["title"])
        
    # Output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print(count, "events recorded")
    
    # For each event, print the place where it occured
    # for anyFeature in theJSON["features"]:
    #     place = anyFeature["properties"]["place"]
    #     print("This is a place", place)
    
    # Print the events that have magnitude less than 1.3
    for anyFeature in theJSON["features"]:
        magnitude = anyFeature["properties"]["mag"]
        # print(type(magnitude))
        place = anyFeature["properties"]["place"]
        if magnitude > 1.3:
            print("The magnitude of the earthquake is ", str(magnitude), "in",place)
            

    
def main():
    url_data = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson'
    # Open the url
    weburl = urllib.request.urlopen(url_data)
    print("Http result code:", str(weburl.getcode()))
    # Read the data
    if (weburl.getcode() == 200):
        data = weburl.read()
        # print(data)
        printResults(data)
    else:
        print('Received error from the server', str(weburl.getcode()))
    
if __name__ == "__main__":
    main()