from process import Process

class Graph:
    def __init__(self, processes: list[Process]) -> None:
        self._processes = processes