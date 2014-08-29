dictionary={}
with open("states, territories and abbreviations.txt","r+") as myfile:
        text=myfile.read()
        newtext=text.split()
for i in range(0,len(newtext),2):
        dictionary[newtext[i]]=newtext[i+1]
print dictionary