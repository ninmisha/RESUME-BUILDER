import openpyxl
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "User Input Data"
sheet.append(["Name", "Age", "City"])
while True:
 name = input("Enter your name (type 'exit' to stop): ")
 if name.lower() == 'exit':
   break
 age = input("Enter your age: ")
 city = input("Enter your city: ")
 sheet.append([name, age, city])
filename = "user_input_data.xlsx"
workbook.save(filename)
print(f"Data saved to {filename}")