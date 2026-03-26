# ALPHABET: !<>()[]{}x


def is_balanced(input):
    output = open("output.txt", "a")
    output.write(f"Processing {input}\n")

    state = "q0"
    stack = ["Z"]
    error = False

    input += "E"
    for i in range(len(input)):
        if i == len(input) - 1:
            output.write(
                f"ID: ({state}, {input[i:]}, {''.join(list(reversed(stack)))})\n"
            )
        else:
            output.write(
                f"ID: ({state}, {input[i:-1]}, {''.join(list(reversed(stack)))})\n"
            )

        symbol = input[i]
        if state == "q0":
            if symbol == "!" and stack[-1] == "Z":
                stack.append("!")
                state = "q1"
            else:
                error = True

        elif state == "q1":
            if symbol == "x" or symbol == "E":
                pass
            elif symbol == "<" or symbol == "(" or symbol == "[" or symbol == "{":
                stack.append(symbol)
            elif (
                (symbol == ">" and stack[-1] == "<")
                or (symbol == ")" and stack[-1] == "(")
                or (symbol == "]" and stack[-1] == "[")
                or (symbol == "}" and stack[-1] == "{")
            ):
                stack.pop()
            elif symbol == "!" and stack[-1] == "!":
                stack.pop()
                state = "q2"
            else:
                error = True

        elif state == "q2" and symbol == "E":
            output.write("q2 is a final state.\n")
            output.write(f"{input[:-1]} is valid and has balanced brackets.\n\n")
            return True

        if error:
            output.write(f"Invalid string. Failed at position {i+1}.\n")
            output.write(f"Remaining unprocessed input string: {input[i:-1]}\n\n")
            return False
    output.write(f"Invalid string. {state} is not a final state.\n\n")
    return False


def evaluate(input):
    pass


def main1():
    input = open("input.txt")
    for i in input:
        is_balanced(i.strip())


def main2():
    input = open("input.txt")
    for i in input:
        if is_balanced(i):
            evaluate(i)


if __name__ == "__main__":
    open("output.txt", "w").close()
    main1()
