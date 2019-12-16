class Pathfinder():
    def __init__(self, vector):
        # Initialize the Pathfinder object
        self.vector = vector
        self.paths = []
        self.been_there = []
        self.findAllPaths(0, [])

    def findAllPaths(self, position, solution):
        self.been_there = []

        solution.append(position)

        if position == len(self.vector) -1:
            self.paths.append(solution.copy())
            popped_item = solution.pop()
            self.been_there.append(popped_item)

            return 1

        valueAtPosition = self.vector[position]

        if (position - valueAtPosition > 0 and position - valueAtPosition not in solution ):
            if not solution.__contains__(position - valueAtPosition):
                result = self.findAllPaths(position - valueAtPosition, solution)
            else:
                solution.pop()
                return

            if solution.__contains__(position + valueAtPosition) and self.been_there.__contains__(position - valueAtPosition):
                popped_item = solution.pop()
                self.been_there.append(popped_item)
                return

        if (position + valueAtPosition < len(self.vector)):

            if not solution.__contains__(position + valueAtPosition):
                result = self.findAllPaths(position + valueAtPosition, solution)
            else:
                solution.pop()
                return

            popped_item = solution.pop()
            self.been_there.append(popped_item)
            return

        if position - valueAtPosition > 0 or position + valueAtPosition > len(self.vector):
            popped_item = solution.pop()
            self.been_there.append(popped_item)

        if position == 0:
            return self.paths
        else:
            return 0


    def getPaths(self):
        if (len(self.paths) > 0):
            return self.paths
        else:
            return []

