from bs4 import BeautifulSoup
import HTMLParser
import requests
import time
import re
import urllib2
import socket

Mylist = list()
mail_list = list()


def ConnectOk(url):
    try:
        urllib2.urlopen(url,timeout=5)
    
    except urllib2.HTTPError, e:
        return False

    except urllib2.URLError, e: 
        return False

    except socket.error, e:
        return False
    
    except socket.timeout, e:
        return False
 
    except ssl.timeout, e:
        return False

    except ssl.SSLError, e:
        return False
    
           

    return True


def Climb(url):
    round_number = 1
    count = 0  
    Mylist.append(url)
  

    while len(Mylist)>0:

        print('The time: %s' %round_number)
        print("This is your input url: "+ Mylist[0])

        if ConnectOk(Mylist[0]):
            
            page = urllib2.urlopen(Mylist[0],timeout=10) 
            
            soup = BeautifulSoup(page,'lxml') #watch the url content
            email = re.findall(r'[A-Za-z0-9_\-\.]+\@[A-Za-z0-9_\-\.]+\.[A-Za-z]{2,4}', soup.prettify())
            #find all e-mail of the page

            #count = 0 
            for i in email:
                if i[-3:] != 'jpg' and i[-3:] != 'png' and i[-3:] != 'JPG' and i[-3:0] != 'PNG':
                    mail_list.append(i)
                    count+=1
    
            for i in mail_list:
                print(i)
            

            print count   # email number
   
            round_number+=1
            print("YYYYYYYYYYYYYYYYYYYYYYY")
            Mylist.pop(0) # pop the end url
       
           # catch = 0  # how many 'tag a'
           #     catch+=1
           # print(catch)
           #     print(i)
                
               # print("**************")
           # for i in range(0, catch-1, +1):
           
           # link = [tag['href'] for tag in soup.findAll('a',{'href':True})][37]
            for i in soup.findAll('a', href=True): 
                link = i.get('href') 

                if link[0:4] == 'http':
                    if link[-3:] != 'pdf' and link[-3:] != 'ppt' and link[-3:] != 'doc' and link[-3:] != 'mp3' and link[-3:] != 'mp4' and link[-3:] != 'zip' and link[-3:] != 'rar' and link[-3:] != 'jpg' and link[-3:] != 'png' and link[-3:] != 'gif' and link[-4:] != 'pptx' and link[-4:] != 'docx':
                        Mylist.append(link)
                        # print("**************")

            print(len(Mylist))

        else:
            round_number+=1
            print("NNNNNNNNNNNNNNNNNNNNNNNNNN")
            Mylist.pop(0)
            print(len(Mylist))
 
           
        


if __name__ == '__main__':
    while True:
        where = raw_input('input your url: ')
        if where[-3:] != 'pdf' and where[-3:] != 'ppt' and where[-3:] != 'doc' and where[-3:] != 'mp3' and where[-3:] != 'mp4' and where[-3:] != 'zip' and where[-3:] != 'rar' and where[-3:] != 'jpg' and where[-3:] != 'png' and where[-3:] != 'gif' and where[-4:] != 'pptx' and where[-4:] != 'docx':
 
            Climb(where)
            break

        else:
            continue   
        
    

    
