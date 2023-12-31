from django.core.management import BaseCommand

from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = "admin"
            email = "admin@gmail.com"
            password = "admin"
            print("Creating account for %s (%s)" % (username, email))
            admin = User.objects.create_superuser(
                username=username, email=email, password=password
            )
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print("Admin accounts can only be initialized if no Accounts exist")
