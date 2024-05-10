from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from PIL import Image, ImageTk

root = tb.Window(themename='cyborg')

root.title("BMI Calculator")
root.geometry("600x600")
root.resizable(width=False, height=False)


#function to calculate BMI
def bmi_calc():
    h = float(Height.get())
    w = float(Weight.get())

    bmi = round(float((w/h**2)*10000), 1)
    label_c5.config(text=bmi)

    if bmi <= 18.5:
        label_c1.config(text="Underweight!")
        print(label_c1)

    elif 18.6 < bmi <= 24.9:
        label_c2.config(text="Normal weight!")
        print(label_c2)

    elif 25 < bmi <= 29.9:
        label_c3.config(text="Overweight!")
        print(label_c3)

    else:
        label_c4.config(text="Obese!")
        print(label_c4)


#icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

#label
top_label = tb.Label(text="BMI Calculator", font=("Bebas Kai", 35), bootstyle="primary", background="black")
top_label.pack(pady=10)

H1_label = tb.Label(text="Height(cm)", font=("Bebas Kai", 18), bootstyle="primary")
H1_label.place(x=80, y=68)

H2_label = tb.Label(text="Weight(kg)", font=("Bebas Kai", 18), bootstyle="primary")
H2_label.place(x=280, y=68)

#two box
box = PhotoImage(file="box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)

#bottom box
Label(root, width=72, height=15, background="lightblue").pack(side=BOTTOM)

#scale
scale3 = PhotoImage(file="scale.png")
Label(root, image=scale3, bg='white').place(x=20, y=300)

##########Slider1##############
current_value = tb.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    Height.set(get_current_value())
    size = int(float(get_current_value()))
    img = (Image.open("man.png"))
    resized_image = img.resize((50, 10+size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550-size)
    secondimage.image = photo2


#command to change bag colour
scale = tb.Scale(bootstyle='primary')
#scale.configure("TScale", background="black")
scale.configure(from_=0, to=300, orient='horizontal', style="TScale", command=slider_changed, variable=current_value)
scale.place(x=80, y=250)

###############################


###############Slider2##################
current_value2 = tb.DoubleVar()


def get_current_value2():
    return '{: .2f}'.format(current_value2.get())


def slider_changed2(event):
    Weight.set(get_current_value2())


scale2 = tb.Scale(bootstyle='primary')
#scale2.configure("TScale", background="black")
scale2.configure(from_=0, to=300, orient='horizontal', style="TScale", command=slider_changed2, variable=current_value2)
scale2.place(x=300, y=250)

#################################


#entry box
Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=10, font="Bebaskai 20", background="white",
               fg="Black", bd=23, justify="center",)
height.place(x=35, y=160)
Height.set(get_current_value())

#entry box 2
weight = Entry(root, textvariable=Weight, width=10, font="Bebaskai 20", background="white",
               fg="Black", bd=23, justify="center")
weight.place(x=255, y=160)
Weight.set(get_current_value2())

#man image
secondimage = Label(root, bg="lightblue")
secondimage.place(x=70, y=530)

Button(root, text="view Report", width=15, height=2, font="Bebaskai 10", bg="black", fg="Black",
       command=bmi_calc).place(x=300, y=340)

#labels
label_c1 = tb.Label(root, bootstyle="danger", font="Bebaskai 10")
label_c1.place(x=280, y=430)

label_c2 = tb.Label(root, bootstyle="success", font="Bebaskai 10")
label_c2.place(x=280, y=430)

label_c3 = tb.Label(root, bootstyle="warning", font="Bebaskai 10")
label_c3.place(x=280, y=430)

label_c4 = tb.Label(root, bootstyle="danger", font="Bebaskai 10")
label_c4.place(x=280, y=430)

label_c5 = tb.Label(root, bootstyle="primary", font="Bebaskai 60")
label_c5.place(x=125, y=305)

root.mainloop()
