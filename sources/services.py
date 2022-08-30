from color import color
from services import linktree
from services import vk
from services import telegram
from services import twitter

def check_services(nickname):
    print (color('cyan')+'-------------------------------------------------'+color('end'))	
    print (color('magenta')+'             EXISTENCE SERVICES CHECKER'+color('end'))
    print (color('cyan')+'-------------------------------------------------'+color('end'))
    print ('Check nickname: ', color('yellow')+nickname+color('end'))
    
    service_list = []

    linktree.linktree_check(nickname, service_list)
    vk.vk_check(nickname, service_list)
    telegram.telegram_check(nickname, service_list)
    twitter.twitter_check(nickname, service_list)

    print (color('cyan')+'-------------------------------------------------'+color('end'))

    outputfile = open('output.txt', 'a') 
    outputfile.write('All avaliable services:')
    outputfile.writelines(str(service_list)+'\n')
    outputfile.close()