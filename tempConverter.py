class InvalidUnitException(Exception):
    '''raised when unit is not C nor F'''

def celsius_to_fahrenheit(celsius:float) -> float:
    fahrenheit:float = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit:float) -> float:
    celsius:float = (fahrenheit - 32) * 5/9
    return celsius

def main():

    temp = input("Enter a temperature and its unit (e.g., \"25 C\" or \"77 F\"): ")
    temp, unit = temp.split(" ")



    # Validation:
    if unit.upper() != "F" and unit.upper() != "C":
        raise InvalidUnitException("Unit should be either C or F.")

    # Converting:
    if unit.upper() == "C":
        print(f"{celsius_to_fahrenheit(float(temp))} F")
    if unit.upper() == "F":
        print(f"{fahrenheit_to_celsius(float(temp))} C")

while True:
    try:
        
        main()
        break
    except InvalidUnitException as e:
        print(e)
        continue
    except ValueError:
        print("Temperature should be a valid number.")
        continue
    except IndexError:
        print("Please enter a unit.")
        continue