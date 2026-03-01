# from tkinter import Tk
# from tkinter import Label
# from tkinter import Checkbutton
# from tkinter import Button
# from tkinter import BooleanVar

# oroot = Tk()
# oroot.geometry("400x300")
# oroot.title("조각 피자 주문 프로그램")

# olabel = Label(oroot, text="피자")
# olabel.pack(side="top")

# pizza = {"치즈 피자":3200, "콤비네이션 피자":3500, "불고기 피자":3600}
# check_value = {}

# i=0
# for key, value in pizza.items():
#     check_value[key] = BooleanVar()
#     ocheckButton = Checkbutton(oroot, text=f"{key}({value}원)", variable=check_value[key])
#     ocheckButton.place(x=0, y=20+i)
#     i += 30

# def order():
#     order_label = Label(oroot, text="주문내역:")
#     order_label.place(x=180, y=130)
#     print(check_value)  
#     pizza_label_text = []
#     total = 0
#     for pizza_key, bool_var in check_value.items():
#         if bool_var.get() == True:
#             pizza_label_text.append(pizza_key)
#             total += pizza[pizza_key]

#     for j in range(len(pizza_label_text)):
#         pizza_label= Label(oroot, text=f"-{pizza_label_text[j]}({pizza[pizza_label_text[j]]}원)")
#         pizza_label.place(x=180, y=150+j*20)
       
#     order_label_total = Label(oroot, text=f"총 가격: {total}원")
#     order_label_total.place(x=180, y=220)     

# oButton = Button(oroot, text="주문", command=order)
# oButton.place(x=180, y=100)

# oroot.mainloop()

# 3주차
# # 1.
# x = 10 
# def example1():
#     x=20
#     print(x)

# example1()
# print(x)

# # 2.
# x = 5
# def example2():
#     global x
#     x=15
#     print(x)

# example2()
# print(x)

# # 3.
# numbers = [42, 17, 23, 56, 9, 34]
# def list_max(num_list):
#     max = num_list[0]
#     for num in num_list:
#         if num > max:
#             max = num
#     print(max)

# list_max(numbers)

# # 4.
# numbers = [42, 17, 23, 56, 9, 34]

# def list_min(num_list):
#     min = num_list[0]
#     for num in num_list:
#         if num < min:
#             min = num
#     print(min)

# list_min(numbers)

# # 5
# class Student:
#     school = "High School"

#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

# s1 = Student("Alice", 1)
# print(Student.school)
# print(s1.school)
# print(s1.name)

# # 6
# from math import factorial
# print(factorial(5))

# # 7
# class Animal:
#     def speak(self):
#         return "Animal speaks"
    
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# dog = Dog()
# sound = dog.speak()
# print(sound)

# # 8
# import tkinter as tk
# from tkinter import messagebox

# def on_button_click():
#     messagebox.showinfo("알림", "버튼이 클릭되었습니다!")

# root = tk.Tk()
# root.title("간단한 Tkinter 앱")
# root.geometry("300x200")

# btn = tk.Button(root, text="클릭하세요", command=on_button_click)
# btn.pack(pady=20)


# root.mainloop()

# 8
import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("알림", "버튼이 클릭되었습니다!")

root = tk.Tk()
root.title("간단한 Tkinter 앱")
root.geometry("300x200")

btn = tk.Button(root, text="클릭하세요", command=on_button_click)
btn.pack(pady=20)


root.mainloop()

