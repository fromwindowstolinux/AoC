import functools

wires = []

with open("1507input.txt") as file:
    for line in file:
        rep = line.replace("->","")
        str = rep.strip()
        words = str.split()

        wire = None

        for bitwise in ["AND","OR","RSHIFT","LSHIFT"]:
            if bitwise in line:
                input1, operation, input2, output = words
                wire = {
                    "input": [input1, input2],
                    "operation": operation,
                    "output": output
                }
                wires.append(wire)
                break

        if wire is not None:
            continue

        if "NOT" in line:
            operation, input1, output = words
            wire = {
                "input": [input1],
                "operation": operation,
                "output": output
            }
            wires.append(wire)
            continue

        input1, output = words
        wire = {
            "input": [input1],
            "operation": None,
            "output": output
        }
        wires.append(wire)


for wire in wires:
    inputs = []
    for number in wire["input"]:
        try:
            number = int(number)
        except ValueError:
            pass
        inputs.append(number)
    wire["input"] = inputs


index = {}
for wire in wires:
    index[wire["output"]] = wire

@functools.cache
def result(signal):
    if type(signal) == int:
        return signal

    wire = index[signal]
    if wire["operation"] == "AND":
        res = result(wire["input"][0]) & result(wire["input"][1])
    elif wire["operation"] == "OR":
        res = result(wire["input"][0]) | result(wire["input"][1])
    elif wire["operation"] == "RSHIFT":
        res = result(wire["input"][0]) >> result(wire["input"][1])
    elif wire["operation"] == "LSHIFT":
        res = result(wire["input"][0]) << result(wire["input"][1])
    elif  wire["operation"] == "NOT":
        res = ~ result(wire["input"][0])
    else:
        res = result(wire["input"][0])

    return res

print(result("a"))
