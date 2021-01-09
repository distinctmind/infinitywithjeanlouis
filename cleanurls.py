""" 
Often after performing a wget -p -k http://example.com
The resulting files will include static resources with query strings appended.
For example: 
wp-content/themes/salient/css/fonts/fontawesome-webfont.woff?v=4.2
etc..
This script strips away the query strings so that you can serve the site statically.
This is the first step in porting a theme from another CMS to a Diazo based Plone theme
"""
import os
import re

for root, dirs, files in os.walk("."):
    print(root)
    for file in files:
        file_to_open = os.path.join(root, file)
        print(file_to_open)
        if "index.html" in file_to_open:
        # if file == "index.html":
            print(os.path.abspath(file))
            with open(file_to_open, "r") as indexfile:
                print("opening")
                lines = indexfile.readlines()
                count=0
                for line in lines:
                    if line.find("%") != -1:
                        print("FOUND symbol")
                        print(line)
                        newstr=""
                        if ".css" in line:
                            newstr= re.sub('%.{14}.css','',line)
                            lines[count] = newstr
                        elif ".js" in line:
                            newstr= re.sub('%.{14}','',line)
                            lines[count] = newstr
                        print(newstr)
                        
                        
                    count = count + 1
            with open(file_to_open,"w") as indexfilew:
                indexfilew.writelines(lines)
        if '?' in file:
            newname = file.split('?')[0]
            oldpath = root + os.sep + file
            newpath = root + os.sep + newname
            os.rename(oldpath,newpath)
