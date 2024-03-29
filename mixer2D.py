from copy import deepcopy
import math


class Screen:
    def __init__(self, display, sign):
        self.screen = list()
        self.screen_data = list()
        self.display = display
        self.sign = sign

    def create_a_screen(self):
        for _ in range(int(self.display[1])):
            self.screen_data += [[str(self.sign)]*int(self.display[0])]
        self.clear_a_screen()

    def clear_a_screen(self):
        self.screen = deepcopy(self.screen_data)

    def display_screen(self):
        list_string = [''.join(i) for i in self.screen]
        print('\n'.join(list_string))

    def display_screen_string(self):
        list_string = [''.join(i) for i in self.screen]
        print(''.join(list_string))

    def print_symbols(self, list_X_Y, sign):
        for i in range(len(list_X_Y)):
            if list_X_Y[i][0] < self.display[0] and list_X_Y[i][0] >= 0 and list_X_Y[i][1] < self.display[1] and list_X_Y[i][1] >= 0:
                self.screen[list_X_Y[i][1]][list_X_Y[i][0]] = str(sign)


class Figure: 
    def clear(self, start_cords):
        end_cords = []
        for i in range(len(start_cords)):
            if start_cords[i] not in end_cords:
                end_cords.append(start_cords[i])
        return end_cords

    def fill(self, data):
        end = list()
        data_X = data.copy()
        prom_data = list()

        data_num_Y = self.clear([data[i][1] for i in range(len(data))])
        data_num_Y.sort()
    
        for i in range(len(data)):
            for I in range(len(data)-i-1):
                if data_X[I][0] > data_X[I+1][0]:
                    data_X[I], data_X[I+1] = data_X[I+1], data_X[I] 

        for i in range(len(data_num_Y)):
            prom_data += [[]]
            for I in range(len(data_X)):
                if data_X[I][1] == data_num_Y[i] :
                    prom_data[i] += [[data_X[I]]]
    
        prom_data = self.clear(prom_data)
    
        for i in range(len(prom_data)):
            try:
                for i in self.rectangle([prom_data[i][0][0][0],prom_data[i][0][0][1]],[prom_data[i][-1][0][0],prom_data[i][-1][0][1]]) :
                    if i not in end:
                        end.append(i)
            except:
                pass
        return end

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

    def turn(self, cords_symvols, angle, center=[0,0]):
        cords = []
        angle/= 180/math.pi
        for i in range(len(cords_symvols)):
            XY = [cords_symvols[i][0]-center[0],cords_symvols[i][1]-center[1]]
            X = round(float((XY[0]*math.cos(angle)) - (XY[1]*math.sin(angle))))+ center[0]
            Y = round(float((XY[0]*math.sin(angle)) + (XY[1]*math.cos(angle))))+ center[1]
            if [X,Y] not in cords:
                cords += [[X,Y]]
        return cords

    def circle(self, radius, cords_circle, angle=360):
        end_cords = list()
        radian = (180/math.pi)
        for i in range(angle):
            i/=radian
            cords = [[round((radius*math.cos(i))+cords_circle[0]), round((radius*math.sin(i))+cords_circle[1])]]
            if cords[0] not in end_cords:
                end_cords += cords
        return end_cords
        
    def vector(self, start_cords, end_cords):
        vector_cord = [end_cords[0]-start_cords[0],end_cords[1]-start_cords[1]] 
        vector_size = round(math.sqrt(vector_cord[0]**2+vector_cord[1]**2))
        mnog = 1/vector_size
        vector_end = list()
        for i in range(vector_size):
            prom_mnog= mnog*i
            vector_prom=[[round(start_cords[0]+vector_cord[0]*prom_mnog),round(start_cords[1]+vector_cord[1]*prom_mnog)]]
            if vector_end not in vector_prom:
                vector_end+=vector_prom
        return vector_end

    
    def new(self, cords_start):
        end_cords = list()
        for i in range(len(cords_start)):
            for i in self.vector(cords_start[i-1],cords_start[i]):
                if i not in end_cords:
                    end_cords.append(i)
        return end_cords

    def new_filled(self, start_cords):
        return self.fill(self.new(start_cords))

    def circle_filled(self, radius_start, cords_circle,angle):
        circle = self.circle(radius_start, cords_circle,angle)
        return self.fill(self.vector(cords_circle,circle[0]) + circle + self.vector(cords_circle,circle[-1]))


class Logics:
    def __init__(self, display):
        self.display = display

    def logical_up(self,data,zdvig=1):
        for item in data:
            if item[1] - zdvig < 0 :
                item[1] = item[1]-zdvig+self.display[1]
            else:
                item[1] -=zdvig
        return data

    def logical_left(self,data,zdvig=1):
        for item in data:
            if item[0] - zdvig < 0:
                item[0] = item[0]-zdvig+self.display[0]
            else:
                item[0] -=zdvig
        return data

    def logical_down(self,data,zdvig=1):
        for item in data:
            if item[1] + zdvig >= self.display[1]:
                item[1] = item[1]+zdvig-self.display[1]
            else:
                item[1] +=zdvig
        return data

    def logical_right(self,data,zdvig=1):
        for item in data:
            if item[0] + zdvig >= self.display[0]:
                item[0] = item[0]+zdvig-self.display[0]
            else:
                item[0]+= zdvig
        return data

    
    def up(self,data,zdvig=1):
        for item in data:
            item[1]-=zdvig
        return data

    def down(self,data,zdvig=1):
        for item in data:
            item[1]+=zdvig
        return data
    
    def left(self,data,zdvig=1):
        for item in data:
            item[0]-=zdvig
        return data
    
    def right(self,data,zdvig=1):
        for item in data:
            item[0]+=zdvig
        return data


    def border_up(self, data):
        for item in data:
            if item[1] == 0-1: return True
        return False

    def border_down(self, data):
        for item in data:
            if item[1] == self.display[1]: return True
        return False

    def border_left(self, data):
        for item in data:
            if item[0] == 0-1: return True
        return False

    def border_right(self, data):
        for item in data:
            if item[0] == self.display[0]: return True
        return False


Figure = Figure()