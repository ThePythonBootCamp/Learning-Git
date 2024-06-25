import random
import string

def character_generator(length):
    character = string.ascii_letters + string.digits
    user_id = "".join(random.choice(character)for _ in range(length))
    return user_id

def user_id_gen_by_user():
    character_num = int(input("Enter the number of characters for each user id: "))
    generated_id_number = int(input("Enter the number of ID's to be generated: "))

    user_ids = []
    for _ in range(generated_id_number):
        user_id = character_generator(character_num)
        user_ids.append(user_id)
    return user_ids

user_ids = user_id_gen_by_user()
print(user_ids)
for user_id in user_ids:
    print(user_id)

    
