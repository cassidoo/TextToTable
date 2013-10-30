import shutil
import os
import urllib

myFile = open('names.txt','r') # file you're reading from
newFile = open("file.txt", "w") # file that'll be written to

newFile.write("<table>"+"\n")

for line in myFile:
	newFile.write("\t<tr>\n\t\t<td>\n"+ "\t\t\t" + line+"\t\t</td>\n\t</tr>\n")

newFile.write("</table>")

myFile.close()
newFile.close()