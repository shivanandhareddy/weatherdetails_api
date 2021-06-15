import requests
import json
import datetime
url = "http://api.openweathermap.org/data/2.5/weather?"
apikey="api key"
loc=input("Enter the location:")
res=requests.get(url + "appid=" + apikey + "&q=" + loc)
#requesting for data
x=res.json()
if(x['cod']!='404'):#cheking for errors
    y=x['weather']
    m=x['main']
    z=y[0]
    s=x['sys']
    w=str(z['description'])
    #getting details and making into celcius
    t=str((m['temp'] - 273.15))
    tmin=(str(m['temp_min'] - 273.15))
    tmax=str(m['temp_max'] - 273.15)
    p=str(m['pressure'])+'hpa'
    h=str(m['humidity'])+'%'
    sr=str(datetime.datetime.fromtimestamp(s['sunrise']).isoformat())
    ss=str(datetime.datetime.fromtimestamp(s['sunset']).isoformat())
    details='It may be  '+w+'\n'+'temperature: '+t[:4]+'˚C'+'\n'+'Min_temperature: '+tmin[:4]+'˚C'+'\n'+'Max_temperature: '+tmax[:4]+'˚C'+'\n'+'Pressure: '+p+'\n'+'Humidity: '+h+'\n'+'Sunrise_time: '+sr[11:]+'\n'+'Sunset_time: '+ss[11:]
    print(details)
else:
    print('ERROR')
