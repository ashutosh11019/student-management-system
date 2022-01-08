from django.db import models



# Create your models here.
class myform(models.Model):
    std_chioces={
        ('i','i'),
        ('ii','ii'),
        ('iii','iii'),
        ('iv','iv'),
        ('v','v'),
        ('vi','vi'),
        ('vii','vii'),
        ('viii','viii'),
        ('ix','ix'),
        ('x','x'),
    }

    c_choice={
        ('Bus','Bus'),
        ('Liberary','Liberary'),
        ('Both','Both'),
        ('None','None'),
    }

    name=models.CharField( max_length=50,null=True)
    
    Roll=models.CharField( max_length=50,null=True)
    Age=models.CharField( max_length=50,null=True )
    Std=models.CharField( max_length=50,choices=std_chioces,null=True)
    Convience=models.CharField( max_length=50,choices=c_choice,null=True)
    profile_pic=models.ImageField(upload_to="images")
   
    def __str__(self):
        return self.name



