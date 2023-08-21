from django.db import models
from apps.user.models import User


# Create your models here.
class Groups(models.Model):
    name = models.CharField(max_length=100)
    members_count = models.IntegerField(default=0)
    date_created =  models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='creator_groups', 
        default=None
    )
    members = models.ManyToManyField(User, related_name='groups_member', blank=True)
    admins = models.ManyToManyField(User, related_name='groups_admin', blank=True)
    description = models.TextField(default='')

    class Meta:
        db_table = 'groups'
        ordering = ['-date_created']
        
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # self.members_count = len(self.members)
        super(Groups, self).save(*args, **kwargs)