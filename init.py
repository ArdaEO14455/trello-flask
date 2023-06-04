from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

#Create instances of functionalities
db = SQLAlchemy() #instance of SQL Alchemy to communicate with the database and provide commands from python
ma = Marshmallow() #instance of Marshmallow, used to create schemas
bcrypt = Bcrypt() #instance of bcrypt, used to encrypt and decrypt passwords
jwt = JWTManager() #instance of the JWT (token) manager app
