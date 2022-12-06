class Exercise:

    def __init__(self, name, weight, sets, reps, rest, completed, day, id = None):
        self.name = name
        self.weight = weight
        self.sets = sets
        self.reps = reps
        self.rest = rest
        self.completed = completed
        self.day = day
        self.id = id

    def exercise_completed(self):
        self.exercise == True