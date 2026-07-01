# print("shivam")
# print("satyam")
# if False:
#     print("shlknsdf")
# print(8 > 6)
# print(82)

# age = 18

# if (age >= 18):
#     print("Adult")
# else:
#     print("Not Adult")

# print(4%2)
# num = 4

# if num % 2 == 0:
#     print("Even")
# else:
#     print("odd")

# if False:
#     print("not Worked")
# elif True:
#     print("This worked")
# else:
#     print("Print this worked")

# day = int(input("Enter a Day:"))

# if day == 1:
#     print("monday")
# elif day == 2:
#     print("tuesday")
# elif day == 3:
#     print("wednesday")
# else:
#     print("Invalid Number")

#english = 50 pass=20, maths = 50 pass=20, science=50 pass=20 total=150 60
english = 24
maths = 16
science = 26
total = english + maths + science
#print((total > 60) and (english > 20) and (maths > 20) and (science > 20))
#        true      and   true         and   false     and   true
#                  true               and   false
#                                    false
# if total >= 60:
#     if ((english >= 20) and (maths >= 20) and (science >= 20)):
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("fail")


#Leap year 
#leap year divible by 4%leap == 0 and also divible by 100
# divisible by leap%4==0 else Not
# divisible by leap%100==0 
# 

leapYear = 2024

if (leapYear%4==0):
    if(leapYear%100==0):
        if(leapYear%400==0):
            print("divisible by 4, 100, 400, hence leap year", leapYear)
        else:
            print("divisible by 4 and 100 but not 400, hence not leap year", leapYear)
    else:
        print("divisible by 4 but not 100, hence leap year", leapYear)
else:
    print("Not divisible by 4, hence not leap year", leapYear)