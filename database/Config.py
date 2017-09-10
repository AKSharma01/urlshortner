from routes import app
from setting import ENVSetting
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = ENVSetting().createConnetionLink()
db = SQLAlchemy(app)

