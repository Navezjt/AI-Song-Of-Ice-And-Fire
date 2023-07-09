# re-format markdown chat to book

def flatten(lst):
    flattened_list = []
    for item in lst:
        if isinstance(item, list):
            flattened_list.extend(flatten(item))
        else:
            flattened_list.append(item)
    return flattened_list

def formatChat(chat):
    chunks = chat.split("ChatGPT: \n- ")
    for i in range(len(chunks)):
        while chunks[i][0] == "\n":
            chunks[i] = chunks[i][1:]
        chunks[i] = chunks[i].split("\n")

    chunks = flatten(chunks)
    newChunks = []
    for i in range(len(chunks)):
        if len(chunks[i]) > 0:
            while chunks[i][0] == "\n":
                chunks[i] = chunks[i][1:]
            
            if chunks[i][0:7] != "Person:" and chunks[i][0:16] != "- Your responses":
                newChunks.append(chunks[i])

    for i in range(len(newChunks)):
        if newChunks[i][:2] == "- ":
            newChunks[i] = newChunks[i][2:]
    
    return newChunks

chat = '''
'''

chunks = formatChat(chat)

for i in range(len(chunks)):
    print(chunks[i])
    if i % 4 == 3:
        print()
