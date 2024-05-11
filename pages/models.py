from django.db import models


class Services(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.FileField(upload_to="images", default="default.jpeg")
    image2 = models.FileField(upload_to="images", default="default.jpeg")

    def __str__(self):
        if len(self.description) > 100:
            return self.description[:100] + "..."
        else:
            return self.description


class Post(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="images", default="default.jpeg")
    dateUpload = models.DateTimeField(auto_now=True)

    def __str__(self):

        if len(self.description) > 100:
            return self.description[:100] + "..."
        else:
            return self.description


class MetaData(models.Model):
    phoneNumber = models.CharField(max_length=13)
    name = models.CharField(max_length=200)
    timeActiveNormalDays = models.CharField(max_length=100)
    timeActiveWeekends = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="images", default="logo.png")
    linkedln = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    officeLocation = models.CharField(max_length=400)
    email = models.CharField(max_length=300)


class Project(models.Model):
    name = models.CharField(max_length=250)
    completeStatus = models.BooleanField()
    image = models.ImageField(upload_to="images", default="default.jpeg")
    description = models.TextField()
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.name
