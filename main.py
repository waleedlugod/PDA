def is_balanced(input):
    output = open("output.txt", "a")

    finals = "q2"
    transitions = {
        # (current state, current symbol, top of stack)
        # !
        ("q0", "!", "Z"): ["q1", "Z", "!"],
        ("q1", "!", "!"): ["q2"],
        # <
        ("q1", "<", "!"): ["q1", "!", "<"],
        ("q1", "<", "<"): ["q1", "<", "<"],
        ("q1", "<", ">"): ["q1", ">", "<"],
        ("q1", "<", "("): ["q1", "(", "<"],
        ("q1", "<", ")"): ["q1", ")", "<"],
        ("q1", "<", "["): ["q1", "[", "<"],
        ("q1", "<", "]"): ["q1", "]", "<"],
        ("q1", "<", "{"): ["q1", "{", "<"],
        ("q1", "<", "}"): ["q1", "}", "<"],
        # (
        ("q1", "(", "!"): ["q1", "!", "("],
        ("q1", "(", "<"): ["q1", "<", "("],
        ("q1", "(", ">"): ["q1", ">", "("],
        ("q1", "(", "("): ["q1", "(", "("],
        ("q1", "(", ")"): ["q1", ")", "("],
        ("q1", "(", "["): ["q1", "[", "("],
        ("q1", "(", "]"): ["q1", "]", "("],
        ("q1", "(", "{"): ["q1", "{", "("],
        ("q1", "(", "}"): ["q1", "}", "("],
        # [
        ("q1", "[", "!"): ["q1", "!", "["],
        ("q1", "[", "<"): ["q1", "<", "["],
        ("q1", "[", ">"): ["q1", ">", "["],
        ("q1", "[", "("): ["q1", "(", "["],
        ("q1", "[", ")"): ["q1", ")", "["],
        ("q1", "[", "["): ["q1", "[", "["],
        ("q1", "[", "]"): ["q1", "]", "["],
        ("q1", "[", "{"): ["q1", "{", "["],
        ("q1", "[", "}"): ["q1", "}", "["],
        # {
        ("q1", "{", "!"): ["q1", "!", "{"],
        ("q1", "{", "<"): ["q1", "<", "{"],
        ("q1", "{", ">"): ["q1", ">", "{"],
        ("q1", "{", "("): ["q1", "(", "{"],
        ("q1", "{", ")"): ["q1", ")", "{"],
        ("q1", "{", "["): ["q1", "[", "{"],
        ("q1", "{", "]"): ["q1", "]", "{"],
        ("q1", "{", "{"): ["q1", "{", "{"],
        ("q1", "{", "}"): ["q1", "}", "{"],
        # >)]}
        ("q1", ">", "<"): ["q1"],
        ("q1", ")", "("): ["q1"],
        ("q1", "]", "["): ["q1"],
        ("q1", "}", "{"): ["q1"],
        # x
        ("q1", "x", "!"): ["q1", "!"],
        ("q1", "x", "<"): ["q1", "<"],
        ("q1", "x", ">"): ["q1", ">"],
        ("q1", "x", "("): ["q1", "("],
        ("q1", "x", ")"): ["q1", ")"],
        ("q1", "x", "["): ["q1", "["],
        ("q1", "x", "]"): ["q1", "]"],
        ("q1", "x", "{"): ["q1", "{"],
        ("q1", "x", "}"): ["q1", "}"],
    }

    output.write(f"Processing {input}\n")

    input += "E"

    stack = ["Z"]
    curr_state = "q0"
    i = 0
    while True:
        if i == len(input) - 1:
            output.write(
                f"ID: ({curr_state}, {input[i:]}, {''.join(list(reversed(stack)))})\n"
            )
        else:
            output.write(
                f"ID: ({curr_state}, {input[i:-1]}, {''.join(list(reversed(stack)))})\n"
            )
        symbol = input[i]
        top = stack.pop()

        key = (curr_state, symbol, top)
        if curr_state == finals:
            output.write("q2 is a final state.\n")
            output.write(f"{input[:-1]} is valid and has balanced brackets.\n\n")
            return True
        elif key in transitions:
            transition = transitions[key]
            curr_state = transition[0]
            stack.extend(transition[1:])
        else:
            if symbol == "E":
                output.write(f"Invalid string. {curr_state} is not a final state.\n\n")
            else:
                output.write(f"Invalid string. Failed at position {i+1}.\n")
                output.write(f"Remaining unprocessed input string: {input[i:-1]}\n\n")
            return False

        i += 1


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
    return len(input) - 2


def main1():
    input = open("input.txt")
    answers = []
    for i in input:
        answers.append([i.strip(), is_balanced(i.strip())])
    return answers


def main2(input):
    output = open("output.txt", "a")
    for i in input:
        if i[1]:
            output.write(f"{i[0]} - Resulting number of x's: {evaluate(i[0])}\n")
        else:
            output.write(f"{i[0]} - Invalid string.\n")


if __name__ == "__main__":
    open("output.txt", "w").close()
    ans = main1()
    main2(ans)
