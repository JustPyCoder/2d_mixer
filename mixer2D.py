class Ecran:
    def __init__(self, cords, znak):
        self.ecran = list()
        self.string = ''
        self.cords = cords
        self.znak = znak

    def plase_ecran(self):
        self.ecran = list()
        for _ in range(int(self.cords[0])):
            self.ecran += [[str(self.znak)]*int(self.cords[1])]

    def print_ec(self):
        for I in range(int(self.cords[1])):
            for i in range(int(self.cords[0])):
                self.string += self.ecran[i][I]
            print(self.string)
            self.string = ''

    def printer(self, list_X_Y, znak):
        for i in range(len(list_X_Y)):
            self.ecran[list_X_Y[i][0]][list_X_Y[i][1]] = str(znak)     

class Logics:
    def __init__(self, data, cords):
        self.data = data
        self.cords = cords

    def logical_W(self):
        for i in range(len(self.data)):
            if self.data[i][1] == 0 :
                self.data[i][1] = int(self.cords[1]) - 1
            else:
                self.data[i][1] -=1
        return list(self.data)

    def logical_A(self):
        for i in range(len(self.data)):
            if self.data[i][0] == 0:
                self.data[i][0] = int(self.cords[0]) - 1
            else:
                self.data[i][0] -=1
        return list(self.data)

    def logical_S(self):
        for i in range(len(self.data)):
            if self.data[i][1] == int(self.cords[1]) - 1:
                self.data[i][1] = 0
            else:
                self.data[i][1] +=1
        return list(self.data)

    def logical_D(self):
        for i in range(len(self.data)):
            if self.data[i][0] == int(self.cords[0]) - 1:
                self.data[i][0] = 0
            else:
                self.data[i][0] +=1
        return list(self.data)