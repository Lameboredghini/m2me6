"""
Reading Data from Thingspeak cloud platform
Fields:
1) Temperature
2) Humidity
3) Light
4) Pressure
Read API Endpoint: https://api.thingspeak.com/channels/1312548/feeds.json?api_key=CVUI9NG48I40B07U&results=4
"""
import requests,sqlite3

response = requests.get(
    "https://api.thingspeak.com/channels/1312548/feeds.json?api_key=CVUI9NG48I40B07U&results=4"
)

if(response.ok):
    response_in_json = response.json()
else:
    exit(1) 

data = response_in_json.get("feeds")

connection = connection = sqlite3.connect("thingspeak.db")
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE Thingspeak (Id INTEGER,Temperature INTEGER, Humidity INTEGER, Light INTEGER, Pressue INTEGER)"
) 

for i in data:
    id_ = i['entry_id']
    Temperature = int(i['field1'])
    Humidity = int(i['field2'])
    Light = int(i['field3'])
    Pressure = int(i['field4'])

    cursor.execute(f"INSERT INTO Thingspeak VALUES ({id_}, {Temperature}, {Humidity}, {Light}, {Pressure})")


connection.commit() 

print("Data Has been completely stored in db")