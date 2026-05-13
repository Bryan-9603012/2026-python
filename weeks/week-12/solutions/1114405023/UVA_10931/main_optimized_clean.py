import sys





def to_binary_and_count_ones(n: int):



    bits = []

    ones = 0



    while n > 0:



        bit = n & 1

        if bit:

            ones += 1

        bits.append(str(bit))





        n >>= 1





    return "".join(reversed(bits)), ones





def solve(data: str) -> str:

    ans = []

    for token in data.split():

        n = int(token)



        if n == 0:

            break



        binary, ones = to_binary_and_count_ones(n)

        ans.append(f"The parity of {binary} is {ones} (mod 2).")



    return "\n".join(ans)





def main() -> None:



    sys.stdout.write(solve(sys.stdin.read()))





if __name__ == "__main__":

    main()
