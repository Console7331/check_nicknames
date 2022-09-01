from color import color
from sources.services import linktree
from sources.services import vk
from sources.services import telegram
from sources.services import twitter
from sources.services import instagram

def check_services(nickname, RU):
    print (color('cyan')+'-------------------------------------------------'+color('end'))	
    print (color('magenta')+'             EXISTENCE SERVICES CHECKER'+color('end'))
    print (color('cyan')+'-------------------------------------------------'+color('end'))
    print ('Check nickname: ', color('yellow')+nickname+color('end'))
    
    service_list = []

    if RU == 'no':
        instagram.instagram_check(nickname, service_list)
    linktree.linktree_check(nickname, service_list)
    telegram.telegram_check(nickname, service_list)
    twitter.twitter_check(nickname, service_list)
    vk.vk_check(nickname, service_list)

    print (color('cyan')+'-------------------------------------------------'+color('end'))

    outputfile = open('output.txt', 'a') 
    outputfile.write('All avaliable services:')
    outputfile.writelines(str(service_list)+'\n')
    outputfile.close()