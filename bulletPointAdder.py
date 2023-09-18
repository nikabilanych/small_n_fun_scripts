#! python3


#add bullet points to text from the clipboard
import pyperclip
text=pyperclip.paste()

lines=text.split('\n')
for i in range(len(lines)):
    lines[i]='* '+lines[i]
text='\n'.join(lines)
pyperclip.copy(text)
#return copied content back into the clipboard w the bullet points



