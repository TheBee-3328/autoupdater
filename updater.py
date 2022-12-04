import urllib.request
import os
import shutil

CHECK_FOLDER = os.path.isdir("./temp") #check if temp folder exists

if not CHECK_FOLDER: # if folder doesn't exist, execute following actions
    os.makedirs("./tmep") #creates the direcotry temp

#version read from the file
f = open("settings.json", "r+") #open the settings.json file where version and other settings are stored
file = f.readlines() #read the content of the file into version_file variable
f.close() #close the file and clear the f varibale

check = file[3] #pick the 4th line of the file (first line is 0) where autoupdate is set
check = check.replace('"', '') #remove all the " character
check = check.replace('autoupdate', '') #remove autoupdate text
check = check.replace(':', '') #remove : character
check = check.replace(' ', '') #remove all the spaces to only keep the autoupdate in the variable

if check == "True": #check if the autoupdate is eneabled

    #edit the version string for the correct version format
    version = file[1] #pick the second line of the file (first line is 0) where version is set
    version = version.replace('"', '') #remove all the " character
    version = version.replace('version', '') #remove version text
    version = version.replace(':', '') #remove : character
    version = version.replace(' ', '') #remove all the spaces to only keep the version in the variable

    vurl = file[6] #pick the 7th line of the file (first line is 0) where version is set
    vurl = vurl.replace('"', '') #remove all the " character
    vurl = vurl.replace('vurl', '') #remove vurl text
    vurl = vurl.replace(':', '') #remove : character
    vurl = vurl.replace(' ', '') #remove all the spaces to only keep the vurl in the variable

    vtarget = file[7] #pick the 8th line of the file (first line is 0) where version is set
    vtarget = vtarget.replace('"', '') #remove all the " character
    vtarget = vtarget.replace('vtarget', '') #remove vtarget text
    vtarget = vtarget.replace(':', '') #remove : character
    vtarget = vtarget.replace(' ', '') #remove all the spaces to only keep the vtarget in the variable

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

        furl = file[8] #pick the 9th line of the file (first line is 0) where version is set
        furl = furl.replace('"', '') #remove all the " character
        furl = furl.replace('furl', '') #remove furl text
        furl = furl.replace(':', '') #remove : character
        furl = furl.replace(' ', '') #remove all the spaces to only keep the furl in the variable

        ftarget = file[9] #pick the 10th line of the file (first line is 0) where version is set
        ftarget = ftarget.replace('"', '') #remove all the " character
        ftarget = ftarget.replace('ftarget', '') #remove ftarget text
        ftarget = ftarget.replace(':', '') #remove : character
        ftarget = ftarget.replace(' ', '') #remove all the spaces to only keep the ftarget in the variable

        cftarget = file[10] #pick the 11th line of the file (first line is 0) where version is set
        cftarget = cftarget.replace('"', '') #remove all the " character
        cftarget = cftarget.replace('cftarget', '') #remove cftarget text
        cftarget = cftarget.replace(':', '') #remove : character
        cftarget = cftarget.replace(' ', '') #remove all the spaces to only keep the cftarget in the variable

        #replacing exe file with a new version
        url = furl #get the new version file
        print ("download start!") #debug line
        filename, headers = urllib.request.urlretrieve(url, filename=ftarget) #download the new version file
        print ("download complete!") #debug line
        print ("download file location: ", filename) #debug line
        print ("download headers: ", headers) #debug line
        os.remove("TheBee RPC.exe") #remove the old version file
        shutil.copyfile(ftarget, cftarget) #copy the file from temp folder to the main folder

        #changing current version in the .json file
        f = open("settings.json", "r+") #openning the .json file where current verison and the other settings are stored in
        vv = f.read() #read the content of the file to variable vv
        f.close() #close the file

        vvn = vv.replace(f'"version": "{version}"', f'"version": "{version_downloaded}"') #replace the old version with the new version
        
        f = open("sttings.json", "w+") #opening the .json file with current version and the other settings
        f.seek(0) #clear the file in case python write funcion does not clear it
        f.write(vvn) #write vv varibale with a new version into the file
        f.close() #close the file