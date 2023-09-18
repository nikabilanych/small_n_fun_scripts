#! python3
#add Wikipedia bullet points to each line of text in a file
import pyperclip

text=pyperclip.paste()
#text has been pasted

#split by \n, return list
lines=text.split('\n')


#now let's do something to it
#list of modified string
for i in range(len(lines)):
    lines[i]='* '+lines[i]
text='\n'.join(lines)
pyperclip.copy(text)
#join the list back together, the glue being yet again, \n



