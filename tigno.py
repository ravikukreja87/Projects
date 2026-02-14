import math


degrees = float(input("Enter the angle in degrees: "))
x = math.radians(degrees)

# Please Enter only in float Eg.(55.0,7.23)

sine_val = 0
cosine_val = 0

for n in range(10):
    
    sine_val += ((-1)**n * (x**(2*n + 1))) / math.factorial(2*n + 1)
    
    
    cosine_val += ((-1)**n * (x**(2*n))) / math.factorial(2*n)


if abs(cosine_val) < 1e-10:
    tangent_val = "Undefined"
else:
    tangent_val = round(sine_val / cosine_val, 4)

print(f"--- Results for {degrees}° ---")
print(f"Sine:    {round(sine_val, 4)}")
print(f"Cosine:  {round(cosine_val, 4)}")
print(f"Tangent: {tangent_val}")