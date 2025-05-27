import unittest

def first_occurance(s1, s2):
    instructions = 0
    instructions += 6
    if len(s1) < len(s2) or len(s2) == 0:
        instructions +=1
        return (-1, 0, instructions)
    it = 0
    for i in range(len(s1)):
        instructions += 1
        it += 1
        instructions += 3
        if s1[i] == s2[0]:
            instructions += 1
            match = True
            for j in range(len(s2)):
                it += 1
                instructions += 1
                instructions += 8
                if i + j >= len(s1) or s1[i + j] != s2[j]:
                    instructions += 1
                    match = False
                    break
            instructions += 1
            if match:
                instructions += 1
                return (i, it, instructions)
    instructions += 1
    return (-1, it, instructions)

test_cases = [
    (('ABC' * 1000) + 'DCD' + ('BDC' * 1000), 'DCD'),
    (('ABCDCBDCBDACBDABDCBADF' * 1000), 'ADF'),
    ('', 'A'),
    ('A', ''),
    ('A', 'A'),
    ('ABCD', 'BCD'),
    ('A' * 1000, 'A' * 999 + 'B'),
    ('A' * 1000, 'B' * 1000),
    (('AHF' * 1000) + ('AUA' * 500000) + 'BCD' + ('A' * 200), 'BCD'),
    (('AHVAS' * 1000000) + ('AHSD' * 5000000) + 'BCD' + ('A' * 200), 'BCD'),
    (('A' * 50000) + 'B', 'A' * 1000 + 'B')
]

for test_case in test_cases:
    a, b = test_case
    result, iterations, instructions = first_occurance(a, b)
    print(f"resultado: {result}, iterações: {iterations}, instruções: {instructions}")

# No pior caso a compexidade será igual à O(s1)
# Instruções para contabilizar o número de iterações foram desconsideradas, 
# logo, a única instrução é a atribuição do 'i' no for