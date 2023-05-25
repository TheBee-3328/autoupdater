import urllib.request
import os
import shutil
import json
import tkinter
import tkinter.messagebox

name = data["name"]
version = data["version"]
check = data["autoupdate"]

vurl = data["data"][0]["vurl"]
vtarget = data["data"][0]["vtarget"]
furl = data["data"][0]["furl"]
ftarget = data["data"][0]["ftarget"]
cftarget = data["data"][0]["cftarget"]

CHECK_FOLDER = os.path.isdir("./temp") #check if temp folder exists

if not CHECK_FOLDER: # if folder doesn't exist, execute following actions
    os.makedirs("./temp") #creates the direcotry temp

if check == "True" or check == True: #check if the autoupdate is eneabled

    #version download
    url = vurl #this is the url of the file with latest published version
    print ("download start!") #debug line
    filename, headers = urllib.request.urlretrieve(url, filename=vtarget) #download the version file
    print ("download complete!") #debug line
    print ("download file location: ", filename) #debug line
    print ("download headers: ", headers) #debug line

    f = open("./temp/v.txt", "r+") #open temp version file
    version_downloaded = f.read() #read temp version file
    f.close() #close temp version file

    if not version == version_downloaded: #if versions does not match

        #replacing exe file with a new version
        url = furl #get the new version file
        print ("download start!") #debug line
        filename, headers = urllib.request.urlretrieve(url, filename=ftarget) #download the new version file
        print ("download complete!") #debug line
        print ("download file location: ", filename) #debug line
        print ("download headers: ", headers) #debug line
        os.remove(cftarget) #remove the old version file
        shutil.copyfile(ftarget, cftarget) #copy the file from temp folder to the main folder

        #changing current version in the .json file
        f = open("settings.json", "r+") #openning the .json file where current verison and the other settings are stored in
        vv = f.read() #read the content of the file to variable vv
        f.close() #close the file

        vvn = vv.replace(f'"version": "{version}"', f'"version": "{version_downloaded}"') #replace the old version with the new version
        
        f = open("settings.json", "w+") #opening the .json file with current version and the other settings
        f.seek(0) #clear the file in case python write funcion does not clear it
        f.write(vvn) #write vv varibale with a new version into the file
        f.close() #close the file
        tkinter.messagebox.showinfo(Title="Update successfull", message=f"{name} was successfully updated.")
