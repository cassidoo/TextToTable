import shutil
import os
import urllib

myFile = open('names.txt','r') # file from which you're reading
newFile = open("file.html", "w") # file to which you'll write

newFile.write("<table>"+"\n") # start table tag

for line in myFile:
	newFile.write("\t<tr>\n\t\t<td>\n" + "\t\t\t" + line + "\t\t</td>\n\t</tr>\n") # where the magic happens

newFile.write("</table>") # end table tag

myFile.close()
newFile.close()