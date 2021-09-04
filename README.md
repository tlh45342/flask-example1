# INTRODUCTION

Fbone (Flask bone) is a [Flask](http://flask.pocoo.org) (Python microframework) template/bootstrap/boilerplate application, with best practices (I hope).

You can use it for

- learning Flask.
- kicking off your new project.

## COMPONENTS

### Frontend

- [HTML5 Boilerplate](https://github.com/h5bp/html5-boilerplate)
- [jQuery](http://jquery.com/)

## STRUCTURE

    ├── CHANGES                     Change logs
    ├── README.markdown
    ├── fabfile.py                  Fabric file to automated managament project
    ├── fbone.conf                  Apache config
    ├── requirements.txt            3rd libraries
    ├── wsgi.py                     Wsgi app
    ├── app
       ├── __init__.py
       ├── app.py                   Main App
       ├── config.py                Develop / Testing configs
       ├── user
       ├── api
       ├── static                   Static files
       │   ├── css
       │   └── robots.txt
       └── templates                Jinja2 templates
           ├── errors
           ├── frontend
           ├── index.html
 
## TODO

- Upgrade to [Python3k](http
