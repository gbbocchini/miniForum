from django.db import models
from django.urls import reverse
from django.conf import settings
from discussoes.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete='PROTECT')
    created_at = models.DateTimeField(auto_now=True)
    texto = models.TextField()
    message_html = models.TextField(editable=False)
    bate_boca = models.ForeignKey(Group, related_name='posts', null=True, blank=True,on_delete='PROTECT')

    def save(self, *args, **kwargs):
        self.message_html = self.texto
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username':self.user.username, 'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ('user', 'texto')

    def __str__(self):
        return self.texto







