from passlib.hash import bcrypt_sha256

hash = bcrypt_sha256.hash("123")
print(f"Hash password: {hash}")
test = bcrypt_sha256.verify("123", hash)
print(f"Test 1: {test}")
test = bcrypt_sha256.verify("124", hash)
print(f"Test 2: {test}")