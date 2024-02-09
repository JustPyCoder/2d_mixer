import math

class Screen:
    def __init__(self, display, sign):
        self.screen = list()
        self.string = ''
        self.display = display
        self.sign = sign

    def create_a_screen(self):
        self.screen = list()
        for _ in range(int(self.display[0])):
            self.screen += [[str(self.sign)]*int(self.display[1])]

    def display_screen(self):
        for I in range(int(self.display[1])):
            for i in range(int(self.display[0])):
                self.string += self.screen[i][I]
            print(self.string)
            self.string = ''

    def print_symbols(self, list_X_Y, sign):
        for i in range(len(list_X_Y)):
            if list_X_Y[i][0] < self.display[0] and list_X_Y[i][0] >= 0 and list_X_Y[i][1] < self.display[1] and list_X_Y[i][1] >= 0:
                self.screen[list_X_Y[i][0]][list_X_Y[i][1]] = str(sign)


class Figure: 
    def rectangle(self, start_pos, end_pos):
        rectangle = []
        save = start_pos[0]

        if start_pos[1] > end_pos[1] :
            return [[1,0]]
        elif start_pos[0] > end_pos[0]:
            return [[0,1]]
        else:
            while start_pos[1]-1 != end_pos[1]:
                start_pos[0] = save
                rectangle += [[start_pos[0],start_pos[1]]]
                while start_pos[0] != end_pos[0]:
                    start_pos[0] += 1
                    rectangle += [[start_pos[0],start_pos[1]]]
                start_pos[1] += 1
            return rectangle 

    def turn(self, cords_symvols, angle):
        end_cords = []
        angle/= 57.8769231
        center = [ round((cords_symvols[0][0]+cords_symvols[-1][0])/2), round((cords_symvols[0][1]+cords_symvols[-1][1])/2)]
        for i in range(len(cords_symvols)):
            XY = [cords_symvols[i][0]-center[0],cords_symvols[i][1]-center[1]]
            X = round(float((XY[0]*math.cos(angle)) - (XY[1]*math.sin(angle))))+ center[0]
            Y = round(float((XY[0]*math.sin(angle)) + (XY[1]*math.cos(angle))))+ center[1]
            end_cords += [[X,Y]]
        return end_cords

    def circle(self, radius, cords_circle):
        end_cords = []
        for i in range(360):
            end_cords+= [[round((radius*math.cos(i))+cords_circle[0]), round((radius*math.sin(i))+cords_circle[1])]]
        for i in range(len(end_cords)):
            for I in range(len(end_cords)):
                if i != I:
                    try:
                        if end_cords[i][0] == end_cords[I][0] and end_cords[i][1] == end_cords[I][1] :
                            end_cords.pop(I)
                    except:
                        pass
        return end_cords


class Logics:
    def __init__(self, data, display):
        self.data = data
        self.display = display

    def logical_left(self):
        for i in range(len(self.data)):
            if self.data[i][1] == 0 :
                self.data[i][1] = int(self.display[1]) - 1
            else:
                self.data[i][1] -=1
        return list(self.data)

    def logical_up(self):
        for i in range(len(self.data)):
            if self.data[i][0] == 0:
                self.data[i][0] = int(self.display[0]) - 1
            else:
                self.data[i][0] -=1
        return list(self.data)

    def logical_down(self):
        for i in range(len(self.data)):
            if self.data[i][1] == int(self.display[1]) - 1:
                self.data[i][1] = 0
            else:
                self.data[i][1] +=1
        return list(self.data)

    def logical_right(self):
        for i in range(len(self.data)):
            if self.data[i][0] == int(self.display[0]) - 1:
                self.data[i][0] = 0
            else:
                self.data[i][0] +=1
        return list(self.data)

Figure = Figure()