import math, random, string


count = 0
while count <= 3:
    print(count)
    count = count + 1 
else:
    print('this is the end of the loop')

print('kennedy')

raw_input= input('please enter a string: ')
if len(raw_input) < 6:
    print('good one')
    
raw_input= int(input('please enter an integer: '))

if raw_input < 6:
    print('good one')
else:
    print('your number should be less than 6')

contact_info = {
    'name_of_person': 'ivara divine',
    'tel': int('09169762709'), 
    'email':  'divineivara@gmail.com'  
}

def about_me() :
    if contact_info['name_of_person'] == 'ivara divine':
        salary = int(input('input your salary ')),
        tithe =  salary / 10
        return tithe
    else: 
        pass

about_me()   
math.pi

#2nd assignment
def area_of_circle(r):
    pi * r * r
    
    
    
def fahrenheit_to_celcius(fahrenheit):
    return celcius

fahrenheit = float(input("Enter the temperature in fahrenheit: "))
celcius = 5 / 9 * (fahrenheit - 32)

print(f"The fahrenheit of {fahrenheit} equals {celcius} celcius: ")

#3rd assignment
def user_id_gen_by_user():
    num_characters = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of IDs to generate: "))
    
    characters = string.ascii_letters + string.digits
    
    for _ in range(num_ids):
        user_id = ''.join(random.choice(characters) for _ in range(num_characters))
        print(user_id)

# Example usage:
user_id_gen_by_user()


