import requests
class IRCTC:

    def __init__(self):
        
        user_input = input("""How would you like to proceed?
                           1. Enter 1 to check live train status
                           2. Enter 2 to check PNR
                           3. Enter 3 to check schedule: """)
        
        if user_input == "1":
            print("live train status")
        elif user_input == "2":
            print("PNR")
        else:
            self.train_schedule()
    
    def train_schedule(self):
        train_no = input("Enter the train no: ")
        self.fetch_data(train_no)

    def fetch_data(self,train_no):
    #indianrailapi.com
        data = requests.get("https://indianrailapi.com/api/v2/TrainSchedule/apikey/cc15df9234f72b1789c1a7d3f9bcc5d6/TrainNumber/{}".format(train_no))

        data = data.json()
        print(data['Route'])

        for i in data['Route']:
            print(i['StationName'],"|",i['ArrivalTime'],"|",i["DepartureTime"],"|",i["Distance"],"kms") 

obj = IRCTC()