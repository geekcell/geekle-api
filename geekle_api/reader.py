from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def read_index(idx: int) -> str:
        pass


class FileReader(Reader):
    def __init__(self, filename: str) -> None:
        super().__init__()
        self.filename = filename

    def read_index(self, idx: int) -> str:
        num_lines = sum(1 for line in open(self.filename))
        if idx < 0:
            raise IndexError(f"Index {idx} out of range")

        idx = idx % num_lines

        with open(self.filename, "r") as f:
            for i, line in enumerate(f):
                if i == idx:
                    return line.strip()


class InMemoryReader(Reader):
    def __init__(self, lines: list) -> None:
        super().__init__()
        self.lines = lines

    def read_index(self, idx: int) -> str:
        if idx < 0:
            raise IndexError(f"Index {idx} out of range")

        idx = idx % len(self.lines)

        return self.lines[idx]
