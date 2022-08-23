from color import color
from sources import linktree

def check_services(nickname):
    print (color('cyan')+'-------------------------------------------------'+color('end'))	
    print (color('magenta')+'             EXISTENCE NICKNAME CHECKER'+color('end'))
    print (color('cyan')+'-------------------------------------------------'+color('end'))
    print ('Check nickname: ', color('yellow')+nickname+color('end'))

    
    nickname_status = {'0': color('red')+'[-] Nickname is already use!'+color('end'), '1': color('green')+'[+] Nickname is available!  '+color('end')}
    
    service_list = []

    linktree.linktree_check(nickname, service_list)

    #Что-нибудь придумать с перезаписью файла
    """ outputfile = open('output.txt', 'w+') 
    outputfile.write('All avaliable nicknames:')
    outputfile.writelines(str(service_list)+'\n')
    outputfile.close() """