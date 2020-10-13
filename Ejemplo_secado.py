import time
import sensorsDatalogger

# Crear objetos de sensores especificando el conector, tipo y id(solo en DS18B20)
dht1 = sensorsDatalogger.DHTConnector('DHT', 'AM2301')
dht2 = sensorsDatalogger.DHTConnector('DHT1', 'AM2301')
dht3 = sensorsDatalogger.DHTConnector('DHT2', 'AM2301')
dht4 = sensorsDatalogger.DHTConnector('DHT3', 'AM2301')

while True:
	# Lectura de sensores DHT
	# Tambien existen los metodos:
	# getHumidityAndTemperature() para DHT, retorna hum, temp
	# getHumidity() para DHT, retorna hum
	print('Temperatura DHT1: ' + str(dht1.getTemperature()))
	print('Temperatura DHT2: ' + str(dht2.getTemperature()))
	print('Temperatura DHT3: ' + str(dht3.getTemperature()))
	print('Temperatura DHT4: ' + str(dht4.getTemperature()))
	print('\n')
	time.sleep(5)
