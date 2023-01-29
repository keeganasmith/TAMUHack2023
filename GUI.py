from tkinter import *
from tkinter import ttk
import yahoo_functions as yahoo
import risk as rk
import bonds_risk as br
import stock_growth
import total_growth
# Creation of root window and stock array
root = Tk()
stocks = []
bond_amounts = []
bond_interests = []
sharpe = 1
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
growthLabel = Label(riskFrame, text= "Expected Annual Growth (taking risk into account): ")


growthLabel.pack()

# Links to Calculate Button, calls function for riskStocksFrame
def calcStock():
    if(len(stocks)!= 0):
        sr, er, rsk, perf = rk.sharpe(stocks)
        # ygrowth = yahoo.get_Total_Avg_Yearly_Growth(stocks)
        sharpe = sr
        # Changing of all Labels
        sharpeRatioLabel.config(text = "Sharpe Ratio (w.r.t S&P 500): " + str(sr))
        excessReturnsLabel.config(text = "Excess Returns (w.r.t S&P 500): " + str(er))
        performanceLabel.config(text = "Performance: " + perf)
        riskLabel.config(text = "Risk: " + rsk)
        annReturnLabel.config(text = "Expected Growth Accounting for Risk Factors: " + str(stock_growth.bruh(sharpe) * 100) + "%")


#Labels and Buttons in riskStocksFrame
sharpeRatioLabel = Label(riskStockFrame, text= "Sharpe Ratio:" )
excessReturnsLabel = Label(riskStockFrame, text= "Excess Returns (w.r.t respect to S&P 500): " )
performanceLabel = Label(riskStockFrame, text= "Performance: " )
riskLabel = Label(riskStockFrame, text= "Risk: " )
annReturnLabel = Label(riskStockFrame, text= "Expected Growth Accounting for Risk Factors: ")

calculateButton = Button(riskStockFrame, text = "Calculate", command = calcStock)

sharpeRatioLabel.pack()
excessReturnsLabel.pack()
riskLabel.pack()
performanceLabel.pack()

annReturnLabel.pack()
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

Grid.rowconfigure(stockFrame,0,weight=1)
Grid.columnconfigure(stockFrame,0,weight=1)
Grid.rowconfigure(stockFrame,1,weight=1)
Grid.columnconfigure(stockFrame,1,weight=1)


stockNameLabel = Label(stockFrame, text = "Stock Name: ")
stockNameLabel.grid(row = 0, column = 0)

stockNameEntry = Entry(stockFrame, width = 18)
stockNameEntry.grid(row = 0, column = 1)
stockNameEntry.insert(0, "Enter Stock name")

stockAmountLabel = Label(stockFrame, text = "Stock Amount: ")
stockAmountLabel.grid(row = 1, column = 0)

stockAmountEntry = Entry(stockFrame, width = 18)
stockAmountEntry.grid(row = 1, column = 1)
stockAmountEntry.insert(0, "Enter Stock amount")

stockAddButton.grid(row = 2, column = 0)
stockDeleteButton.grid(row = 2, column = 1)

stockTree.pack()
stockListFrame.grid(row = 3, column = 0, columnspan = 3)

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
bondTree.column("# 3", anchor=CENTER)
bondTree.heading("# 3", text="Interest Rate")


# Addition and deletion to bond list
def addBond(nm, amu):
    inter = br.get_interest(nm)
    bond_interests.append(inter)
    bond_amounts.append(amu)
    bondTree.insert('', 'end', values=(str(nm), str(amu), str(inter)))

def deleteBond():
    for item in reversed(bondTree.selection()):
        itemindex = bondTree.index(item)
        bondTree.delete(item)
    if(len(bond_interests) > 0):
        bond_interests.pop(-1)
        bond_amounts.pop(-1)

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

saving_amount = 0
saving_interest = 0
# Setting of Savings and Interest Labels
def setSavings(sav):
    savingLabel.config(text = "Savings: $" + str(sav))
    saving_amount = sav
def setInterest(interest):
    interestLabel.config(text = "Interest: " + str(interest) + "%")
    saving_interest = interest;
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

def calculateTotal():
    sg = stock_growth.bruh(sharpe)
    stock_amount= 0;
    for i in range(0, len(stocks)):
        stock_amount += stocks[i][1]
    growth = total_growth.total_growth(stock_amount, sg, bond_amounts, bond_interests, saving_amount, saving_interest)
    growthLabel.config(text = f"Expected Annual Growth (taking risk into account):\n{growth}%\n")

    return 0
setCalculateTotalButton = Button(riskBondFrame, text = "Calculate Total", command = lambda : calculateTotal())
setCalculateTotalButton.pack()
root.mainloop()