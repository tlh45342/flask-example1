from flask import Flask
from flask import render_template, url_for, flash, request, redirect, Response
import sqlite3

from forms import LoginForm


# ------------------------------
 
if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080,threaded=True)
