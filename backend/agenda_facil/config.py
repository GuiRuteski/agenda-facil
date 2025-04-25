import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usuario:senha@localhost/agenda_facil'
    SQLALCHEMY_TRACK_MODIFICATIONS = False