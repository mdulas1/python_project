import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
lebels = ['a', 'b' 'c', 'd']

plt.pie(sizes, labels=lebels, autopct='%1.1f%%')
circle = plt.circle((0,0), 0.8, color='white')
plt.gca().add_artist(circle)
plt.title('donut chart')
plt.show()