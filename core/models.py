from django.db import models

# Create your models here.
class ContactForm(models.Model):
  first_name = models.CharField(max_length=300, default="")
  last_name = models.CharField(max_length=300, default="")
  email_Address = models.CharField(max_length=300, default="")
  message = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.title