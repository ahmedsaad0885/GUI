from tkinter import *

# window
window = Tk()

window.title("GUI")
window.geometry('600x600')
# widgets

# label
lbl0 = Label(window, text="file name", font=("Arial Bold ", 20))
lbl0.grid(column=0, row=0)

lbl1 = Label(window, text="f(x1)", font=("Arial Bold ", 20))
lbl1.grid(column=0, row=1)

lbl2 = Label(window, text="f(x2)", font=("Arial Bold ", 20))
lbl2.grid(column=0, row=2)

lbl3 = Label(window, text="f(x3)", font=("Arial Bold ", 20))
lbl3.grid(column=0, row=3)

reslbl = Label(window, text="", font=("Arial Bold ", 20))
reslbl.grid(column=0, row=5)
#Entries

filename=Entry(window, width=20)
filename.grid(column=1, row=0)
func1=Entry(window, width=20)
func1.grid(column=1, row=1)
func2=Entry(window, width=20)
func2.grid(column=1, row=2)
func3=Entry(window, width=20)
func3.grid(column=1, row=3)

#functions


def addnum():


    print(tempfunc1)
    lbl1.configure(text=tempfunc1)
def gauss_elimination():

    i = 0
    x = [0] * 3
    coffmat = []
    for i in range(3):
        col = []
        for j in range(4):
            col.append(0)
        coffmat.append(col)

    all_equations = [0]*3
    if readfile==True:
        all_equations[0] = tempfunc1
        all_equations[1] = tempfunc2
        all_equations[2] = tempfunc3
    else:
        all_equations[0]=func1.get()
        all_equations[1] = func2.get()
        all_equations[2] = func3.get()
    print(all_equations)
    #all_equations = ["2x+1y+4z+1", "1x+2Y+3z+1.5", "2-1y+4x+2z"]

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
        if intercept =='':
            intercept='0'
        return float(coef_x), float(coef_y), float(coef_z), float(intercept)

    i = 0
    for equation in all_equations:
        cof_x, cof_y, cof_z, cof_c, = CoefficientIntercept(equation)
        coffmat[i][0] = cof_x
        coffmat[i][1] = cof_y
        coffmat[i][2] = cof_z
        coffmat[i][3] = cof_c
        # print(coffmat, flush=True)
        i = i + 1
    print(coffmat)
    for b in range(3):
        for m in range(4):
            if coffmat[b][m] == -0:
                coffmat[b][m] = 0
        for l in range(b + 1, 3):
            factor = coffmat[l][b] / coffmat[b][b]
            for c in range(b, 3):
                coffmat[l][c] = coffmat[l][c] - factor * coffmat[b][c]
            coffmat[l][3] = coffmat[l][3] - factor * coffmat[b][3]



    for q in range(2, -1, -1):
        sum = 0
        for s in range(q + 1, 3):
            sum = sum + coffmat[q][s] * x[s]
        x[q] = ((coffmat[q][3]) - sum) / coffmat[q][q]
        if x[q]==-0:
            x[q]=0
    print(x)
    temp="x=: "+str(x[0])+"  y=: "+str(x[1])+"  z=: "+str(x[2])


    reslbl.configure(text=temp)






def gauss_jordan():

    coffmat = []
    for i in range(3):
        col = []
        for j in range(4):
            col.append(0)
        coffmat.append(col)
    all_equations = [0] * 3
    if readfile==True:
        all_equations[0] = tempfunc1
        all_equations[1] = tempfunc2
        all_equations[2] = tempfunc3
    else:
        all_equations[0] = func1.get()
        all_equations[1] = func2.get()
        all_equations[2] = func3.get()


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
        temp = "x=: " + str(coffmat[0][3]) + "  y=: " + str(coffmat[1][3]) + "  z=: " + str(coffmat[2][3])

        reslbl.configure(text=temp)






def gauss_sidel():
    i = 0
    x = [0] * 3
    coffmat = []
    for i in range(3):
        col = []
        for j in range(4):
            col.append(0)
        coffmat.append(col)

    all_equations = [0] * 3
    if readfile == True:
        all_equations[0] = tempfunc1
        all_equations[1] = tempfunc2
        all_equations[2] = tempfunc3
    else:
        all_equations[0] = func1.get()
        all_equations[1] = func2.get()
        all_equations[2] = func3.get()
    print(all_equations)
    #all_equations = ["2x+1y+4z+1", "1x+2Y+3z+1.5", "2-1y+4x+2z"]

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
        if intercept =='':
            intercept='0'
        return float(coef_x), float(coef_y), float(coef_z), float(intercept)

    i = 0
    for equation in all_equations:
        cof_x, cof_y, cof_z, cof_c, = CoefficientIntercept(equation)
        coffmat[i][0] = cof_x
        coffmat[i][1] = cof_y
        coffmat[i][2] = cof_z
        coffmat[i][3] = cof_c
        # print(coffmat, flush=True)
        i = i + 1

    x[0]*3


def read_from_file():
    choice = filename.get()
    if len(choice) != 0:
        global readfile
        readfile=True
        file = open(choice, 'r')
        n = (file.readline())
        method = (file.readline())
        global tempfunc1
        global tempfunc2
        global tempfunc3
        tempfunc1= (file.readline())
        tempfunc2 = (file.readline())
        tempfunc3 = (file.readline())
        if method=="Gauss-sidel":
            global initial
            initial = (file.readline())
        if method == "Gaussian-elemination\n":
            gauss_elimination()
        if method == "Gaussian-jordan\n":
            gauss_jordan()
        #
        # initial_guess = float(initial_guess)
        # n = int(n)
        # tol = float(tol)


# button



btn1 = Button(window, text="Gaussian-elimination",bg="#7322c7",fg="#f0f0f0",command =read_from_file)
btn2 = Button(window, text="Gauss-jordan",bg="#7322c7",fg="#f0f0f0",command =read_from_file)
btn3 = Button(window, text="Gauss-sidel",bg="#7322c7",fg="#f0f0f0",command =read_from_file)
btn4 = Button(window, text="read from file",bg="#7322c7",fg="#f0f0f0",command =read_from_file)

btn1.grid(column=1, row=4)
btn2.grid(column=1, row=5)
btn3.grid(column=1, row=6)
btn4.grid(column=1, row=7)

window.mainloop()
