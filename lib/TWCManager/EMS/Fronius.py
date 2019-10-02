# Fronius Datamanager Solar.API Integration (Inverter Web Interface)

class Fronius:

  consumedW   = 0
  generatedW  = 0
  importW     = 0
  exportW     = 0
  voltage     = 0

  def __init__(self, serverIP):
    self.serverIP = serverIP

  def getConsumed():
    return self.consumedW

  def getGenerated():
    return self.generatedW
    
  def getInverterData():
    url = "http://" + self.serverIP + "/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DeviceID=1&DataCollection=CommonInverterData"
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    jsondata = r.json()

  def getMeterData():
    url = "http://" + self.serverIP + "/solar_api/v1/GetMeterRealtimeData.cgi?Scope=Device&DeviceId=0"
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    jsondata = r.json()

  def update():
    inverterData = getInverterData()
    meterData = getMeterData()
    