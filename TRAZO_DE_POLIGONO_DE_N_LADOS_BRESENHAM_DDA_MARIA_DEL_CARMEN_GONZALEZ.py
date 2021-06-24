from turtle import Turtle
import subprocess
import bresenham

def main():
    subprocess.call(["cmd.exe","/C","cls"])
    t=Turtle()
    t.hideturtle()
    arregloX = []
    arregloY = []
    x1= 0
    y1= 0
    x2= 20
    y2= 20
    tipo = int(input("ELIGUE EL ALGORITMO QUE GRAFICARA \n1.DDA \n2.BRESENHAM\n=>"))

    
    dx= abs(x2-x1)
    dy= abs(y2-y1)
    p= (2 * dy) - dx

    t.color("white")
    t.setx(dx)
    t.sety(dy)
    t.color("black")

    t.pensize("5")
    n= int(input("REGISTRA EL NUMERO DE LADOS: "))
    ang=180-(((n-2)/n)*180)#CALCULAMOS EL ANGULO DE GIRO
    
    if tipo == 1:
        if n <= 306:
            for i in range(n):
                t.left(ang)
                x1=x1+1
                if p < 0:
                    p = p + (2 * dy)
                else:
                    p = p + (2 * dy) - (2 * dx)
                    y1=y1+1
                print(x1, ',', y1)
                t.fd(p)
        else:
            print("LOS LADOS NO PUEDEN SER MAYORES A 360")
    if tipo == 2:
        if n <= 306:
            for i in range(n):
                t.left(ang)
                x1=x1+1
                if p < 0:
                    p = p + (2 * dy)
                else:
                    p = p + (2 * dy) - (2 * dx)
                    y1=y1+1
                print(x1, ',', y1)
                t.fd(p)
        else:
            print("LOS LADOS NO PUEDEN SER MAYORES A 360")
        

    

if __name__== '__main__':
    main()