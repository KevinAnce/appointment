from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = "Create a new superuser with additional fields"

    def handle(self, *args, **options):
        # Prompt the user for basic details (username, email, password)
        username = input("Username: ")
        email = input("Email: ")

        # Ensure the username is unique
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR(f"Username '{username}' already exists."))
            return

        # Prompt for the password and validate it
        password = self.get_password()

        # Request additional information
        first_name = input("First name: ")
        last_name = input("Last name: ")

        # Create the user
        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=make_password(password),  # Hash the password
        )

        # Output a success message
        self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully"))

    def get_password(self):
        """
        Helper method to ask the user to enter the password and validate it.
        """
        while True:
            password = input("Password: ")
            password_confirmation = input("Confirm password: ")

            if password != password_confirmation:
                self.stdout.write(self.style.ERROR("Passwords do not match. Please try again."))
            elif len(password) < 8:
                self.stdout.write(self.style.ERROR("Password is too short. It must be at least 8 characters."))
            else:
                return password
