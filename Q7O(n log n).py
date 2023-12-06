def sortedSquares(nums):
    return sorted(x ** 2 for x in nums)

# Exemplo de uso
nums = [-4, -1, 0, 3, 10]
resultado = sortedSquares(nums)
print(resultado)
