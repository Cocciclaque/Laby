import random
import pygame

class Labyrinthe :
    # constructeur
    def __init__(self, sizeX:int, sizeY:int, file, screen:pygame.display, tilesize:int):
        """sizeX, sizeY désignent la taille du labyrinthe sur l'axe (x,y)"""
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.file = file
        self.s = screen
        self.t = tilesize
        #attention création d'une matrice en Y X
        self.matrice = [ [0]* self.sizeX for _ in range(self.sizeY) ]
        self.genereFromFile()

    def affiche(self):
        """Sortie console du labyrinthe"""
        for j in range(self.sizeY):
            for i in range(self.sizeX):
                # rappel: matrice en Y,X
                print(self.matrice[j][i], end = "")
            print()
        #print(self.matrice)

    def draw(self):
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                if self.matrice[i][j] == "1":
                    pygame.draw.rect(self.s, "red", pygame.Rect(j*self.t, i*self.t, self.t, self.t))

    def get_matrice(self):
        """renvoie la matrice associée au labyrinthe"""
        return self.matrice
    
    def getXY(self, i,j):
        """Renvoie la case (i,j) du labyrinthe sur l'axe (x,y)"""
        return self.matrice[j][i]

    def setXY(self, i,j,v):
        """Modifie par v la case (i,j) sur l'axe (x,y)"""
        self.matrice[j][i] = v
    
    def getSize(self):
        """Renvoie la taille (x,y) du labyrinthe"""
        return (self.sizeX, self.sizeY)
    
    def détruire_mur(self, i,j):
        """Détruit un mur du labyrinthe en (i,j) sur l'axe (x,y)"""
        self.matrice[j][i]=0

    def genereFromFile(self):
        with open(self.file, "r") as f:
            rows = f.readlines()
            newrows = []
            for row in rows:
                newrows.append(row.rstrip().split(","))
            rows = newrows
            for i in range(len(rows)):
                for j in range(len(rows[i])):
                    self.setXY(j, i, rows[i][j])


# if __name__ == __main__:
#     laby = Labyrinthe(20,10)
#     laby.setXY(5,2,1)
#     print(laby.getSize())
#     laby.genereFromFile("laby-01.csv")
#     laby.affiche()


