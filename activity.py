class activity: 
    idKegiatan = -1
    listKegiatan = {}
    namaKegiatan = None
    status = None
    batasWaktu = None
    kategori = None
    def __init__(self, newNamaKegiatan, newStatus, newBatasWaktu, newKategori):
        self.namaKegiatan = newNamaKegiatan
        self.status = newStatus
        self.batasWaktu = newBatasWaktu
        self.kategori = newKategori
        if (len(activity.listKegiatan) == 0): 
            self.idKegiatan = 0
        else:
            self.idKegiatan = len(activity.listKegiatan)

    def __init__(self, newNamaKegiatan, newBatasWaktu, newKategori):
        self.namaKegiatan = newNamaKegiatan
        self.status = 'idle'
        self.batasWaktu = newBatasWaktu
        self.kategori = newKategori
        if (len(activity.listKegiatan) == 0):
            self.idKegiatan = 0
        else:
            self.idKegiatan = len(activity.listKegiatan)

    @staticmethod
    def save(object):
        if (len(activity.listKegiatan) == 0):
            activity.listKegiatan.update({0: object})
        else: 
            activity.listKegiatan.update({len(activity.listKegiatan):object})
         
    def getNamaKegiatan(self):
        return self.namaKegiatan
    def setStatus(self, newStatus):
        self.status = newStatus
    def getBatasWaktu(self):
        return self.batasWaktu
    def getStatus(self):
        return self.status
    
    def filterKategori(selectedKategori):
        n = len(activity.listKegiatan)
        newListKegiatan = {}
        for i in range(n):
            if (activity.listKegiatan[i].kategori == selectedKategori):
                newListKegiatan.append(activity.listKegiatan[i])
        return newListKegiatan

    def filterBatasWaktu(selectedBatasWaktu):
        n = len(activity.listKegiatan)
        newListKegiatan = []
        for i in range(n):
            if (activity.listKegiatan[i].BatasWaktu == selectedBatasWaktu):
                newListKegiatan.append(activity.listKegiatan[i])
        return newListKegiatan
    
    def filterStatus(selectedStatus):
        n = len(activity.listKegiatan)
        newListKegiatan = []
        for i in range(n):
            if (activity.listKegiatan[i].Status == selectedStatus):
                newListKegiatan.append(activity.listKegiatan[i])
        return newListKegiatan

    def getListKegiatan():
        return activity.listKegiatan

    @staticmethod
    def deleteKegiatan(selectedIdKegiatan):
        found = False
        i = 0
        while(not found):
            if (activity.listKegiatan[i].idKegiatan == selectedIdKegiatan):
                # print(i)
                # print(activity.listKegiatan[i])
                # activity.listKegiatan[i] = 0
                # print(activity.listKegiatan[i])
                del activity.listKegiatan[i]
                found = True
            else:
                # print(activity.listKegiatan[i].namaKegiatan)
                i += 1
                

## Driver Code
Kegiatan_1 = activity("Gym", "01-022-0223", "Sport")
activity.save(Kegiatan_1)
Kegiatan_2 = activity("Bola", "01-02-03", "Sport")
activity.save(Kegiatan_2)
Kegiatan_3 = activity("Basket", "013-023-033", "Sport")
activity.save(Kegiatan_3)

print("----------------------------------------------------------")
print("")
print("List Object Kegiatan: ")
print(activity.listKegiatan)
print("Deleting Object Kegiatan Number 1")
activity.deleteKegiatan(1)
print("")
print("----------------------------------------------------------")
print("List Object Kegiatan: ")
print(activity.listKegiatan)
print("")
print("")
print(activity.listKegiatan[0].namaKegiatan)



