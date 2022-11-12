class category():
    listKategori = {}
    idKategori = None
    jenisKategori = None
    def __init__(self, idKategori, namaKategori):
        self.idKategori = idKategori
        self.jenisKategori = namaKategori
        if (len(category.listKategori) == 0):
            self.idKategori = 0
        else:
            self.idKategori = len(category.listKategori)

    def getListKategori(self):
        return self.listKategori

    @staticmethod
    def save(object):
        if (len(category.listKategori) == 0):
            category.listKategori.update({0: object})
        else: 
            category.listKategori.update({len(category.listKategori):object})

    def getJenisKategori(id):
        return category.listKategori[id]
    