from tkinter import *
import time
import threading
WINDOW_X = "600"
WINDOW_Y = "400"

class Pelota():
    def __init__(self,master):
        self._listpos=[int(int(WINDOW_X)/2),int(int(WINDOW_Y)/2)]
        self._a=0
        self.fball=Frame(master, width=10,height=10,bg="blue")
        self.fball.place(x=int(int(WINDOW_X)/2),y=int(int(WINDOW_Y)/2))
        self._direction="down"
        self._side="center"
        
    def change_direction(self,direction,side):
        self._direction=direction
        self._side=side
    
    @property
    def listpos(self):
        return self._listpos
    @property
    def side(self):
        return self._side
    
    def listpos_setter(self,x,y):
        self._listpos=[x,y]
        self.fball.place(x=x,y=y)
    
        
        
class Raqueta():
    def __init__(self,master):
        self._init_pos_x=int(int(WINDOW_X)/2)-40
        self._init_pos_y=int(int(WINDOW_Y)-50)
        self._fraq = Frame(master,width=100,height=10,bg="green")
        self._fraq.place(x=int(int(WINDOW_X)/2)-40,y=int(int(WINDOW_Y)-50))
    def change_pos(self,sense):
        if sense==1 and self._init_pos_x<int(WINDOW_X)-100:
            self._init_pos_x+=5
            self._fraq.place(x=self._init_pos_x,y=int(int(WINDOW_Y)-50))
            #print(self._fraq.winfo_rootx()+10)
        elif sense==2 and self._init_pos_x>0:
            self._init_pos_x-=5
            self._fraq.place(x=self._init_pos_x,y=int(int(WINDOW_Y)-50))
            #print(self._fraq.winfo_rootx()-10)
    @property
    def posicion(self):
        return self._init_pos_x
    
    @property
    def posicion_y(self):
        return self._init_pos_y

        
def animacion():
    p1.change_direction("down","right")
    reverse=False
    while True:
        l = p1.listpos
        if reverse:
            if l[1] == 0:
                print(1)
                reverse=False
                print(r1.posicion, r1.posicion_y)
                if p1.side == "left":
                    p1.change_direction("down","left")
                else:
                    p1.change_direction("down","right")
            if p1.side == "left":
                    if l[0] + 10 > int(WINDOW_X):
                        p1.listpos_setter(l[0]-1,l[1]-1)
                        p1.change_direction("up","left")
                        
                    elif l[0] < 0:
                        p1.listpos_setter(l[0]+1,l[1]-1)
                        p1.change_direction("up","right")
                        print(p1.listpos)
                        time.sleep(0.01)
                    p1.listpos_setter(l[0]-1,l[1]-1)
                    print(p1.listpos)
                    time.sleep(0.01)
                        
            elif p1.side == "right":
                    if l[0] + 10 > int(WINDOW_X):
                        p1.listpos_setter(l[0]-1,l[1]-1)
                        p1.change_direction("up","left")
                        print(p1.listpos)
                        time.sleep(0.01)
                    elif l[0] < 0:
                        p1.listpos_setter(l[0]+1,l[1]-1)
                        p1.change_direction("up","right")
                        print(p1.listpos)
                        time.sleep(0.01)
                    p1.listpos_setter(l[0]+1,l[1]-1)
                    print(p1.listpos)
                    time.sleep(0.01)
                    #elif p1.side == "right":
                        #p1.listpos_setter(l[0]+1,l[1]+1)
                        
                        #print(p1.listpos)
                        #time.sleep(0.01)
                        #print(r1.posicion,l[0],r1.posicion+100)
            
        elif reverse == False:
            if r1.posicion-10 < l[0] and l[0] < r1.posicion+100 and l[1] == r1.posicion_y-10:
                if p1.side=="right":
                    p1.change_direction("up","right")
                else:
                    p1.change_direction("up","left")
                reverse=True
                print(2)
            else:
                if p1.side == "left":
                    if l[0] + 10 > int(WINDOW_X):
                        p1.listpos_setter(l[0]-1,l[1]+1)
                        p1.change_direction("down","left")
                        
                    elif l[0] < 0:
                        p1.listpos_setter(l[0]+1,l[1]+1)
                        p1.change_direction("down","right")
                        print(p1.listpos)
                        time.sleep(0.01)
                    p1.listpos_setter(l[0]-1,l[1]+1)
                    print(p1.listpos)
                    time.sleep(0.01)
                        
                elif p1.side == "right":
                    if l[0] + 10 > int(WINDOW_X):
                        p1.listpos_setter(l[0]-1,l[1]+1)
                        p1.change_direction("down","left")
                        print(p1.listpos)
                        time.sleep(0.01)
                    elif l[0] < 0:
                        p1.listpos_setter(l[0]+1,l[1]+1)
                        p1.change_direction("down","right")
                        print(p1.listpos)
                        time.sleep(0.01)
                    p1.listpos_setter(l[0]+1,l[1]+1)
                    print(p1.listpos)
                    time.sleep(0.01)
                    #elif p1.side == "right":
                        #p1.listpos_setter(l[0]+1,l[1]+1)
                        
                        #print(p1.listpos)
                        #time.sleep(0.01)
                        #print(r1.posicion,l[0],r1.posicion+100)
                    
            
            
def key(event):
    print(event.keysym)
    if event.keysym=="Right":
        r1.change_pos(1)
    elif event.keysym=="Left":
        r1.change_pos(2)
    print(r1.posicion)

t1 = threading.Thread(name="animation",target=animacion)
root = Tk()
root.geometry("{}x{}".format(WINDOW_X,WINDOW_Y))
p1 = Pelota(root)
r1 = Raqueta(root)

#f1 = Frame(root, bg="green", width=100,height=10)
#f1.place(x=100,y=50)

t1.start()

root.bind_all('<Key>',key)
root.mainloop()
