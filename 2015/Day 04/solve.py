import hashlib

SECRET_KEY = "ckczppom"


def get_md5hash(key, zero_length):
    conta = 0
    while True:
        conta += 1
        md5hash = hashlib.new("md5", bytes(key + str(conta), 'utf-8'))
        md5hash_hex = md5hash.hexdigest()

        if md5hash_hex[:zero_length] == (zero_length * "0"):
            return conta


if __name__ == "__main__":
    print(f"The lowest number (five zeros) is {get_md5hash(SECRET_KEY, 5)}")
    print(f"The lowest number (six zeros) is {get_md5hash(SECRET_KEY, 6)}")
