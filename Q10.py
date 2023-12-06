def busca_binaria(nums, alvo):
    inicio, fim = 0, len(nums) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if nums[meio] == alvo:
            return meio
        elif nums[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return inicio

# Exemplo 1
nums1 = [1, 3, 5, 6]
alvo1 = 5
saida1 = busca_binaria(nums1, alvo1)
print(saida1)  # Saída: 2

# Exemplo 2
nums2 = [1, 3, 5, 6]
alvo2 = 2
saida2 = busca_binaria(nums2, alvo2)
print(saida2)  # Saída: 1
