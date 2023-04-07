x = sorted(list(map(int, input().split())))
# искомое число
value = int(input())

mid = len(x) // 2
low = 0
high = len(x) - 1

while x[mid] != value and low <= high:
    if value > x[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2


if low > high and low< high:
    print("No value")
else:
    print(f"ID={mid-1,mid+1}")