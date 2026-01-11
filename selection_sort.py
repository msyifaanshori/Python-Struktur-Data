def selection_sort(data):
    n = len(data)
    for i in range(n):
        # Cari indeks elemen minimum di sisa array
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j

        # Tukar elemen minimum dengan elemen di posisi i
        data[i], data[min_idx] = data[min_idx], data[i]
    return data