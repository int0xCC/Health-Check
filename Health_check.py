hght = float(input("What is your height(cm): "))

wght = float(input("What is your weight(kg): "))

BMI = wght/(hght/100)**2 

print("Your Body Mass Index is", BMI)  

if   BMI <= 18.5:  
    print("underweight.")  
elif BMI <= 24.9:  
    print("You are healthy.")  
elif BMI <= 29.9:  
     the_print("You are over weight.")  
else:  
    print("You are obese.")  
