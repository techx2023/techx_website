from django.db import models

# Create your models here.
class Services(models.Model):
    titre = models.CharField(max_length=255, verbose_name="Titre du service",blank=False,null=False)
    # description for card in home page
    intro = models.TextField(verbose_name="Introduction",null=False, blank=False)
    # description about service in the detail page
    description = models.TextField(verbose_name="Description du service", blank=False, null=False)
    # description for front and back about service for example (dev web and monile)
    front_descrption = models.TextField(verbose_name="Description Front-end", blank=True, null=True)
    back_descrption = models.TextField(verbose_name="Description Back-end", blank=True, null=True)
    # service icon for representation
    icon = models.ImageField(upload_to='Images/services',verbose_name="Icon du service", blank=False, null=False)
    # service image in detail page
    img_detail_page = models.ImageField(upload_to='Images/services',verbose_name="Image du service pour la page détail", blank=False, null=False)
    # service image in service page
    img_service_page = models.ImageField(upload_to='Images/services',verbose_name="Image du service pour la page service", blank=False, null=False)
    is_home = models.BooleanField(default=False)
    

class Contact(models.Model):
    fname = models.CharField(max_length=255, verbose_name="Nom complet",blank=False,null=False)
    email = models.EmailField(verbose_name="Email",null=False, blank=False)
    subject = models.CharField(max_length=255, verbose_name="Objet",blank=False,null=False)
    message = models.TextField(verbose_name="Message", blank=False, null=False)
    