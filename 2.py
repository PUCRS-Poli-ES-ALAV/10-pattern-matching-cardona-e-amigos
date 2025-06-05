R = 26
Q = 2_147_483_647

def search(text: str, pattern: str):
    instructions = 0
    it = 0

    instructions += 2
    M = len(pattern)
    N = len(text)
    instructions += 3
    pattern_hash, it_hash, ins_hash = hash(pattern, M)
    it += it_hash
    instructions += ins_hash
    instructions += 1
    for i in range(N - M):
        instructions += 1
        it += 1
        text_hash, it_hash_2, ins_hash_2 = hash(text[i:i+M], M)
        it += it_hash_2
        instructions += ins_hash_2
        instructions += 1
        if pattern_hash == text_hash:
            instructions += 1
            return i, it, instructions
    instructions += 1
    return N, it, instructions

def hash(s: str, M: int):
    global R, Q
    instructions = 0
    it = 0
    instructions += 1
    h = 0
    for j in range(M):
        it += 1
        instructions += 5
        h = (h * R + ord(s[j])) % Q
    instructions += 1
    return h, it, instructions

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
    result, iterations, instructions = search(a, b)
    print(f"resultado: {result}, iterações: {iterations}, instruções: {instructions}")

# 3.2: O(N*M)