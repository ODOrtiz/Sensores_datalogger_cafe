# =====================================
# Configuracion AM2301 (DHT22)
# =====================================
import Adafruit_DHT
dht = Adafruit_DHT.DHT22

# =====================================
# Configuracion DS18B20
# =====================================
from ds18b20 import DS18B20
tempSensor = DS18B20()

# =====================================
# Clase de conectores DHT
# =====================================
class DHTConnector:
	def __init__(self, _connector, _typeSensor, _deviceId = '0'):
		if _typeSensor == 'DS18B20' and _deviceId != '0':
			self.pin = getPinSensor('DHT1')
			self.typeSensor = _typeSensor
			self.deviceId = getRegisteredId(_deviceId)
			self.error = False
		elif _typeSensor == 'AM2301':
			self.pin = getPinSensor(_connector)
			self.typeSensor = _typeSensor
			self.deviceId = _deviceId
			self.error = False
		else:
			self.error = True
			print('Error al configurar DHT connector')
		
	def getTemperature(self):
		if self.error == False:
			hum, temp = getValueDHTConnector(self.pin, self.typeSensor, self.deviceId)
			return temp
		else: 
			print('Error al configurar DHT connector')
	
	def getHumidity(self):
		if self.error == False:
			hum, temp = getValueDHTConnector(self.pin, self.typeSensor, self.deviceId)
			return hum
		else: 
			print('Error al configurar DHT connector')
		
	def getHumidityAndTemperature(self):
		if self.error == False:
			hum, temp = getValueDHTConnector(self.pin, self.typeSensor, self.deviceId)
			return hum, temp
		else: 
			print('Error al configurar DHT connector')
		
			
# =====================================
# Funcion para obtener el pin
# =====================================
def getPinSensor(connector):
	if connector == 'DHT':
		return 23
	elif connector == 'DHT1':
		return 18
	elif connector == 'DHT2':
		return 24
	elif connector == 'DHT3':
		return 25
	else:
		return 999

# =====================================
# Funcion para obtener el id registrado
# =====================================
def getRegisteredId(deviceId):
	if deviceId == '1':
		return '/sys/bus/w1/devices/28-01191f152963/w1_slave'
	elif deviceId == '2':
		return '/sys/bus/w1/devices/28-01191f21bc5c/w1_slave'
	elif deviceId == '3':
		return '/sys/bus/w1/devices/28-01191f1515d9/w1_slave'
	elif deviceId == '4':
		return '/sys/bus/w1/devices/28-0301979462e9/w1_slave'
	else:
		return '/nada'

# =====================================
# Obtener el valor de sensores de 
# conectores DHT
# =====================================
def getValueDHTConnector(pin, typeSensor, path):
	if typeSensor == 'AM2301':
		hum, temp = readAM2301(pin)
		return hum, temp
	elif typeSensor == 'DS18B20':
		temp = readDS18B20(pin, path)
		return 0,temp
	else:
		return 0,0

# =====================================
# Funcion para leer dht
# =====================================
def readAM2301(pin):
	try:
		humidity, temperature = Adafruit_DHT.read_retry(dht, pin)
		if temperature == None:
			print("DHT no conectado")
			return 0, 0
		else:
			return humidity, temperature
	except:
		print("DHT no conectado")
		return 0, 0

# =====================================
# Funcion para leer ds18b20
# =====================================
def readDS18B20(pin, path):
	try:
		temp = tempSensor.getTemperatureById(path)
		return temp
	except:
		print("DS18B20 no conectado")
		return 0
