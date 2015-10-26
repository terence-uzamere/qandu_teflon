from django.db import models
VISIBILITY_CHOICES = (
(0, 'Mr.'),
(1, 'Mrs.'),
(2, 'Ms.'),
(3, 'Dr.'),

)

# Create your models here.
class ContactForm(models.Model):
  title = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)
  first_name = models.CharField(max_length=300, default="")
  last_name = models.CharField(max_length=300, default="")
  email_Address = models.CharField(max_length=300, default="")
  message = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)


  def __unicode__(self):
    return self.title
