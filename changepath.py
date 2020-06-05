import re

with open("single.html", "r+") as file:
 pattern = r'href=\"(?!https)([^#]*?)\">$|src=\"(.*)\"'
 for line in file:
  a = re.search(pattern,line)
  print(a)
  if a != None:
   line.replace(a.group(1),"../../.." + a.group(1))
   line.replace(a.group(2),"../../../"+ a.group(2))
  else:
    continue
 file.close()  
