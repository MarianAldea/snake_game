from turtle import Screen, Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self,culoare, lungime):
        self.x_coord = 0
        self.segment_list = []
        self.build_snake(culoare, lungime)
        self.head = self.segment_list[0]

    def build_snake(self,culoare, lungime):
        for i in range(lungime):
            self.add_segment(culoare)


    def reset(self):
        for seg in self.segment_list:
            seg.goto(1000,1000)
        self.x_coord = 0
        self.segment_list.clear()
        self.build_snake("green", 5)
        self.head = self.segment_list[0]


    def miscare(self):
        for seg_num in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[seg_num - 1].xcor()
            new_y = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(new_x, new_y)

    def left(self):
        if self.segment_list[0].heading() != RIGHT:
            self.miscare()
            self.segment_list[0].setheading(LEFT)

    def right(self):
        if self.segment_list[0].heading() != LEFT:
            self.miscare()
            self.segment_list[0].setheading(RIGHT)

    def up(self):
        if self.segment_list[0].heading() != DOWN:
            self.miscare()
            self.segment_list[0].setheading(UP)

    def down(self):
        if self.segment_list[0].heading() != UP:
            self.miscare()
            self.segment_list[0].setheading(DOWN)

    def forward(self):
        self.miscare()
        self.segment_list[0].forward(MOVE_DISTANCE)

    def add_segment(self, culoare):
        segment = Turtle(shape="square")
        segment.color(f"{culoare}")
        segment.penup()
        segment.speed("fastest")
        segment.setx(self.x_coord)
        self.x_coord += 20
        self.segment_list.append(segment)

    def extend(self,culoare):
        self.add_segment(culoare)