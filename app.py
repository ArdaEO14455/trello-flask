from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spammeggs123@localhost:5432/trello'

db = SQLAlchemy(app)
# print (db.__dict__)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True) #This specifies the primary key
    title = db.Column(db.String(100)) #the value next to string indicates max characters, if not specified, it will be 255. no need to specify no null, sqlalchemy will take care of that
    description = db.Column(db.Text()) #text has no limit of characters
    date = db.Column(db.Date)


@app.cli.command('create')
def create_db():
    db.create_all()
    print('Tables created successfully')

@app.route('/')
def index():
    return 'hello world!'

if __name__ == '__main__':
    app.run(debug=True)