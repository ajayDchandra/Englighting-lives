
import os
import shutil
from os import path


def make_post(year, post,image):

    
    file1 = open("./blogs/" + year + "/" + post,"rt")

    #reads the file line by line to capture each element
    title = file1.readline()
    author = file1.readline()
    lead = file1.readline()
    lead = lead + file1.readline()
    description = file1.readlines()

    file1.close()
    
    year.strip()

    imagelink = "../images/post_pictures/{}".format(image)
    fin = open("single.html", "rt")
    fout = open("./blogs/" + year + "/websites/1.html", "w+")
    
    changes = {
        "title_sample":title,
        "author_sample": author,
        "pic_sample":imagelink,
        "lead_sample":lead,
        "description_sample":description
        }

    for line in fin:
        for item,replacement in changes.items():
            if item in line:
                line = line.replace(item,replacement)

        fout.write(line)    
    
    fin.close()
    fout.close()
    print(year)
    #updateHtml()


def updateHtml():
    fpost = open("out.txt","r")

    post = fpost.read()
    
    fhtml = open("index.html","r")
    content = fhtml.readlines()
    fhtml.close()
    Word = '<!FirstPost>\n'
    

    for index,word in enumerate(content):
        for letter in word:
            if letter == "!":
                content[index] = "<!FirstPost> \n {}  /\n \n ".format(post)
    
    listToStr = ''.join([str(elem) for elem in content]) 


    fhtml = open("index.html","w")
    fhtml.write(listToStr)
    fhtml.close()


    fhtml.close()
    fpost.close()
    return 

Year = input("Year of publishing:")
Image = input("Name of the image with its extension:")
Post = input("Name of the post file")

make_post(Year,Post,Image)