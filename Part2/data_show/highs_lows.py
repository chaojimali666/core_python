import csv
from datetime import datetime
from matplotlib import pyplot as plt 
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	"""
	#读取头文件
	for index,column_header in enumerate(header_row):
		print(index,column_header)
	"""
	dates,highs,lows = [],[],[]
	for row in reader:
		current_date = datetime.strptime(row[0],"%Y-%m-%d")
		dates.append(current_date)
		highs.append(int(row[1]))
		lows.append(int(row[3]))

#绘图
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
#设置图形格式
plt.title("Daily high temperatures - 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.locator_params('y',nbins = 10)
plt.show()