import urllib.request

def main():
    weburl = urllib.request.urlopen("http://www.google.com/")
    print("Http result code:", weburl.getcode())
    data = weburl.read()
    print(data)
    
if __name__ == "__main__":
    main()