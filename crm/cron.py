from datetime import datetime

def log_crm_heartbeat():
    with open('/tmp/crm_heartbeat_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now().strftime('%d/%m/%Y-%H:%M:%S')} CRM is alive\n")
    print("CRM heartbeat logged!")
