from utils import password_utils, jwt_utils

# result = password_utils.hash('maman')
# result2 = password_utils.hash('maman')

# print(result)
# print(result2)

# print(password_utils.verify_password('test', result)) 
# print(password_utils.verify_password('maman', result)) 

token = jwt_utils.create_token(42, "Admin")
print(token)
