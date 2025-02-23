from aocd import data

def parse_input(input_text):
    sections = input_text.strip().split('\n\n')
    initial_values = {}
    gates = []
    
    for line in sections[0].split('\n'):
        wire, value = line.split(': ')
        initial_values[wire] = int(value)
    
    for line in sections[1].split('\n'):
        if line.strip():
            gates.append(line.strip())
            
    return initial_values, gates

def simulate_circuit(initial_values, gates):
    wires = initial_values.copy()
    made_progress = True
    while made_progress:
        made_progress = False
        
        for gate in gates:
            inputs, output = gate.split(' -> ')
            if output in wires:
                continue  # Skip if output wire already has a value
                
            if ' AND ' in inputs:
                in1, in2 = inputs.split(' AND ')
                if in1 in wires and in2 in wires:
                    wires[output] = 1 if wires[in1] and wires[in2] else 0
                    made_progress = True
            elif ' OR ' in inputs:
                in1, in2 = inputs.split(' OR ')
                if in1 in wires and in2 in wires:
                    wires[output] = 1 if wires[in1] or wires[in2] else 0
                    made_progress = True
            elif ' XOR ' in inputs:
                in1, in2 = inputs.split(' XOR ')
                if in1 in wires and in2 in wires:
                    wires[output] = 1 if wires[in1] != wires[in2] else 0
                    made_progress = True
    
    return wires

def calculate_result(wires):
    z_wires = sorted([wire for wire in wires.keys() if wire.startswith('z')], 
                    key=lambda x: int(x[1:]), reverse=True)
    binary = ''.join(str(wires[wire]) for wire in z_wires)
    print(f"Binary number: {binary}")
    return int(binary, 2)


initial_values, gates = parse_input(data)
wires = simulate_circuit(initial_values, gates)
result = calculate_result(wires)

print(f"\nThe decimal number output is: {result}")
