from tkinter import *

# window
window = Tk()

window.title("GUI")
window.geometry('600x600')
# widgets

# label
lbl1 = Label(window, text="hello", font=("Arial Bold ", 20))
lbl1.grid(column=0, row=0)
#Entries

entry1=Entry(window, width=10)
entry1.grid(column=0,row=1)
#functions



def gauss_jordan():

    coffmat = []
    for i in range(3):
        col = []
        for j in range(4):
            col.append(0)
        coffmat.append(col)



    all_equations = ["2x+1y+4z+1", "1x+2Y+3z+1.5", "2-1y+4x+2z"]

    def CoefficientIntercept(equation):
        if (equation.__contains__("x")) | (equation.__contains__("X")):
            coef_x = re.findall(r'-?[0-9.]*[Xx]', equation)[0][:-1]

        else:
            coef_x = '0'
        if (equation.__contains__("y")) | (equation.__contains__("Y")):
            coef_y = re.findall(r'-?[0-9.]*[Yy]', equation)[0][:-1]
        else:
            coef_y = '0'
        if (equation.__contains__("z")) | (equation.__contains__("Z")):
            coef_z = re.findall(r'-?[0-9.]*[Zz]', equation)[0][:-1]
        else:
            coef_z = '0'
        intercept = re.sub("[+-]?\d+[XxYyZz]|[+-]?\d+\.\d+[XxYyZz]|[+-]?\d+\.\d+[XxYyZz]", "", equation)
        return float(coef_x), float(coef_y), float(coef_z), float(intercept)

    i = 0
    for equation in all_equations:
        cof_x, cof_y, cof_z, cof_c, = CoefficientIntercept(equation)
        coffmat[i][0] = cof_x
        coffmat[i][1] = cof_y
        coffmat[i][2] = cof_z
        coffmat[i][3] = cof_c
        i = i + 1

    for b in range(3):
        dev = coffmat[b][b]
        for m in range(4):
            coffmat[b][m] = coffmat[b][m] / dev
            if coffmat[b][m] == -0:
                coffmat[b][m] = 0

        for l in range(b + 1, 3):
            factor1 = coffmat[l][b] / coffmat[b][b]
            factor2 = coffmat[l - 2][b] / coffmat[b][b]
            if b == 1:
                for c in range(b, 4):
                    coffmat[l][c] -= factor1 * coffmat[b][c]
                    coffmat[l - 2][c] -= factor2 * coffmat[b][c]
            else:
                for c in range(b, 4):
                    coffmat[l][c] = coffmat[l][c] - factor1 * coffmat[b][c]
        if b == 2:
            factor1 = coffmat[0][2]
            factor2 = coffmat[1][2]
            for e in range(2, 4):
                coffmat[0][e] -= factor1 * coffmat[2][e]
                coffmat[1][e] -= factor2 * coffmat[2][e]
        print(coffmat)

    print(coffmat)



def addnum():

    num=int(entry1.get())
    num=num+5
    lbl1.configure(text=str(num))
# button



btn1 = Button(window, text="button",bg="#338877",fg="#220050",command =gauss_jordan)
btn1.grid(column=1, row=0)

window.mainloop()
