import sys





def sum_digits_text(text: str) -> int:



    return sum(ord(ch) - 48 for ch in text)





def nine_degree(num: str) -> int:



    current = sum_digits_text(num)

    if current % 9 != 0:

        return 0





    degree = 1

    while current != 9:



        current = sum_digits_text(str(current))

        degree += 1



    return degree





def solve(data: str) -> str:

    ans = []

    for num in data.split():



        if num == "0":

            break



        degree = nine_degree(num)

        if degree == 0:

            ans.append(f"{num} is not a multiple of 9.")

        else:

            ans.append(f"{num} is a multiple of 9 and has 9-degree {degree}.")



    return "\n".join(ans)





def main() -> None:



    sys.stdout.write(solve(sys.stdin.read()))





if __name__ == "__main__":

    main()
