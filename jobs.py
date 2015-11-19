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
        new_job = {'position' : job['POSITION'],
            'joburl' : job['JOBURL'],
            'postdate' : job['POSTDATE'],
            'expirydate' :job['EXPIRYDATE'],
            'salarymax': job['SALARYMAX'],
            'name': job['NAME'],
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
print(job_list)
