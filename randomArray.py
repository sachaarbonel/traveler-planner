from random import uniform
random_number_controlled = uniform(20, 180)
rounded = round(random_number_controlled)   
print(rounded)
random_array = [int(round(uniform(20, 180))) for _ in range(364)]
print(random_array)
print(random_array[0])