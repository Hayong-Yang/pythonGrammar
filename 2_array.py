# 예제 1. 2차원 리스트를 한 줄씩 출력해보세요
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(matrix)):
    print(matrix[i])
    
for row in matrix:
    for item in row:
        print(item, end=' ')
    print()

# 예제 2. 리스트에서 가장 큰 값과 그 인덱스를 찾아 출력하세요.
scores = [67, 89, 92, 56, 100, 75]

maxNum=0
for num in scores:
    if num>maxNum:
        maxNum=num
    print(f'현재까지 가장 큰 수: {maxNum}')    
    continue
print(maxNum)
print(scores.index(maxNum))

print(max(scores))