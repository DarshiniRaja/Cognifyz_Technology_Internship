# Task 04 : Temperature Converter

def celsius_to_fahrenheit(celsius):
   return (celsius * 9/5 ) + 32
def fahrenheit_to_celsius(fahrenheit):
   return (fahrenheit - 32) * 5/9

def main():
   print("Temperature Converter!")
   temp = float(input("Enter temperature: "))
   print("\n Choose conversion:")
   print("1. Celsius to Farenheit")
   print("2. Fahrenheit to Celsius")
   choice = input("Your choice (1 or 2): ")
   if choice == "1":
      result = celsius_to_fahrenheit(temp)
      print(f"\n Result: {temp}°C = {round(result, 2)}°F")
   elif choice == "2":
      result = fahrenheit_to_celsius(temp)
      print(f"\n Result: {temp}°F = {round(result, 2)}°C")
   else:
      print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
   main()
      