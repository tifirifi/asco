from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


class Ticket(models.Model):
    PRIORITY_NAMES = (
        ('low', _('Low')),
        ('medium', _('Medium')),
        ('high', _('High')),
    )

    user = models.ForeignKey('auth.User')
    title = models.CharField(
        max_length=200,
        verbose_name=_('Title'),
    )
    description = models.TextField(null=True, verbose_name=_('Description'))
    code = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name=_('Ticket_ID'),
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name=_('Created date')
    )
    category = models.ForeignKey('Category')
    priority = models.CharField(
        max_length=40,
        choices=PRIORITY_NAMES,
        verbose_name=_('Priority'),
    )
    status = models.ForeignKey('Status')

    def save(self, *args, **kwargs):
        if not self.code:
            super().save(*args, **kwargs)
            self.code = '{}/{}'.format(self.category, self.pk)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ticket_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['-created_date']


class Category(models.Model):
    name = models.CharField(
        null=True,
        max_length=100,
        verbose_name=_('Category'),
    )

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(null=True, max_length=100,
                            verbose_name=_('Status'))

    def __str__(self):
        return self.name