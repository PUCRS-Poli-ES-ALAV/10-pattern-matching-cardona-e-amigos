def search(text: str, pattern: str):
    d = 256
    q = 101

    M = len(pattern)
    N = len(text)

    p = 0
    t = 0 
    h = 1  

    ans: list[int] = [] 

    for _ in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(N - M + 1):
        if p == t:
            match = True
            for j in range(M):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                ans.append(i + 1)

        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t += q

    return ans


if __name__ == "__main__":
    # Exemplo de uso
    text = "birthboybirth"
    pattern = "birth"
    res = search(text, pattern)
    for index in res:
        print(index, end=" ")
    print()