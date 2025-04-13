# apps/tenants/management/commands/create_tenant.py
import psycopg2
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.tenants.models import Tenant

class Command(BaseCommand):
    help = 'Creates a new tenant with its own database'

    def add_arguments(self, parser):
        parser.add_argument('--name', required=True, help='Tenant name')
        parser.add_argument('--db_name', required=True, help='Database name')
        parser.add_argument('--domain', required=True, help='Tenant domain')

    def handle(self, *args, **options):
        name = options['name']
        db_name = options['db_name']
        domain = options['domain']
        
        # Create the tenant in the management database
        tenant = Tenant.objects.create(
            name=name,
            db_name=db_name,
            domain=domain
        )