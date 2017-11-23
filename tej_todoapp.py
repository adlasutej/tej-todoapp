from flask import Flask
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.secret_key="Sairam@123"
from views import *
 
if __name__ == '__main__':
	app.run()
