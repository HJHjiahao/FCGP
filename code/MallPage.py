import tkinter as tk
from data import data


class MallPage(object):
    def __init__(self, master=None):
        self.root = master
        root=self.root
        self.root.geometry('800x500')
        self.root.title("-----FC游戏平台------")
        self.root.resizable(width=False, height=False)

        self.create_page()

    def create_page(self):
        self.toplevel=tk.Label(self.root,text="道具商城",font=('微软雅黑', 20, 'bold'),relief= tk.GROOVE)
        self.toplevel.grid(row=0,column=0,stick=tk.W,columnspan=20,ipadx=350)
        self.pointlevel=tk.Label(self.root,text="积分点数:",font=('微软雅黑', 15, 'bold'),relief= tk.GROOVE)
        self.pnumber=tk.IntVar()
        self.pnumber.set(data().number)
        self.pointnum=tk.Label(self.root,textvariable=self.pnumber,font=('微软雅黑', 10, 'bold'))
        self.pointnum.grid(row=1,column=1,stick=tk.W)
        self.pointlevel.grid(row=1,stick=tk.W)
        self.gamelevel=tk.Label(self.root,text="游戏名称",font=('微软雅黑', 30, 'bold'),relief= tk.GROOVE)
        self.gamelevel.grid(row=2,columnspan=2,stick=tk.W,ipadx=36)
        self.game1=tk.Button(self.root,text="坦克大战",font=('微软雅黑', 30, 'bold'),command=self.go_game1)
        self.game1.grid(row=3,ipadx=20,columnspan=2,stick=tk.W)
        self.game2=tk.Button(self.root,text="兔獾大作战",font=('微软雅黑', 30, 'bold'),command=self.go_game2)
        self.game2.grid(row=4,stick=tk.W,columnspan=2)
        self.frame1 = tk.Frame(self.root, width=600, height=460)
        self.frame1.grid(row=1, rowspan=100, column=2)
        self.game1frame=tk.Frame(self.root,width=600,height=460)
        self.game2frame=tk.Frame(self.root,width=600,height=460)
        global prop
        prop = tk.PhotoImage(file='prop.gif')
        self.b1 = tk.Button(self.game1frame, text="双倍buff", font=('微软雅黑', 30, 'bold'), image=prop, command=self.go_b1)
        self.b1.grid(ipadx=50, stick=tk.W)
        self.b2 = tk.Button(self.game2frame, text="双倍buff", font=('微软雅黑', 30, 'bold'), image=prop, command=self.go_b1)
        self.b2.grid(ipadx=50, stick=tk.W)
        #self.b2=tk.Button(self.game1frame,text="增加生命",font=('微软雅黑', 30, 'bold'))
        #self.b2.grid(ipadx=10,stick=tk.W)
    def go_game1(self):
        self.game2frame.grid_forget()
        self.frame1.grid_forget()
        self.game1frame.grid(row=1,rowspan=100,column=2)
        self.game1frame.grid_propagate(0)
        self.b1.grid(row=0,column=0,stick=tk.W)
    def go_game2(self):
        self.game1frame.grid_forget()
        self.frame1.grid_forget()
        self.game2frame.grid(row=1,rowspan=100,column=2)
        self.game2frame.grid_propagate(0)
        self.b2.grid(row=0,column=0,stick=tk.W)
    def go_b1(self):
        self.newwin1= tk.Toplevel(self.b1)
        self.newwin1.geometry('800x500')
        self.newwin1.title("-----FC游戏平台------")
        self.root.resizable(width=False, height=False)
        self.newwin1level=tk.Label(self.newwin1,text="双倍",font=('微软雅黑', 20, 'bold'),relief= tk.GROOVE)
        self.newwin1level.grid(row=0,column=1,ipadx=400,columnspan=10,stick=tk.N)
        self.newwin1y=tk.Label(self.newwin1)
        self.newwin1y.grid(row=0,column=0,rowspan=100,ipady=800,stick=tk.N)
        self.newwin1text=tk.Label(self.newwin1,text="获得双倍积分和生命值",font=('微软雅黑', 20, 'bold'))
        self.newwin1text.grid(row=1,column=1,stick=tk.NW)
        self.newwin1button=tk.Button(self.newwin1,text="兑换",font=('微软雅黑', 30, 'bold'))
        self.newwin1button.grid(row=22,column=9,stick=tk.SE)
    #def goexchange(self):

#MallPage(root)
#root.mainloop()
        
        
        
        

