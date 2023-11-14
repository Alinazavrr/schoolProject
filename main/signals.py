from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FavoritesDiets

# @receiver(post_save, sender=FavoritesDiets)
# def add_favorites_user(sender, **kwargs):
#     user = kwargs['instance']
#
