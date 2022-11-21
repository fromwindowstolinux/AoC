import hashlib

def AdventCoins(part1=False):

    answer = 0

    while True:

        encode_sk = f'{secret_key}{answer}'.encode("utf-8")
        hash_sk = hashlib.md5(encode_sk)
        hex_sk = hash_sk.hexdigest()

        if part1:
            if hex_sk[0:5] == "00000":
                return answer
            
        else:
            if hex_sk[0:6] == "000000":
                return answer

        answer += 1


if __name__ == "__main__":

    with open('1504input.txt') as file:

        secret_key = file.read()
        
        print("Answer for Part 1:", AdventCoins(part1=True))
        print("Answer for Part 2:", AdventCoins())
