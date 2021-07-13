class Coordenadas:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distancia(self,otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff+y_diff)**0.5
    

if __name__ == '__main__':
    f_coord = Coordenadas(3, 30)
    s_coord = Coordenadas(4, 8)
    
    #print(f_coord.distancia(s_coord))
    print(isinstance(s_coord, Coordenadas))