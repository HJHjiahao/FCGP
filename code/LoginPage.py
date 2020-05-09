import tkinter as tk
from tkinter import messagebox
import RegisterPage
import RecoverPage
import MainPage

import random

from PIL import Image
from PIL import ImageTk
from PIL import ImageDraw
from PIL import ImageFont


# 在画布背景上创建标签
def canvas_label(canvas, text, x, y):
    label = tk.Label(canvas, text=text, font=('微软雅黑', 10, 'bold')
                      )
    canvas.create_window(x, y,  width=50, height=25, window=label)


# 在画布背景上创建按钮
def canvas_button(canvas, text, x, y, size, width, height, command=None):
    button = tk.Button(canvas, text=text, font=('微软雅黑', size, 'bold', 'underline')
                            , command=command)
    canvas.create_window(x, y, width=width, height=height, window=button)


# 在画布背景上创建输入框
def canvas_entry(canvas, text, x, y):
    entry = tk.Entry(canvas, textvariable=text,
                            )
    canvas.create_window(x, y, width=150, height=25, window=entry)


class LoginPage(object):
    def __init__(self, master=None, conn=None):
        self.root = master
        self.root.geometry('400x248')
        self.root.resizable(width=False, height=False)

        self.account = tk.StringVar()
        self.password = tk.StringVar()
        self.captcha = tk.StringVar()
        self.verification_code = None

        self.conn = conn
        # 通过cursor创建游标
        self.cursor = self.conn.cursor()

        self.create_page()

    def create_page(self):
        canvas = tk.Canvas(self.root, width=400, height=248)
        global image_file  # 背景画布
        image_file = tk.PhotoImage(file='bg_login.gif')
        # image_file = ImageTk.PhotoImage(Image.open('bg_login.png'))
        canvas.create_image(0, 0, anchor='nw', image=image_file)
        canvas.grid()

        canvas_label(canvas, '账号: ', 100, 50)
        canvas_entry(canvas, self.account, 200, 50)

        canvas_label(canvas, '密码: ', 100, 90)
        # canvas_entry(canvas, self.password, 200, 90)
        pw = tk.Entry(canvas, textvariable=self.password, show='*')
        canvas.create_window(200, 90, width=150, height=25, window=pw)

        canvas_label(canvas, '验证码: ', 100, 130)
        canvas_entry(canvas, self.captcha, 200, 130)
        global verification_file  # 验证码的值
        verification_file = self.verification()
        vf = tk.Label(canvas, image=verification_file)
        canvas.create_window(200, 160, width=70, height=25, window=vf)

        canvas_button(canvas, '登录', 337, 90, size=12, width=80, height=50,
                      command=self.login)
        canvas_button(canvas, '注册账号', 337, 150, size=10, width=80, height=25,
                      command=self.go_register)
        canvas_button(canvas, '忘记密码', 337, 175, size=10, width=80, height=25,
                      command=self.go_recover)

    def verification(self):
        # 生成验证码的字符
        def rndChar():
            random_num = str(random.randint(0, 9))
            random_low_alpha = chr(random.randint(97, 122))
            random_char = random.choice([random_num, random_low_alpha])
            code_list.append(random_char)
            return random_char

        # 生成验证码的背景颜色
        def rndColorBackGrond():
            return (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))

        # 生成验证码的字符颜色
        def rndColorChar():
            return (random.randint(0, 128), random.randint(0, 128), random.randint(0, 128))

        width = 70
        height = 25
        image = Image.new('RGB', (width, height), (0, 0, 0))
        # 创建Font对象
        font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 20)
        # 创建Draw对象
        draw = ImageDraw.Draw(image)
        # 填充每个像素的颜色
        for x in range(width):
            for y in range(height):
                draw.point((x, y), rndColorBackGrond())
        code_list = []
        for t in range(4):
            draw.text((15 * t + 8, 4), rndChar(), font=font, fill=rndColorChar())
        self.verification_code = "".join(code_list)
        image.save('VerificationCode.jpg', 'JPEG')
        return ImageTk.PhotoImage(file='VerificationCode.jpg')

    '''
    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.grid()
        
        Label(self.page).grid(row=0, )  # 占空行

        Label(self.page, text='               ').grid(row=2, column=0)  # 占空列
        Label(self.page, text='账号: ', font=('微软雅黑', 10, 'bold')).grid(
            row=2, column=1, )
        Entry(self.page, textvariable=self.username).grid(
            row=2, column=2, )

        Label(self.page, text='               ').grid(row=3, column=0)  # 占空列
        Label(self.page, text='密码: ', font=('微软雅黑', 10, 'bold')).grid(
            row=3, column=1, )
        Entry(self.page, textvariable=self.password,
              show='*').grid(row=3, column=2, )

        Label(self.page, text='               ').grid(row=4, column=0)  # 占空列
        Label(self.page, text='验证码: ', font=('微软雅黑', 10, 'bold')).grid(
            row=4, column=1, )
        Entry(self.page, textvariable=self.captcha,
              show='*').grid(row=4, column=2, )

        Label(self.page, text='       ').grid(row=3, column=3)  # 占空列
        Button(self.page, text='登录', font=('微软雅黑', 12, 'bold', 'underline'),
               width=6, height=2, command=self.login_check).grid(row=3, column=4,)

        Label(self.page).grid(row=5, )  # 占空行
        Label(self.page, text='   ').grid(row=6, column=3)
        Button(self.page, text='注册账号', font=('微软雅黑', 10, 'bold', 'underline'),
               ).grid(row=6, column=4)

        Label(self.page, text='   ').grid(row=7, column=3)
        Button(self.page, text='忘记密码', font=('微软雅黑', 10, 'bold', 'underline'),
               ).grid(row=7, column=4)
    '''

    def login(self):  # 点击登录后的事件
        usr_name = self.account.get()
        usr_pwd = self.password.get()
        # print(type(usr_pwd))
        # print(usr_pwd)
        usr_code = self.captcha.get()
        if not usr_name or not usr_pwd or not usr_code:  # 缺少输入
            tk.messagebox.showinfo(message='Error,there is a blank input.try again.')
        else:
            self.cursor.execute("select u_id from USEER")  # 取出全部账号
            result1 = self.cursor.fetchall()

            name_list = []
            for data in result1:
                sdata = "".join(data)
                # print(type(sdata))
                name_list.append(sdata)
            # print(name_list)
            if usr_name not in name_list:
                tk.messagebox.showinfo(message='Error,your have not sign up.try again.')
            self.cursor.execute('''select u_password from USEER where u_id=('%s');''' % (usr_name))
            result2 = self.cursor.fetchone()  # 取出该账号的密码
            # sresult2 = "".join(result2)
            sresult2 = result2[0]
            # print(type(result2))
            # print(type(sresult2))
            # print(sresult2)
            self.conn.commit()
            if usr_code == self.verification_code:
                if usr_pwd == sresult2:
                    tk.messagebox.showinfo(title='Welcome', message='How are you?' + usr_name)
                    self.go_login()
                elif not usr_pwd:
                    tk.messagebox.showinfo(message='Error,your password is empty.try again.')
                else:
                    tk.messagebox.showinfo(message='Error,your password is wrong,try again.')
            elif not usr_name:
                tk.messagebox.showinfo(message='Error,your username is empty.try again.')
            else:
                tk.messagebox.showinfo(message='Error,your code is wrong.try again.')

    def go_login(self):
        self.root.destroy()

        root = tk.Tk()
        root.title('                   FC Game Platform')
        MainPage.MainPage(root, self.conn, self.account)
        root.mainloop()

    def go_register(self):
        # self.root.withdraw()
        self.root.destroy()

        root = tk.Tk()
        root.title('注册账号')
        RegisterPage.RegisterPage(root, self.conn)
        root.mainloop()

    def go_recover(self):
        self.root.destroy()

        root = tk.Tk()
        root.title('找回密码')
        RecoverPage.RecoverPage(root, self.conn)
        root.mainloop()


