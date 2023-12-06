def longest_palindromic_subsequence(s):
    n = len(s)
    
    dp = [[0] * n for _ in range(n)]


    for i in range(n):
        dp[i][i] = 1

    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])


    length = dp[0][n - 1]
    subsequence = [''] * length

    i, j = 0, n - 1
    k = length - 1
    while i < j:
        if s[i] == s[j]:
            subsequence[k] = s[i]
            subsequence[length - k - 1] = s[i]
            i += 1
            j -= 1
            k -= 1
        elif dp[i][j - 1] > dp[i + 1][j]:
            j -= 1
        else:
            i += 1

    return ''.join(subsequence)

sequence = "ACGTGTCAAAATCG"
result = longest_palindromic_subsequence(sequence)
print("Subsequência palindrômica de tamanho máximo:", result)
