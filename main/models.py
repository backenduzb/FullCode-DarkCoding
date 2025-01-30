from django.db import models

class Post(models.Model):
    image=models.ImageField()
    date=models.DateField()
    text=models.TextField(default='Salom!')

    def __str__(self):
        return self.text

turlari=[
    ('Phishing', 'Phishing'),
    ('DOS', 'DOS'),
    ('DDOS', 'DDOS'),
    ('Malware', 'Malware'),
    ('SQL Injection', 'SQL Injection'),
]

tillar=[
    ('Python', 'Python'),
    ('Golang', 'Golang'),
    ('Java Script', 'Java Script'),
    ('Bat', 'Bat'),
]

nimagaligi=[
    ('Softwere', 'Softwere'),
    ('raspberry-pi', 'raspberry-pi'),
    ('Arduino', 'Arduino'),
    ('USB', 'USB'),
    ('Bluetooth', 'Bluetooth'),
]

class Content(models.Model):
    nomi=models.CharField(max_length=50,default="Nomi...",null=False,blank=False)
    nimaga=models.CharField(max_length=50,choices=nimagaligi,null=False,blank=False)
    tili=models.CharField(max_length=50,choices=tillar,null=False,blank=False)
    turlari=models.CharField(max_length=50,choices=turlari,null=False,blank=False)
    izoh=models.TextField(null=False,blank=False)
    kod=models.TextField(null=False,blank=False)
    
    def __str__(self):
        return f"{self.nomi}-{self.tili}"
 
