def calculate_bmi(weight_kg, height_cm):
    """
    It calculates the Body Mass Index (BMI).
    BMI = weight (kg) / [height (m)]^2
    """
    height_m=height_cm/100
    if height_m <= 0 or weight_kg <= 0:
        return None
    bmi = weight_kg / (height_m ** 2)
    return bmi

def classify_bmi(bmi):
    """
    It classifies the BMI into standard categories based on
    World Health Organization (WHO) guidelines.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

def main():
    """
    Main function to run the BMI calculator CLI.
    """
    print("--- BMI Calculator ---")
    
    try:
        # Prompt for weight (kg)
        weight_input = input("Enter your weight in kilograms (kg): ")
        weight = float(weight_input)

        # Prompt for height (m)
        height_input = input("Enter your height in centimeters (cm): ")
        height = float(height_input)

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        if bmi is not None:
            # Classify and display results
            category = classify_bmi(bmi)
            print(f"\nYour BMI is: {bmi:.2f}")
            print(f"Category: {category}")
        else:
            print("Error: Weight and height must be positive values.")

    except ValueError:
        print("Error: Please enter valid numerical values for weight and height.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
