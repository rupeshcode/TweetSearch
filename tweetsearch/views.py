import pytz
import time
import json
import csv
from datetime import datetime

from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.settings import api_settings

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

from rest_framework_csv import renderers as r

from .models import Tweet
from .serializers import TweetListSerializer
from .filter import filter


#imporing twitter keys from settings
consumer_key = settings.CONSUMER_KEY
consumer_secret = settings.CONSUMER_SECRET
access_token = settings.ACCESS_TOKEN
access_token_secret = settings.ACCESS_TOKEN_SECRET

#Listener function
class Listener(StreamListener):

    def __init__(self, time_limit=30):
        self.start_time = time.time() #for stopping the api after time
        self.limit = time_limit
        super(Listener, self).__init__()

    def on_connect(self):
        print("Connection successfuly established to API.")

    def on_status(self, status):
        if (time.time() - self.time) >= self.limit:
            print('time is over')
            return False
    #perform operations on data returned
    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            try:
                datajson = json.loads(data)
                tz = pytz.timezone('Asia/Kolkata')
                user_id = datajson['user']['id']
                user_name = datajson['user']['name']
                user_screenname = datajson['user']['screen_name']
                user_location = datajson['user']['location']
                user_followers = datajson['user']['followers_count']
                user_friends = datajson['user']['friends_count']
                t_id = datajson['id']
                t_rtcount = datajson['retweet_count']
                t_favcount = datajson['favorite_count']
                t_mention = datajson['entities']['user_mentions']
                t_create = datetime.fromtimestamp((int(datajson['timestamp_ms'])/1000), tz)
                t_text = datajson['text']
                lang = datajson['lang']
                lang = datajson['lang']
                T1 = Tweet(user_id=user_id, user_name=user_name, user_screenname=user_screenname,
                            user_location=user_location, user_followers=user_followers, user_friends=user_friends,
                            t_id=t_id, t_rtcount=t_rtcount, t_favcount=t_favcount,
                            t_create=t_create, t_text=t_text, lang=lang)
                T1.save()
            except Exception as e:
        	       print(e)
            return(True)
        else:
            return False

    def on_error(self, status):
        print(status.text)

class StreamAPI(APIView):
    '''Api 1 to stream data and store in the database from
     Twitter using tweepy. The api accepts a keyword for streaming'''

    def get(self, request, keyword):
        try:
    	    print("Streaming keyword:-", keyword)
    	    auth = OAuthHandler(consumer_key, consumer_secret)
    	    auth.set_access_token(access_token, access_token_secret)
    	    st = Listener()
    	    stream = Stream(auth, st)
    	    stream.filter(track=[keyword])
    	    print("Streaming over")
    	    response = {
    			"status":"success",
    		}
    	    return JsonResponse(response)
        except:
            response = {
                "status":"failure",
                }
            return jsonify(response)

class TweetListAPIView(ListAPIView):
    '''Api 2 to search/filter/order data from the database and
    return to the user'''

    serializer_class = TweetListSerializer #defining serializer class
    filter_backends = [SearchFilter, OrderingFilter,]
    search_fields = ['user_name', 't_text'] #search fields for default search in query
    pagination_class = PageNumberPagination #pagination module

    def get_queryset(self, *args, **kwargs):
        queryset_list = filter(self) #calling filter module
        return queryset_list

class CSVTweetListAPIView(ListAPIView):
    '''API 3 to saves the data in form of an .csv file in the current directory
    according to the filters requested by the user'''

    serializer_class = TweetListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user_name', 't_text']
    renderer_classes = (r.CSVRenderer, ) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    
    def get_queryset(self, *args, **kwargs):
        queryset_list = filter(self)
        model = queryset_list.model
        writer = csv.writer(open('./tweets.csv', 'w+'))
        headers = []
        for field in model._meta.fields:
            headers.append(field.name)
        writer.writerow(headers)
        qs=queryset_list
        for obj in qs:
            row = []
            for field in headers:
                val = getattr(obj, field)
                if callable(val):
                    val = val()
                if type(val) == str:
                    val = val.encode("utf-8")
                row.append(val)
            writer.writerow(row)

        return queryset_list
