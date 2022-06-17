# Import bcrypt:
import bcrypt

password = "mypasswordstring"  # type string
print(password, type(password))

# Encode password into a readable utf-8 byte code:
password = password.encode('utf-8')  # type bytes
print(password, type(password))

# Hash the ecoded password and generate a salt:
hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())  # type bytes
print(hashedPassword, type(hashedPassword))


# Check provided password

provided_password = input("check password: ")
print(type(provided_password))

# Encode the authenticating password as well:
provided_password_encoded = provided_password.encode('utf-8')

# Use conditions to compare the authenticating password with the stored one:
if bcrypt.checkpw(provided_password_encoded, hashedPassword):
    print("login success")
else:
    print("incorrect password")


# Python bcrypt cost factor
# The cost factor increases security by slowing down the hashing.
salt = bcrypt.gensalt(rounds=16)


# function to hash
def hash_password(password: str) -> bytes:
    """This function creates an encrypted
    version of a password with bcrypt 

    Args:
        password (str): Original password

    Returns:
        bytes: Encrypted password
    """
    password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashedPassword = bcrypt.hashpw(password, salt)
