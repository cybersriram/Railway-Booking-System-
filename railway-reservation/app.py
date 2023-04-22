from flask import Flask, render_template,request
import sqlite3

app = Flask(__name__, static_url_path="", static_folder="static")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store',methods=['POST', 'GET'])
def store():
   if request.method=='POST':
      try:
         fname=request.form['fname']
         lname=request.form['lname']
         from1=request.form['from1']
         to1=request.form['to1']
         date=request.form['date']
         type1=request.form['type1']
         count=request.form['count']
         class1=request.form['class1']
         email=request.form['email']
         tel=request.form['tel']
         payment=request.form['payment']
         conn = sqlite3.connect('')
         conn.execute("INSERT INTO details VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}')".format(fname,lname,from1,to1,date,type1,count,class1,email,tel,payment));
         conn.commit()
         conn.close()
         return render_template('index.html',response = "Booking was Successful")
      except Exception as e:
         print(e)
         return render_template('index.html',response = "Internal Server Error")
   else:
      return render_template('index.html',response = 'Error')

if __name__ == "__main__":
    app.run(debug = True)
