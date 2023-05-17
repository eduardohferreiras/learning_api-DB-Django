from django.db import models

class Profile():   
    def __init__(self, email, id, isHidden = False):
        self.id = id
        self.email = email
        self.isHidden = isHidden
    
class Connection():
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2