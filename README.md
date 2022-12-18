<img src="github_logo.png"></img>
<br>
Social Media Archival Utility
<br>
<h1>Installation and Use</h1>

To run Salii on your own system, you are going to need to run a Linux or Unix distribution with Python 3 and Dialog installed.

Just run this in your terminal and you should be fine.

`sudo apt update -y && sudo apt install python3 python3-pip dialog -y && pip3 install configparser tweepy wget mysql-connector-python pythondialog colorama`

When you run the service for the first time, you will be required to fill out an automatically generated form. You can ignore the MYSQL section of
the setup dialog for now since this project is meant to report to a central database, but you can change those variables by navigating to `libraries/sqlmod.py`
and replacing the low access keys provided with your own.

<h1>Custom Utilization</h1>

For custom instances of this bot, you will probably want to change some stuff. The list below will have data related to what you may want to change:

<h2>Tags</h3>

When you want to change what the bot looks for, you will want to change the tags. These tags can be found in the `main.py` file for now.

NOTE: If you are using existing API tags which where used for Salii, you will want to remove them by adding these lines of code after line 
line 120.

`for RemovedTag in ["@saliibot", "#saliibot", "#Saliibot", "@Saliibot"]:
    stream.DeleteRule(RemovedTag)
 exit()`
 
After the program quits, you should be able to remove those lines and restart it like normal.
 
<h2>Databases</h2>
 
Salii uses MYSQL since it runs as a web accessible archive. I ain't about to get into setting up MYSQL for linux so I'm gonna let you 
look that up on YouTube. Here's the SQL file for it though.

<a href="https://github.com/808-Dev/Salii/blob/main/salii.sql">Download Template File Here</a>

<h2>To Do:</h2>

-Add filters (Phone number, address and other personally identifiable stuff)
-Clean up code
-Make images downloadable
