class Player:
    def __init__(self, uid, name):
        self._uid = str(uid)
        self._name = name
        self._score = 0

    def __str__(self):
        return f"location: {id(self)}, uid: {self._uid}, name: {self._name}"

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