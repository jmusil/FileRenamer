# To change this template, choose Tools | Templates
# and open the template in the editor.
import os

#TODO: remove non-png files from list of files in directory
#TODO: skip renaming in case file already exists

__author__="Josef Musil"
__date__ ="$10.7.2010 13:25:28$"

if __name__ == "__main__":
    print "Renaming started..."

#get directory content into an array
dir = os.listdir(os.getcwd())

#for each item in directory listing
for item in dir:
    #check whether this one is a directory or not
    if os.path.isdir(item):
        
        #get inside that directory
        os.chdir(item)

        #list all files
        files = os.listdir(os.getcwd())

        for file in files:
            #check if its png
            if os.path.splitext(file)[1] == '.png' or os.path.splitext(file)[1] == '.PNG':
                #check for amount of files in directory
                if len(files) != 1:
                    #rename and add index
                    print "Renaming " + file + " to " + item + '_' + str(files.index(file) ) +  '.png'
                    os.renames(file, item+'_'+ str(files.index(file)) +  '.png')

                else:
                    #prejmenuj
                    print "Renaming " + file + " to " + item + ".png"
                    os.renames(file, item+'.png')
                
        
        #get outside that directory
        os.chdir('..')

    else:
        print item + ' is a file, skipping...'

