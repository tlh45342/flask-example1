# INTRODUCTION

![Tests](https://github.com/maxcountryman/flask-login/workflows/Tests/badge.svg)
[![Software License](https://img.shields.io/badge/license-Apache%202-blue)](LICENSE)

flask-example1 is a simple example flask app that implements authentication.  This is not designed to be pretty, or clever per-se.  This is not nearly finished. 

- learning Flask.
- kicking off your new project.

## INSTALLATION

```bash
git clone https://github.com/tlh45342/flask-example1.git
```

To make sure you have all the python modules installed.

```bash
pip install -r requirements.txt
```

### Frontend

- [HTML5 Boilerplate](https://github.com/h5bp/html5-boilerplate)
- [jQuery](http://jquery.com/)

## STRUCTURE

    ├── LICENSE                     Copy of the Apache 2.0 license
    ├── requirements.txt            module requirements
    ├── server.py                   Wsgi app
    ├── app
       ├── __init__.py
       ├── app.py                   Main App
       ├── routes.py                flask routes
       ├── static                   Static files
       │   ├── css
       │      ├── normalize.css    
       │      └── skeleton.css      
       └── templates                Jinja2 templates
           ├── html_tamplates.html
           ├── login.html
           └── welcome.html
 
## TODO

- Upgrade to [Python3k](http

## LICENSE

flask-example1 is licensed under the Apache License, Version 2.0. See LICENSE for the full license text.

## ACKNOWLEDGEMENTS

Many thanks to Python, Flask and other good stacks.
Please note that this does include http://getskeleton.com/ skeleton.css and normal.css
