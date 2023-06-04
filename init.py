from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

#Create instances of functionalities
db = SQLAlchemy(app) #instance of SQL Alchemy to communicate with the database and provide commands from python
ma = Marshmallow(app) #instance of Marshmallow, used to create schemas
bcrypt = Bcrypt(app) #instance of bcrypt, used to encrypt and decrypt passwords
jwt = JWTManager(app) #instance of the JWT (token) manager app
