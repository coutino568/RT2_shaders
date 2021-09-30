


from os import read


class Object(object):

    def __init__ (self,filename):
        self.vertices =[]
        self.faces=[]
        self.normals =[]
        self.texcoords =[]
        

        with open(filename, "r") as file:
            self.lines = file.read().splitlines()

        self.readFile()

    def readFile(self):
        for line in self.lines:
            if line:
                #divide cada linea en prefijo y contenido
                try:
                    prefix, value = line.split(' ', 1)
                except:
                    continue
                #clasifica segun prefijos
                #Vertices
                if prefix == 'v':
                    self.vertices.append(list(map(float, value.split(' '))))
                #texcoor
                elif prefix == 'vt': 
                    self.texcoords.append(list(map(float, value.split(' '))))
                #vertex normals
                elif prefix == 'vn': 
                    self.normals.append(list(map(float, value.split(' '))))
                #faces
                elif prefix == 'f': 
                    self.faces.append( [ list(map(int, vert.split('/'))) for vert in value.split(' ')] )







class Texture(object):
    def __init__(self, filename):
        self.filename = filename
        self.read()


    def read(self):
        with open(self.filename, "rb") as image:
            image.seek(10)
            headerSize = struct.unpack('=l', image.read(4))[0]

            image.seek(14 + 4)
            self.width = struct.unpack('=l', image.read(4))[0]
            self.height = struct.unpack('=l', image.read(4))[0]

            image.seek(headerSize)

            self.pixels = []

            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1)) / 255
                    g = ord(image.read(1)) / 255
                    r = ord(image.read(1)) / 255

                    self.pixels[y].append( _color(r,g,b) )


    def getColor(self, tx, ty):
        if 0<=tx<1 and 0<=ty<1:
            x = int(tx * self.width)
            y = int(ty * self.height)
            return self.pixels[y][x]
        else:
            return _color(0,0,0)



