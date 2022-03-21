import json
import csv
f = open('isha.csv','a',encoding='utf-8')
csvWriter = csv.writer(f)
headers=['full_text','retweet_count','user_followers_count','favorite_count','place','coordinates','geo','created_at','id_str']
csvWriter.writerow(headers)

for inputFile in ['tweet.txt']:#all the text-file names you want to convert to Csv in the sae folder as this code
    tweets = []
    for line in open('tweet.txt', 'r'):
      try:
        all_data=(json.loads(line))
        tweets.append(all_data)
      except:
        continue

    print('Tweets are',len(tweets))
    count_lines=0
    for tweet in tweets:
        try:
            csvWriter.writerow([tweet['text'],tweet['retweet_count'],tweet['user']['followers_count'],tweet['favorite_count'],tweet['place'],tweet['coordinates'],tweet['geo'],tweet['created_at'],str(tweet['id_str'])])
            count_lines+=1
        except Exception as e:
            print(e)
    print(count_lines)