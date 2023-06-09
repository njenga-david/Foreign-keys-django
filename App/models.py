from django.db import models

# Create table with fk
class Career(models.Model):
    career=models.CharField(max_length=100)
    def __str__(self):
        return self.career
    

#table cadidate


GENDER=(('M','M'),
        ('F','F'),
        )

class Candidate(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    gender=models.CharField(max_length=1,null=True,choices=GENDER)
    career=models.ForeignKey(Career,on_delete=models.CASCADE)

    