#!/bin/bash

# Activate the virtual environment
source /home/shad/Projects/alx-backend-graphql_crm/.venv/bin/activate

# Run the Django shell command to delete inactive customers
/home/shad/Projects/alx-backend-graphql_crm/.venv/bin/python manage.py shell <<EOF
from datetime import datetime, timedelta
from crm.models import Customer

a_year_ago = datetime.now() - timedelta(days=365)
deleted_count, _ = Customer.objects.filter(orders__isnull=True, created_at__lt=a_year_ago).delete()

with open('/tmp/customer_cleanup_log.txt', 'a') as log_file:
    log_file.write(f"{datetime.now()} - Deleted {deleted_count} inactive customers\n")
EOF
