import requests
import time
import adafruit_dht as ad
import board

humidity = 0
temperature = 0
 
  # create a string to hold the first part of the URL
WUurl = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"
WU_station_id = "KKSOLATH478" # Replace XXXX with your PWS ID
WU_station_pwd = "U7P7Sfoi" # Replace YYYY with your Password
WUcreds = "ID=" + WU_station_id + "&PASSWORD="+ WU_station_pwd
date_str = "&dateutc=now"
action_str = "&action=updateraw"
def upload(temp, humid):
    r= requests.get(str(WUurl) + str(WUcreds) + str(date_str) +"&humidity=" + str(humidity) + "&tempf=" + str(temperature) + action_str)
    print(r)
    with open("/home/sitrus/data/data.csv", "a") as file:
        file.write(str(time.time()) + "," + str(temp) + "," + str(humid) + "\n")


sensor = ad.DHT11(board.D12, use_pulseio=False)

while True:
    try:
        temperature = round(sensor.temperature * (9/5) + 32, 2)
        print(temperature)
        humidity = sensor.humidity
        print(humidity)
        upload(temperature, humidity)
        
    except RuntimeError as error:
        print(error.args[0])
        
    time.sleep(30)
