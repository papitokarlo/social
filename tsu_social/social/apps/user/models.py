from django.db import models


class User(models.Model):
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)
    user_name = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user'

    def save(self, *args, **kwargs):
        self.user_name = f'{self.first_name} {self.last_name}'
        super(User, self).save(*args, **kwargs)