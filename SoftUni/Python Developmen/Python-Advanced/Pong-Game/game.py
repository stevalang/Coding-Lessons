class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.__ball_pos = (0, 0)
        self.__ball_delta_x = 1
        self.__ball_delta_y = 1

        self.paddle_a_pos = (-self.width / 2 + 50, 0)
        self.paddle_height = self.height / 4
        self.paddle_width = 20

    def tick(self):
        self.__perform_border_checking()
        x, y = self.__ball_pos
        self.__ball_pos = (x + self.__ball_delta_x, y + self.__ball_delta_y)

    def __perform_border_checking(self):
        x, y = self.__ball_pos
        if abs(y) >= (self.height / 2):
            self.__ball_delta_y *= -1
        if abs(x) >= (self.width / 2):
            self.__ball_delta_x *= -1

    def ball_pos(self):
        return self.__ball_pos
