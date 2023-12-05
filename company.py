"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

# Первый блок
import statistics

# deparmens
def all_deparment():
    for department in departments:
        print(f"Отдел: {department['title']}")

#names
def all_employers():
    for department in departments:
        for employers in department['employers']:
            print(employers['first_name'], employers['last_name'], sep=' ')

#names + depatmens
def name_and_departament():
    for department in departments:
        for employer in department['employers']:
            print(f"{department['title']}: {employer['first_name']} {employer['last_name']}")

# names >= 100 k salary

def rich_bitch():
    for department in departments:
        for employer in department['employers']:
            if employer['salary_rub'] >= 100000:
                print(f"{employer['first_name']} {employer['last_name']} is rich bitch")
            else:
                continue

# salay less than 80 000
def low_salary():
    for department in departments:
        for employer in department['employers']:
            if employer['salary_rub'] < 80000:
                print(f"Position: {employer['position']} earns lower than 80 000 rub.")
            else:
                continue

# Сколько денег на отдел(тут фантазия на инглиш у меня коничалась)
def department_sum():
    for department in departments:
        sum_salary = 0
        for employer in department['employers']:    
            sum_salary += employer['salary_rub']
        
        print(f"{department['title']} sum of salary is {sum_salary}")
        

# первый блок готов      

# Второй блок:


# отделы и мин зарлата в них
def departament_min_salary():
    for department in departments:
        list_salary = []
        for salary in department['employers']:    
            list_salary.append(salary['salary_rub'])
        print(f"Самая низкая зарплата в {department['title']}: {min(list_salary)}")

# min, max, average salary
def departament_min_average_max_salary():
    for department in departments:
        list_salary = []
        for salary in department['employers']:    
            list_salary.append(salary['salary_rub'])
        print()
        print(f"Самая низкая зарплата в {department['title']}: {min(list_salary)}")
        print(f"Средняя зарплата в {department['title']}: {statistics.mean(list_salary)}")
        print(f"Самая высокая зарплата в {department['title']}: {max(list_salary)}")
        
# avrage salaty by company
def average_salary():
    list_salary = []
    for department in departments:
        for salary in department['employers']:    
            list_salary.append(salary['salary_rub'])
    print()
    print(f"Средняя зарплата в компании: {statistics.mean(list_salary)}")

# more than 90 000 rub positions
def position_big_salary():
    for departament in departments:
        for position in departament['employers']:
            if position['salary_rub'] > 90_000:
                print(f"Зарабатывает более 90 000 рублей позиция: {position['position']}")


#average salary by women
def female_average_salary():
    women =  ("Michelle", "Caitlin", "Nicole", "Christina")
    women_salary = []
    for departament in departments:
        for salary in departament['employers']:
            if salary['first_name'] in women:
                women_salary.append(salary['salary_rub'])
            else:
                continue
    print(f"Средняя зарплата среди женщин: {statistics.mean(women_salary)}")

#Вывод имени по гласной букве в фамилии
def last_name_vowel():
    vowels = ('a','e', 'i' 'u', 'o','u', 'y')
    for departament in departments:
        for last_name in departament['employers']:
            if last_name['last_name'][-1] in vowels:
                print(f"Имя, фамилия которого заканчивается на гласную: {last_name['last_name']}")
            else:
                continue
         
# Второй блок всё!!!


# Третий блок

# Вывести список отделов со средним налогом на сотрудников этого отдела.

def averege_department_taxes():
    for deparment in departments:
        current_tax = 0
        deparment_name = deparment['title']
        for tax in taxes:
            if tax['department'] is None or tax['department'].lower() == deparment_name.lower():
                current_tax += tax['value_percents']
        tax_sum = 0.0
        for employer in deparment['employers']:
            tax_sum += employer['salary_rub'] * current_tax / 100
        print(f"Средний налог в {deparment_name}: {tax_sum / len(deparment['employers'])} рублей.")    
           


# Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
# Господи, надеюсь я правильно понял задание))))))))))))))

def salary_taxed_untaxed():
    for department in departments:
        deparment_name = department['title']
        current_tax = 0
        for tax in taxes:
            if tax['department'] is None or tax['department'].lower() == deparment_name.lower():
                current_tax += tax['value_percents']
        for employer in department['employers']:
            employer_name = f"{employer['first_name']} {employer['last_name']}"
            employer_salary = employer['salary_rub']
            employer_salary_taxed = employer_salary - (employer_salary * current_tax / 100)
            print(f"""Имя сотрудника: {employer_name}
Жалование с учетом налога: {float(employer_salary)} 
Жалование после вычета налога: {employer_salary_taxed}
""")
            

#  Вывести список отделов, отсортированный по месячной налоговой нагрузки.

def tax_per_mounth():
    for deparment in departments:
        current_tax = 0
        deparment_name = deparment['title']
        for tax in taxes:
            if tax['department'] is None or tax['department'].lower() == deparment_name.lower():
                current_tax += tax['value_percents']
        tax_sum = 0.0
        for employer in deparment['employers']:
            tax_sum += employer['salary_rub'] * current_tax / 100
            
        print(f"Отдел:{deparment_name} сумма налогов: {tax_sum}")
            
        


# Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.

def tax_per_year():
    for department in departments:
        deparment_name = department['title']
        current_tax = 0
        for tax in taxes:
            if tax['department'] is None or tax['department'].lower() == deparment_name.lower():
                current_tax += tax['value_percents']
        for employer in department['employers']:
            employer_name = f"{employer['first_name']} {employer['last_name']}"
            employer_salary = employer['salary_rub']
            tax_per_year = (employer_salary * current_tax / 100) * 12
            if tax_per_year > 100_000.0:
                print(f"""
За сотрудника {employer_name} 
Компания платит: {tax_per_year} в год.""")

# Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.

def min_tax_employer():
    min_tax_value = 999999999.0
    for department in departments:
        deparment_name = department['title']
        current_tax = 0
               
        for tax in taxes:
            if tax['department'] is None or tax['department'].lower() == deparment_name.lower():
                current_tax += tax['value_percents']
                
        for employer in department['employers']:
            employer_name = f"{employer['first_name']} {employer['last_name']}"
            employer_salary = employer['salary_rub']
            employer_tax = employer_salary * current_tax / 100
            
            if min_tax_value > employer_tax:
                min_tax_value = employer_tax
            else:
                continue
            print(f"Самый низкий налог в компании на сотрудника: {employer_name} - {min_tax_value} руб.")
        



if __name__ == '__main__':
    all_deparment()
    all_employers()
    name_and_departament()
    rich_bitch()
    low_salary()
    department_sum()
    departament_min_salary()
    departament_min_average_max_salary()
    average_salary()
    position_big_salary()
    female_average_salary()
    last_name_vowel()
    averege_department_taxes()
    salary_taxed_untaxed()
    tax_per_mounth()
    tax_per_year()
    min_tax_employer()