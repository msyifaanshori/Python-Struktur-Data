def insertion_sort(data):
    # Mulai dari elemen kedua (indeks 1)
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Geser elemen di bagian terurut yang lebih besar dari key
        # ke kanan
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1

        # Sisipkan key ke posisi yang tepat
        data[j + 1] = key
    return data