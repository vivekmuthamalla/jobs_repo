import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','vivekjobs.settings')
import django
django.setup()

from testapp.models import hydjobs,knrjobs,ngpjobs
from faker import Faker
from random import *
fake = Faker()

def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdata =fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team leader','Software Engineer','Associate Engineer'))
        feligibility = fake.random_element(elements=('B.Tech','M.Tech','MCA','Phd'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        hyd_job_record = hydjobs.objects.get_or_create(
            date=fdata,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
        )

    for i in range(n):
        fdata =fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team leader','Software Engineer','Associate Engineer'))
        feligibility = fake.random_element(elements=('B.Tech','M.Tech','MCA','Phd'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        hyd_job_record = knrjobs.objects.get_or_create(
            date=fdata,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
        )

    for i in range(n):
        fdata =fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team leader','Software Engineer','Associate Engineer'))
        feligibility = fake.random_element(elements=('B.Tech','M.Tech','MCA','Phd'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        hyd_job_record = ngpjobs.objects.get_or_create(
            date=fdata,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
        )
n=int(input("enter number of records:"))
populate(n)
print(f'{n} records inserted successfully...')

'''def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('project Manager','Team Lead','Software Engineer','Associate Engineer'))
        feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA','MBA'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        hyd_jobs_records=HydJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)'''
