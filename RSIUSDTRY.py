from clr import AddReference
AddReference("System")
AddReference("QuantConnect.Algorithm")
AddReference("QuantConnect.Indicators")
AddReference("QuantConnect.Common")

from System import *
from QuantConnect import *
from QuantConnect.Data import *
from QuantConnect.Algorithm import *
from QuantConnect.Indicators import *
from System.Collections.Generic import List
from datetime import datetime

class RSIUSDTRY(QCAlgorithm):

    def Initialize(self):
        self.AddForex("USDTRY", Resolution.Daily, Market.OANDA)
        self.SetStartDate(2008, 2, 1)  
        self.SetEndDate(2019,1,1)
        self.SetCash(100000)
        self.SetBenchmark("SPY")
        self.rsi = self.RSI("USDTRY", 10,  MovingAverageType.Simple, Resolution.Daily)
        self.SetWarmUp(timedelta(20))

    def OnData(self, data):
        
         if not self.rsi.IsReady: return
     
         if self.__previous.date() == self.Time.date(): return
         

         holdings = self.Portfolio["USDTRY"].Quantity

         signalrsi = self.rsi.CurrentValue

      
         if holdings <= 0 and signalrsi> 30:
             self.SetHoldings("USDTRY", 1.0)

         elif holdings >= 0 and signalrsi < 60:
             self.Liquidate("USDTRY")


         self.__previous = self.Time
