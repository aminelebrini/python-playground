class Event:
    def __init__(self):
        self.events = []
        
    
    def add_event(self,id, title, start_date, end_date):
        i = 0
        self.events.append({
            "id": id,
            "title": title,
            "start_date":start_date,
            "end_date":end_date
        })
    
    def remove_events(self, id):
        for event in self.events:
            if(id == event["id"]):
                self.events.remove(event)
                print("The event was successfully removed !")
                return True
            else:
                print("isn't exist !")
        return False
                
    
    def display_events(self):
        print(self.events)


event = Event()
for i in range(1, 5):
    event.add_event(i,"startgate", "20-07-2026", "25-07-2026")
event.display_events()
if event.remove_events(2):
    event.display_events()

