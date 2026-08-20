# Task: Clean and validate user data.
# - Reject missing/invalid name, age, or email.
# - Clean valid names and emails.
# - Separate clean and rejected records.
# - Email format validation is intentionally left for the next exercise.

users = [
    {"name": " Arun ", "age": 22, "email": "ARUN@GMAIL.COM"},
    {"name": "meera", "age": 25, "email": "meera@gmail.com"},
    {"name": " Rahul ", "age": None, "email": "rahul@gmail.com"},
    {"name": "Vishnu", "age": 24, "email": None},
    {"name": "  ", "age": 20, "email": "test@gmail.com"},
    {"name": "John", "age": -5, "email": "john@gmail.com"},
    {"name": "Sara", "age": "twenty", "email": "sara@gmail.com"},
]

def clean_users(users):
    if not users:
        return None

    clean_data = []
    rejected_data = [] 
    for user in users:
        age = user.get('age')
        name = user.get('name')
        email = user.get('email')
        clean_user = {}
        if name is None or age is None or email is None or not name.strip() or not email.strip() or type(age) is not int or age <=0:
            rejected_data.append(user)
            continue
        clean_user["name"] = name.strip().capitalize()
        clean_user["age"] = age
        clean_user["email"] = email.strip().lower()
        clean_data.append(clean_user)
    return { "clean_data" : clean_data,
             "rejected_data" : rejected_data}

clean = clean_users(users)
if clean is None:
    print("Given invalid data")
else:
    print(f"Clean data : {clean['clean_data']}")
    if not clean['clean_data']:
        print("your full data is messy")
        print(f"Messy data : {clean['rejected_data']}")
    elif not clean['rejected_data']:
        print("No messy data")
    else:
        print(f"Messy data : {clean['rejected_data']}")