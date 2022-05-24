task 0.8

def num_to_hrs_mins(num):
    hrs = 0
    min = 0
    if num >= 60:
        hrs = num // 60
        min = num % 60
        if hrs <= 1 and min > 1:
            print(str(hrs) + " hour, " + str(min) + " minutes")   
        else:
            print(str(hrs) + " hours, " + str(min) + " minutes")           
    else: 
        hrs = 0
        min = num
        print(str(hrs) + " hour, " + str(min) + " minutes")
        
num_to_hrs_mins(71)
