from django.contrib.auth.management.commands.createsuperuser import Command as BaseCommand
from django.core.management import CommandError

class Command(BaseCommand):
    help = 'Create a superuser with first name, last name, and phone number'

    def handle(self, *args, **options):
        username = options.get('username', None)
        email = options.get('email', None)
        password = options.get('password', None)
        database = options.get('database')

        # Prompt for missing required fields
        if not username:
            username = self.get_input_data("Username", options.get('stdin'), self.style, default=None, strip=True)
            if not username:
                raise CommandError("Username not provided")
            options['username'] = username

        if not email:
            email = self.get_input_data("Email", options.get('stdin'), self.style, default=None, strip=True)
            if not email:
                raise CommandError("Email not provided")
            options['email'] = email

        if not password:
            password = self.get_input_data("Password", options.get('stdin'), self.style, default=None, strip=False)
            if not password:
                raise CommandError("Password not provided")
            options['password'] = password

        first_name = self.get_input_data("First name", options.get('stdin'), self.style, default=None, strip=True)
        options['first_name'] = first_name

        last_name = self.get_input_data("Last name", options.get('stdin'), self.style, default=None, strip=True)
        options['last_name'] = last_name

        phone = self.get_input_data("Phone number", options.get('stdin'), self.style, default=None, strip=True)
        options['phone'] = phone

        # Call create_superuser method of CustomUserManager
        self.UserModel._default_manager.db_manager(database).create_superuser(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone=phone
        )

    def get_input_data(self, prompt, stdin, style, default=None, strip=True):
        data = stdin.get(prompt, default=default)
        if strip:
            data = data.strip()
        return data
