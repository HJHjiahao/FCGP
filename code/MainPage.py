import tkinter as tk
import time

from data import data
from MallPage import MallPage


class MainPage(object):
    def __init__(self, master=None, conn=None, ac=' '):
        self.root = master
        self.root.geometry('1085x800')
        self.root.title("-----FC游戏平台------")
        self.root.resizable(width=False, height=False)

        self.conn = conn
        # 通过cursor创建游标
        self.cursor = self.conn.cursor()

        self.account = ac

        self.create_page()

    def create_page(self):
        self.toplevel=tk.Label(self.root,text="FCGP",font=('微软雅黑', 20, 'bold'),relief= tk.GROOVE)
        self.toplevel.grid(row=0,column=0,columnspan=4,ipadx=504,stick=tk.W)
        self.person_button = tk.Button(self.root,text="查看个人信息",font=('微软雅黑', 30, 'bold'),command=self.go_PersonPage)
        self.person_button.grid(row=1,rowspan=2,column=0,ipady=5,stick=tk.W)
        self.gamelevel=tk.Label(self.root,text="游戏列表",font=('微软雅黑', 30, 'bold'),relief= tk.GROOVE)
        self.gamelevel.grid(row=3,column=0,ipadx=57,ipady=10,stick=tk.W)
        global bag
        bag=tk.PhotoImage(file='bag.gif')
        self.bag_button = tk.Button(self.root,text="查看背包",font=('微软雅黑', 30, 'bold'),image=bag,command=self.go_BagPage)
        self.bag_button.grid(row=1,rowspan=2,column=1,ipady=5,ipadx=120,stick=tk.W)
        global mall
        mall=tk.PhotoImage(file='mall.gif')
        self.mallbutton = tk.Button(self.root,text="商城",font=('微软雅黑', 30, 'bold'),image=mall,command=self.go_MallPage)
        self.mallbutton.grid(row=1,rowspan=2,column=2,ipady=5,ipadx=100,stick=tk.W)

        StopWatch(self.root, self.conn, self.account)
        Watch(self.root)

        self.frame1=tk.Frame(self.root,width=850,height=700)
        self.frame1.grid(row=3,column=1,rowspan=200,columnspan=300,stick=tk.N)
        self.frame1.grid_propagate(0)
        self.game1frame=tk.Frame(self.root,width=100,height=700)
        self.game1=tk.Button(self.root,text="兔獾大作战",font=('微软雅黑', 30, 'bold'),command=self.go_game1)
        self.game1.grid(row=4,ipadx=20,ipady=10,stick=tk.W)
        self.game2frame=tk.Frame(self.root,width=850,height=700)
        self.game2=tk.Button(self.root,text="坦克大战",font=('微软雅黑', 30, 'bold'),command=self.go_game2)
        self.game2.grid(row=5,ipadx=40,ipady=10,stick=tk.W)
        self.personframe=tk.Frame(self.root,width=850,height=700)
        self.bagframe=tk.Frame(self.root,width=850,height=700)

    def go_PersonPage(self):
        self.game1frame.grid_forget()
        self.bagframe.grid_forget()
        self.game2frame.grid_forget()
        self.personframe.grid(row=3, column=1, rowspan=200, columnspan=300, stick=tk.N)
        self.personframe.grid_propagate(0)
        self.pnamelevel = tk.Label(self.personframe, text="角色名称:", font=('微软雅黑', 30, 'bold'), relief=tk.GROOVE)
        self.pnamelevel.grid(row=5, column=5)
        pname = tk.StringVar()
        string = data.name
        pname.set(string)
        self.pnamenumber = tk.Label(self.personframe, textvariable=pname, font=('微软雅黑', 30, 'bold'))
        self.pnamenumber.grid(row=5, column=6)
        self.pointlevel = tk.Label(self.personframe, text="账号积分:", font=('微软雅黑', 30, 'bold'), relief=tk.GROOVE)
        self.pointlevel.grid(row=6, column=5)
        pnumber = tk.IntVar()
        number = data.number
        pnumber.set(number)
        self.pnamenumber = tk.Label(self.personframe, textvariable=pnumber, font=('微软雅黑', 30, 'bold'))
        self.pnamenumber.grid(row=6, column=6)
        self.personx = tk.Label(self.personframe)
        self.personx.grid(row=0, column=0, ipadx=800, columnspan=100)
        self.persony = tk.Label(self.personframe)
        self.persony.grid(row=0, column=0, ipady=800, rowspan=100)

    def go_BagPage(self):
        self.game1frame.grid_forget()
        self.personframe.grid_forget()
        self.game2frame.grid_forget()
        self.bagx = tk.Label(self.bagframe)
        self.bagx.grid(row=0, column=0, ipadx=800, columnspan=100)
        self.bagy = tk.Label(self.bagframe)
        self.bagy.grid(row=0, column=0, ipady=800, rowspan=100)
        self.bagframe.grid(row=3, column=1, rowspan=200, columnspan=300, stick=tk.N)
        self.bagframe.grid_propagate(0)
        self.propname1 = tk.Label(self.bagframe, text="道具名称", font=('微软雅黑', 30, 'bold'), relief=tk.GROOVE)
        self.propname1.grid(row=0, column=5)
        self.propname2 = tk.Label(self.bagframe, text="道具数量", font=('微软雅黑', 30, 'bold'), relief=tk.GROOVE)
        self.propname2.grid(row=0, column=15)
        self.propname3 = tk.Label(self.bagframe, text="双倍", font=('微软雅黑', 30, 'bold'), relief=tk.GROOVE)
        self.propname3.grid(row=1, column=5)
        prop1number = tk.IntVar()
        self.propnumber3 = tk.Label(self.bagframe, textvariable=prop1number, font=('微软雅黑', 30, 'bold'),
                                    relief=tk.GROOVE)
        self.propnumber3.grid(row=1, column=15)
        self.propuse3 = tk.Button(self.bagframe, text="使用", font=('微软雅黑', 30, 'bold'))
        self.propuse3.grid(row=1, column=25)

    # def gopropuse3(self):
    def go_MallPage(self):
        Mallwindow = tk.Toplevel(self.mallbutton)
        MallPage(Mallwindow)

    def go_game1(self):
        self.personframe.grid_forget()
        self.bagframe.grid_forget()
        self.game2frame.grid_forget()
        self.game1x = tk.Label(self.game1frame)
        self.game1x.grid(row=0, column=0, ipadx=800, columnspan=100)
        self.game1y = tk.Label(self.game1frame)
        self.game1y.grid(row=0, column=0, ipady=800, rowspan=100)
        self.game1frame.grid(row=3, column=1, rowspan=200, columnspan=300, stick=tk.W)
        self.game2level1 = tk.Label(self.game1frame, text="兔獾大作战是一款以兔獾对战为主题的射击游戏", font=('微软雅黑', 20, 'bold'))
        self.game2level1.grid(row=1, columnspan=15, stick=tk.W)
        self.game2level1 = tk.Label(self.game1frame, text="兔子通过射箭抵御獾的进攻保卫自己的四个堡垒", font=('微软雅黑', 20, 'bold'))
        self.game2level1.grid(row=3, stick=tk.W)
        global setupphoto
        setupphoto = tk.PhotoImage(file='setup.gif')
        self.game1setup = tk.Button(self.game1frame, image=setupphoto, command=self.setupgame1)
        self.game1setup.grid(row=23, column=6, stick=tk.NW)
    def setupgame1(self):
        import G1.Game1
        # game1window = tk.Toplevel(self.game1setup)
        G1.Game1.main()

    def go_game2(self):
        self.personframe.grid_forget()
        self.bagframe.grid_forget()
        self.game1frame.grid_forget()
        self.game2x = tk.Label(self.game2frame)
        self.game2x.grid(row=0, column=0, ipadx=800, columnspan=100)
        self.game2y = tk.Label(self.game2frame)
        self.game2y.grid(row=0, column=0, ipady=800, rowspan=100)
        self.game2frame.grid(row=3, column=1, rowspan=200, columnspan=300, stick=tk.W)
        self.game2level1 = tk.Label(self.game2frame, text="坦克大战是一款以坦克对战为主题的第三人称射击游戏", font=('微软雅黑', 20, 'bold'))
        self.game2level1.grid(row=1, columnspan=15, stick=tk.W)
        self.game2level1 = tk.Label(self.game2frame, text="你将操纵你的坦克保卫基地消灭其他的坦克", font=('微软雅黑', 20, 'bold'))
        self.game2level1.grid(row=3, stick=tk.W)
        global setupphoto
        setupphoto = tk.PhotoImage(file='setup.gif')
        self.game2setup = tk.Button(self.game2frame, image=setupphoto, command=self.setupgame2)
        self.game2setup.grid(row=23, column=8,stick=tk.W)

    def setupgame2(self):
        import G2.Game2
        # game2window = tk.Toplevel(self.game2setup)
        G2.Game2.main()


class Watch(object):  # 显示实时时间
    def __init__(self, master=None):
        self.root = master

        self.timestr1 = tk.StringVar()  # 年月日
        self.timestr2 = tk.StringVar()  # 时分秒
        self.create_watch()

    def create_watch(self):
        page = tk.Frame(self.root)
        page.grid(row=2,column=3,ipadx=50,stick=tk.E)

        self.timestr1.set(str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
        self.timestr2.set(str(time.strftime('%H:%M:%S', time.localtime(time.time()))))

        tk.Label(page, textvariable=self.timestr1).grid()
        tk.Label(page, textvariable=self.timestr2).grid()
        self.get_time()

    def get_time(self):  # 获取实时时间
        self.timestr1.set(str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
        self.timestr2.set(str(time.strftime('%H:%M:%S', time.localtime(time.time()))))
        self.root.after(1000, self.get_time)  # 每秒递归调用


class StopWatch(object):  # 显示本次登录在线时间
    def __init__(self, master=None, conn=None, ac=' '):
        self.root = master

        self._start = time.time()
        self.timestr = tk.StringVar()

        self.conn = conn
        # 通过cursor创建游标
        self.cursor = self.conn.cursor()

        self.account = ac

        self.create_stop()

    def create_stop(self):
        page = tk.Frame(self.root)
        page.grid(row=1,column=3,stick=tk.W)

        tk.Label(page, textvariable=self.timestr).grid()
        self.get_time()

    def get_time(self):
        elap = time.time() - self._start  # 时间差
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)

        # if int(elap) % 60 == 0:
        #    self.cursor.execute('''select u_time from USEER where u_id=('%s');'''
        #                        % self.account)
        #    result = self.cursor.fetchone()  # 取出该账号的在线时长
        #    self.cursor.execute('''update USEER set u_time=('%s')  where u_id=('%s');'''
        #                        % (result[0]+1, self.account))

        self.timestr.set('本次登录在线时长 %02d:%02d' % (minutes, seconds))
        self.root.after(1, self.get_time)  # 每隔1ms调用函数自身获取时间