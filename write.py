"""
Writing Data to Thingspeak cloud platform
Fields:
1) Temperature
2) Humidity
3) Light
4) Pressure
URL: https://api.thingspeak.com/update?api_key=8FZP4MM91KR13886&field1=0
"""

import requests,random,time

try:
    while True:
        Temperature = random.randint(1,100)
        Humidity = random.randint(1,100)
        Light = random.randint(1,1000)
        Pressure = random.randint(1,100)

        response = requests.get(
            "https://api.thingspeak.com/update?api_key=8FZP4MM91KR13886",
            params={'field1':Temperature,'field2':Humidity,'field3':Light,'field4':Pressure}
        )

        print(f"Status Code {response.status_code}")
        time.sleep(1)
except:
    print("\nError")