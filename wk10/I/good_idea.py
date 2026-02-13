#ISP - Interface Segreation Princiiple
#กล่าวว่า คลาสลูกควรจะไม่ถูกบังคับให้ต้องพึ่งพา interface ที่ไม่ใช้งาน
from abc import abstractclassmethod
class Printer:
    @abstractclassmethod
    def print(Self, document):
        pass

class Scanner:
    @abstractclassmethod
    def scan(self, document):
        pass

class Fax:
    @abstractclassmethod
    def fax(sself, document):
        pass

class MultiFunctionPrinter(Printer,Scanner,Fax):

    def print(self, document):
        print("Print document................")
    def scan(self, document):
        print("Scanning document..................")
    def fax(self,document):
        print("Fax document......................................")
    
