import matplotlib.pyplot as plt


labels=['java','python','c++','C','C#']

#to create pie chart
per=[25,25,25,0,25]
plt.pie(per,labels=labels,autopct='%1.1f%%',startangle=150)
plt.show()

#to create bar graph
util=[1,2,3,4,5]

plt.bar(labels,util)
plt.xlabel('usage') 
plt.ylabel('language')
plt.title('data')
plt.show()

#to create graph
x=[1,2,3,4,5]
y=[2,1,4,5,6]


plt.plot(x,y,marker='o',linestyle='--')
plt.show()

