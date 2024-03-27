# Mi código
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

def days_in_month(in_year, in_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

    # guardamos el valor de salida de la función is_leap()
    is_leap_year = is_leap(in_year)

    # si is_leap_year es True, entonces el año es bisisteso y el mes '2' tendrá 28 + 1 dias
    if is_leap_year:
        if in_month == 2:
            return month_days[1] + 1
    else:
        # si el año no es bisiesto simplemente obtenemos el número de dias a partir del arreglo month_days, pero debemos restar -1 al mes ingresado pues el en arreglo partimos contando los meses desde 0
        return month_days[in_month - 1]
    
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# Respuesta
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

def days_in_month(year, month):
    # if month > 12 or month < 1:
    #     return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]
    
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)








