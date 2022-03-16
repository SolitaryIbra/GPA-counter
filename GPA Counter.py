degree_ls, hours_ls = [],[]
def gpa_clac(degree):
    
    if degree >= 90:
        degree = 4
    elif degree >= 85:
        degree = 3.7
    elif degree >= 80:
        degree  = 3.3
    elif degree >= 75:
        degree = 3
    elif degree >= 70:
        degree = 2.7
    elif degree >= 65:
        degree = 2.4
    elif degree >= 60:
        degree = 2.2
    elif degree >= 50:
        degree = 2
    else:
        degree = 0
    return degree

while True:
    try:
        x = input("Enter course Name: ")
        y = int(input("Enter Degree: "))
        z = int(input("Enter Hour: "))
        print("if finished, press letter.")
        degree_ls.append(gpa_clac(y)*z)
        hours_ls.append(z)
    except BaseException:
        break
        

try:
    print(sum(degree_ls)/sum(hours_ls))
except BaseException:
    pass