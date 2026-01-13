def merge(left, right):
    """
    Menggabungkan dua array terurut (left, right)
    menjadi satu array terurut.
    """
    result = []
    i, j = 0, 0

    # Bandingkan elemen dari kedua array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Tambahkan sisa elemen (jika ada) dari salah satu array
    # Hanya salah satu dari dua baris ini yang akan berjalan
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    """
    Mengurutkan array menggunakan prinsip Divide and Conquer.
    """

    # Base Case (Conquer Sederhana)
    # Jika array punya 1 elemen atau kurang, array sudah terurut.
    if len(arr) <= 1:
        return arr

    # Divide (Membagi)
    # Bagi array menjadi dua bagian: kiri dan kanan.
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Conquer (Rekursif)
    # Urutkan kedua bagian secara terpisah dengan memanggil
    # fungsi ini lagi.
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Combine (Menggabungkan)
    # Gabungkan kedua bagian yang sudah terurut menggunakan merge.
    return merge(left_sorted, right_sorted)