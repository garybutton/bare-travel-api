from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


class StoryManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(draft=False)


class Story(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", verbose_name=_("Author"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = StoryManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('stories:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created', '-updated']


def story_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.title)
        new_slug = slug
        count = 0
        while Story.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
            count += 1
            new_slug = '{slug}-{count}'.format(slug=slug, count=count)
        instance.slug = new_slug

pre_save.connect(story_pre_save, sender=Story)
