# TweetSearch

API has be created to Stream, Search, filter, Export Tweets by a twitter streaming API
It has been made to complete as assignment for Innovaccer Hacker Camp 2019.

The assignment is currently hosted at http://ruptweet.pythonanywhere.com

### Built With

1. Python3
2. Django 2.1
3. Django Rest Framework
4. Tweepy
5. MongoDb

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
* [Virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) - Setting up virtual environment
* [Pip](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/) - Installing Pip
* [Homebrew](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/) - Installing Homebrew
* [Python3](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/)
* MongoDb

### Setup project (Installation Instructions)
**Change the twitter stream Api credentials in settings.py file.**
* consumer_key
* consumer_secret
* access_token
* access_token_secret

Install the dependencies and devDependencies and start the server.

```sh
$ cd TweetBot
$ virtualenv -p python3.6 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
### 1. API1 to trigger Twitter Stream (/stream)
This API triggers twitter streaming and stores the data returned by Twitter Streaming API.
API 1 = `http://127.0.0.1:8000/stream/<keyword>/`

(methods supported - GET, POST)

Where keywords can be any keyword for which streaming needs to be performed.
Successful response
```
  {
  "status": "success",
  }
 ```
**Default time for streaming is 30 seconds. you can change the Stream time in views.py file**
### 2. API2 to filter/search stored tweets (/search)
This API fetches the data stored by the first api based on the filters and search keywords provided and sorts them as required.
## Operators

**Operators**: Following operators are available in order to filter, order, paginate the API.

| Ordering | operator | Description | Example |
| ------ | ------ | ------ | ------ |
| Ordering by field ascending | ordering  | Returns the tweets in ordered entered in query | http://127.0.0.1:8000/search/?ordering=id |
| Ordering by field descending | ordering  | Returns the tweets in ordered entered in query | http://127.0.0.1:8000/search/?ordering=-id |


**The fileds in ordering can be:
id, user_id, user_name, user_screenname, user_location, user_followers, user_friends,
t_id, t_rtcount, t_favcount, t_create, t_text, lang**


| Pagination | operator | Description | Example |
| ------ | ------ | ------ | ------ |
| Pagination | page | Returns the page no in query | http://127.0.0.1:8000/search/?page=2 |

**Returns page in api. By default there are 10 entries in every page.
can be change in settings file**


| Filter | operator | Description | Example |
| ------ | ------ | ------ | ------ |
| Search Text/Name/Sc_Name | q | Returns the tweets containing query in text/name/screen name | http://127.0.0.1:8000/search/?q=modi |
| Name | name | Returns tweets with name containing query | http://127.0.0.1:8000/search/?name=sethi |
|  | sw_name | Returns tweets with name starting with query | http://127.0.0.1:8000/search/?sw_name=sethi |
|  | ew_name | Returns tweets with name ending with query | http://127.0.0.1:8000/search/?ew_name=sethi |
|  | x_name | Returns tweets with exact name in query | http://127.0.0.1:8000/search/?x_name=sethi |
| Screen Name | name_sc | Returns tweets with screen name containing query | http://127.0.0.1:8000/search/?name_sc=sethi |
| | sw_name_sc | Returns tweets with screen name starting with query | http://127.0.0.1:8000/search/?sw_name_sc=sethi |
|  | ew_name_sc | Returns tweets with screen name ending with query | http://127.0.0.1:8000/search/?ew_name_sc=sethi |
|  | x_name_sc | Returns tweets with exact screen name in query | http://127.0.0.1:8000/search/?x_name_sc=sethi |
| Tweet text | text | Returns tweets with text containing query | http://127.0.0.1:8000/search/?text=modi |
| | sw_text | Returns tweets with text starting with query | http://127.0.0.1:8000/search/?sw_name=modi |
|  | ew_text | Returns tweets with text ending with query | http://127.0.0.1:8000/search/?ew_text=modi |
|  | x_text | Returns tweets with exact text in query | http://127.0.0.1:8000/search/?x_text=modi |
| ReTweet Count | rtcount | Returns Tweets with re-tweet count as query | http://127.0.0.1:8000/search/?rtcount=0 |
| | lt_rtcount | Returns Tweets with re-tweet count less than query | http://127.0.0.1:8000/search/?lt_rtcount=10 |
| | gt_rtcount | Returns Tweets with re-tweet count greater than query | http://127.0.0.1:8000/search/?gt_rtcount=0 |
| Favourites Count | favcount | Returns Tweets with favourites count as query | http://127.0.0.1:8000/search/?favcount=0 |
| | lt_favcount | Returns Tweets with favourites count less than query | http://127.0.0.1:8000/search/?lt_favcount=10 |
| | gt_favcount | Returns Tweets with favourites count greater than query | http://127.0.0.1:8000/search/?gt_favcount=0 |
| Followers Count | follow | Returns Tweets with followers count as query | http://127.0.0.1:8000/search/?follow=0 |
| | lt_follow | Returns Tweets with followers count less than query | http://127.0.0.1:8000/search/?lt_follow=10 |
| | gt_follow | Returns Tweets with followers count greater than query | http://127.0.0.1:8000/search/?gt_follow=0 |
| Friends Count | friends | Returns Tweets with friends count as query | http://127.0.0.1:8000/search/?friends=0 |
| | lt_friends | Returns Tweets with friends count less than query | http://127.0.0.1:8000/search/?lt_friends=10 |
| | gt_friends | Returns Tweets with friends count greater than query | http://127.0.0.1:8000/search/?gt_friends=0 |
| Language | lang | Returns Tweets with language as query | http://127.0.0.1:8000/search/?lang=en |
| Date Range | st_date, en_date | Returns tweets in date range/ or date time range as entered by user| http://127.0.0.1:8000/search/?en_date=2018-10-07T03%3A02%3A01&st_date=2018-10-07T00%3A00%3A00 OR http://127.0.0.1:8000/search/?en_date=2018-10-07&st_date=2018-10-07 |
#### Request
API 2- `http://127.0.0.1:8000/search/?st_date=2018-10-07&en_date=2018-10-08&lang=en&ordering=user_name&page=3&q=modi`
#### Response
Response by the API in Raw form

```
{  
   "count":46,
   "next":"http://127.0.0.1:8000/search/?en_date=2018-10-08&format=json&lang=en&ordering=user_name&page=4&q=modi&st_date=2018-10-07",
   "previous":"http://127.0.0.1:8000/search/?en_date=2018-10-08&format=json&lang=en&ordering=user_name&page=2&q=modi&st_date=2018-10-07",
   "results":[  
      {  
         "id":79,
         "user_id":"1048543498423549952",
         "user_name":"Rahul Tripathi",
         "user_screenname":"RahulTr95399870",
         "user_location":null,
         "user_followers":25,
         "user_friends":124,
         "t_id":1048928754016247809,
         "t_rtcount":0,
         "t_favcount":0,
         "t_create":"2018-10-07T19:01:17.768000+05:30",
         "t_text":"RT @RomeshNadir: PM Modi inaugurated today Uttarakhand Investors’ Summit 2018 in Dehradun. PM apprised that Business has become easier with…",
         "lang":"en"
      },
      {  
         "id":91,
         "user_id":"1048194722391572481",
         "user_name":"Ravikant Tiwari",
         "user_screenname":"Ravikan88848084",
         "user_location":"Madhya Pradesh, India",
         "user_followers":2,
         "user_friends":87,
         "t_id":1048928914897170432,
         "t_rtcount":0,
         "t_favcount":0,
         "t_create":"2018-10-07T19:01:56.125000+05:30",
         "t_text":"#BrandIndia\nIn the last 4 years, PM Modi's leadership has garnered greater recognition for India. From patents to s… https://t.co/XSVruBzn66",
         "lang":"en"
      },
      {  
         "id":88,
         "user_id":"913102253896151040",
         "user_name":"Sadhavi Rutambhara",
         "user_screenname":"ChandFeku",
         "user_location":"Planet Earth",
         "user_followers":3707,
         "user_friends":4976,
         "t_id":1048928908110835712,
         "t_rtcount":0,
         "t_favcount":0,
         "t_create":"2018-10-07T19:01:54.507000+05:30",
         "t_text":"RT @kukk44: Now What Mr Modi ?? Answers pls !!\n\nRupee devaluated because of certain malpractices https://t.co/G0esy7O8I9 via @YouTube",
         "lang":"en"
      }
      {.....}
      {.....}
      {.....}
      {.....}
      {.....}
      {.....}
      {.....}
      {.....}
   ]
}
```

### 3. API3 to trigger CSV (/csv)
This API triggers CSV storage of data filtered by the query url.
#### Request
API 1 = `http://127.0.0.1:8000/csv/?st_date=2018-10-07&en_date=2018-10-08&lang=en&ordering=user_name&page=3&q=modi`

A CSV file will be saved to the current directory with name tweets.csv you can change the name in views.py

#### Response
**The data will be saved to the current directory as tweets.csv**

### Using Mongo DB
**To migrate database to MongoDb
un-comment
'ENGINE': 'djongo',
'NAME': 'tweet',
and comment
#'ENGINE': 'django.db.backends.sqlite3',
#'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
in Settigns.py
Than migrate again after startng MongoDb server
by default SQLite 3 is used**
