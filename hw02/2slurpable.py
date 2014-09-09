import csv
dictionary={}
with open("states, territories and abbreviations (source).txt","r+") as myfile:
        text=myfile.read()
        newtext=text.split()
for i in range(0,len(newtext),2):
        dictionary[newtext[i]]=newtext[i+1]
print dictionary

def main():        
        with open("flat_file_database.csv","wb") as outfile:
                w=csv.DictWriter(outfile,dictionary.keys())
                w.writeheader()
                w.writerow(dictionary)        
if __name__=='__main__':
        main()