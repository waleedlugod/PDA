# ALPHABET: !<>()[]{}x


def is_balanced(input, write_to_output):
    output = open("output.txt", "a")
    if write_to_output:
        output.write(f"Processing {input}\n")

    state = "q0"
    stack = ["Z"]
    error = False

    input += "E"
    # change to while true and more verbose
    for i in range(len(input)):
        if write_to_output:
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
            if write_to_output:
                output.write("q2 is a final state.\n")
                output.write(f"{input[:-1]} is valid and has balanced brackets.\n\n")
            return True

        if error:
            if write_to_output:
                output.write(f"Invalid string. Failed at position {i+1}.\n")
                output.write(f"Remaining unprocessed input string: {input[i:-1]}\n\n")
            return False
    if write_to_output:
        output.write(f"Invalid string. {state} is not a final state.\n\n")
    return False


def evaluate(input):
    stack = []
    i = 0
    while True:
        new_string = input
        c = input[i]
        if c == "!" and i > 0:
            break
        elif c == "<" or c == "(" or c == "[" or c == "{":
            stack.append([c, i])
            i += 1
        elif c == ">" and stack[-1][0] == "<":
            top = stack.pop()
            content = input[top[1] + 1 : i]
            new_string = input[: top[1]] + content * 2 + input[i + 1 :]
            i += len(content) - 2
        elif c == ")" and stack[-1][0] == "(":
            top = stack.pop()
            content = input[top[1] + 2 : i]
            new_string = input[: top[1]] + content + input[i + 1 :]
            i -= 1 + len(content)
        elif c == "]" and stack[-1][0] == "[":
            top = stack.pop()
            content = input[top[1] + 1 : i]
            new_string = input[: top[1]] + input[i + 1 :]
            i -= len(content) + 1
        elif c == "}" and stack[-1][0] == "{":
            top = stack.pop()
            content = input[top[1] + 1 : i] + "x"
            new_string = input[: top[1]] + content + input[i + 1 :]
        else:
            i += 1
        input = new_string
        print(input)
    return len(input) - 2


def main1():
    input = open("input.txt")
    for i in input:
        is_balanced(i.strip(), True)


def main2():
    input = open("input.txt")
    for i in input:
        if is_balanced(i.strip(), False):
            evaluate(i.strip())


if __name__ == "__main__":
    open("output.txt", "w").close()
    main1()
    main2()
