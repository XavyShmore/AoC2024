import numpy as np

class Guard:
    def __init__(self, position: (int, int), direction: (int, int), level_map: np.array):
        self.position = np.array(position)
        self.direction = np.array(direction)

        self.visited_squares = np.zeros(level_map.shape)
        self.visited_squares[position] = 1

        self.visited_squares_and_directions = set()

        self.level_map = level_map

    def rotate(self):
        rotation_matrix = np.array(
            [[0, 1],
             [-1, 0]]
        )
        self.direction = rotation_matrix @ self.direction

    def next_move_is_inbounds(self):

        bounds = self.level_map.shape
        next_position = self.position + self.direction

        x_is_in = 0 <= next_position[0] < bounds[0]
        y_is_in = 0 <= next_position[1] < bounds[1]

        return x_is_in and y_is_in

    def can_go_forward(self) -> bool:
        next_position = self.position + self.direction
        return self.level_map[tuple(next_position)] == '.'

    def move_foward(self):
        self.position = self.position + self.direction
        self.visited_squares[tuple(self.position)] = 1

    def in_a_loop(self):
        if (tuple(self.position), tuple(self.direction)) in self.visited_squares_and_directions : return True

        self.visited_squares_and_directions.add((tuple(self.position), tuple(self.direction)))

    def calculate_visited_squares(self) -> (int, bool):
        while self.next_move_is_inbounds():
            if self.in_a_loop(): return self.visited_squares.sum(), True

            if self.can_go_forward():
                self.move_foward()
            else:
                self.rotate()

        return self.visited_squares.sum(), False