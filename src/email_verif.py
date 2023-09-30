import dns.resolver
import socket
import smtplib
import logging
from time import sleep, time

from numpy import random
from song_lists import email_verification, email_public

# Initialize a logger
logger = logging.getLogger("email_verification")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("email_verification.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

valid_email = []
invalid_email = []

data_into_list = email_public


def email_check():
    start_time = time()  # Record the start time
    total_emails = len(data_into_list)

    for idx, email_address in enumerate(data_into_list, start=1):
        # Calculate the estimated time remaining
        elapsed_time = time() - start_time
        estimated_remaining_time = (
            ((elapsed_time / idx) * (total_emails - idx)) if idx > 0 else 0
        )
        print(
            f"Processed {idx}/{total_emails} emails. Estimated time remaining: {estimated_remaining_time:.2f} seconds"
        )

        # Step 2: Getting MX record
        # Pull domain name from email address
        domain_name = email_address.split("@")[1]

        try:
            # Get the MX record for the domain
            records = dns.resolver.resolve(domain_name, "MX")
            mxRecord = records[0].exchange
            mxRecord = str(mxRecord)
        except dns.resolver.NXDOMAIN:
            logger.warning(f"Domain not found for email: {email_address}")
            email_verification.append("invalid")
            continue
        except dns.resolver.NoAnswer:
            logger.warning(f"No MX record found for domain: {domain_name}")
            email_verification.append("invalid")
            continue
        except Exception as e:
            logger.error(f"Error resolving MX record: {str(e)}")
            email_verification.append("invalid")
            continue

        # Step 3: Ping email server
        try:
            # Get local server hostname
            host = socket.gethostname()

            # SMTP lib setup (use debug level for full output)
            server = smtplib.SMTP()
            server.set_debuglevel(0)

            # SMTP Conversation
            server.connect(mxRecord)
            server.helo(host)
            server.mail(
                "your_email@your_domain.com"
            )  # Replace with a valid email from your domain
            code, message = server.rcpt(str(email_address))
            server.quit()

            # Assume 250 as Success
            if code == 250:
                valid_email.append(email_address)
                logger.info(f"Valid email: {email_address}")
                email_verification.append("valid")
            else:
                invalid_email.append(email_address)
                logger.warning(f"Invalid email: {email_address}")
                email_verification.append("invalid")

            # Add sleep time for smoother operation
            sleeptime = random.uniform(0.01, 0.2)
            sleep(sleeptime)

        except smtplib.SMTPConnectError as e:
            logger.error(f"SMTP Connection Error: {str(e)}")
            email_verification.append("invalid")
        except smtplib.SMTPServerDisconnected as e:
            logger.error(f"SMTP Server Disconnected: {str(e)}")
            email_verification.append("invalid")
        except Exception as e:
            logger.error(f"Error during SMTP verification: {str(e)}")
            email_verification.append("invalid")

    end_time = time()  # Record the end time
    elapsed_time = end_time - start_time
    print(f"Email verification completed in {elapsed_time:.2f} seconds.")
