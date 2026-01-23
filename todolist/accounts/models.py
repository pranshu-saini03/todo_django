from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Permission(models.Model):
    role = models.OneToOneField(Role, on_delete=models.CASCADE)

    can_create = models.BooleanField(default=False)
    can_read = models.BooleanField(default=False)
    can_update = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
