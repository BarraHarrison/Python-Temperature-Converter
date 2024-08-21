def celcius_to_kelvin(celcius):
    return celcius + 273.15

def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def celcius_to_rankine(celcius):
    return (celcius + 273.15) * 9/5

def celcius_to_reaumur(celcius):
    return celcius * 4/5

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

def rankine_to_celcius(rankine):
    return (rankine - 491.67) * 5/9

def reaumur_to_celcius(reaumur):
    return reaumur * 5/4

def temperature_converter():
    try:
        print("Choose the initial temperature unit:")
        print("1. Celcius (°C)")
        print("2. Fahrenheit (°F)")
        print("3. Kelvin (K)")
        print("4. Rankine (°R, °Ra)")
        print("5. Réaumur (°Ré, °Re)")
        
        initial_choice = input("Enter your choice (1/2/3/4/5): ")
        
        if initial_choice == '1':
            temp_in_celcius = float(input("Enter temperature in Celcius (°C): "))
        elif initial_choice == '2':
            temp_in_fahrenheit = float(input("Enter temperature in Fahrenheit (°F): "))
            temp_in_celcius = fahrenheit_to_celcius(temp_in_fahrenheit)
        elif initial_choice == '3':
            temp_in_kelvin = float(input("Enter temperature in Kelvin (K): "))
            temp_in_celcius = kelvin_to_celcius(temp_in_kelvin)
        elif initial_choice == '4':
            temp_in_rankine = float(input("Enter temperature in Rankine (°R): "))
            temp_in_celcius = rankine_to_celcius(temp_in_rankine)
        elif initial_choice == '5':
            temp_in_reaumur = float(input("Enter temperature in Réaumur (°Ré): "))
            temp_in_celcius = reaumur_to_celcius(temp_in_reaumur)
        else:
            print("Invalid choice. Please select a valid option.")
            return
        
        print("Choose the conversion unit:")
        print("1. Kelvin (K)")
        print("2. Fahrenheit (°F)")
        print("3. Rankine (°R, °Ra)")
        print("4. Réaumur (°Ré, °Re)")
        print("5. Celcius (°C)")
        
        conversion_choice = input("Enter your choice (1/2/3/4/5): ")
        
        if conversion_choice == '1':
            result = celcius_to_kelvin(temp_in_celcius)
            print(f"The temperature is equal to {result} K")
        elif conversion_choice == '2':
            result = celcius_to_fahrenheit(temp_in_celcius)
            print(f"The temperature is equal to {result} °F")
        elif conversion_choice == '3':
            result = celcius_to_rankine(temp_in_celcius)
            print(f"The temperature is equal to {result} °R")
        elif conversion_choice == '4':
            result = celcius_to_reaumur(temp_in_celcius)
            print(f"The temperature is equal to {result} °Ré")
        elif conversion_choice == '5':
            print(f"The temperature is equal to {temp_in_celcius} °C")
        else:
            print("Invalid choice. Please select a valid option.")
    
    except ValueError:
        print("Please enter a valid numerical temperature.")

# Run the temperature converter
temperature_converter()
