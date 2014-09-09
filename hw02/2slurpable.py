import csv  # Imports the csv module
dictionary={}  # creates an empty dictionary called dictionary
with open("states, territories and abbreviations (source).txt","r+") as myfile:  # opens a plain text file for reading and calls it as myfile
        text=myfile.read()  # creates "text" which is the contents of myfile
        newtext=text.split()  # creates "newtext" which consists of text split 
for i in range(0,len(newtext),2):  # for the information in range of "newtext"
        dictionary[newtext[i]]=newtext[i+1]  # modifies dictionary and its key,value
	
def main():        
        with open("flat_file_database.csv","wb") as outfile:  # opens csv file for writing and assigns it as "outfile"
                w=csv.DictWriter(outfile,dictionary.keys())  # assigns variable w to DictWriter function to write dictionary keys into csv files in given the format
                w.writeheader()
                w.writerow(dictionary)
        outfile.close()  # closes the open for writing outfile
        with open("plain_output.txt","w") as plain:  # opens plain text file for writing and assigns it as "plain"
		for i in dictionary:  # for the information in dictionary
			plain.write(i + "," + ".".join(dictionary[i]) + "\n")  # write the information from dictionary to the plain text file in given format
	plain.close()  # closes the open for writing plain text file
if __name__=='__main__':
        main()