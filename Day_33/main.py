import requests
from datetime import datetime
import smtplib


LONG = 40.489674
LAT = 9.145000

MY_EMAIL = 'example@gmail.com'
PASSWORD = 'test password'

def iss_close():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    if LONG -5  <= iss_longitude <= LONG + 5 and LAT -5 <= iss_latitude <= LAT + 5:
        return True


parameters = {
    'lat': LAT,
    'lng': LONG,
    'formatted': 0,
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

current_time = datetime.now()


with smtplib.SMTP('YOUR EMAIL PROVIDER SMTP SERVER ADDRESS') as connection:
    connection.starttls()
    connection.login(MY_EMAIL, PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs='test@gmail.com', msg='LOOK UP')




