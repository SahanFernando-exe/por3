class Player:
    def __init__(self, uid, name, score=0):
        self._uid = str(uid)
        self._name = name
        self._score = score

    def __str__(self):
        return f"location: {id(self)}, uid: {self._uid}, name: {self._name}"

    def __repr__(self):
        return f"name: {self._name}, ID: {self._uid}, score: {self._score}"

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.uid == other.uid
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Player):
            return self.score < other.score
        return NotImplemented

    def display(self):
        return f"Player '{self._uid}': {self._name}"

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score: int):
        if new_score >= 0:
            self._score = new_score
        else:
            raise ValueError("score cannot be below 0")

    @classmethod
    def custom_sort(cls, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = []
        right = []
        prev = pivot
        is_sorted = True
        for x in arr[1:]:
            if x > pivot:
                left.append(x)
            else:
                right.append(x)
            if x > prev:
                is_sorted = False
            prev = x
        if is_sorted:
            return arr
        return cls.custom_sort(left) + [pivot] + cls.custom_sort(right)