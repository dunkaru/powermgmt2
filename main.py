#!/usr/bin/env python
import json
from ina219 import INA219
from ina219 import DeviceRangeError

SHUNT_OHMS = 0.1
json_dict = {}
bus = ""
power = ""
supl = ""
shunt = ""


def read():
    ina = INA219(SHUNT_OHMS)
    ina.configure()
    print("Bus Voltage: %.3f V" % ina.voltage())


    while 1:
        try:
            print("Bus Current: %.3f mA" % ina.current())
            print("Power: %.3f mW" % ina.power())
            power = str(ina.power())
            print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
            shunt = str(ina.shunt_voltage())
            print("Supply voltage: %3f mV" % ina.supply_voltage())
            supl = str(ina.supply_voltage())
            bus = str(ina.voltage())

            for variable in ["bus", "power", "supl", "shunt"]:
                json_dict[variable] = eval(variable)
                with open("/home/albatross/Data/pwer_data.json", "w") as f:
                    json.dump(json_dict, f)
            print(json_dict)
        except DeviceRangeError as e:
                # Current out of device range with specified shunt resistor
            print(e)

        continue


if __name__ == "__main__":
        read()
