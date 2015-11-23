import json
import urllib
#import urllib2
import requests


response = requests.get('http://www.ottawacityjobs.ca/fr/data/'	)
data = response.json()

'''
resource_url = 'http://localhost:8080/service/'
resource_url = 'http://www.ottawacityjobs.ca/en/data/'
response = json.loads(urllib2.urlopen(resource_url).read())
print(response)
'''

'''
r = urllib.request.urlopen(url)
data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
print(data)
'''


def get_jobs(data):
    job_list = []
    for job in data['jobs']:
        new_job = {'position' : job.get('POSITION', None),
            'joburl' : job.get('JOBURL', None),
            'postdate' : job.get('POSTDATE', None),
            'expirydate' :job.get('EXPIRYDATE', None),
            'salarymax': job.get('SALARYMAX', None),
            'name': job.get('NAME', None),
            'jobref': job.get('JOBREF', None),
            #EXTRA
            #'salarytype': job.get('SALARYTYPE', None),
            #'job_summary': job.get('JOB_SUMMARY', None),
            #'knowledge':job.get('KNOWLEDGE', None),
            #'language_certificates' : job.get('LANGUAGE_CERTIFICATES', None),
            #'educationandexp': job.get('EDUCATIONANDEXP', None)
            #'company_desc': job.get('COMPANY_DESC', None)
            }
        job_list.append(new_job)
        print("\n")
        print(new_job)
    return job_list

job_list = get_jobs(data)
print(len(job_list))




import sqlite3

CreateDataBase = sqlite3.connect('jobs.db')

QueryCurs = CreateDataBase.cursor()

def CreateTable():
    QueryCurs.execute('''CREATE TABLE Jobs
    (id INTEGER PRIMARY KEY, Position TEXT, JobRef TEXT, JobUrl TEXT,PostDate TEXT,ExpiryDate TEXT, SalaryMax TEXT, Title REAL)''')

def AddEntry(Position,JobRef,JobUrl,PostDate,ExpiryDate,SalaryMax,Title):
    QueryCurs.execute('''INSERT INTO Jobs (Position,JobRef,JobUrl,PostDate,ExpiryDate,SalaryMax,Title)
    VALUES (?,?,?,?,?,?,?)''',(Position,JobRef,JobUrl,PostDate,ExpiryDate,SalaryMax,Title))

#If I want to create the Database
#CreateTable()

for job in job_list:
	AddEntry(job['position'],job['jobref'],job['joburl'],job['postdate'],job['expirydate'],job['salarymax'],job['name'])


CreateDataBase.commit()

QueryCurs.execute('SELECT * FROM Jobs')

for i in QueryCurs:
    print ("\n")
    for j in i:
        print (j)


QueryCurs.close()
print(len(job_list))

"""
#To write to file as a backup
with open('jobs_fr.json', 'w') as outfile:
	json.dump(job_list, outfile, sort_keys = True, indent = 4,ensure_ascii=True)
"""

"""
https://wa0x6e.github.io/cal-heatmap/v2/

#unixtimestamp and number of Work published for that day
{
  "946705035": 4,
  "946706692": 4,
  "946707210": 0
}
https://wa0x6e.github.io/cal-heatmap/v2/datas-years.json

command line
date -d @946707210 +'%Y-%m-%d %H:%M:%S'
There is NO space after the + sign
"""


"""
Calculate the number of days between to date

from datetime import date

d0 = date(2008, 8, 18)
d1 = date(2008, 9, 26)
delta = d0 - d1
print delta.days
"""


"""
Database for Django
--Jobs
--Language
--Profile (details)
"""