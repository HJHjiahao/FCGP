import tkinter as tk
import RegisterPage
import LoginPage

from tkinter import messagebox


def answ(page, text1, text2, text3, textvariable, row):
    tk.Label(page, text='        ').grid(row=row, column=0)  # 占空列
    tk.Label(page, text=text1, font=('微软雅黑', 10, 'bold')).grid(
        row=row, column=1, )
    tk.Label(page, text=text2, font=('微软雅黑', 10, 'bold')).grid(
        row=row, column=2, )

    tk.Label(page, text=text3, font=('微软雅黑', 10, 'bold'), ).grid(
        row=row + 1, column=1, )
    tk.Entry(page, textvariable=textvariable).grid(
        row=row + 1, column=2, )


class RecoverPage(object):
    def __init__(self, master=None, conn=None):
        self.root = master
        self.root.geometry('300x380')
        self.root.resizable(width=False, height=False)

        self.conn = conn
        # 通过cursor创建游标
        self.cursor = self.conn.cursor()

        self.account = tk.StringVar()
        self.password = tk.StringVar()
        self.password_confirm = tk.StringVar()
        self.q = ['您曾经就读小学的名字是什么？',
                  '您父母相识的城市名字是什么？',
                  '您最喜欢的电视剧名字是什么？']
        self.a = [' ', ' ', ' ']
        self.answer1 = tk.StringVar()
        self.answer2 = tk.StringVar()
        self.answer3 = tk.StringVar()

        self.get_ac()
        # self.create_page()

    def get_ac(self):
        page = tk.Frame(self.root)
        page.grid()

        tk.Label(page).grid(row=0, )  # 占空行
        RegisterPage.info(page, text='账      号: ', textvariable=self.account, row=1)

        tk.Label(page).grid(row=2, )  # 占空行
        tk.Label(page, text='        ').grid(row=3, column=0)  # 占空列
        tk.Label(page, text='        ').grid(row=3, column=1)  # 占空列
        tk.Button(page, text='修改账号密码', font=('微软雅黑', 12, 'bold', 'underline')
                  , command=self.get_q).grid(row=3, column=2)

    def create_page(self, ac):
        page = tk.Frame(self.root)
        page.grid()
        '''
        tk.Label(page).grid(row=0, )  # 占空行
        RegisterPage.info(page, text='账      号: ', textvariable=self.account, row=1)
        '''
        tk.Label(page, text='        ').grid(row=1, column=0)  # 占空列
        tk.Label(page, text='账      号: ', font=('微软雅黑', 10, 'bold')).grid(
            row=1, column=1, )
        tk.Label(page, text=ac, font=('微软雅黑', 10, 'bold')).grid(
            row=1, column=2, )

        RegisterPage.info(page, text='新  密 码: ', textvariable=self.password, row=2)
        RegisterPage.info(page, text='确认密码: ', textvariable=self.password_confirm, row=3)

        tk.Label(page).grid(row=4, )  # 占空行
        answ(page, text1='验证问题1:', text2=self.q[0], text3='问题1答案:',
             textvariable=self.answer1, row=5)
        answ(page, text1='验证问题2:', text2=self.q[1], text3='问题2答案:',
             textvariable=self.answer2, row=7)
        answ(page, text1='验证问题3:', text2=self.q[2], text3='问题3答案:',
             textvariable=self.answer3, row=9)

        tk.Label(page).grid(row=11, )  # 占空行
        tk.Button(page, text='修改密码', font=('微软雅黑', 10, 'bold', 'underline'),
                  command=self.recover).grid(row=12, column=2)
        tk.Button(page, text='返回登录', font=('微软雅黑', 10, 'bold', 'underline'),
                  command=self.return_login).grid(row=13, column=2)

    # 账号是否已注册过
    def ac_exist(self, ac):
        self.cursor.execute("select u_id from USEER")
        result = self.cursor.fetchall()
        flag = False
        name_list = []
        for data in result:
            sdata = "".join(data)
            name_list.append(sdata)
        if ac in name_list:
            flag = True
        return flag

    # 获得账号之前选择的问题和答案
    def get_q(self):
        ac = self.account.get()
        if not ac:
            tk.messagebox.showinfo(message='Error,your account is empty.try again.')
        elif not self.ac_exist(ac):
            tk.messagebox.showinfo(message='Error,your account does not exist.try again.')
        else:
            self.cursor.execute('''select U_question1,U_answer1,
                      U_question2,U_answer2,
                      U_question3,U_answer3 from USEER where u_id=('%s');''' % ac)
            result = self.cursor.fetchone()
            # print(result)

            self.q[0] = result[0]
            self.q[1] = result[2]
            self.q[2] = result[4]
            self.a[0] = result[1]
            self.a[1] = result[3]
            self.a[2] = result[5]

            for widget in self.root.winfo_children():
                widget.destroy()
            self.create_page(ac)

    # 验证
    def recover(self):
        pw = self.password.get()
        pwc = self.password_confirm.get()
        a1 = self.answer1.get()
        a2 = self.answer2.get()
        a3 = self.answer3.get()

        if pw == pwc:
            if a1 == self.a[0]:
                if a2 == self.a[1]:
                    if a3 == self.a[2]:
                        tk.messagebox.showinfo(message='Successfully modified!')
                        self.return_login()
                    else:
                        tk.messagebox.showinfo(message='Error,your third answer is wrong.try again.')
                else:
                    tk.messagebox.showinfo(message='Error,your second answer is wrong.try again.')
            else:
                tk.messagebox.showinfo(message='Error,your first answer is wrong.try again.')
        else:
            tk.messagebox.showinfo(message='Error,the password you entered twice is different.try again.')

    # 返回登录界面
    def return_login(self):
        self.root.destroy()

        root = tk.Tk()
        root.title('FC Game Platform')
        LoginPage.LoginPage(root, self.conn)
