from datetime import datetime
from activity import *

class dashboard:
    @classmethod
    def showToDoList():
        today = datetime.now()
        temp = []
        for i in range(len(activity.listKegiatan)):
            if ((activity.listKegiatan[i].BatasWaktu.year == today.year) and (activity.listKegiatan[i].BatasWaktu.month == today.month) and (activity.listKegiatan[i].BatasWaktu.day == today.day)):
                temp.append(activity.listKegiatan[i])
        return temp
    
    

