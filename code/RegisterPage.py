import tkinter as tk
from tkinter import ttk
import LoginPage
from tkinter import messagebox


# 获取信息
def info(page, text, textvariable, row):
    tk.Label(page, text='        ').grid(row=row, column=0)  # 占空列
    tk.Label(page, text=text, font=('微软雅黑', 10, 'bold')).grid(
        row=row, column=1, )
    tk.Entry(page, textvariable=textvariable, ).grid(
        row=row, column=2, )


class RegisterPage(object):
    def __init__(self, master=None, conn=None):
        self.root = master
        self.root.geometry('300x400')
        self.root.resizable(width=False, height=False)

        self.conn = conn
        # 通过cursor创建游标
        self.cursor = self.conn.cursor()

        self.username = tk.StringVar()
        self.account = tk.StringVar()
        self.password = tk.StringVar()
        self.password_confirm = tk.StringVar()
        self.q = ['您曾经就读小学的名字是什么？',
                  '您父母相识的城市名字是什么？',
                  '您最喜欢的电视剧名字是什么？']
        self.answer1 = tk.StringVar()
        self.answer2 = tk.StringVar()
        self.answer3 = tk.StringVar()

        self.create_page()

    def create_page(self):
        page = tk.Frame(self.root)
        page.grid()

        tk.Label(page).grid(row=0, )  # 占空行
        info(page, text='角色名称: ', textvariable=self.username, row=1)
        info(page, text='账      号: ', textvariable=self.account, row=2)
        info(page, text='密      码: ', textvariable=self.password, row=3)
        info(page, text='确认密码: ', textvariable=self.password_confirm, row=4)

        tk.Label(page).grid(row=5, )  # 占空行
        self.ques(page, i=0, text1='验证问题1:', text2='问题1答案:', textvariable=self.answer1, row=6)
        self.ques(page, i=1, text1='验证问题2:', text2='问题2答案:', textvariable=self.answer2, row=8)
        self.ques(page, i=2, text1='验证问题3:', text2='问题3答案:', textvariable=self.answer3, row=10)
        # print(self.q[0])

        tk.Label(page).grid(row=12, )  # 占空行
        tk.Button(page, text='申请注册', font=('微软雅黑', 10, 'bold', 'underline'),
                  command=self.sign_to_FCPG).grid(row=13, column=2)
        tk.Button(page, text='返回登录', font=('微软雅黑', 10, 'bold', 'underline'),
                  command=self.return_login).grid(row=14, column=2)

    # 点击注册之后的事件
    def sign_to_FCPG(self):
        nn = self.account.get()
        np = self.password.get()
        npf = self.password_confirm.get()
        name = self.username.get()
        q1 = self.q[0]
        q2 = self.q[1]
        q3 = self.q[2]
        a1 = self.answer1.get()
        a2 = self.answer2.get()
        a3 = self.answer3.get()

        self.cursor.execute('''select u_id from USEER;''')
        result3 = self.cursor.fetchall()
        name_list = []
        for data in result3:
            sdata = "".join(data)
            name_list.append(sdata)
        self.conn.commit()

        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif not nn:
            tk.messagebox.showinfo(message='Error,your account is empty.try again.')
        elif nn in name_list:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        elif self.q[0] == self.q[1] or self.q[0] == self.q[2] or self.q[1] == self.q[2]:
            tk.messagebox.showinfo(message='Error,your questions are duplicated.try again.')
        else:
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            self.cursor.execute('''insert into USEER(u_id,u_password,
            U_name,U_question1,
            U_answer1,U_question2,
            U_answer2,U_question3,
            U_answer3,U_score,
            U_prop1,U_prop2,
            U_time) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');'''
                                % (nn, np, name, q1, a1, q2, a2, q3, a3, 0, 1, 1, 0))
            self.conn.commit()
            self.return_login()

    def ques(self, page, i, text1, text2, textvariable, row):
        tk.Label(page, text='        ').grid(row=row, column=0)  # 占空列
        tk.Label(page, text=text1, font=('微软雅黑', 10, 'bold')).grid(
            row=row, column=1, )

        comb = ttk.Combobox(page, values=['您曾经就读小学的名字是什么？',
                                          '您父母相识的城市名字是什么？',
                                          '您最喜欢的电视剧名字是什么？',
                                          '您理想的居住城市名字是什么？',
                                          '您读过的最喜欢的书籍是什么'],
                            state="readonly", width=17)
        comb.current(i)
        comb.grid(row=row, column=2)
        tk.Label(page, text=text2, font=('微软雅黑', 10, 'bold'), ).grid(
            row=row + 1, column=1, )
        tk.Entry(page, textvariable=textvariable).grid(
            row=row + 1, column=2, )
        '''
        def go(event):
            self.q[i] = comb.get()
            print(self.q[i])
        '''
        comb.bind("<<ComboboxSelected>>", self.go(i, comb))

    # 获得选中的问题
    def go(self, i, comb):
        self.q[i] = comb.get()

    # 返回登录界面
    def return_login(self):
        self.root.destroy()

        root = tk.Tk()
        root.title('FC Game Platform')
        LoginPage.LoginPage(root, self.conn)
