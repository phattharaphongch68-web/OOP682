#S = SRP = SIngle Responsibility prinpicle
#GOODIDEA
#Support classes for each respomsibility

class ReportGenerator:

    def __init__(self,data):
        self.data = data

    def genarte_pdf(self):
        pass

    def generate_exel(self):
        pass

    def send_gmail(self,recipient):
        pass