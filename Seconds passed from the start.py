import datetime
now=str(datetime.datetime.now())
sec=int(now[17]+now[18])
mins=int(now[14]+now[15])
hrs=int(now[11]+now[12])
days=int(now[8]+now[9])
months=int(now[5]+now[6])
years=int(now[0]+now[1]+now[2]+now[3])
vis=24*15+25*5+5
print(now,sec,mins,hrs,days,months,years)
s=sec+(mins*60)+(hrs*3600)+(days*86400)+(months*2419200)+(years*31536000)+(vis*86400)
print(s)
