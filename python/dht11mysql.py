#!/usr/bin/python
import sys
import Adafruit_DHT
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="dht11",
  passwd="dht11",
  database="dht11"
)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    mycursor = mydb.cursor()
    sql = "INSERT INTO dht11 (temperature,humidity) VALUES(%s, %s)"
    val = (temperature,humidity)
    mycursor.execute(sql, val)
    mydb.commit()
