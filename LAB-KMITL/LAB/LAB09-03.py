def lcs(s1, s2):
    n = len(s1)

    # precompute positions ของแต่ละ char ใน s2
    pos = {}
    for j, c in enumerate(s2):
        pos.setdefault(c, []).append(j)

    prev_dp = {}  # {j: run_length} เก็บแค่ค่าที่ไม่ใช่ 0
    best_len = 0
    best_end = 0
    max_prev = 0

    for i in range(n):
        if n - i + max_prev <= best_len:
            break

        c = s1[i]
        curr_dp = {}
        max_curr = 0

        if c in pos:
            for j in pos[c]:  # loop แค่ตำแหน่งที่ match เท่านั้น
                val = prev_dp.get(j, 0) + 1
                curr_dp[j + 1] = val
                if val > best_len:
                    best_len = val
                    best_end = i + 1
                if val > max_curr:
                    max_curr = val

        prev_dp = curr_dp
        max_prev = max_curr

    if best_len == 0:
        print("No common substring.")
    else:
        print(s1[best_end - best_len:best_end])
        print(best_len)


s1 = input()
s2 = input()
lcs(s1, s2)
