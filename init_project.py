import random

SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
STEAM_KEY = raw_input("We need a steam dev key (https://steamcommunity.com/dev/apikey): ")
ADMIN_PASS = raw_input("And a password for 'admin' user: ")

secret = open('.env', 'w')
secret.write('SECRET_KEY=' + SECRET_KEY)
secret.write('\nSTEAM_KEY=' + STEAM_KEY)
secret.write('\nADMIN_PASS=' + ADMIN_PASS)
secret.close()
