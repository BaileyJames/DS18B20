# Use Multiple DS18B20 Temperature Sensors
---

## Description
This is a simple Python script that enables you to use multiple [DS18B20](https://www.raspberryfield.life/2020/05/23/ds18b20-temperature-probe-raspberry-pi/) temperature sensors.

## How to use
On a Raspberry Pi, navigate to `/sys/bus/w1/devices/` and run `ls` to list the sensors.
![img](https://i.imgur.com/z3ffNmc_d.webp?maxwidth=760&fidelity=grand)

The sensors' serial codes will start with `28-` followed by the serial code. 
To use the script, simply just paste your serial codes into the array at the top of the script, like so:
![Imgur](https://i.imgur.com/s2LgnWW.png)

From there, run the script and you should (hopefully) have some results :).

![Imgur](https://i.imgur.com/xKDST85.png)
