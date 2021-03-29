import time

sensors = [] ## Add your DS18B20 serial numbers into this array
base_dir = '/sys/bus/w1/devices/'
count = 0

def getData():
    data = []
    for sensor in sensors:
        tempFile = open(base_dir + sensor + "w1_slave") 
        tempText = tempFile.read()
        tempFile.close()
        value = sensor + tempText
        data.append(value)
    return data

def processData():
    lines = getData()
    count = 0
    data = []
    for line in lines:
        sPosition = lines[count].find("t=")
        temp_string = (float(lines[count][sPosition+2:]))
        count = count + 1
        temp_c = temp_string /1000
        data.append(temp_c)
    return data

while True:
    print(processData())