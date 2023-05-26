from django.db import models

class Profile(models.Model):   
    email = models.EmailField()
    isHidden = models.BooleanField(default=False)
    
class Connection(models.Model):
    id1 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="id1")
    id2 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="id2")