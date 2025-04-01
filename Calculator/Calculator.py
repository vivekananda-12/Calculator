import tkinter as tk
import math
def Start(val):
    e = entry.get()
    ans = " "
    try:
        # Clear
        if val == "C":
            e = e[0:len(e) - 1]
            entry.delete(0, "end")
            entry.insert(0, e)
            return
        # All clear
        elif val == "CE":
            entry.delete(0, "end")
        # square root
        elif val == "√":
            ans = math.sqrt(eval(e))
        # pi value
        elif val == "π":
            ans = math.pi
        # trigonometric values
        elif val == "cosθ":
            ans = math.cos(math.radians(eval(e)))
        elif val == "sinθ":
            ans = math.sin(math.radians(eval(e)))
        elif val == "tanθ":
            ans = math.tan(math.radians(eval(e)))
        elif val == "cosh":
            ans = math.cosh(eval(e))
        elif val == "sinh":
            ans = math.sinh(eval(e))
        elif val == "tanh":
            ans = math.tanh(eval(e))
        # 2pi value
        elif val == "2π":
            ans = 2 * math.pi
        # cube root value
        elif val == chr(8731):
            ans = eval(e) ** (1 / 3)
        # x to the power y
        elif val == "x\u02b8":
            entry.insert("end", "**")
            return
        # cube value
        elif val == "x\u00B3":
            ans = eval(e) ** 3
        # square value
        elif val == "x\u00B2":
            ans = eval(e) ** 2
        # log value
        elif val == "ln":
            ans = math.log2(eval(e))
        # degree value
        elif val == "deg":
            ans = math.degrees(eval(e))
        # radian value
        elif val == "rad":
            ans = math.radians(eval(e))
        # e value
        elif val == "e":
            ans = math.e
        # log10 value
        elif val == "log10":
            ans = math.log10(eval(e))
        # factorial value
        elif val == "x!":
            ans = math.factorial(eval(e))
        # division operator
        elif val == chr(247):
            entry.insert("end", "/")
            return
        elif val == "=":
            ans = eval(e)
        else:
            entry.insert("end", val)
            return
        entry.delete(0, "end")
        entry.insert(0, ans)
    except SyntaxError:
        pass


root = tk.Tk() #object creation
root.title("Calculator") #tittle
root.geometry("680x500+100+100") #size
root.config(bg="#2c2f36") #background color
entry = tk.Entry(root, font=("Arial", 20, "bold"), bg="#212529", fg="white", bd=10, width=30, justify="right")
entry.grid(row=0, column=0, columnspan=8, padx=5, pady=5)
#button names
button_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ","1", "2", "3", "-", "2π", "cosh", "tanh", "sinh","4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2","7", "8", "9", chr(247), "ln", "deg", "rad", "e","0", ".", "%", "=", "log10", "(", ")", "x!"]
# button colors
button_colors = {
    "C": "#343a40", "CE": "#343a40", "√": "#495057", "+": "#6c757d", "π": "#495057", "cosθ": "#6c757d",
    "tanθ": "#6c757d", "sinθ": "#6c757d",
    "1": "#495057", "2": "#495057", "3": "#495057", "-": "#6c757d", "2π": "#495057", "cosh": "#6c757d",
    "tanh": "#6c757d", "sinh": "#6c757d",
    "4": "#6c757d", "5": "#6c757d", "6": "#6c757d", "*": "#6c757d", chr(8731): "#495057", "x\u02b8": "#495057",
    "x\u00B3": "#495057", "x\u00B2": "#495057",
    "7": "#495057", "8": "#495057", "9": "#495057", chr(247): "#6c757d", "ln": "#495057", "deg": "#495057",
    "rad": "#495057", "e": "#495057",
    "0": "#495057", ".": "#495057", "%": "#495057", "=": "#28a745", "log10": "#495057", "(": "#495057", ")": "#495057",
    "x!": "#495057"
}
r = 1
c = 0
for i in button_list:
    button = tk.Button(root, width=5, height=2, bd=2, text=i,
                       bg=button_colors.get(i, "yellow"), fg="white",
                       font=("Arial", 15, "bold"),
                       relief="solid",activebackground="#495057", activeforeground="white",
                       command=lambda button=i: Start(button))

    button.grid(row=r, column=c, pady=2, padx=2, ipadx=5, ipady=5)
    c += 1
    if c > 7:
        r += 1
        c = 0
root.mainloop()

