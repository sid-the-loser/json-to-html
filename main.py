import json

keywords = ["single", "attributes"]

filename = input("Enter the filename: ")
data = json.load(open(filename, "r"))

def notforcheck(value, lst:list):
    flag = False
    for i in lst:
        if value == i:
            break
    else:
        flag = True
    return flag

output = ""

def write(d:dict, parent_tag:str):
    global output
    output += "<"+parent_tag
    if keywords[1] in d:
        for i in d[keywords[1]]:
            output += f' {i}="{d[keywords[1]][i]}"'
    output += ">"
    flag = True
    if keywords[0] in d and d[keywords[0]]:
        flag = False
    
    if flag:
        for i in d:
            if notforcheck(i, keywords):
                if type(d[i]) == type({}):
                    write(d[i], i)
                else:
                    output += f"<{i}>{d[i]}</{i}>"
        output += f"</{parent_tag}>"

write(data, "html")
f = open(filename+".html", "w")
f.write("<!DOCTYPE html>")
f.write(output)
f.close()
