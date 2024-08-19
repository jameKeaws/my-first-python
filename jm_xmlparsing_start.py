import xml.dom.minidom

def main():
    # Use the parse() function to load and parse the xml file
    # This will create an in memory dom object
    doc = xml.dom.minidom.parse("samplexml.xml")
    
    # Print out the document node and the name of the first child tag
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    
    # Get a list of xml tags from the document and print each one
    skills = doc.getElementsByTagName("skill")
    print(skills.length, " skills are listed")
    for anySkill in skills:
        print(anySkill.getAttribute("name"))
        
    # Create a new xml tag and add it to the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name","Guava")
    doc.firstChild.appendChild(newSkill)
    
    
    skills = doc.getElementsByTagName("skill")
    for anySkill in skills:
        print(anySkill.getAttribute("name"))

if __name__ == "__main__":
    main()