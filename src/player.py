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
        return False

    def __lt__(self, other):
        if self.score < other.score:
            return True
        return False

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
    def sort_quickly(cls, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = []
        right = []
        prev = pivot
        sorted = True
        for x in arr[1:]:
            if x > pivot:
                left.append(x)
            else:
                right.append(x)
            if x > prev:
                sorted = False
            prev = x
        if sorted:
            return arr
        return cls.sort_quickly(left) + [pivot] + cls.sort_quickly(right)