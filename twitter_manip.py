
import json
import csv 
import sys
import numpy as np
#https://dzone.com/articles/python-reading-json-file

with open("ourtweets020816.json") as twt:
    j_tweets=[line.rstrip() for line in twt]

#json.loads(j_tweets[0]) works
#tweets=json.loads(j_tweets[0])

#tweets=[json.loads() for i in j_tweets]
tweets=[]
k=0
for i in j_tweets:
    try:
        k+=1
        d_tweets=json.loads(i)
        tweets.append(d_tweets)
    except ValueError:
        sys.stderr.write("%d: %s\n" % (k,i))

# gets tweets    
text=[x["text"] for x in tweets]

# gets user name of poster
usern=[x["user"]["screen_name"]for x in tweets] 


textfile=open('tweets020816.txt', 'w')
#spamwriter =textfile.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL) 


textfile.close()




# extracting mentions


mention=[x["entities"]["user_mentions"]for x in tweets] 
ument=[]
for i in mention:
    if len(i)>0:
        for k in range(0,len(i)):
            ument.append(i[k]["screen_name"])


all_users=usern
for i in ument:
    all_users.append(i)
# making a list with every user that tweeted or was mentioned
all_users=list(set(all_users))    
#Run this next part only if exporting tweets
'''
for i in range(0,len(text)):
    itext = text[i].replace('\n',' ')
    textfile.write(usern[i].encode("utf-8")+';'+itext.encode("utf-8")+"\n")
'''



