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