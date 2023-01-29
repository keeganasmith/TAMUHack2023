from tkinter import *
from tkinter import ttk
import yahoo_functions as yahoo
import risk as rk

# Creation of root window and stock array
root = Tk()
stocks = []

# Shrinking and growing speed of rows and columns
Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=2)
Grid.rowconfigure(root,1,weight=1)
Grid.columnconfigure(root,1,weight=2)
Grid.rowconfigure(root,2,weight=1)
Grid.columnconfigure(root,2,weight=1)
Grid.rowconfigure(root,3,weight=1)
Grid.columnconfigure(root,3,weight=1)

#Creating of all smaller frames
stockFrame = LabelFrame(root)
bondFrame = LabelFrame(root)
savingFrame = LabelFrame(root)
riskStockFrame = LabelFrame(root)
riskBondFrame = LabelFrame(root)
riskFrame = LabelFrame(root)

#Positioning of frames into grid
stockFrame.grid(row=0,column=0, rowspan = 2, sticky= "NSEW")
bondFrame.grid(row=0,column=1, rowspan = 2, sticky= "NSEW")
savingFrame.grid(row=0, column = 2, rowspan= 2, sticky = "NSEW")
riskStockFrame.grid(row=2, column = 0, sticky = "NSEW")
riskBondFrame.grid(row=2, column = 1, sticky = "NSEW")
riskFrame.grid(row=2, column = 2, sticky = "NSEW")

# Savings and Interest Label in Saving Frame
savingLabel = Label(savingFrame, text= "Savings: $0")
interestLabel = Label(savingFrame, text= "Interest: 0%")

savingLabel.pack()
interestLabel.pack()

# Risk and Growth Label in Risk Frame
riskLabel = Label(riskFrame, text= "Risk:")
growthLabel = Label(riskFrame, text= "Growth:")

riskLabel.pack()
growthLabel.pack()

# Links to Calculate Button, calls function for riskStocksFrame
def calcStock():
    if(len(stocks)!= 0):
        sr, er, rsk, perf = rk.sharpe(stocks)
        ygrowth = yahoo.get_Total_Avg_Yearly_Growth(stocks)
        # Changing of all Labels
        annReturnLabel.config(text = "Annualized Return: " + str("%.2f" % (ygrowth*100) ) + "%")
        sharpeRatioLabel.config(text = "Sharpe Ratio: " + str(sr))
        excessReturnsLabel.config(text = "Excess Returns (in respect to S&P 500): " + str(er))
        performanceLabel.config(text = "Performance: " + perf)
        riskLabel.config(text = "Risk: " + rsk)

#Labels and Buttons in riskStocksFrame
annReturnLabel = Label(riskStockFrame, text= "Annualized Return:")
sharpeRatioLabel = Label(riskStockFrame, text= "Sharpe Ratio:" )
excessReturnsLabel = Label(riskStockFrame, text= "Excess Returns (in respect to S&P 500): " )
performanceLabel = Label(riskStockFrame, text= "Performance: " )
riskLabel = Label(riskStockFrame, text= "Risk: " )
calculateButton = Button(riskStockFrame, text = "Calculate", command = calcStock)

annReturnLabel.pack()
sharpeRatioLabel.pack()
excessReturnsLabel.pack()
riskLabel.pack()
performanceLabel.pack()
calculateButton.pack()

#List of stocks
stockListFrame = LabelFrame(stockFrame, highlightthickness=0, borderwidth = 0)
stockScroll = Scrollbar(stockListFrame, orient=VERTICAL)
stockTree = ttk.Treeview(stockListFrame, column=("Name", "Amount"), show='headings', height=5, yscrollcommand= stockScroll.set, selectmode = EXTENDED)
stockScroll.config(command = stockTree.yview)
stockScroll.pack(side = RIGHT, fill= Y)

stockTree.column("# 1", anchor=CENTER)
stockTree.heading("# 1", text="Name")
stockTree.column("# 2", anchor=CENTER)
stockTree.heading("# 2", text="Amount")

# Addition and deletion of stock list
def addStock(nm, amu):
    stockTree.insert('', 'end', values=(str(nm), str(amu)))
    stocks.append((str(nm), int(amu)))

def deleteStock():
    for item in reversed(stockTree.selection()):
        itemindex = stockTree.index(item)
        #print(itemindex)
        stockTree.delete(item)
        stocks.pop(itemindex)

#Entry fields for stock list
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
stockListFrame.pack()

#List of bonds
bondListFrame = LabelFrame(bondFrame, highlightthickness=0, borderwidth = 0)
bondScroll = Scrollbar(bondListFrame, orient=VERTICAL)
bondTree = ttk.Treeview(bondListFrame, column=("Name", "Amount", "Interest Rate"), show='headings', height=5, yscrollcommand= bondScroll.set, selectmode = EXTENDED)
bondScroll.config(command = bondTree.yview)
bondScroll.pack(side = RIGHT, fill= Y)

bondTree.column("# 1", anchor=CENTER)
bondTree.heading("# 1", text="Name")
bondTree.column("# 2", anchor=CENTER)
bondTree.heading("# 2", text="Amount")
bondTree.column("# 2", anchor=CENTER)
bondTree.heading("# 2", text="Interest Rate")


# Addition and deletion to bond list
def addBond(nm, amu, ir):
    bondTree.insert('', 'end', values=(str(nm), str(amu), str(ir)))

def deleteBond():
    for item in reversed(bondTree.selection()):
        itemindex = bondTree.index(item)
        bondTree.delete(item)

#Entry fields for bond list
bondAddButton = Button(bondFrame, text = "Add Bond", command = lambda : addBond(sec.get(), bondAmountEntry.get()))
bondDeleteButton = Button(bondFrame, text = "Delete Bond", command = deleteBond)

sec = StringVar()
securities = OptionMenu(bondFrame, sec, 'Treasury Bills', 'Treasury Notes', 'Treasury Bonds',
'Treasury Inflation-Protected Securities (TIPS)', 'Treasury Floating Rate Notes (FRN)', 'Federal Financing Bank',
'Special Purpose Vehicle', 'Foreign Series', 'State and Local Government Series', 'United States Savings Securities',
'United States Savings Inflation Securities', 'Government Account Series', 'Government Account Series Inflation Securities')
securities.pack()

bondAmountEntry = Entry(bondFrame, width = 36)
bondAmountEntry.pack()
bondAmountEntry.insert(0, "Enter Bond amount")

bondAddButton.pack()
bondDeleteButton.pack()

bondTree.pack()
bondListFrame.pack()


# Setting of Savings and Interest Labels
def setSavings(sav):
    savingLabel.config(text = "Savings: $" + str(sav))

def setInterest(interest):
    interestLabel.config(text = "Interest: " + str(interest) + "%")

#Entry fields for Savings and Interest
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

root.mainloop()