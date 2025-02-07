import random

names_string = input("Give me everybody's names, separated by a comma. ").split(", ")

number_of_people = len(names_string)
random_choice = random.randint(0, number_of_people - 1)
person_to_pay_bill = names_string[random_choice]

print(person_to_pay_bill + " is going to pay the bill")

