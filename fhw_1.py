students = {'Евгений', 'Анастасия', 'Игорь', 'Светлана', 'Татьяна', 'Виктория', 'Александр', 'Мария', 'Оксана', 'Федор'}
grades = [[5,4,5,5,4], [3,5,2,3], [3,4,5,2], [4,4,4,4,3], [5,5,3,4,5], [1,2,3,4,5], [3,3,3,3,3], [4,5,5,5], [3,4,4,3,5], [5,3,3,3,3]]       
grades_avrsum = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4]), sum(grades[5])/len(grades[5]), sum(grades[6])/len(grades[6]), sum(grades[7])/len(grades[7]), sum(grades[8])/len(grades[8]), sum(grades[9])/len(grades[9])]
students_sort = sorted(students)
dnevnik = dict(zip(students_sort, grades_avrsum))
print(dnevnik)
