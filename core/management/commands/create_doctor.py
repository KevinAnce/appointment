from django.core.management.base import BaseCommand
from core.models import Doctor


class Command(BaseCommand):
    help = "Create a new doctor"

    def add_arguments(self, parser):
        # Add options for name and email
        parser.add_argument('--name', type=str, help='Name of the doctor')
        parser.add_argument('--email', type=str, help='Email of the doctor')

    def handle(self, *args, **options):
        # If name and email are provided via options
        name = options['name']
        email = options['email']

        # If any option is missing, prompt the user for input
        if not name:
            name = input("Name of doctor: ")
        if not email:
            email = input("Email of doctor: ")

        # Create the doctor in the database
        Doctor.objects.create(name=name, email=email)

        # Output a success message
        self.stdout.write(self.style.SUCCESS(f"Doctor '{name}' created successfully"))
