from tkinter import *
from tkinter import messagebox as mb
import time
import random

t = Tk()
t.title("Virus fight")
t.resizable(0, 0)
t.wm_attributes("-topmost", 1)
c = Canvas(t, width = 800, height = 600, bd = 0, highlightthickness=0,  bg = 'green')
c.pack()
t.update()

class protector:
    def __init__(self, canvas, moe):
        self.canvas = canvas
        self.id = canvas.create_image(10,10, anchor= NW,  image = moe)
        canvas.move(self.id, random.randint(10,790), random.randint(10, 290))
        starts = [ -3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        random.shuffle(starts)
        self.y = starts[0]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) 
        if pos[1] <= 0:
            self.y = starts = random.randint(5, 10)
        if pos [1] >= self.canvas_height - 100:
            self.y = starts = random.randint(-10, -5)
        if pos [0] <= 0:
            self.x = starts = random.randint(5, 10)
        if pos [0] >= self.canvas_width - 100:
            self.x =starts = random.randint(-10, -5)
class viruses:
    def __init__(self, canvas, moe):
        self.canvas = canvas
        self.id = canvas.create_image(10,10, anchor= NW,  image = moe)
        canvas.move(self.id, random.randint(10,790), random.randint(10, 290))
        starts = [ -3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        random.shuffle(starts)
        self.y = starts[0]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = random.randint(1, 5)
        if pos [1] >= self.canvas_height - 50:
            self.y = random.randint(-5, -1)
        if pos [0] <= 0:
            self.x = random.randint(1, 5)
        if pos [0] >= self.canvas_width - 50:
            self.x = random.randint(-5, -1)

    def Check_contakt(self,p_x,p_y):
        pos = self.canvas.coords(self.id)
        if pos[0] > (p_x - 45.00) and pos[0] < (p_x + 45.00) and pos[1] > (p_y - 45.00) and pos[1] < (p_y + 45.00):       
          return 1
        else:
          return 0
skins = (PhotoImage(file='vv.png'),
         PhotoImage(file='vv1.png'),
         PhotoImage(file='vv2.png'),
         PhotoImage(file='vv3.png'))
img= PhotoImage(file='Leucocyte.png')
virus_list = []
pp= protector(c,img)
virus_list.append(viruses(c, skins[random.randint(0,3)]))  

NV_Time = time.time()
Game_time = time.time()
NV_period = 3.00
while 1:
    pp.draw();
    p_pos = c.coords(pp.id)
    i=0
    for x in virus_list:
        if x.Check_contakt(p_pos[0],p_pos[1]) == 1:
           c.delete(virus_list.pop(i).id)
        else:
           x.draw()
           i = i + 1        
    if time.time() - NV_Time >= NV_period:
        virus_list.append(viruses(c, skins[random.randint(0,3)]))  
        NV_Time = time.time()
    ## Пришвидшуєм появу вірусів кожні десять секунд
    if time.time() - Game_time >= 10.00 and NV_period > 1:
      
      NV_period = NV_period - 1
      Game_time = time.time()

    if len(virus_list) >= 9:
        m = mb.showinfo ('Журбинка', 'Занадто багато вірусів. Ти скоро помреш')
        break
    elif  len(virus_list) == 0:
        m = mb.showinfo('Ура!!!!!','Ти виздоровів і готовий йти на роботу')
        break
    t.update_idletasks()
    t.update()
    time.sleep(0.01)
