def process_string(string, prompts=True):
    # Replace "- - " with "- "
    string = string.replace("- - ", "- ")
    
    string = string.split("ChatGP")

    strList = []
    for i in range(len(string)):
        if (string[i][:2] == "T:"):
            strList.append(string[i])

    for i in range(len(strList)):
        if "Person:" in strList[i]:
            strList[i] = strList[i][:strList[i].index("Person:")]

    # Remove trailing spaces from each element
    strList = [phrase.rstrip() for phrase in strList]

    chunkPrompt = "\n\nYour responses should contain lots of sensory details. Your word choice should parallel that of George R R Martin. Do not use bland wording. Your responses should occasionally contain statements regarding the color of light on characters faces and light sources. Your responses should be extremely detail oriented and long. Your responses should never summarize dialogue. Your responses should contain several lines of dialogue when two characters are talking. CHUNK: "

    for i in range(len(strList)):
        strList[i] = strList[i].replace("T: \n- ","")
        strList[i] = strList[i].replace("\n\n",chunkPrompt)

    for i in range(len(strList)):
        while strList[i][-2:] == "\n":
            strList[i] = strList[i][:-2]

    length = 0
    strList[1] = chunkPrompt[2:] + strList[1]

    for i in range(len(strList)-1):
        length+=len(strList[i+1])
        print(strList[i+1]+"\n")
        
    print("Length: "+str(length))

# Example usage
input_str = """
CONTENT GOES HERE
"""

process_string(input_str)
