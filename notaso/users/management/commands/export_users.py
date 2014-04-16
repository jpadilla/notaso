from django.core.management.base import BaseCommand
from ...models import User


class Command(BaseCommand):
    help = 'Exports users to csv. (first_name, last_name, email)'

    def handle(self, *args, **options):
        users = User.objects.all().values(
            'first_name', 'last_name', 'email')
        for u in users:
            print unicode(u['first_name']).encode("UTF-8")
            +"," + unicode(u['last_name']).encode("UTF-8")
            +"," + unicode(u['email']).encode("UTF-8")
