import hashlib

secret_key = "yzbqklnj"

part1 = 0

while True:
    encode_sk = f'{secret_key}{part1}'.encode("utf-8")
    hash_sk = hashlib.md5(encode_sk)
    hex_sk = hash_sk.hexdigest()

    if hex_sk[0:5] == "00000":
        print("Answer for Part 1:", part1)
        break
    
    part1 += 1
