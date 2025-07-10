#Main Calc

from tkinter import *
from tkinter import ttk
import tkinter as tk
import Maths

root = Tk()
root.title("Art Price Calculator")
s=ttk.Style()
s.theme_use('classic')

# icon_image = PhotoImage(file= "IconPicture.png")
# root.wm_iconphoto(False, icon_image)

notebook = ttk.Notebook(root)
tab1 = tk.Frame(notebook)
notebook.add(tab1, text= "Price Calc")

tab2 = tk.Frame(notebook)
notebook.add(tab2, text= "Profit Calc")

# tab3 = tk.Frame(notebook)
# notebook.add(tab3, text = "View saved")
# tab3Canvas = Canvas(tab3)
# tab3Canvas.pack(side=LEFT, fill=BOTH, expand=1)

# scrollbar = tk.Scrollbar(tab3, orient= VERTICAL, command= tab3Canvas.yview)
# scrollbar.pack(side=RIGHT, fill=Y)

# tab3Canvas.configure(yscrollcommand= scrollbar.set)
# tab3Canvas.bind(
#     '<Configure>', lambda e: tab3.configure(scrollregion=tab3.bbox("all"))
# )
# tab3Frame2 = Frame(tab3Canvas, width = 1000, height= 100)

# tab3Canvas.create_window((0, 0), window=tab3, anchor="nw")


notebook.grid(row=0, column=0)



def PysicalCalc(tab):
    num1 = float(box1.get())
    num2 = float(box2.get())
    num3 = float(box3.get())
    num4 = float(box4.get())
    num5 = float(box5.get())
    num6 = float(box6.get())
    num7 = float(box7.get())
    num8 = float(box8.get())
    num9 = float(box9.get())
    # error = Maths.errorCheck(num1, num2, num3, num4, num5, num6)
    # if error == False:
    #     total = "Error: All values must be numbers"
    # else:
    global total  
    global withProfit
    total, withProfit = (Maths.PhysicalPriceCalc(num1, num2, num3, num4, num5, num6, num7, num8, num9))
    sumTxt = Label(tab, text=str("Base Cost: $" + str(total) + "    With 50% profit: $"+ str(withProfit)))
    sumTxt.grid(row=11, column=1)

def DigitalCalc(tab):
    num1 = float(box12.get())
    num2 = float(box22.get())
    num3 = float(box32.get())
    num4 = float(box42.get())
    num5 = float(box52.get())
    num6 = float(box62.get())
    num7 = float(box72.get())
    num8 = float(box82.get())
    num9 = float(box92.get())
    num10 = float(box102.get())
    # error = Maths.errorCheck(num1, num2, num3, num4, num5, num6)
    # if error == False:
    #     total = "Error: All values must be numbers"
    # else:
    global total  
    total = (Maths.DigitalPriceCalc(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10))
    sumTxt = Label( tab, text=str("$" + str(total) + " /hr"))
    sumTxt.grid(row=12, column=1)


def Save(tab):
    if tab == tab1:

        name = str(nameBox.get())
    # elif tab == tab2:
    #     name = str(nameBox2.get())
   
    with open("SavedPrices.txt", "a") as file1:
        saveTxt = name + ": Base Cost: $" + str(total) + "    With 50% profit: $"+ str(withProfit) + "\n"
        file1.write(saveTxt)
    with open("SavedPrices.txt", "r+")as file1:
        print(file1.read())
    saveConfirm = Label(tab, text="Saved!")
    if tab == tab1:
        saveConfirm.grid(row= 13, column=1)
    else:
        saveConfirm.grid(row= 16, column=1)

def showSaved(tab):
    
    # if tab != tab3:
        rowCounter = 19
        columnCounter = 0
        with open("SavedPrices.txt", "r+") as file1:
            content = file1.readlines()
            contentLen = len(content)
            # contentList = Listbox(root, yscrollcommand= scrollbar.set)
            for saved in range(0, contentLen - 4):
                savedLabel = Label(tab, text=str(content[contentLen - saved - 1]))
                
                if saved % 3 == 1:
                    columnCounter = 0
                    rowCounter += 1

                savedLabel.grid(row = rowCounter, column= columnCounter)
                columnCounter += 1
            
       
    # else:
    #     rowCounter = 2
    #     columnCounter = 0
    #     with open("SavedPrices.txt", "r+") as file1:
    #         content = file1.readlines()
    #         contentLen = len(content)
    #         # contentList = Listbox(root, yscrollcommand= scrollbar.set)
    #         for saved in range(0, contentLen - 4):
    #             savedLabel = Label(tab3, text=str(content[contentLen - saved - 1]))
                
    #             if saved % 3 == 1:
    #                 columnCounter = 0
    #                 rowCounter += 1

    #             savedLabel.pack()
    #             columnCounter += 1

    
#Tab 1


titleTxt = Label(tab1, text= "What should I charge for my Art?")
titleTxt.grid(row=0, column=1)

Label1 = Label(tab1, text="Enter Material Cost:")
Label1.grid(row=1, column=0)

box1 = Entry(tab1, width=50, border=10)
box1.grid(row=1, column=1)

Label2 = Label(tab1, text="Enter time spent on project and traveling in hrs :")
Label2.grid(row=2, column=0)

box2 = Entry(tab1, width=50, border=10)
box2.grid(row=2, column=1)

Label3 = Label(tab1, text="Cost of Class or Studio:")
Label3.grid(row=3, column=0)

box3 = Entry(tab1, width=50, border=10)
box3.grid(row=3, column=1)

Label9 = Label(tab1, text="Time available in the class or studio:")
Label9.grid(row=4, column=0)

box9 = Entry(tab1, width=50, border=10)
box9.grid(row=4, column=1)

Label4 = Label(tab1, text="Enter the gallery cut (in % or if dna put 0):")
Label4.grid(row=5, column=0)

box4 = Entry(tab1, width=50, border=10)
box4.grid(row=5, column=1)

Label5 = Label(tab1, text="Enter the credit card fee (in %):")
Label5.grid(row=6, column=0)

box5 = Entry(tab1, width=50, border=10)
box5.grid(row=6, column=1)

Label6 = Label(tab1, text="Enter art show cost (if none put 0):")
Label6.grid(row=7, column=0)

box6 = Entry(tab1, width=50, border=10)
box6.grid(row=7, column=1)

Label7 = Label(tab1, text="Enter packaging/shipping cost: ")
Label7.grid(row=8, column=0)

box7 = Entry(tab1, width= 50, border=10)
box7.grid( row=8, column=1)

Label8 = Label(tab1, text="Enter government tax %: ")
Label8.grid(row=9, column=0)

box8 = Entry(tab1, width= 50, border=10)
box8.grid( row=9, column=1)

calcButton = Button(tab1, text="Calculate Price", command= lambda: PysicalCalc(tab1))
calcButton.grid(row= 10, column=1)

Spacer = Label(tab1, text="")
Spacer.grid(row=11, column=0)

nameLabel = Label(tab1, text="Name this piece:")
nameLabel.grid(row=12, column=0)

nameBox = Entry(tab1, width=30, border=5)
nameBox.grid(row=12, column=1)

saveButton = Button(tab1, text="Save", command= lambda: Save(tab1))
saveButton.grid(row=14, column=1)

# spacer2 = Label(tab1, text="")
# spacer2.grid(row=11, column=0)


showSavedButton = Button(tab1, text="Show Recent Saved", command= lambda: showSaved(tab1))
showSavedButton.grid(row=16, column=1)

savedDisclamer = Label(tab1, text= "*You can view and edit all saved prices by opening the 'SavedPrices.txt' file in notepad*")
savedDisclamer.grid(row=15, column=1)

# priceEX = Label(tab1, text= "Equation used: totalPrice = (timePrice + matCost + artShowCostMult) * yearsMult * galleryCutMult * creditFeeMult")
# priceEX.grid(row= 15, column=1)












#Tab 2


titleTxt2 = Label(tab2, text= "What Am I Actually Making?")
titleTxt2.grid(row=0, column=1)

Label92 = Label(tab2, text="Enter Art Pice Price:")
Label92.grid(row=1, column=0)

box92 = Entry(tab2, width=50, border=10)
box92.grid(row=1, column=1)

Label12 = Label(tab2, text="Enter Material Cost:")
Label12.grid(row=2, column=0)

box12 = Entry(tab2, width=50, border=10)
box12.grid(row=2, column=1)

Label22 = Label(tab2, text="Enter time spent on project and traveling in hrs :")
Label22.grid(row=3, column=0)

box22 = Entry(tab2, width=50, border=10)
box22.grid(row=3, column=1)

Label32 = Label(tab2, text="Enter Cost of Studio or Class:")
Label32.grid(row=4, column=0)

box32 = Entry(tab2, width=50, border=10)
box32.grid(row=4, column=1)

Label102 = Label(tab2, text="Enter time available in Studio or Class:")
Label102.grid(row=5, column=0)

box102 = Entry(tab2, width=50, border=10)
box102.grid(row=5, column=1)

Label42 = Label(tab2, text="Enter the gallery cut (in % or if dna put 0):")
Label42.grid(row=6, column=0)

box42 = Entry(tab2, width=50, border=10)
box42.grid(row=6, column=1)

Label52 = Label(tab2, text="Enter the credit card fee (in %):")
Label52.grid(row=7, column=0)

box52 = Entry(tab2, width=50, border=10)
box52.grid(row=7, column=1)

Label62 = Label(tab2, text="Enter art show cost (if none put 0):")
Label62.grid(row=8, column=0)

box62 = Entry(tab2, width=50, border=10)
box62.grid(row=8, column=1)

Label72 = Label(tab2, text="Enter packaging cost: ")
Label72.grid(row=9, column=0)

box72 = Entry(tab2, width= 50, border=10)
box72.grid( row=9, column=1)

Label82 = Label(tab2, text="Enter tax %: ")
Label82.grid(row=10, column=0)

box82 = Entry(tab2, width= 50, border=10)
box82.grid( row=10, column=1)

calcButton2 = Button(tab2, text="Calculate Hourly Rate", command=  lambda: DigitalCalc(tab2))
calcButton2.grid(row= 11, column=1)

Spacer2 = Label(tab2, text="")
Spacer2.grid(row=12, column=0)

# nameLabel2 = Label(tab2, text="Name this piece:")
# nameLabel2.grid(row=13, column=0)

# nameBox2 = Entry(tab2, width=30, border=5)
# nameBox2.grid(row=13, column=1)

# saveButton2 = Button(tab2, text="Save", command= lambda: Save(tab2))
# saveButton2.grid(row=14, column=1)

# spacer2 = Label(tab2, text="")
# spacer2.grid(row=11, column=0)


# showSavedButton = Button(tab2, text="Show Recent Saved", command= lambda: showSaved(tab2))
# showSavedButton.grid(row=18, column=1)

# savedDisclamer = Label(tab2, text= "*You can view and edit all saved prices by opening the 'SavedPrices.txt' file in notepad*")
# savedDisclamer.grid(row=17, column=1)

# priceEX = Label(tab2, text= "Equation used: totalPrice = (timePrice + matCost + artShowCostMult) * yearsMult * galleryCutMult * creditFeeMult")
# priceEX.grid(row= 15, column=1)





#Tab 3

# refresh = Button(tab3, text="Refresh Saved", command= lambda: showSaved(tab3))
# refresh.pack()





root.mainloop()