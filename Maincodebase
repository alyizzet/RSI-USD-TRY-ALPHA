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


class TurtleAlgorithm(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2008, 2, 1)  
        self.SetEndDate(2019,1,1)
        self.SetCash(100000) 
        self.AddEquity("GLD", Resolution.Daily)
        self.rsi = self.RSI("")
        self.SetWarmUp()
        self.SetBenchmark("SPY")
        self.SetTimeZone("Europe/London")
        pass
    
    def OnData(self, data):
        if 
        elif
        
    pass
