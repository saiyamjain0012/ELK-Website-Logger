
from flask import render_template, redirect, request, url_for, flash,abort
from models import logger
import os
from flask import Flask

app = Flask(__name__)
title=''
status='new'

@app.route('/')
def home():
    return render_template('index.html',errormsg="")
   



@app.route('/components',methods=['POST'])
def component():
    global a
    global title
  
    val_id=request.form['cred_id']
    val_pass=request.form['cred_pass']
    try:
        
        print(val_id)
        print(val_pass)
    except:
        return render_template('index.html',errormsg="Please enter a valid Id Password")
    logger.login(val_id,val_pass)
    return render_template('options.html', title=title)



@app.route('/xps',methods=['POST'])
def dellxps():
    
    logger.product('Dell XPS')
    return render_template('xps.html')

@app.route('/allinone',methods=['POST'])
def dellallinone():
    
    logger.product('Dell All In One PC')
    return render_template('allinone.html')

@app.route('/inspiron',methods=['POST'])
def dellinspiron():

    logger.product('Dell Inspiron')
    return render_template('inspiron.html')

@app.route('/review',methods=['POST'])
def dellreview():
    
    return render_template('review.html')

@app.route('/thankyou',methods=['POST'])
def thanks():
    val_prod=request.form['prod']
    val_quality=request.form['quality']
    val_price=request.form['price']
    
    try:
        print(val_prod)
        print(val_quality)
        print(val_price)
        logger.review(val_prod,val_quality,val_price)
        
    except:
        return render_template('review.html',errormsg="Please select a valid option")
    return render_template('end.html')

if __name__ == '__main__':
    app.run(debug=True)
