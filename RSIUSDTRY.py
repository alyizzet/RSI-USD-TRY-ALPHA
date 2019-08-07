import numpy as np
class RSIUSDTRY(QCAlgorithm):
    '''Basic template algorithm simply initializes the date range and cash'''

    def Initialize(self):
        self.SetStartDate(2008,1, 1)  #Set Start Date
        self.SetEndDate(2019,1,1)    #Set End Date
        self.SetCash(50000)           #Set Strategy Cash
        self.AddForex("USDTRY", Resolution.Hour, Market.Oanda)
        self.SetBrokerageModel(BrokerageName.OandaBrokerage) 
        self.rsi = self.RSI("USDTRY", 14)

    def OnData(self, data):
        
        if not self.rsi.IsReady: 
            return
    
        if self.rsi.Current.Value < 30 and self.Portfolio["USDTRY"].Invested <= 0:
            self.Debug("RSI is less then 30")
            self.Order("USDTRY", 25000)
            self.Debug("Market order was placed")
        
        if self.rsi.Current.Value > 70:
            self.Debug("RSI is greater then 70")
            self.Liquidate()
            
    def OnEndOfDay(self):
        self.Plot("Indicators","RSI", self.rsi.Current.Value)                        
