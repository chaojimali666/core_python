from die import Die
import pygal 
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(100):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#分析结果
frequencies = []
for value in range(1,die_1.num_sides*2+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#结果可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
#hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
hist.x_labels = [('%d') % i for i in range(2*die_1.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual2.svg')