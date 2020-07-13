"""
script create airflow user account / password
https://airflow.apache.org/docs/stable/security.html
"""

from argparse import ArgumentParser
import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

parser = ArgumentParser()
parser.add_argument("-u", dest="username")
parser.add_argument("-p", dest="password")
#parser.add_argument("-mail", dest="email")
args = parser.parse_args()

try:
    user = PasswordUser(models.User())
    print (">>> create user...")
    user.username = args.username
    user.email = 'dev@example.com'
    user.password = args.password
    session = settings.Session()
    session.add(user)
    session.commit()
    print (">>> create user OK")
except Exception as e:
    print (">>> create user failed : {}".format(e))
session.close()
exit()