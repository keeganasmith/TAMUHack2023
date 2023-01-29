from tkinter import *
from tkinter import ttk
import yahoo_functions as yahoo
import risk as rk

root = Tk()
stocks = []

#root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))

root.geometry("1920x1080")

enterFrame = LabelFrame(root, highlightthickness=0, borderwidth = 0)
enterFrame.pack()

wdth = root.winfo_width()
hght = root.winfo_height()

print(wdth)
print(hght)


# wdth = root.winfo_screenwidth()
# hght = root.winfo_screenheight()

# root.geometry("%dx%d" % (wdth, hght))

#root.update_idletasks()
#print(wdth)
#print(hght)

stockBigFrame = LabelFrame(enterFrame, height= hght, width= wdth/3)
stockFrame = LabelFrame(stockBigFrame, height= 4*hght/5, width= wdth/3)
bondFrame = LabelFrame(enterFrame, height= hght, width= wdth/3)
savingFrame = LabelFrame(enterFrame, height= 4*hght/5, width= wdth/3)
riskStockFrame = LabelFrame(stockBigFrame, height= hght/5, width= wdth/3)
riskFrame = LabelFrame(enterFrame, height= hght/5, width= wdth/3)

savingLabel = Label(savingFrame, text= "Savings: $0")
interestLabel = Label(savingFrame, text= "Interest: 0%")

riskLabel = Label(riskFrame, text= "Risk:")
growthLabel = Label(riskFrame, text= "Growth:")


def calcStock():
    ftime = ""
    if(len(stocks)!= 0):
        if(timeChoice == "6 Months"):
             ftime = "6mo"
        if(timeChoice == "1 Year"):
             ftime = "1y"
        if(timeChoice == "2 Years"):
             ftime = "2y"
        if(timeChoice == "5 Years"):
             ftime = "5y"
        ygrowth = yahoo.get_Total_Avg_Yearly_Growth(stocks)
        annReturnLabel.config(text = "Annualized Return: " + str("%.2f" % (ygrowth*100) ) + "%")
        sharpeRatioLabel.config(text = "Sharpe Ratio: " + str("%.2f" % (rk.sharpe(stocks))))
    
annReturnLabel = Label(riskStockFrame, text= "Annualized Return:")
sharpeRatioLabel = Label(riskStockFrame, text= "Sharpe Ratio:" )

timeChoice = StringVar()
timeMenu = OptionMenu(riskStockFrame, timeChoice, "6 Months", "1 Year", "2 Years", "5 Years")

calculateButton = Button(riskStockFrame, text = "Calculate", command = calcStock)

annReturnLabel.pack()
sharpeRatioLabel.pack()
timeMenu.pack()
calculateButton.pack()

riskLabel.pack()
growthLabel.pack()

stockListFrame = LabelFrame(stockFrame, highlightthickness=0, borderwidth = 0)

stockBigFrame.pack_propagate(False)
stockFrame.pack_propagate(False)
riskStockFrame.pack_propagate(False)
bondFrame.pack_propagate(False)
savingFrame.pack_propagate(False)
riskFrame.pack_propagate(False)

stockScroll = Scrollbar(stockListFrame, orient=VERTICAL)
stockTree = ttk.Treeview(stockListFrame, column=("Name", "Amount"), show='headings', height=5, yscrollcommand= stockScroll.set, selectmode = EXTENDED)
stockScroll.config(command = stockTree.yview)
stockScroll.pack(side = RIGHT, fill= Y)

stockTree.column("# 1", anchor=CENTER)
stockTree.heading("# 1", text="Name")
stockTree.column("# 2", anchor=CENTER)
stockTree.heading("# 2", text="Amount")

bondListFrame = LabelFrame(bondFrame, highlightthickness=0, borderwidth = 0)

bondScroll = Scrollbar(bondListFrame, orient=VERTICAL)
bondTree = ttk.Treeview(bondListFrame, column=("Name", "Amount"), show='headings', height=5, yscrollcommand= bondScroll.set, selectmode = EXTENDED)
bondScroll.config(command = bondTree.yview)
bondScroll.pack(side = RIGHT, fill= Y)

bondTree.column("# 1", anchor=CENTER)
bondTree.heading("# 1", text="Name")
bondTree.column("# 2", anchor=CENTER)
bondTree.heading("# 2", text="Amount")

def addStock(nm, amu):
    stockTree.insert('', 'end', values=(str(nm), str(amu)))
    stocks.append((str(nm), int(amu)))

def deleteStock():
    for item in reversed(stockTree.selection()):
        itemindex = stockTree.index(item)
        print(itemindex)
        stockTree.delete(item)
        stocks.pop(itemindex)

def addBond(nm, amu):
    bondTree.insert('', 'end', values=(str(nm), str(amu)))

def deleteBond():
    for item in reversed(bondTree.selection()):
        itemindex = bondTree.index(item)
        bondTree.delete(item)

def setSavings(sav):
    savingLabel.config(text = "Savings: $" + str(sav))

def setInterest(interest):
    interestLabel.config(text = "Interest: " + str(interest) + "%")

stockAddButton = Button(stockFrame, text = "Add stock", command = lambda : addStock(stockNameEntry.get(), stockAmountEntry.get()))
stockDeleteButton = Button(stockFrame, text = "Delete stock", command = deleteStock)

stockNameEntry = Entry(stockFrame, width = 36)
stockNameEntry.pack()
stockNameEntry.insert(0, "Enter Stock name")

stockAmountEntry = Entry(stockFrame, width = 36)
stockAmountEntry.pack()
stockAmountEntry.insert(0, "Enter Stock amount")

stockAddButton.pack()
stockDeleteButton.pack()

stockTree.pack()

bondAddButton = Button(bondFrame, text = "Add Bond", command = lambda : addBond(bondNameEntry.get(), bondAmountEntry.get()))
bondDeleteButton = Button(bondFrame, text = "Delete Bond", command = deleteBond)

bondNameEntry = Entry(bondFrame, width = 36)
bondNameEntry.pack()
bondNameEntry.insert(0, "Enter Bond name")

bondAmountEntry = Entry(bondFrame, width = 36)
bondAmountEntry.pack()
bondAmountEntry.insert(0, "Enter Bond amount")

bondAddButton.pack()
bondDeleteButton.pack()

bondTree.pack()

setSavingsButton = Button(savingFrame, text = "Set Savings", command = lambda : setSavings(savingsAmountEntry.get()))
setInterestButton = Button(savingFrame, text = "Set Interest", command = lambda : setInterest(interestAmountEntry.get()))

savingsAmountEntry = Entry(savingFrame, width = 36)
savingsAmountEntry.pack()
savingsAmountEntry.insert(0, "Enter savings")

interestAmountEntry = Entry(savingFrame, width = 36)
interestAmountEntry.pack()
interestAmountEntry.insert(0, "Enter Interest")

setSavingsButton.pack()
setInterestButton.pack()

savingLabel.pack()
interestLabel.pack()

stockFrame.pack(side = TOP)
riskStockFrame.pack(side = BOTTOM)
stockBigFrame.pack(side = LEFT)
bondFrame.pack(side = LEFT)
savingFrame.pack(side= TOP)
riskFrame.pack()

stockListFrame.pack()
bondListFrame.pack()

root.mainloop()