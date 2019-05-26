def and_gate(x1, x2):
  w1, w2 = 0.5, 0.5
  if x1*w1 + x2*w2 >= 1:
    return 1
  else:
    return 0

def or_gate(x1, x2):
  w1, w2 = 0.5, 0.5
  b      = 0.5
  if x1*w1 + x2*w2 + b >= 1:
    return 1
  else:
    return 0

def nand_gate(x1, x2):
  w1, w2 = 0.5, 0.5
  if x1*w1 + x2*w2 >= 1:
    return 0
  else:
    return 1

def xor_gate(x1, x2):
  return and_gate(nand_gate(x1, x2), or_gate(x1, x2))

print("AND")
print("0 0 : ", and_gate(0, 0))
print("0 1 : ", and_gate(0, 1))
print("1 0 : ", and_gate(1, 0))
print("1 1 : ", and_gate(1, 1))

print("OR")
print("0 0 : ", or_gate(0, 0))
print("0 1 : ", or_gate(0, 1))
print("1 0 : ", or_gate(1, 0))
print("1 1 : ", or_gate(1, 1))

print("XOR")
print("0 0 : ", xor_gate(0, 0))
print("0 1 : ", xor_gate(0, 1))
print("1 0 : ", xor_gate(1, 0))
print("1 1 : ", xor_gate(1, 1))
