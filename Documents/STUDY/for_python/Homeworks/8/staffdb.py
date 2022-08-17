import pandas as pd
import openpyxl
import datetime

# Всякая работа с данными.

depts_data = pd.DataFrame({'dept_id': [1, 2, 3, 4, 5, 6, 7, 8],
     'departments': ['Sales&Distrib', 'PR', 'Logistics', 'LegalDept', 'FinDept', 'IT', 'AccountingDept', 'EnergyDept'],
     })
print('Прописан DataFrame с отделами.')
writer = pd.ExcelWriter('departments.xlsx')
depts_data.to_excel(writer, 'depts')
writer.save()
print()
print('Список отделов записан в файл.')
print()
staff_data = pd.read_excel('staff.xlsx')
print('Импортированная таблица с данными о персонале.')
print(staff_data)
print()
salary_data = pd.DataFrame({'id_pers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
     'salary': [19300, 24187, 23008, 20877, 19385, 25434, 21789, 23188, 18884, 20112, 23565, 24744, 21555, 27188, 24003]
     })
print('Прописан DataFrame с зарплатами.')
writer = pd.ExcelWriter('salaries.xlsx')
salary_data.to_excel(writer, 'salaries')
writer.save()
print()
print('Зарплаты записаны в файл.')
print()
print('Таблица стаффа, отсортированная по датам рождения.')
sorted_staff = staff_data.sort_values(by='birthdate')
print(sorted_staff)
print()
print('Отсортированное по зарплате пересечение таблиц персонала и зарплат')
persnsalary = pd.merge(staff_data, salary_data, how='inner')
print(persnsalary[['name', 'surname', 'salary']].sort_values(by='salary'))
print()
print('Приняли нового сотрудника')
new_staff_data = staff_data.copy()
new_staff_data.loc['16']=[17, 'Arkadiy', 'Ivanov', '1973-06-17']
print(new_staff_data)
print()
print('Ушел Константин Васильев')
new_staff_data.drop(index=14,inplace=True)
print(new_staff_data)
print()
print('Алина Белова вышла замуж')
new_staff_data.loc[(new_staff_data.name == 'Alina')&(new_staff_data.surname == 'Belova'), 'surname'] = 'Kolodina'
print(new_staff_data)
print()
print('Сводная таблица по сотрудникам с отделами и зарплатами')
persnsalarynew = pd.merge(staff_data, salary_data, how='inner')
employ_data = pd.read_excel('staffToDepts.xlsx')
deptsnstaff = pd.merge(depts_data, employ_data)
pers_depts_salary_data = pd.merge(persnsalarynew, deptsnstaff, how = 'inner')
print(pers_depts_salary_data[['departments', 'name', 'surname', 'salary']].sort_values(by='departments'))
print()
print('Та же таблица, но с фильтрацией по зарплате.')
filtered_final = pers_depts_salary_data.loc[lambda pers_depts_salary_data: pers_depts_salary_data['salary'] >= 20000][['departments', 'name', 'surname', 'salary']]
print(filtered_final.sort_values(by='salary'))