from typing import Any, List

class Stack:
    """Implementasi kelas Stack."""
    def __init__(self) -> None:
        self._data: List[Any] = []

    def push(self, x: Any) -> None:
        """Menambahkan elemen ke puncak stack."""
        self._data.append(x)

    def pop(self) -> Any:
        """Menghapus dan mengembalikan elemen dari puncak stack."""
        if self.is_empty():
            raise IndexError("Stack kosong")
        return self._data.pop()

    def peek(self) -> Any:
        """Mengintip elemen di puncak tanpa menghapusnya."""
        return None if self.is_empty() else self._data[-1]

    def is_empty(self) -> bool:
        """Memeriksa apakah stack kosong."""
        return not self._data

    def __repr__(self) -> str:
        """Representasi stack (top -> bottom)."""
        return f"Stack(top->bottom): {list(reversed(self._data))}"


def is_balanced(expr: str) -> bool:
    """
    Memeriksa apakah ekspresi memiliki tanda kurung berpasangan yang seimbang.
    """
    pairs = {")": "(", "]": "[", "}": "{"}
    st = Stack() # Menggunakan kelas Stack yang telah didefinisikan

    for ch in expr:
        if ch in '([{':
            st.push(ch)
        elif ch in ')]}':
            if st.is_empty() or st.pop() != pairs[ch]:
                return False

    return st.is_empty()

# Contoh penggunaan gabungan code
print(f"'{'{[()]}'}' seimbang? {is_balanced('{[()]}')}")
print(f"'{'([)]'}' seimbang? {is_balanced('([)]')}")