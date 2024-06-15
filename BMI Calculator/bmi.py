def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert height to meters
    try:
        bmi = weight / (height_m ** 2)
        return bmi
    except ZeroDivisionError:
        return None

def get_bmi_category(bmi):
    if bmi is None:
        return "Invalid height provided."
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator")
    
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height_cm = float(input("Enter your height in centimeters: "))
        
        bmi = calculate_bmi(weight, height_cm)
        if bmi is not None:
            print(f"Your BMI is: {bmi:.2f}")
        else:
            print("Error in calculating BMI due to invalid height.")
        
        category = get_bmi_category(bmi)
        print(f"BMI Category: {category}")
    
    except ValueError:
        print("Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    main()
