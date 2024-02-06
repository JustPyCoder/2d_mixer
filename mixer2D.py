class Ecran:
    def __init__(self, display, sign):
        self.ecran = list()
        self.string = ''
        self.display = display
        self.sign = sign

    def plase_ecran(self):
        self.ecran = list()
        for _ in range(int(self.display[0])):
            self.ecran += [[str(self.sign)]*int(self.display[1])]

    def print_ecran(self):
        for I in range(int(self.display[1])):
            for i in range(int(self.display[0])):
                self.string += self.ecran[i][I]
            print(self.string)
            self.string = ''

    def plase_sign(self, list_X_Y, sign):
        for i in range(len(list_X_Y)):
            self.ecran[list_X_Y[i][0]][list_X_Y[i][1]] = str(sign)     


class Figure: 
    def rectangle(self, start_pos, end_pos):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.rectangle = []
        self.save = self.start_pos[0]

        if self.start_pos[1] > self.end_pos[1] :
            return [[1,0]]
        elif self.start_pos[0] > self.end_pos[0]:
            return [[0,1]]
        else:
            while self.start_pos[1]-1 != self.end_pos[1]:
                self.start_pos[0] = self.save
                self.rectangle += [[self.start_pos[0],self.start_pos[1]]]
                while self.start_pos[0] != self.end_pos[0]:
                    self.start_pos[0] += 1
                    self.rectangle += [[self.start_pos[0],self.start_pos[1]]]
                self.start_pos[1] += 1
            return self.rectangle 


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