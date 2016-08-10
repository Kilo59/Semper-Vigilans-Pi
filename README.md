# Semper-Vigilans-Pi
The Always Vigilant Network Monitoring Device

##[Word Doc](https://github.com/Kilo59/Semper-Vigilans-Pi/raw/master/SemperVigilansPi.doc)

![Example](https://github.com/Kilo59/Semper-Vigilans-Pi/blob/master/images/speed_tweet1.PNG?raw=true)

###Abstract
This paper outlines the creation and operation of a lightweight, remotely accessed Raspberry Pi based network testing device. The device interfaces with Twitter and Google App APIs to read from and send information back to the user.

###I.	INTRODUCTION 
The proliferation of low-cost high speed internet services has led to an increase in personal servers located within the home. Without a dedicated IT team, it can be difficult to diagnose and fix problems that arise while the user is away from home. The goal of this project is to create a lightweight network monitoring device that can send and receive instructions remotely. The device will be connected via Ethernet to the target network and will run periodic network speed and reliability tests (via Speedtest.net) that can be accessed remotely via Twitter and Google Drive integration. Network tests can be triggered remotely or at predefined times (peak times and off-peak times). Device will automatically document/log and store the tests it performs. The logs, will be stored in automatically generated Google Docs for easy remote access. Functions will be coded and implemented using Python 3.5. Due to the difficulty in obtaining a Pi Zero the Raspberry Pi 2 running Raspbian will be the platform for this project. Project should not require any peripherals or access to a screen apart from the initial setup. Twitter integration will use a private Twitter account so that sensitive information about the network is only viewable by approved followers.  Secondary goal of the project is to allow for the Device to read and execute instructions stored in a Google Doc or Google Sheet. Reading inputs from a text file, is relatively trivial to implement but presumably reading input from a web based cloud word processor would pose a much greater challenge. 

###II.	RASPBERRY PI SETUP
####A.	Raspberry Pi selection and OS selection
Any currently available Raspberry Pi platform can meet the modest requirements of this project. However, the scope of this paper will not cover the installation of an Ethernet access port, or wireless setup on a Raspberry Pi Zero. Raspberry Pi 2 and 3 both come with a functioning Ethernet access port standard. 
There are no set operating system requirements as long as the raspberry pi has a python interpreter installed and a way to add python library packages. The Debian-based operating system Raspbian includes these by default. The latest images are available at  www.raspberrypi.org. 
###B.	Installion of python libraries
To install libraries on the raspberry pi first install pip by using the following at the command line: sudo apt-get install python3-pip
The following python libraries must be installed via pip using the commands ‘pip install [libraryname]’. This must be repeated for each library. 
*	python-twitter
*	pyOpenSSL
*	oauthlib
*	oauth2client
*	gspread
*	time
*	datetime

###C.	Installation of main python script
Using a file transfer application such as Filezilla copy the main python file speed_tweet_v2.py and the modified speedtest_cli.py file into the root pi directory[1]. 
##III.	TWITTTER AND GOOGLE DOC SET UP
To implement Twitter and Google Doc interaction, app credentials must be obtained. 
###A.	Google Docs Set up
Google App credentials can be obtained at https://console.developers.google.com/project [2]. The credentials needed are for a ‘App Engine service account’ downloaded in a JSON format and stored in the raspberry pi root directory along with the main python script. 
A Google spreadsheet should be created using the referenced sample spreadsheet. If the title and worksheet titles are changed the corresponding references within the python scrip will need to be changed. Cell coordinates references will likewise also need to be changed if the Google Spreadsheet changes. 
###B.	Twitter Credentials and Set up
A Twitter account will need to be created and a Twitter app registered to receive the necessary credentials.
Twitter credentials must be obtained from https://apps.twitter.com/. Keys and access tokens must be obtained and inserted into the speed_tweet.py python script.[3]

##IV.	OPERATION AND USE
When running the device will check the Google Spreadsheet for configuration settings. It will match the current system time against the arguments it receives from the spreadsheet, if it finds a match a network test will procced. The network test results will be appended to a local .txt file stored on the local drive and the ‘log’ worksheet within the spreadsheet. The result will be ‘tweeted’ out if the appropriate argument is received. If indicated the tweet will be preceded by an @mention and followed by secondary tweet with a customized message. The script will loop according to an interval passed from the configuration sheet.

![Settings](https://github.com/Kilo59/Semper-Vigilans-Pi/blob/master/images/Capture.PNG?raw=true)

![TwitterBot](https://github.com/Kilo59/Semper-Vigilans-Pi/blob/master/images/Speed_tweeter.png?raw=true)

##V.	CONCLUSION
Potential improvements could take the form of twitter based configuration of the device and automated warning when network performance drops below a certain level. Limitations inherent to the Raspberry Pi Ethernet port results in inaccurate speed-tests on networks with over 100Mbits/s bandwidth. However, the device still retains its use as early detector of network problems even while the user is away from home.     
##REFERENCES

[1]	 https://github.com/Kilo59/Semper-Vigilans-Pi

[2]	https://github.com/burnash/gspread/blob/master/docs/oauth2.rst

[3]	https://python-twitter.readthedocs.io/en/latest/getting_started.html.

[4]	https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest_cli.py 
 
 
