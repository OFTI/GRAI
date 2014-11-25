def open_file(file_name):
    file_object = open(file_name, 'r')
    return file_object



def water_calculator(weight, activity_leveler, size):
    ounces = ((weight * (2/3))+((activity_leveler/30)*12))
    total_ounces = ounces*size
    return total_ounces
 
 
def calorie_calculator(age, sex, activity_level, size):
    if age > 3:
            if 3 < age < 8:
                if sex == 'M':
                        print ('M')
                        print ("child")
                        if activity_level == 'sedentary':
                            calories = size*1400
                        elif activity_level == 'moderate':
                             calories = size * 1500
                        elif activity_level == 'active':
                            calories = size * 1800

                elif sex == 'F':
                        print ('F')
                        print ('child')
                        if activity_level == 'sedentary':
                            calories = size * 1400
                        elif activity_level == 'moderate':
                            calories = size * 1500
                        elif activity_level == 'active':
                            calories = size * 1600

            elif 8 < age < 13:
                if sex == 'M':
                        print ('M')
                        print ("big kid")
                        if activity_level == 'sedentary':
                            calories = size * 1800
                        elif activity_level == 'moderate':
                            calories = size * 2000
                        elif activity_level == 'active':
                            calories = size * 2300

                elif sex == 'F':
                        print ('F')
                        print ('big kid')
                        if activity_level == 'sedentary':
                            calories = size * 1600
                        elif activity_level == 'moderate':
                            calories = size * 1800
                        elif activity_level == 'active':
                            calories = size * 2000

            elif 13 < age < 18:
                if sex == 'M':
                        print ('M')
                        print('teen')
                        if activity_level == 'sedentary':
                            calories = size * 2200
                        elif activity_level == 'moderate':
                            calories = size * 2600
                        elif activity_level == 'active':
                            calories = size * 3000

                elif sex == ('F'):
                        print ('F')
                        print ('teen')
                        if activity_level == 'sedentary':
                            calories = size * 1800
                        elif activity_level == 'moderate':
                            calories = size * 2000
                        elif activity_level == 'active':
                            calories = size * 2400

            elif 18 < age < 30:
                if sex == 'M':
                        print ('M')
                        print ('young adult')
                        if activity_level == 'sedentary':
                            calories = size * 2400
                        elif activity_level == 'moderate':
                            calories = size * 2700
                        elif activity_level == 'active':
                            calories = size * 3000

                elif sex == 'F':
                        print ('F')
                        print ('young adult')
                        if activity_level == 'sedentary':
                            calories = size * 2000
                        elif activity_level == 'moderate':
                            calories = size * 2100
                        elif activity_level == 'active':
                            calories = size * 2400

            elif 30 < age < 50:
                if sex == 'M':
                        print ('M')
                        print ('middle aged')
                        if activity_level == 'sedentary':
                            calories = size * 2200
                        elif activity_level == 'moderate':
                            calories = size * 2500
                        elif activity_level == 'active':
                            calories = size * 2900

                elif sex == 'F':
                        print ('F')
                        print ('middle aged')
                        if activity_level == 'sedentary':
                            calories = size * 1800
                        elif activity_level == 'moderate':
                            calories = size * 2000
                        elif activity_level == 'active':
                            calories = size * 2200

            elif 50 < age < 150:
                if sex == 'M':
                        print ('M')
                        print ('old')
                        if activity_level == 'sedentary':
                            calories = size * 2000
                        elif activity_level == 'moderate':
                            calories = size * 2300
                        elif activity_level == 'active':
                            calories = size * 2600

                        
                elif sex == 'F':
                        print ('F')
                        print ('old')
                        if activity_level == 'sedentary':
                            calories = size * 1600
                        elif activity_level == 'moderate':
                            calories = size * 1800
                        elif activity_level == 'active':
                            calories = size * 2100

    else:
        print ("baby")
        if activity_level == 'sedentary':
            calories = size * 1000
        elif activity_level == 'moderate':
            calories = size * 1200
        elif activity_level == 'active':
            calories = size * 1400

    return calories

def main():
    continuity = input ("Press enter to continue: ")
    while not continuity:
        sex = input("Enter sex, M or F:")
        age = int(input("Enter age:"))
        weight = int(input("Please enter your weight:"))
        activity_level = input("Enter activity level (sedentary, moderate, or active:)")
        activity_leveler = int(input("Please enter how many minutes a day you work out:"))
        size = int(input("Enter size of population:"))
        water = water_calculator(weight, activity_leveler, size)
        food = calorie_calculator(age, sex, activity_level, size)
        print ("{} ounces of water and {} calories".format(str(water), food))
        continuity = input ("Press enter to continue: ")
        


main()
