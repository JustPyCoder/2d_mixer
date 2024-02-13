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
    def clear(self, start_cords):
        end_cords = []
        for i in range(len(start_cords)):
            if start_cords[i] not in end_cords:
                end_cords.append(start_cords[i])
        return end_cords

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
        cords = []
        angle/= 57.8769231
        center = [ round((cords_symvols[0][0]+cords_symvols[-1][0])/2), round((cords_symvols[0][1]+cords_symvols[-1][1])/2)]
        for i in range(len(cords_symvols)):
            XY = [cords_symvols[i][0]-center[0],cords_symvols[i][1]-center[1]]
            X = round(float((XY[0]*math.cos(angle)) - (XY[1]*math.sin(angle))))+ center[0]
            Y = round(float((XY[0]*math.sin(angle)) + (XY[1]*math.cos(angle))))+ center[1]
            cords += [[X,Y]]
        end_cords = self.clear(cords)
        return end_cords

    def circle(self, radius, cords_circle):
        cords = []
        for i in range(360):
            cords+= [[round((radius*math.cos(i))+cords_circle[0]), round((radius*math.sin(i))+cords_circle[1])]]
        end_cords = self.clear(cords)
        return end_cords

    def circle_filled(self, radius_start, cords_circle):
        cords = []
        for radius in range(radius_start):
            for i in range(360):
                cords+= [[round((radius*math.cos(i))+cords_circle[0]), round((radius*math.sin(i))+cords_circle[1])]]
        end_cords = self.clear(cords)
        return end_cords

    def vector(self, start_pos, end_pos):
        cords_vector = [end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]] 
        сord_per = 0.01
        end_cords = []
        while сord_per <= 1:
            end_cords += [[round(start_pos[0]+сord_per*cords_vector[0]),round(start_pos[1]+сord_per*cords_vector[1])]]
            сord_per += 0.01
        pure_cords = self.clear(end_cords)
        return pure_cords

    def triangle(self, pos_A, pos_B, pos_C):
        end_cords = []
        res_1 = self.vector(pos_A, pos_B)
        res_2 = self.vector(pos_B, pos_C)
        res_3 = self.vector(pos_C, pos_A)
        cords = res_1 + res_2 + res_3
        end_cords = self.clear(cords)
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