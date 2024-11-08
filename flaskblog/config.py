import os


class Config:
    SECRET_KEY = os.environ.get('FLASK_BLOG_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('FLASK_BLOG_SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'      #Name/IP address of email server
    MAIL_PORT = 587                     #Port number of server used
    MAIL_USE_TLS = True                 #Enable/Disable Transport Security Layer encryption
    MAIL_USERNAME = os.environ.get('FLASK_BLOG_EMAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('FLASK_BLOG_EMAIL_PASSWORD')