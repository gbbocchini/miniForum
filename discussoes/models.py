from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse

User = get_user_model()

register = template.Library()

class Group(models.Model):
    nome = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    descritivo = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    class Meta:
        ordering = ['nome']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        self.description_html = self.descritivo
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('discussoes:single', kwargs={'slug':self.slug})


    def __str__(self):
        return self.nome


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete='PROTECT')
    user = models.ForeignKey(User, related_name='user_groups', on_delete='PROTECT')

    class Meta:
        unique_together = ('group', 'user')

    def __str__(self):
        return self.user.username
