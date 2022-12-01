import hashlib

def AdventCoins(secret_key):
    answer, part1 = 0, False
    while True:
        encode_sk = f'{secret_key}{answer}'.encode("utf-8")
        hash_sk = hashlib.md5(encode_sk)
        hex_sk = hash_sk.hexdigest()

        if hex_sk[0:5] == "00000" and not part1:
            yield ["Part 1", answer]
            part1 = True
        elif hex_sk[0:6] == "000000":
            yield ["Part 2", answer]
            return
        answer += 1

if __name__ == "__main__":
    with open('1504input.txt') as file:
        secret_key = file.read()
        for ans in AdventCoins(secret_key):
            print("Answer for", ans[0],":",ans[1])