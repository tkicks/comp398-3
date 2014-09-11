import markdown, codecs  # Imports the markdown and codecs modules

x=input("Enter your input file (ending with .md) within quotations: ")  # assigns first user input to variable x
y=input("Enter the title of your output file (ending with .html) within quotations: ")  # assigns second user input to variable y

def converter(x,y):
    input_file=codecs.open(x,mode="r",encoding="utf-8")
    contents=input_file.read()
    html=markdown.markdown(contents)
    output_file=codecs.open(y,"w",encoding="utf-8")
    return output_file.write(html)

"""
A function named converter takes arguments/uses previously defined variabes x and y. input_file opens the given input file based on user input for reading and ensures the encoding is utf-8. html is using the markdown feature on contents (the contents of the input file). the function then returns a new output file with a name given by the user's 2nd input.
"""

def main():
    
    converter(x,y)  #calls to function converter using two user inputs
    
if __name__=='__main__':
    main()