grades = [[5, 3, 3, 5, 4],[2, 2, 2, 3],[4, 5, 5, 2],[4, 4, 3],[5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#average = sum(grades[0])/len(grades[0])
#print(average)
#average_1 = sum(grades[1])/len(grades[1])
#print(average_1)
#average_2 = sum(grades[2])/len(grades[2])
#print(average_2)
#average_3 = sum(grades[3])/len(grades[3])
#print(average_3)
#average_4 = sum(grades[4])/len(grades[4])
average = {}
names = list(students)
names.sort()
average.update({names[0]:sum(grades[0])/len(grades[0]), names[1]:sum(grades[1])/len(grades[1])})
average.update({names[2]:sum(grades[2])/len(grades[2]), names[3]:sum(grades[3])/len(grades[3])})
average.update({names[4]:sum(grades[4])/len(grades[4])})
print(average)