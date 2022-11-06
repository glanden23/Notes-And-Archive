tmpdata = open("temperature_data.csv","r").readlines()
data = []

#Year, Anomaly, Lowess
for i in tmpdata:
    data.append(i.rstrip().split(","))

anomalyData = []
for i in data:
    try:
        anomalyData.append(float(i[1]))
    except:
        print(f"Couldn't append data, likely due to it not being able to be converted to a float.\n\"{i[1]}\"")

lowessData = []
for i in data:
    try:
        lowessData.append(float(i[2]))
    except:
        print(f"Skipped Data due to not able to be turned to a float:\n\"{i[2]}\"")

#https://www.geeksforgeeks.org/find-average-list-python/
print(f'''
      Average
Max: {max(anomalyData)}
Min: {min(anomalyData)}
Average: {sum(anomalyData)/len(anomalyData)}
      ''')

print(f'''
      LOWESS
Max: {max(lowessData)}
Min: {min(lowessData)}
Average: {sum(lowessData)/len(lowessData)}
      ''')