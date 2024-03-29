import hashlib

hashed_password = "bb3d5f7c75e608f1eae62935ac104023"

def check_password():
    for year in range(1900, 2023):
        password = f"{year}_football"
        hashed = hashlib.md5(password.encode()).hexdigest()
        if hashed == hashed_password:
            return password

password = check_password()

print("Flag:", "CSCTF{" + password + "}")