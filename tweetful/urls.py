API_URL = "https://api.twitter.com"

#---For authorization of the app-------#
REQUEST_TOKEN_URL = API_URL + "/oauth/request_token"
AUTHORIZE_URL = API_URL + "/oauth/authorize?oauth_token={request_token}"
ACCESS_TOKEN_URL = API_URL + "/oauth/access_token"

#---For accessing the Users home Timeline----#
TIMELINE_URL = API_URL + "/1.1/statuses/home_timeline.json"

#--For accessing the followers of a specified User
FOLLOWERS_URL = API_URL + "/1.1/followers/list.json"

#--For posting status updates or tweets------#
POST_REQUEST_URL = API_URL + "/1.1/statuses/update.json"

