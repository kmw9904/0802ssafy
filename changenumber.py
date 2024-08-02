words = list(input())
result = []
for word in words:
    result.append(ord(word)-64)

print(*result)