# autoupdater
Python code for automatic software update. If there is a new version, updater file will automatically update the software from the software download link.

#Setup
- *1* - Clone the repository into the new folder using following code : `git clone https://github.com/TheBee-3328/autoupdater`
- *2* - Open the **settings.json** file and edit the following variables:
  - `name` : Change this to name of your software
  - `version` : Change this to the current version of the app
  - `autoupdate` : Set this to **True** for automatic updates
  - `vurl` : Set this to your **version.txt** download link for the version checl
  - `vtarget` : set this to location where file will be temporarily saved
  - `furl` : Set this to your **file** download link location
  - `ftarget` : Set this to location where app file will be temporarily saved.
  - `cftarget` : Set this to location where main app is saved on computer
- *3* - Add updater to the direcotry with the main app
- *4* - Set the updater to run the app after the update or without the update


#Credits

This code was coded in Visual Studio Code by TheBee. Any use that this page does not allow is prohibited!

**Users are not allowed:**
- to publish the file as their own
- to edit the file and publish it as their own
- sell the file

**Users are allowed to:**
- Use the file for personal use
- Use the file for comercial use
- Edit the file in any way
- Sell the software that uses the updater (AutoUpdater must be part of the cheapest plan)

#Future plans
- **Add the manual update option**
- **Add the messagebox on update**
- **Add the messagebox that asks you if you want to update (only when autoupdate is set to False)**
