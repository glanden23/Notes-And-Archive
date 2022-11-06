from pandaFun import *
import math

co2Data = readCSV("co2_data.csv",header=5)
co2Data["Average"] = replaceData(co2Data["Average"], -99.99,math.nan)
dropData(co2Data,"Average",True)
createGraph(co2Data["decimal_year"], co2Data["Average"], "Change in Temperatures", "Years", "Temp Anomalies in C")