import os
from datetime import datetime, timedelta

def scan_directory(folder):
    data=[]
    now=datetime.now()
    limit=now-timedelta(days=30)

    for f in os.listdir(folder):
        p=os.path.join(folder,f)
        if os.path.isfile(p):
            m=datetime.fromtimestamp(os.path.getmtime(p))
            extra=0
            fine=0
            if m<limit:
                extra=(now-m).days-30
                fine=extra*10
            data.append([f,os.path.getsize(p),os.path.splitext(f)[1],m,extra,fine])
    return data

def generate_reports(d):
    t=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    with open("audit_"+t+".txt","w") as a:
        for i in d:
            a.write(str(i)+"\n")

    with open("penalty_"+t+".txt","w") as p:
        for i in d:
            if i[5]>0:
                p.write(i[0]+" Fine Rs."+str(i[5])+"\n")
