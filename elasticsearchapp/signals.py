from forum.models import Questions
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Questions)
def index_post(sender, instance, **kwargs):
    instance.indexing()