from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


class Ticket(models.Model):
    OPEN_STATUS = 1
    REOPENED_STATUS = 2
    RESOLVED_STATUS = 3
    CLOSED_STATUS = 4
    DUPLICATE_STATUS = 5

    STATUS_CHOICES = (
        (OPEN_STATUS, _('Open')),
        (REOPENED_STATUS, _('Reopened')),
        (RESOLVED_STATUS, _('Resolved')),
        (CLOSED_STATUS, _('Closed')),
        (DUPLICATE_STATUS, _('Duplicate')),
    )
    
    PRIORITY_NAMES = (
        (1, _('1. Critical')),
        (2, _('2. High')),
        (3, _('3. Normal')),
        (4, _('4. Low')),
        (5, _('5. Very Low')),
    )

    user = models.ForeignKey('auth.User')
    title = models.CharField(
        max_length=200,
        verbose_name=_('Title'),
    )
    description = models.TextField(
        null=True, 
        verbose_name=_('Description'))
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
    updated = models.DateTimeField(
        auto_now = True,
        auto_now_add = False,
        verbose_name=_('Updated')
    )
    category = models.ForeignKey('Category')
    priority = models.IntegerField(
        choices=PRIORITY_NAMES,
        default = 3,
        blank = 3,
        verbose_name=_('Priority'),
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default = OPEN_STATUS,
        verbose_name=_('Status')
    )
   
    def _get_priority_css_class(self):
        """
        Return the boostrap class corresponding to the priority.
        """
        if self.priority == 2:
            return "warning"
        elif self.priority == 1:
            return "danger"
        elif self.priority == 5:
            return "success"
        else:
            return "test"
    get_priority_css_class = property(_get_priority_css_class)
    
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


"""class Status(models.Model):
   name = models.CharField(null=True, max_length=100,
                            verbose_name=_('Status'))

    def __str__(self):
        return self.name"""
        