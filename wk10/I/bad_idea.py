#ISP - Interface Segreation Princiiple
#กล่าวว่า คลาสลูกควรจะไม่ถูกบังคับให้ต้องพึ่งพา interface ที่ไม่ใช้งาน

class Machine:
    def print(Self, document):
        pass
    def scan(self, document):
        pass
    def fax(sself, document):
        pass

class PldPrinter(Machine):
    def print(self, document):
        print("Print document................")
    def scan(self, document):
        raise NotImplementedError("This printer cannot fax")
    def fax(self,document):
        raise NotImplementedError("This printer cannot fax")
    
