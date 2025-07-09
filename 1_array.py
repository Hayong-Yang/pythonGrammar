#리스트란?
#여러 개의 값을 하나의 변수로 묶는 자료형
#순서 있음(인덱스 있음)
#가변적(Mutable): 요소 추가/삭제 가능
#여러 자료형 혼합 가능

#리스트(배열) 연습 예제

#예제 1.과일 이름이 담긴 리스트를 만들고 출력해보세요
fruitList = ['apple', 'banana', 'melon']
print(fruitList)

#예제 2. 아래 리스트에서 두 번째 요소를 출력하세요
numbers = [10, 20, 30, 40, 50]
print(numbers[1])

#예제 3. 리스트에서 중간 3개 요소만 슬라이싱하여 출력하세요
numbers = [100, 200, 300, 400, 500]
print(numbers[1:4])

#예제 4. colors 리스트에서 'yellow'를 맨 뒤에 추가하고 'green'을 삭제하세요
colors = ['red', 'green', 'blue']
colors.append('yellow')
colors.remove('green')
print(colors)

#예제 5. 리스트의 모든 요소를 한 줄씩 출력하세요
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(name)

#예제 6. 두 리스트를 합쳐서 오름차순 정렬하세요
list1 = [5, 2, 9]
list2 = [1, 7]

addedList = list1 + list2
sortedAddedList = sorted(addedList)
print(addedList)
print(sortedAddedList)
addedList.sort()
print(addedList)

#예제 7. 1부터 5까지 제곱한 수들을 리스트로 만들어보세요
squared = [i**2 for i in range(1,6)]
print(squared)

#예제 8. 사용자에게 숫자 5개를 입력받아 리스트로 저장하세요
userList=[]
for i in range(5):
    if i == 0: 
        print('숫자를 5번 입력받을거에요.')
        print('숫자를 한번씩 입력해주세요!')
    else:
        print(f'현재 리스트 상황: {userList}')     
    inputNum = int(input(f'{i+1}번째 숫자: '))
    userList.append(inputNum)
print(userList)       



