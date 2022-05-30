from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # self.bg=ImageTk.PhotoImage(file=r"C:\Desktop\Images\login_bg.jpg")

        # lbl_bg=Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open("./Images/login_logo.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)  # Antialias is imp
        self.photoimage1 = ImageTk.PhotoImage(img1)

        lbling1 = Label(self.root, image=self.photoimage1,
                        bg="black", borderwidth=0)
        lbling1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
