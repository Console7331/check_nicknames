from color import color
from sources import linktree
from sources import vk
from sources import telegram

def check_services(nickname):
    print (color('cyan')+'-------------------------------------------------'+color('end'))	
    print (color('magenta')+'             EXISTENCE SERVICES CHECKER'+color('end'))
    print (color('cyan')+'-------------------------------------------------'+color('end'))
    print ('Check nickname: ', color('yellow')+nickname+color('end'))
    
    service_list = []

    print (color('cyan')+'------------------LINKTR.EE---------------------'+color('end'))
    linktree.linktree_check(nickname, service_list)

    print (color('cyan')+'------------------VK.COM---------------------'+color('end'))
    vk.vk_check(nickname, service_list)

    print (color('cyan')+'------------------TELEGRAM---------------------'+color('end'))
    telegram.telegram_check(nickname, service_list)

    print (color('cyan')+'-------------------------------------------------'+color('end'))

    outputfile = open('output.txt', 'a') 
    outputfile.write('All avaliable services:')
    outputfile.writelines(str(service_list)+'\n')
    outputfile.close()