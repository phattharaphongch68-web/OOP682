#DIP - DEpendency Inversion Principle
#โมดูลระดับสูงไม่ควรขึ้นกับโมดูลระดับต่ำ ทั้งคู่ควรขึ้นอยู่กับ Abstraction หรือ interface ที่เป็นระดับสูง
class App:
    def __init__(self):
        self.database = MySQLDatabase()
        def save_data(self, data):
            self.database.save(data)

class MySQLDatabase:
    def save(self,data):
        print("saving data to MySQL database")

app = App()
app.save_data("my data")