This README focus on how to set up you computer and launch this code for chess tournaments use with the following actions:
-save tournament's informations
-save player's informations
-give player's pairing
-save results for each round and tournament
-display reports of saved tournaments and players

Using this program will allow you to save all needed informations in a json database 

Be careful: - For each code line found in the README between "", take only the text and forget about ""
	    - In your powershell windows, using your right click will automatically paste
	    - In your terminal application for mac or linux use the right click and paste(cf after in this README)

PYTHON INSTALLATION:
To run this code you need Python 3.8 version or further 
Download python's executable file on the following website: "https://www.python.org/downloads/"
Lauch the installation without any modification.

CREATION OF THE WORKING REPOSITORY:
To run this code and find the informations you seek for, you need to create a working folder.
With your explorer go at the place you choose to work, create a new working folder. 

SET YOUR SYSTEM TO THE RIGHT PLACE (your working folder pathway):
You now need to open your terminal:
- windows: use Windows Powershell(admin). to find it use windows + x as keyboard shortcut 
- mac: use terminal. to find it open your Utilities folder in applications
- linux: use terminal. to find it type terminal in your applications's research bar

In the new windows, you have to put your working folder's path
For that go back to your windows explorer, go in your working folder.
now you're in, copy the pathway of your folder found in the adress bar (C:\Users\...\.... for windows)

In the terminal type "cd .." several time. you need to be at the root of your computer (C: for Windows, /Home on Mac)
Next type "cd 'yourfolderpathwaythatyoujustcopied'" (this time keep the small quote marksand let a space after cd) and ENTER

Your computer knows right now where it have to work

CREATE A SPECIAL WORKING ENVIRONMENT:
With Python, you have to create a special working environment to install specifics modules for each project.
In the terminal using the following command will set a new environment 'env':
"python -m venv env" and ENTER

You now need to activate it, for that:
-On Windows: "source env/Scripts/activate" or env/Scripts/activate.ps1 and ENTER
-On Mac and Linux: "source env/bin/activate" and ENTER

if you have any issue to activate your environment:
-go to the env folder and search for the folder name which contain the "activate" file 
-replace "Scripts" by this name

With that your working environment is now running

DOWNLOAD REQUESTED FILES AND MODULES:
go to the following repository: https://github.com/Satupathe/OC-P4-AG
-find the green button
-clic on the arrow
-choose download ZIP
-download the zip file
-extract its content and put all files and folders in your working folder

now use this command on the terminal:
"pip install -r requirements.txt"

This step will install necessary modules to execute the code

LAUNCH OF THE CODE:
In the terminal type "python main.py" and ENTER
it will launch the program and you will see the main menu asking for the first action 

To navigate through this program, just follow displayed instructions, type one of proposed possibilities and put ENTER

QUIT THE CODE:
Return first to the main menu, type "exit" and you'll see following message "Merci d'avoir utilisé ce programme"
You have now quit this program.

SHOW FLAKE8 HTML REPORT:
Be careful: you can't execute this action when using the pairing program, 
Be sure to quit the pairing program (with instructions in the section just above) before calling for Flake8 report

With your terminal still set on your working directory and your working activated environment:
Type "flake8 --format=html --htmldir=flake-report" and ENTER
This will create a new directory called "flake-report"
Go inside and open "index.html": this will open an html window showing "All good"

QUIT YOUR WORKING ENVIRONMENT AND TERMINAL:
Type "deactivate" in your terminal: this action will shut down your working environment 
You now can quit your terminal using the closing button

Thank for reading this README and using my program