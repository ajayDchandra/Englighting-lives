
import os
import shutil
from os import path


def make_post(year, post,image,name):

    ##Takes the post from the year folder inside the blogs folder
    file1 = open("./blogs/" + year + "/" + post,"rt")

    #reads the file line by line to capture each element
    title = str(file1.readline())
    author = str(file1.readline())
    lead = str(file1.readline())
    lead = lead + str(file1.readline())
    description = str(file1.readlines())

    file1.close()
    
    year.strip()

    imagelink = "../images/post_pictures/{}".format(image)
    fin = open("single.html", "rt")

    ##Puts a html file in the websites folder of the blogs folder
    fout = open("./blogs/" + year + "/websites/" + name , "w+")
    
    changes = {
        "title_sample":title,
        "author_sample": author,
        "pic_sample":imagelink,
        "lead_sample":lead,
        "description_sample":description
        }

    for line in fin:
        for item in changes.keys():
            if item in line:
                line = line.replace(item,changes[item])

        fout.write(line)    
    
    fin.close()
    fout.close()

Year = input("Year of publishing: ")
Image = input("Name of the image with its extension: ")
Post = input("Name of the post file: ")
Name = input("Enter the name of the resulting file (Add '.html' extension to it)")

make_post(Year,Post,Image,Name)