from django.db import models
import json

class Profile():   
    def __init__(self, email, isHidden = False):
        self.email = email
        self.isHidden = isHidden
    

class Connection():
    
    def __init__(self, email_1, email_2):
        self.email_1 = email_1
        self.email_2 = email_2