from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

def customer_profile(sender, instance, created,**kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        User.objects.create(
            user=instance,
            name=instance.username,
            email = instance.email,
        )
        print('Perfil Criado')

post_save.connect(customer_profile, sender=User)