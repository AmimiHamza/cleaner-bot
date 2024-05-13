class Environment:
    def __init__(self, dirty_squares, initial_position):
        self.dirty_squares = dirty_squares
        self.current_position = initial_position

    def get_perception(self):
        return {
            'current_position': self.current_position,
            'dirty_squares': self.dirty_squares
        }

    def perform_action(self, action):
        if action == 'Move Right':
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
        elif action == 'Move Left':
            self.current_position = (self.current_position[0] - 1, self.current_position[1])
        elif action == 'Move Down':
            self.current_position = (self.current_position[0], self.current_position[1] + 1)
        elif action == 'Move Up':
            self.current_position = (self.current_position[0], self.current_position[1] - 1)
        elif action == 'Clean':
            self.dirty_squares.remove(self.current_position)
        return self.get_perception()

    def print_state(self):
        return (self.current_position,self.dirty_squares)

    def is_clean(self):
        return len(self.dirty_squares) == 0
