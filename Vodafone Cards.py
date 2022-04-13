import requests,json,random,string,pyfiglet,time,datetime,webbrowser as e
from bs4 import BeautifulSoup
print ('\033[;095mWelcome')
print ()
e.open('https://t.me/Techno0099')
time.sleep(2)
print ('\033[;092mclick on this link to get password👇')
print ()
time.sleep (1)
print ('\033[;093mhttps://miklpro.com/hRdtC')
print ()

m=input ('\033[;092m》Enter Password Script  :  ')

'''# import module
import requests
from bs4 import BeautifulSoup
  
# link for extract html data
def getdata(url):
    r = requests.get(url)
    return r.text
  
htmldata = getdata("https://pastelink.net/w2rq0jtw")
soup = BeautifulSoup(htmldata, 'html.parser')
data = m
for data in soup.find_all('<div id="bod'):
#    print(data.get_text())
    if m in data:'''
if m=='Abdullah8010':
    time.sleep (1)
    print ()
    print ('\033[;096m《True password》')
else :
    print ('\033[;091mError Password Try again')
    exit()
time.sleep (1)
h=pyfiglet.figlet_format ('VODAFONE \n         CARDS')
print ('\033[;096m'+h)
import os, time, pyfiglet,sys
c=('\033[;092m××××××××××××××××××××××××××××××××××××')
for I in c+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.030)
print ()
d =('\033[;092m#####Welcome To AbdullahScript#####')
for I in d +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.030)
print ()
p=('\033[;092m##### Script Creating Vodafone Cards##')
for I in p+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.030)
print ()
u=('\033[;092m### Projected By Abdullah Salah###')
for I in u+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.030)
print ()
print ()

print ()
i='''\033[;092m Telegram channel : 

  ◇ http://t.me/Techno0099
       

Youttube channel  : 

 ◇ https://youtube.com/channel/UCAbtkFAe9yyX0HJNFXyKJUg '''
for I in i +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.030)
print ()
time.sleep (1)
print ()
number = input("\033[;092m》》Enter Your Number : ")
print ()
pwd = input("》Enter password Ana Vodafone : ")
print ()

while True :
    with requests.Session() as req:
        def generationLink(stringLingth):
            latters = string.ascii_lowercase
            return ''.join(random.choice(latters) for i in range(stringLingth))  
        url = f'https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/auth?client_id=website&redirect_uri=https%3A%2F%2Fweb.vodafone.com.eg%2Far%2FKClogin&state=286d1217-db14-4846-86c1-9539beea01ed&response_mode=query&response_type=code&scope=openid&nonce={generationLink(10)}&kc_locale=en'
        responsePageLogin = req.get(url)
        soup = BeautifulSoup(responsePageLogin.content, 'html.parser')
        getUrlAction = soup.find('form').get('action')
        headerRequest = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'web.vodafone.com.eg',
    'Origin': 'https://web.vodafone.com.eg',
    'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
        formData = {
        'username':number,
        'password':pwd
    }
        sendUserData = req.post(getUrlAction,headers=headerRequest,data=formData)
        checkRegistry = sendUserData.url
        _checkRegistry = checkRegistry.find('KClogin')
        if _checkRegistry != -1:
            code = checkRegistry
            _code = code[code.index('code=') + 5:]
            header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-type': 'application/x-www-form-urlencoded',
        'Host': 'web.vodafone.com.eg',
        'Origin': 'https://web.vodafone.com.eg',
        'Referer': 'https://web.vodafone.com.eg/ar/KClogin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }  
            formDataAccessToken = {
        'code': _code,
        'grant_type': 'authorization_code',
        'client_id': 'website',
        'redirect_uri': 'https://web.vodafone.com.eg/ar/KClogin'
        }  
            sendDataAccessToken = req.post('https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token',headers=header,        data=formDataAccessToken)
            access_token = sendDataAccessToken.                    json()['access_token']
    url7=f"https://web.vodafone.com.eg/services/dxl/ramadanpromo/promotion?@type=RamadanHub&channel=website&msisdn={number}"
    head6={'Host': 'web.vodafone.com.eg',
'Connection': 'keep-alive',
'msisdn': number,
'api-host': 'PromotionHost',
'Accept-Language': 'AR',
'Authorization': f'Bearer {access_token}',
'Content-Type': 'application/json',
'x-dtreferer': 'https://web.vodafone.com.eg/spa/portal/hub?error=login_required&state=0650be48-8504-42fe-a750-5ee60013b9bf',
'Accept': 'application/json',
'clientId': 'WebsiteConsumer',
'User-Agent': 'Mozilla/5.0 (Linux; Android 9; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.94 Mobile Safari/537.36',
'channel': 'WEB',
'Referer': 'https://web.vodafone.com.eg/spa/portal/hub',
'Accept-Encoding': 'gzip, deflate, br'}

    r6=requests.get(url7,headers=head6).json()
    m = (r6[1])
    f = 0
    for i in range(int(49)):
    	f += 1
    	ss = (m["pattern"][f]["action"])
    	mm = (ss[0])
    	price = (mm["characteristics"][1]["value"])
    	units= (mm["characteristics"][2]["value"])
    	card= (mm["characteristics"][3]["value"])
    	users = (mm["characteristics"][0]["value"])
    	now = datetime.datetime.now()
    	tim = (now.strftime("%I:%M:%S"))
    	hgt = (card[0:3])
    	k='#'
    	if price == "10":
    	    print (' ')
    	elif hgt == "010":
    	    print(" ")
    	elif hgt == "011":
    	    print (' ')
    	else:
    	    msg = (f'\033[;096m*858*\033[;096m{card}#\n\033[;093m{price}UNIT\n\033[;092m{units}USER')
    	    time.sleep(1)
    	    print (msg)
    	    time.sleep (1)
