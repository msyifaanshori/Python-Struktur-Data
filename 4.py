data = [5,10,15,90,80]
print(data[1])

def binary_search(arr,x, low=0, high=None):
  if high is None:
    high = len(arr) -1

  if low <= high:
    mid = (low + high) // 2
    if arr[mid] == x:
      return mid
    elif arr[mid] < x:
      return binary_search(arr,x,mid+1,high)

    else:
      return binary_search(arr,x,mid + 1,high)

data_sorted = []
data_sorted.extend(sorted(data))
print(binary_search(data_sorted,80))

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

merge_sort(data)
print(merge_sort(data))

def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Pindahkan cakram 1 dari {source} ke {target}")
        return

    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Pindahkan cakram {n} dari {source} ke {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)


jumlah_cakram = 3
tower_of_hanoi(jumlah_cakram, "A", "B", "C")