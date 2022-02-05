import requests
import psycopg2
import bs4
import sys

def create_db():
	
	dbconn = psycopg2.connect(database = 'naukri')	#connects to the database using psycopg2
	cursor = dbconn.cursor()	#cursor to the database
	f = open('jobs.sql')
	sql = f.read()
	cursor.execute(sql)	#executes the sqlcode
	dbconn.commit()	#commits the changes done
	

def fetch_jobs():

	url = "https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_key_loc&searchType=adv&keyword=python&location=bangalore&k=python&l=bangalore&seoKey=python-jobs-in-bangalore&src=jobsearchDesk&latLong="
	header = {"appid" : "109", "systemid" : "109"}
	r = requests.get(url, headers = header)
	data = r.json()	#converts the content to a json format. The contents in this url are now available as a dictionary in python
	#print(data['jobDetails'])
	return data['jobDetails']	#if you print the json file we see that the job details are present at the index 'job details'
	
def insert_jobs(jobs):

	dbconn = psycopg2.connect(database = 'naukri')
	cursor = dbconn.cursor()
	
	for i in jobs:
		title = i['title']
		jobId = i['jobId']
		companyName = i['companyName']
		tagsAndSkills = i['tagsAndSkills']
		jdURL = i['jdURL']
		soup = bs4.BeautifulSoup(i['jobDescription'], features = 'html.parser')
		jd = str(soup.txt)
		print(f"Inserting {title} to the database.......")
		cursor.execute('insert into openings (title, jobId, companyName, t_s, jdURL, jobDescription) values (%s, %s, %s, %s, %s, %s)', (title, jobId, companyName, tagsAndSkills, jdURL, jd))
		dbconn.commit()
		
	

def main(arg):
	if arg == 'create':
		create_db()
	elif arg == 'fetch':
		jobs = fetch_jobs()
		insert_jobs(jobs)
		
if __name__ == "__main__":
	main(sys.argv[1])	#the argv contains the command written
	
