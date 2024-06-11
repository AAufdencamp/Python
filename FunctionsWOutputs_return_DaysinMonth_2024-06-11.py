#####Functions with Outputs (return)####
####Days in Month Exercise####

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇

####MY CODE START####

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) == False:
    return month_days[(month-1)]
  if is_leap(year) == True:
    if month == 2:
      return 29
    else:
      return month_days[(month-1)]

####MY CODE END####
  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

####Instructor Code####

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1] 

####End Instructor Code####