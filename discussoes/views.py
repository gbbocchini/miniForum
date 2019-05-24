from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from .models import Group, GroupMember
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db import IntegrityError


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('nome', 'descritivo')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group

class JoinGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request,('Você já está participando'))
        else:
            messages.success(self.request,('Você está nesse bate-boca!'))

        return super().get(request, *args, **kwargs)



class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = GroupMember.objects.filter(
                user = self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()
        except GroupMember.DoesNotExist:
            messages.warning(self.request, "Você não está batendo boca aqui (ainda)")
        else:
            membership.delete()
            messages.success(self.request, 'Você saiu deste bate boca')
        return super().get(request, *args, **kwargs)