N = int(input())
arr = list(map(int, input().split()))

for i in range(N - 1, 0, -1): # 마지막 항부터 돈다.
    if arr[i - 1] < arr[i]: # 만약 앞 값이 뒤의 값보다 작다면
        for j in range(N - 1, 0, -1): # 다시 앞의 값을 맨 뒤와 비교
            if arr[i - 1] < arr[j]: # 그 앞의 값이 뒤에 있는 어떠한 값보다 작다면
                arr[i - 1], arr[j] = arr[j], arr[i - 1] # 스왑
                arr = arr[:i] + sorted(arr[i:])
                print(*arr) # *를 이용해 리스트 내부의 원소들을 공백을 사용하여 출력
                exit()

print(-1)
