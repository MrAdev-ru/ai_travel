from decouple import config

print("DB_NAME =", repr(config("DB_NAME")))
print("DB_USER =", repr(config("DB_USER")))
print("DB_PASSWORD =", repr(config("DB_PASSWORD")))
print("DB_HOST =", repr(config("DB_HOST")))
print("DB_PORT =", repr(config("DB_PORT")))