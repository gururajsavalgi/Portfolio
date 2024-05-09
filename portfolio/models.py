from django.db import models

# Create your models here.
class Index(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    about1=models.TextField(default="")
    about=models.TextField(default="")
    link1 = models.CharField(max_length=100)
    link2 = models.URLField(blank=True, null=True)
    link3 = models.URLField(blank=True, null=True)
    link4 = models.URLField(blank=True, null=True)
    resume = models.FileField(upload_to='media/pdf/', blank=True, null=True)
    image=models.ImageField(upload_to="img/", default="")
    
    def __str__(self):
        return self.name
    
class Projects(models.Model):
    msg_id=models.AutoField(primary_key=True)
    link1 = models.URLField(blank=True, null=True,default='#')
    link2 = models.URLField(blank=True, null=True,default='#')
    name=models.CharField(max_length=50,default=None)
    about=models.TextField(default="")


class Skills(models.Model):
    msg_id=models.AutoField(primary_key=True)
    icon=models.CharField(max_length=100,default=None)
    color=models.CharField(max_length=100,default=None)
    name=models.CharField(max_length=100,default=None)
    percentage=models.IntegerField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    gmail=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    number=models.IntegerField()

    def __str__(self):
        return self.gmail
class People(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.TextField(default="")
    description=models.TextField(default="")
    def __str__(self):
        return self.name