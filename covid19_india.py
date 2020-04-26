#this is done for constructive purpose through BeautifulSoup.I respect the nation and the Ministry of health and family affairs 
def Carona(para):
    if para == 'active':
        x = 'blue'
    elif para == 'deaths':
        x = 'red'
    elif para == 'recovery':
        x = 'green'
    elif para == 'migrated':
        x == 'orange'    


    mhaw = requests.get('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(mhaw.content, 'html.parser')
    status = soup.select('.bg-'+x)
    actstr = str(status[0])
    # print(actstr)
    splv2 = actstr.split('strong>')
    # print(splv2)
    sth = splv2[1]
    num = sth[:-2]
    print(num)
Carona('deaths')   #sample for deaths (can also be 'active', 'recovery', 'migrated')
