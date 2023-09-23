from os import system
system('cls')
from math import tan, pi
zel=input('Enter zel: ')
Z=float(zel)
number_zel=input('Enter the nimber of zel: ')
num_z=int(number_zel)
#pi=float(22/7)
S_area=(num_z*(Z)**2)/(4*tan(pi/num_z))
print('S_area=', S_area)

# این کد مهم است وقتی میخواهی از توابع ریاضی استفاده
#  کنی باید کتابخانه مث را فراخوانی کنی 
# مثلا اینجا عدد پی و تابع تانژانت فراخوانی شدند