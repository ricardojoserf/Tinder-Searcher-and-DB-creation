import re, time, os, csv, collections, argparse, pynder, robobrowser, itertools
from optparse import OptionParser
import config as config


def get_args_db():
  parser = argparse.ArgumentParser()
  parser.add_argument('-m', '--minAge', required=True, action='store', help='Min age')
  parser.add_argument('-M', '--maxAge', required=True, action='store', help='Max age')
  parser.add_argument('-d', '--maxDistance', required=True, action='store', help='Max distance')
  my_args = parser.parse_args()
  return my_args

def get_args_searcher():
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', '--name', required=True, action='store', help='Max distance')
  parser.add_argument('-m', '--minAge', required=True, action='store', help='Min age')
  parser.add_argument('-M', '--maxAge', required=True, action='store', help='Max age')
  parser.add_argument('-d', '--maxDistance', required=True, action='store', help='Max distance')
  my_args = parser.parse_args()
  return my_args

### Credits for this function to the Github user Venomous
def createFBToken(email,password):
	try:
		MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"
		FB_AUTH = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"
		s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")
		s.open(FB_AUTH)
		f = s.get_form()
		f["pass"] = password
		f["email"] = email
		s.submit_form(f)
		f = s.get_form()
		s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
		access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]
		return access_token
	except:
		print("Auth token generation failed")


def updateSearch(session,minAge,maxAge,distance):
	session.update_profile({
            "gender_filter": 1,
            "age_filter_min": minAge,
            "age_filter_max": maxAge,
            "distance_filter": distance
        })



def changeLocation(session, coord):	
	session.update_location(coord[0],coord[1])
	time.sleep(20)

