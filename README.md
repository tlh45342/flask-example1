# INTRODUCTION

![Tests](https://github.com/maxcountryman/flask-login/workflows/Tests/badge.svg)
[![Software License](https://img.shields.io/badge/license-Apache%202-blue)](LICENSE)

flask-example1 is a simple example flask app that implements authentication.  This is not designed to be pretty, or clever. This is simply designed TO WORK.  There are a lot of Flask examples out there that either are incomplete or are online tutorials that could not have ever been independently checked as they are missing critical pieces (glue, code, whatever).  Then there are long drawn-out blogs (for which I am thankful for) but where the "magic" of the developing intermediate steps per stage are missing.  Hence:  There is a flask-example2 as a seperate which adopts additional complexity and is designed to look more like a portal / application. 

Work will have been done to test this on Windows 10, Ubuntu 20.04.3 LTS, Apple Mac OS x.

- learning Flask.
- kicking off your a new project.

## Version:

(9/21/2021)  I think this works and usefully demonstrates a combination of Flask, Sqlite, and flask_login

## NOTES:

I have left commented print statements in place (#print) I would encourage new users of flask to evaluate some of the variables in their different states.  I am  confident that there are coding tricks that I have still to learn from the innards of flask, and implementing items in python.

Please note that SQLITE is kinda crap when it comes from quering rowcount when there are no matches.  For now this version simply uses the try and exception method to catch this.  My experience show I can print rowcount and get -1 for a number of choices.  This does not seem to indicates ... well anything to my surprise. 

## INSTALLATION

```bash
git clone https://github.com/tlh45342/flask-example1.git
cd flask-example1
pip install -r requirements.txt
python server.py
```

## SIDEBAR: Notes for creating a service for Linux based distributions

I am putting my notes here now - because I will use them.  Consider these random notes used to implement the Flask APP as a service.

To create a service entry cd /etc/systemd/system
Create a file that looks something like is found in the following block.
As much as I hate assumptions - you will need to edit this to your tastes and for your environment.

```bash
[Unit]
Description=flask-example1

[Service]
WorkingDirectory=/mnt/python/flask-example1/
ExecStart=/usr/local/bin/gunicorn -b 0.0.0.0:80 -w 4 server:app

[Install]
WantedBy=multi-user.target
```

The key commands for reference are: 

```bash
sudo systemctl daemon-reload
sudo systemctl start flask1.service
sudo systemctl restart flask1.service
sudo systemctl stop flask1.service
```

## STRUCTURE

    ????????? LICENSE                     Copy of the Apache 2.0 license
    ????????? README.md                   This file.
    ????????? requirements.txt            module requirements
    ????????? server.py                   Wsgi app
    ????????? app
       ????????? __init__.py
       ????????? app.py                   Main App
       ????????? routes.py                flask routes
       ????????? user.py                  manager user management routes
       ????????? user_db.py               manage sqlite3 db       
       ????????? static                   Static files
       ???   ????????? mystyle.css          Fairly minimalistic choices   
       ????????? templates                Jinja2 templates
           ????????? login.html
           ????????? protected.html
           ????????? welcome.html
 
## LICENSE

flask-example1 is licensed under the Apache License, Version 2.0. See LICENSE for the full license text.

## ACKNOWLEDGEMENTS

Many thanks to Python, Flask and other good stacks.
Please note that this does include http://getskeleton.com/ skeleton.css and normal.css (credit to them)

URLS:
  https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
  https://medium.com/analytics-vidhya/how-to-use-flask-login-with-sqlite3-9891b3248324
     * There are errors in the above medium document (reviewed: 9/4/2021) - however I was able to bridge the gap and fill in holes in my knowledge with this.
  https://github.com/anfederico/flaskex
     * This example brought it home for me.
