class Cleaner:
    def __init__(self):
        self.memory = []

    def update_memory(self, perception_actuelle):
        self.memory.append(perception_actuelle)
    

    def draw_letter_A(self,c,l):
        # Create a 10x10 grid
        grid = [[' ' for _ in range(10)] for _ in range(10)]

        # Set the positions to draw the letter D
        for i in l:
            grid[i[1]][i[0]]='D'
        # Set the positions to draw the letter D

        grid[c[1]][c[0]] ='AA'        
        return grid



    def choose_best_action(self):
        perception = self.memory[-1]
        dirty_squares = perception['dirty_squares']

        if dirty_squares:
            current_position = perception['current_position']
            
            nearest_square = None
            min_distance = 100

            for square in dirty_squares:
                x_diff = abs(square[0] - current_position[0])
                y_diff = abs(square[1] - current_position[1])
                total_distance = x_diff + y_diff
                
                if total_distance < min_distance:
                    min_distance = total_distance
                    nearest_square = square

            x_diff = nearest_square[0] - current_position[0]
            y_diff = nearest_square[1] - current_position[1]
            
            if x_diff > 0:
                return 'Move Right'
            elif x_diff < 0:
                return 'Move Left'
            elif y_diff > 0:
                return 'Move Down'
            elif y_diff < 0:
                return 'Move Up'
            else:
                return 'Clean'

        return 'NoOp'