import unittest

def first_occurance(s1, s2):
    if len(s1) < len(s2) or len(s2) == 0:
        return (-1, 0)
    it = 0
    for i in range(len(s1)):
        it += 1
        if s1[i] == s2[0]:
            if s1[i:i+len(s2)] == s2:
                return (i, it)
    return (-1, it)

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
    (('AHVAS' * 1000000) + ('AHSD' * 5000000) + 'BCD' + ('A' * 200), 'BCD')
]

for test_case in test_cases:
    a, b = test_case
    result, iterations = first_occurance(a, b)
    print(f"resultado: {result}, iterações: {iterations}, instruções: {iterations}")

# No pior caso a compexidade será igual à O(s1)
# Instruções para contabilizar o número de iterações foram desconsideradas, 
# logo, a única instrução é a atribuição do 'i' no for