import csv
import os
from email.quoprimime import quote
from lib2to3.pgen2.token import NEWLINE
from urllib import request
import urllib.request
from flask import Flask,render_template,request,redirect
app = Flask(__name__)
print(__name__)



@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def home(page_name):
    return render_template(page_name)

def write__to_csv(data):
    with open('D:/python practice/flask_project/database.csv',mode='a') as database2:
        email= data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data  = request.form.to_dict()
        write__to_csv(data)
        print(data)
        return redirect('/thankyou.html')
    else:
        print('something went wrong')

port=os.environ.get("PORT", 5000)
app.run(debug=False, host="0.0.0.0",port=port )
