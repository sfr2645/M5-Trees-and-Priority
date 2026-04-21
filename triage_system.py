import heapq

class TriageSystem:
    _arrival_counter = 0  # class-level counter

    def __init__(self):
        self._queue = []

    @staticmethod
    def _next_arrival_order():
        order = TriageSystem._arrival_counter
        TriageSystem._arrival_counter += 1
        return order

    def add_patient(self, name, severity):
        if not name or not (1 <= severity <= 5):
            raise ValueError("Invalid name or severity (1–5 required)")

        order = self._next_arrival_order()
        heapq.heappush(self._queue, (-severity, order, name, severity))

    def process_next(self):
        if self.is_empty():
            return None
        _, _, name, severity = heapq.heappop(self._queue)
        return (name, severity)

    def peek_next(self):
        if self.is_empty():
            return None
        _, _, name, severity = self._queue[0]
        return (name, severity)

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)

    def clear(self):
        self._queue = []
