import os

os.system('cls' if os.name=='nt' else 'clear')
nickname = input("Please, type your nickname here: ")

if nickname is None:
		print ("Please type your nickname")
		os._exit(0)

f = open('output.txt', 'w').close()

email_check = input("Do you wanna check emails? y/n: ")
if (email_check == 'y'):
    from sources import emails
    emails.check_emails(nickname)

services_check = input("Do you wanna check services? y/n: ")
if (services_check == 'y'):
    from sources import services
    services.check_services(nickname)

if (services_check == 'y') or (email_check == 'y'):
    print("Check output.txt file, there is list of all available emails and services")