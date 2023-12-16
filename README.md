Displays your distro, ram usage and uptime as your activity in discord

## Installation:
1- Clone or download the repository.

2- Download the required packages.
```
pip install pypresence
```
```
pip install distro
```

## usage: 
Screenshot of how it looks like:

![image](https://github.com/L3pux/Discord-pc-usage-activity-/assets/123013187/786c236a-c579-4b1f-9c4e-fc4c29124e7b)

1- Go to [Discord Developer's](https://discord.com/developers/) site and login

2- Click on "New Application" and enter your name (NOTE: the name you'll enter is going to be what's shown in the activity)

3- Copy the client ID

4- Paste the ID in the code, search for ```"client_id="EnterYourID"``` in l3xactivity.py

5- Run the program

```
python l3xactivity.py
```
## to add your image:

1- Go to rich presence > art assets

2- click on Add Image(s) and name the image "status"

## Notes:
* currently it's only for linux but I might make another program for windows

* If your on debian or any debian based distro you might need to use "python3" instead of just "python"

* If your on arch or any arch based distro you need to create a python virtual environment to use pip
