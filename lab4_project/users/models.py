from django.db import models

class Client(models.Model):
    name = models.CharField( 'Имя', max_length=255)
    email = models.EmailField('Электронная почта',unique=True)
    password = models.CharField('Пароль',max_length=255)
    about = models.TextField('Обо мне',blank=True, null=True)

    def __str__(self):
        return self.email