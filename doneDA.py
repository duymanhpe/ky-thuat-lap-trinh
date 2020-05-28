from tkinter import *
import time
import random

#tao hình bóng, hướng bóng và tốc độ bóng chạy, xử lý khi va chạm
class Ball:
    def __init__(seft, canvas, color, thanh, thanh1):
        seft.canvas = canvas
        seft.thanhtruot = thanh;
        seft.thanhtruot1 = thanh1
        seft.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        seft.canvas.move(seft.id, 100, 200)
        start = [-3, -2, -2, 1, 2, 3]
        random.shuffle(start)
        seft.x = start[0];
        seft.y = 1;
        seft.canvas_height = 600;
        seft.canvas_width = 400;
        seft.over = False
        seft.diem = 0
        seft.diem1 = 0
#bóng va chạm với thanh trượt dưới
    def vatram(seft, pos):
        pos_thanhtruot = seft.canvas.coords(seft.thanhtruot.id)
        if pos[0] >= pos_thanhtruot[0] and pos[2] <= pos_thanhtruot[2]:
            if pos[1] >= pos_thanhtruot[1] and pos[3] <= pos_thanhtruot[3]:
                seft.diem += 1
                print('Mạnh dzai',seft.diem,'điểm')
                return True
        return False
#bóng va chạm với thanh trượt trên
    def vacham(seft, pos):
        pos_thanhtruot1 = seft.canvas.coords(seft.thanhtruot1.id1)
        if pos[0] >= pos_thanhtruot1[0] and pos[0] <= pos_thanhtruot1[2]:
            if pos[1] >= pos_thanhtruot1[1] and pos[3] <= pos_thanhtruot1[3]:
                seft.diem1 += 1
                print('đối thủ',seft.diem1,'điểm')
                return True
        return False
#bóng chạy trong canvas
    def draw(seft):
        seft.canvas.move(seft.id, seft.x, seft.y)
        pos = seft.canvas.coords(seft.id)
        if pos[1] <= 0:
            seft.over = True
        if pos[3] >= seft.canvas_height:
            seft.over = True
        if seft.vatram(pos) == True:
            seft.y = -3;
        if seft.vacham(pos) == True:
            seft.y = 3;
        if pos[0] <= 0:
            seft.x = 3;
        if pos[2] >= seft.canvas_width:
            seft.x = -3;

#thanh trượt dưới
class thanhtruot:
    def __init__(seft, canvas, color):
        seft.canvas = canvas
        seft.id = canvas.create_rectangle(0, 0, 100, 20, fill=color)
        seft.canvas.move(seft.id, 300, 500)


        seft.canvas.bind_all('<KeyPress-Left>', seft.trai)
        seft.canvas.bind_all('<KeyPress-Right>', seft.phai)



        seft.x = 0;
        seft.y = 0;

    def draw(seft):
        seft.canvas.move(seft.id, seft.x, seft.y)

    def trai(seft, event):
        seft.x = -2;

    def phai(seft, event):
        seft.x = 2;

#thanh tren
class thanhtruot1:
    def __init__(seft, canvas, color):
        seft.canvas = canvas
        seft.id1 = canvas.create_rectangle(0, 0, 100, 20, fill=color)
        seft.canvas.move(seft.id1, 300,70)

        seft.canvas.bind_all('<KeyPress-a>', seft.trai)
        seft.canvas.bind_all('<KeyPress-d>', seft.phai)

        seft.x = 0;
        seft.y = 0;

    def draw(seft):
        seft.canvas.move(seft.id1, seft.x, seft.y)

    def trai(seft, event):
        seft.x = -2;

    def phai(seft, event):
        seft.x = 2;



tk = Tk()
tk.title("game for you")
tk.resizable(0, 0)
can = Canvas(tk, width=400, height=600)
can.pack()
thanh = thanhtruot(can, "blue")
thanhtren = thanhtruot1(can, 'Blue',)
bong = Ball(can, "red", thanh, thanhtren)
#?????????
while 1:
    if bong.over != True:
        bong.draw()
        thanh.draw()
        thanhtren.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    else:
        break;
print("game over")
