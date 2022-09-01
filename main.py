from sources import emails_check
from sources import services_check
import os
import find_country

def main():
    os.system('cls' if os.name=='nt' else 'clear')
    nickname = input("Please, type your nickname here: ")

    if nickname is None:
            print ("Please type your nickname")
            os._exit(0)

    f = open('output.txt', 'w').close()

    find_country.country()
    if find_country.country == 'RU':
        RU = 'yes'
    else: 
        RU = 'no'
    
    email_check = input("Do you wanna check emails? y/n: ")
    if (email_check == 'y'):
        emails_check.check_emails(nickname)

    service_check = input("Do you wanna check services? y/n: ")
    if (service_check == 'y'):
        services_check.check_services(nickname, RU)

    if (service_check == 'y') or (email_check == 'y'):
        print("Check output.txt file, there is list of all available emails and services")

print(__name__)
if __name__ == "__main__":
	main()