#creating a script that converts temperatures between Celsius and Fahrenheit, 
# using global variables to store conversion factors.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    print(f"{float(fahrenheit)}°F is {(fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR}°C")


def convert_to_fahrenheit(celsius):
    print(f"{float(celsius)}°C is { (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32}°F")

def main():
    temperture = int(input("Enter the temperature to convert: "))
    celcius_farenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    match celcius_farenheit:
        case "C":
            fahrenheit = temperture
            convert_to_fahrenheit(fahrenheit)
        case "F":
            celsius = temperture
            convert_to_celsius(celsius)
        case _:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
