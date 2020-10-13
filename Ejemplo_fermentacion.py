import time
import sensorsDatalogger

# Crear objetos de sensores especificando el conector, tipo y id(solo en DS18B20)
dht1 = sensorsDatalogger.DHTConnector('DHT', 'AM2301')
tempSensor1 = sensorsDatalogger.DHTConnector('DHT1', 'DS18B20', '1')
tempSensor2 = sensorsDatalogger.DHTConnector('DHT1', 'DS18B20', '2')
tempSensor3 = sensorsDatalogger.DHTConnector('DHT1', 'DS18B20', '3')

while True:
	# Lectura de sensores DHT
	# Tambien existe el metodo getHumidityAndTemperature() para DHT, retorna hum, temp
	print('Temperatura DHT: ' + str(dht1.getTemperature()))
	print('Humedad DHT: ' + str(dht1.getHumidity()))
	# Lectura de sensores DS18B20
	print('Temperatura DS1: ' + str(tempSensor1.getTemperature()))
	print('Temperatura DS2: ' + str(tempSensor2.getTemperature()))
	print('Temperatura DS3: ' + str(tempSensor3.getTemperature()))
	print('\n')
	time.sleep(5)
