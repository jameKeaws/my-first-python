from html.parser import HTMLParser

paragraphs = 0
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("This is the comment we encountered:", data)
        pos = self.getpos()
        print("At line:", pos[0], " character position", pos[1])
    
    def handle_starttag(self, tag, attrs):
        print("This is the start tag we encountered:", tag)
        pos = self.getpos()
        print("At line:", pos[0], " character position", pos[1])
        
        global paragraphs
        if tag == "p":
            paragraphs +=1
            
        if len(attrs) > 0:
            print("Attributes:")
            for anyAttr in attrs:
                print("\t", anyAttr[0], "=", anyAttr[1])
    
    
    def handle_data(self, data):
        if data.isspace():
            return
        
        print("This is the text data we encountered:", data)
        pos = self.getpos()
        print("At line:", pos[0], " character position", pos[1])
    
    
def main():
    # Instantiate the parser and feed it some html
    myParser = MyHTMLParser()
    
    f_html = open("sample_original.html","r")
    if f_html.mode == "r":
        # Read the entire file
        contents = f_html.read()
        myParser.feed(contents)
    
    print("Paragraphs tag", paragraphs)

if __name__ == "__main__":
    main()