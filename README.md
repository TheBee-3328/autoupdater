# autoupdater
Python code for automatic software update. If there is a new version, updater file will automatically update the software from the software download link.

**Setup**
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
