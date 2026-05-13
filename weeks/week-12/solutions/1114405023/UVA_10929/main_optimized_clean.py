import sys





def is_multiple_of_11(num: str) -> bool:



    diff = 0

    sign = 1

    for ch in num:



        diff += sign * (ord(ch) - 48)

        sign = -sign



    return diff % 11 == 0





def solve(data: str) -> str:

    ans = []

    for num in data.split():



        if num == "0":

            break





        word = "" if is_multiple_of_11(num) else " not"

        ans.append(f"{num} is{word} a multiple of 11.")



    return "\n".join(ans)





def main() -> None:



    sys.stdout.write(solve(sys.stdin.read()))





if __name__ == "__main__":

    main()
