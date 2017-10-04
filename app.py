
from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'finn'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.195.14.10'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format

@app.route("/add")
def add(name, email) :
	cur = mysql.connection.cursor()
	cur.execute('''INSERT INTO students (studentName, email) values ('%s', '%s'); COMMIT;''' % (name, email))
	return 'Hi'

@app.route("/update")
def update(name, email, id):
	cur = mysql.connection.cursor()
	cur.execute('''UPDATE  students set studentName = %s, email = %s WHERE studentID = %d; commit;''' % (name, email, id))
	return 'Hi again'

@app.route("/delete")
def delete(id):
	cur = mysql.connection.cursor()
	cur.execute('''DELETE  FROM students WHERE studentID = %d; commit;''' % (id))
	return 'Hi third time'

if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000
