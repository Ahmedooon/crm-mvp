import os
from django.core.management import call_command

if os.environ.get("RUN_MANAGEMENT_COMMANDS") == "true":
    try:
        call_command("migrate")
        call_command(
            "createsuperuser",
            interactive=False,
            username=os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin"),
            email=os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com"),
        )
    except Exception as e:
        print(f"Setup error: {e}")
