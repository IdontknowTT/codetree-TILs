k,n = map(int, input().split()) 



# 1~K 까지 중 n번 골라서 나올 수 있는 순서쌍 개수 
# 당연히 총 개수는 k^n제곱 (k*k*....n번)
arr = []

def choose(num):
    
    # 종료 조건
    if num == n+1:
        for i in arr:
            print(i, end = " ")
        print()
        return

    for i in range(1, k+1):
        arr.append(i)
        choose(num+1)
        arr.pop()
        
choose(1)