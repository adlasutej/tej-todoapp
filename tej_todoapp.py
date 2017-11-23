from flask import Flask
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sutej:Sairam123@localhost/tej_todoapp'
app.secret_key="Sairam@123"
from views import *
 
if __name__ == '__main__':
	app.run()