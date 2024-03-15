user_string = input("Please enter a string: ")

if len(user_string) < 10:
    print("String not long enough")
elif len(user_string) > 10:
    print("String too long")
else:
    print("Perfect string")

    print(f"First character: {user_string[0]}")
    print(f"Last character: {user_string[-1]}")
        
    for i in range(1, len(user_string)+1):
        print(user_string[0:i])

    import random
    user_string_list = list(user_string)
    random.shuffle(user_string_list)
    jumbled_string = ''.join(user_string_list)
    print(f"Jumbled string: {jumbled_string}")
