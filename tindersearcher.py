import re, time, os, csv, collections, pynder
import common_functions as cf
import config as config



def search(session,name,timesleeping):
	req=session.nearby_users()
	for user in req:
		try:	
			time.sleep(timesleeping)
			if (user.name == name):
				print("Name:     "+str(user.name) )
				# print("Bio:      "+str(user.bio.encode("utf-8")) +"\n")
				print("Age:      "+str(user.age) )
				print("Photos:      "+str(user.photos) )
				print("Id:      "+str(user.id) )
				print("Distance: "+str(user.distance_km) )
		except:
				pass				


def funct_(id_,token,timesleeping):
	if id is None or token is None:
		print("Facebook ID or Facebook Token not generated correctly")
	else:
		session = pynder.Session(facebook_id=id_, facebook_token=token)
		args = cf.get_args_searcher()
		cf.updateSearch(session,args.minAge,args.maxAge,args.maxDistance)
		search(session,args.name,timesleeping)


def main():
	SLEEP_TIME=config.timesleeping
	FBID = config.fb_id
	FBTOKEN = cf.createFBToken(config.fb_email,config.fb_password)
	funct_(FBID,FBTOKEN,SLEEP_TIME)


if __name__ == "__main__":
    main()
