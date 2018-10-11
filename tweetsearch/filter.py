from django.db.models import Q
from .models import Tweet

def filter(self, *args, **kwargs):
    '''filters queryset according to the query by user
    filters written for different query parameters'''

    queryset_list = Tweet.objects.all() #getting all queries in the database

    #search query
    query = self.request.query_params.get('q', None) 

    #user name
    name = self.request.query_params.get('name', None)
    sw_name = self.request.query_params.get('sw_name', None)
    ew_name = self.request.query_params.get('ew_name', None)
    x_name = self.request.query_params.get('x_name', None)

    #user screen name
    name_sc = self.request.query_params.get('name_sc', None)
    sw_name_sc = self.request.query_params.get('sw_name_sc', None)
    ew_name_sc = self.request.query_params.get('ew_name_sc', None)
    x_name_sc = self.request.query_params.get('x_name_sc', None)

    #tweet text
    text = self.request.query_params.get('text', None)
    sw_text = self.request.query_params.get('sw_text', None)
    ew_text = self.request.query_params.get('ew_text', None)
    x_text = self.request.query_params.get('x_text', None)

    #Re Tweet count
    rtcount = self.request.query_params.get('rtcount', None)
    lt_rtcount = self.request.query_params.get('lt_rtcount', None)
    gt_rtcount = self.request.query_params.get('gt_rtcount', None)

    #Favourite Count
    favcount = self.request.query_params.get('favcount', None)
    lt_favcount = self.request.query_params.get('lt_favcount', None)
    gt_favcount = self.request.query_params.get('gt_favcount', None)

    #Followers count
    follow = self.request.query_params.get('follow', None)
    lt_follow = self.request.query_params.get('lt_follow', None)
    gt_follow = self.request.query_params.get('gt_follow', None)

    #friends_count
    friends = self.request.query_params.get('friends', None)
    lt_friends = self.request.query_params.get('lt_friends', None)
    gt_friends = self.request.query_params.get('gt_friends', None)

    #Language
    lang = self.request.query_params.get('lang', None)

    #Date Start and End
    st_date = self.request.query_params.get('st_date', None)
    en_date = self.request.query_params.get('en_date', None)


    # query
    if query:
        queryset_list = queryset_list.filter(
            Q(user_name__icontains=query)|
            Q(t_text__icontains=query)|
            Q(user_screenname__icontains=query)
            ).distinct()

    # name
    if name:
        queryset_list = queryset_list.filter(
            Q(user_name__icontains=name)
            )
    if sw_name:
        queryset_list = queryset_list.filter(
            Q(user_name__istartswith=sw_name)
            )
    if ew_name:
        queryset_list = queryset_list.filter(
            Q(user_name__iendswith=ew_name)
            )
    if x_name:
        print('xyz')
        queryset_list = queryset_list.filter(
            Q(user_name__iexact=x_name)
            )

    #user screen name
    if name_sc:
        queryset_list = queryset_list.filter(
            Q(user_screenname__icontains=name_sc)
            )
    if sw_name_sc:
        queryset_list = queryset_list.filter(
            Q(user_screenname__istartswith=sw_name_sc)
            )
    if ew_name_sc:
        queryset_list = queryset_list.filter(
            Q(user_screenname__iendswith=ew_name_sc)
            )
    if x_name_sc:
        queryset_list = queryset_list.filter(
            Q(user_screenname__iexact=x_name_sc)
            )

    #tweet text
    if text:
        queryset_list = queryset_list.filter(
            Q(t_text__icontains=text)
            )
    if sw_text:
        queryset_list = queryset_list.filter(
            Q(t_text__istartswith=sw_text)
            )
    if ew_text:
        queryset_list = queryset_list.filter(
            Q(t_text__iendswith=ew_text)
            )
    if x_text:
        queryset_list = queryset_list.filter(
            Q(t_text__iexact=x_text)
            )

    #re tweet count
    if rtcount:
        queryset_list = queryset_list.filter(t_rtcount=rtcount)
    if lt_rtcount:
        queryset_list = queryset_list.filter(t_rtcount__lt=lt_rtcount)
    if gt_rtcount:
        queryset_list = queryset_list.filter(t_rtcount__gt=gt_rtcount)

    #favcount
    if favcount:
        queryset_list = queryset_list.filter(t_favcount=favcount)
    if lt_favcount:
        queryset_list = queryset_list.filter(t_favcount__lt=lt_favcount)
    if gt_favcount:
        queryset_list = queryset_list.filter(t_favcount__gt=gt_favcount)

    #followers count
    if follow:
        queryset_list = queryset_list.filter(user_followers=follow)
    if lt_follow:
        queryset_list = queryset_list.filter(user_followers__lt=lt_follow)
    if gt_follow:
        queryset_list = queryset_list.filter(user_followers__gt=gt_follow)

    #friends count
    if friends:
        queryset_list = queryset_list.filter(user_friends=friends)
    if lt_friends:
        queryset_list = queryset_list.filter(user_friends__lt=lt_friends)
    if gt_friends:
        queryset_list = queryset_list.filter(user_friends__gt=gt_friends)

    #Start to end date
    if st_date and en_date:
        queryset_list = queryset_list.filter(t_create__range=[st_date, en_date])

    #language
    if lang:
        queryset_list = queryset_list.filter(lang=lang)

    return queryset_list
