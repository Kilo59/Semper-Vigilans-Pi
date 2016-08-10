import twitter
import speedtest_cli
import time
import datetime
import imaplib
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Google credentials
#JSON filename here
JSONfilename = ''

#Twitter credentials
api1 = twitter.Api(  consumer_key='',\
                    consumer_secret='',\
                    access_token_key='',\
                    access_token_secret='')



def current_hour():
    date = time.localtime(time.time())
    now = datetime.datetime.now()
    hour = '%d' % now.hour
    currentHour = str(hour)

    return currentHour

###Get GoogleApp credentials from JSON file in directory
scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name(JSONfilename, scope)

gc = gspread.authorize(credentials)
    #open spreadsheet by 'title'
g_sheet = gc.open("gspread_test")
    #select worksheet by title
config_ws = g_sheet.worksheet('config')
log_ws = g_sheet.worksheet('cloud_log')
#get cell value by label
#set up intitial loop length
loopLength = int(config_ws.acell('B6').value)
print('Intitial Test Freqeuncy: ' + str(loopLength) +' minutes')

#depreciated
"""
def email_start(Hour):

    Subject = str(Hour)
    message = ''

    M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    email = ''
    password = ''
    M.login(email, password)

    M.select()
    typ, data = M.search(None, 'SUBJECT', Subject)
    for num in data[0].split():
        typ, data = M.fetch(num, '(RFC822)')
        message = ('Message %s\n%s\n' % (num, data[0][1]))

    M.close()
    M.logout()

    if len(message) > 10:
        print('Message')
        start_test = True
    else:
        print('No Message')
        start_test = False
    return (start_test)
"""
def test_start(Hour):
    time1 = config_ws.acell('B2').value
    time2 = config_ws.acell('B3').value
    time3 = config_ws.acell('B4').value

    if time1 == Hour or time2 == Hour or time3 == Hour:
        start_boolean = True
    else:
        start_boolean = False
    return(start_boolean)

date = time.localtime(time.time())
now = datetime.datetime.now()
hour = '%d' % now.hour
minute = '%d' % now.minute
second = '%d' % now.second
currentTime = str(hour) +':'+ str(minute) +':'+ str(second)

##file is named Month_Day_2digitYear
fileName = '%d_%d_%d.txt'%(date[1], date[2], (date[0]%100))

f = open(fileName, 'a')         #opens log file in "append" mode
f.write('Initialize' + ' @ ' + currentTime + '\n')
f.close()

print('***')
time.sleep(3)

#loops decrement after each loop, stop at 0
loops = 20
print('**Loop '+str(loops)+' times**' )
loopNum = 1
log_cell_row = 2
while loops > 0:

    cHour = current_hour()
    #cHour = 2 #Debug
    #start_wait = email_start(cHour)
    start_wait = test_start(cHour)

    if start_wait == True:
        speedtest_cli.main()
    else:
        print('Check again soon...')
    print('**')
    time.sleep(2)

    # reads the txt file network_speed and passes into string ns_String
    r = open('network_speed.txt', 'r')
    ns_String = (r.read())
    # print(ns_String)
    r.close()

    #check config_ws for tweet settings
    mention = ''
    if config_ws.acell('B8').value == ('yes'):
        tweet_boolean = True
    else:
        tweet_boolean = False
    #check for @mention
    mention = config_ws.acell('B5').value
    #get outgoing message
    outgoing = config_ws.acell('B7').value
    #check for loop length setting
    loopLength = int(config_ws.acell('B6').value)
    print('***Loop interval:'+str(loopLength)+' minute(s)***')
    #prepare for google log spreadsheet update
    log_cell_row = 1 + loopNum
    print('LogRow:'+str(log_cell_row))
    log_ws.update_cell(log_cell_row, 1, ns_String)

    if start_wait == True and tweet_boolean:
        # Basic Tweet
        status = api1.PostUpdate(mention +' '+ ns_String)
        print('*Tweet Tweet*')
        time.sleep(2)
        status_message = api1.PostUpdate(mention +' '+outgoing)
        print('**Tweet Finished**')

    print(loopNum)
    loopNum += + 1
    print(loopNum)
    time.sleep(15 * loopLength)
    print('***/2***')
    time.sleep(15 * loopLength)
    print('***LOOP'+str(loopNum)+'***')
    #Debug
    loops = loops - 1
