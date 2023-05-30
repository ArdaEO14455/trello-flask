from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spammeggs123@localhost:5432/trello'

db = SQLAlchemy(app)
# print (db.__dict__)

class Card(db.Model):
    __tablename__ = 'cards'
    
    id = db.Column(db.Integer, primary_key=True) #This specifies the primary key
    title = db.Column(db.String(100)) #the value next to string indicates max characters, if not specified, it will be 255. no need to specify no null, sqlalchemy will take care of that
    description = db.Column(db.Text()) #text has no limit of characters
    date = db.Column(db.Date)


@app.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all() #if a table that is already created is called to be created again, it will be ignored. its like an 'if not exists' statement.
    print('Tables created successfully')

@app.cli.command('seed')
def seed_db():
    card = Card(
        title = 'Start the Project',
        description = 'Stage 1 - Create an ERD',
        date = date.today()
    )

    #Truncate the Card Table
    db.session.query(Card).delete()
    #add the card to the session (transaction)
    db.session.add(card) #the 'session' acts like version control, whereby the entire block of code its embedded in needs to be successfully executed. if it partially works but something goes wrong, it rolls back.

    #Commit the transaction to the database
    db.session.commit() #This line then commits the transaction 
    print('Models Seeded')


@app.route('/')
def index():
    return 'hello world!'

if __name__ == '__main__':
    app.run(debug=True)