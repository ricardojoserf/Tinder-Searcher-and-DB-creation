import re, time, os, csv, collections, datetime, pynder
import common_functions as cf
import config as config



def search(session,timesleeping,csvname):

	req=session.nearby_users()
	csvFile = open(csvname, 'a')
	csvWriter = csv.writer(csvFile)
	csvWriter.writerow(["name","age","id","photos_urls"])
	for user in req:
		try:
			time.sleep(timesleeping)
			csvWriter.writerow([str(user.name.encode("utf-8")), user.age, user.id, user.photos])
		except:
			pass


def generateCSV(id_,token,timesleeping,csvname):
	if id is None or token is None:
		print("Facebook ID or Facebook Token not generated correctly")
	else:
		session = pynder.Session(facebook_id=id_, facebook_token=token)
		args = cf.get_args_db()
		cf.updateSearch(session,args.minAge,args.maxAge,args.maxDistance)
		search(session,timesleeping,csvname)


def main():
	CSV_NAME=(str(datetime.datetime.now().date())+".csv")
	SLEEP_TIME=config.timesleeping
	FBID = config.fb_id
	FBTOKEN = cf.createFBToken(config.fb_email,config.fb_password)
	generateCSV(FBID,FBTOKEN,SLEEP_TIME,CSV_NAME)


if __name__ == "__main__":
    main()
