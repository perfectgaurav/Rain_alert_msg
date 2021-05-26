import requests
import os
from twilio.rest import Client
# *********Generate your own token and id on twilio(these will not work)*****************
sid="AC158a7ca256febedbaa61f9cf5a8540b4"
token="58ef9229c25a7a4d3e6182bdca853ab9"
key="aac8cab534dc996b255e47145d669b72"
endpoint="https://api.openweathermap.org/data/2.5/onecall"
parameters={
    "lat":28.613939,
    "lon":77.209023,
    
    "appid":key,
    "exclude":"current,daily,minutely"

}

response= requests.get(endpoint,params=parameters)
data=response.json()
will_rain=False
weather_slice=data["hourly"][:12]
for hour_data in weather_slice:
    condition=(hour_data["weather"][0]["id"])
    # print(condition)
    if int(condition)<700:
        will_rain=True

if will_rain:
    # account_sid = os.environ["sid"]
    # auth_token = os.environ["token"]
    client = Client(sid, token)
    message = client.messages \
                .create(
                     body="Its going to rain.Bring your Umberella",
                     from_='+17204459939',
                     to='+919034973746'
                 )

    print(message.status)
    

    
     
# print(data["hourly"][0]["weather"][0]["id"])
