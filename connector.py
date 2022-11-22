import mariadb
import sys
from datetime import datetime

class connector():
    _host = None
    _user = None
    _password = None
    _database = None
    _session = None
    _connection = None

    def __init__(self, host, user, password, database):
        self._host = host
        self._user = user
        self._password = password
        self._database = database

    def openConnection(self):
        try:
            conn = mariadb.connect(
                user = self._user,
                password = self._password,
                host = self._host,
                port = 3306,
                database = self._database
                )
            self._connection = conn
            self._session = conn.cursor()
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    def closeConnection(self):
        self._connection.close()
        self._session.close()

    def allToDoList(self):
        statement = "SELECT idKegiatan, namaKegiatan, batasWaktu, jenisStatus, jenisKategori FROM Kegiatan INNER JOIN Kategori"
        try:
            self._session.execute(statement)
            data = self._session.fetchall()
        except:
            print("Failed!")
        return data
    
    def todayToDoList(self):
        statement = "SELECT idKegiatan, namaKegiatan, batasWaktu, jenisStatus, jenisKategori FROM Kegiatan INNER JOIN Kategori WHERE batasWaktu = DATE('now') AND jenisStatus = 'ongoing'"
        try:
            self._session.execute(statement)
            data = self._session.fetchall()
        except:
            print("Failed!")
        return data

    def allCategory(self):
        statement = "SELECT * FROM Kategori"
        try:
            self._session.execute(statement)
            data = self._session.fetchall()
        except:
            print("Failed!")
        return data


    def updateStatusOnGOing(self, activityID):
        statement = f"UPDATE Kegiatan SET status = 'ongoing' WHERE = {activityID}"
        try:
            self._session.execute(statement)
            self._connection.commit()
        except:
            print("Failed!")

    def autoUpdateStatusExpired(self, activityID):
        statement = f"UPDATE Kegiatan SET status = 'expired' WHERE idKegiatan = {activityID}"
        try:
            self._session.execute(statement)
            self._connection.commit()
        except:
            print("Failed!")
    
    def addActivity(self, activityID, name, status, deadline, categoryID):
        statement = f"INSERT INTO Kegiatan (idKegiatan, namaKegiatan, jenisStatus, batasWaktu, idKategori) VALUES ({activityID}, '{name}', '{status}', '{deadline}', {categoryID})"
        try:
            self._session.execute(statement)
            self._connection.commit()
        except:
            print("Failed Adding Activity! ")

    def deleteKegiatan(self, activityID):
        statement = f"DELETE FROM Kegiatan WHERE idKegiatan = {activityID}"
        try:
            self._session.execute(statement)
            self._connection.commit()
        except:
            print("Failed!")
    

    def filterKategori(self, selectedKategori):
        statement = f"SELECT idKegiatan, namaKegiatan, batasWaktu, jenisStatus, jenisKategori FROM Kegiatan INNER JOIN Kategori WHERE jenisKategori = '{selectedKategori}'"
        try:
            self._session.execute(statement)
            data = self._session.fetchall()
        except:
            print("Failed!")
        return data

    def filterStatus(self,selectedstatus):
        statement = f"SELECT idKegiatan, namaKegiatan, batasWaktu, jenisStatus, jenisKategori FROM Kegiatan INNER JOIN Kategori WHERE jenisStatus = '{selectedstatus}'"
        try:
            self._session.execute(statement)
            data = self._session.fetchall()
        except:
            print("Failed!")
        return data

# Hari ini 
# Minggu ini 
# Semua
    def filterBatasWaktuToday(self):
        today = datetime.now()
        strToday = f"{today.year}-{today.month}-{today.day}"
        statement = f"SELECT * FROM Kegiatan WHERE batasWaktu = DATE('now') AND status = 'On Going' "
        try:
            self._session.execute(statement)
            data = self._session.fetchall()
        except:
            print("Failed!")
        return data

    def addCategory(self, categoryID, namaKategori):
        statement = f"INSERT INTO Kategori (idKategori, jenisKategori) VALUES ({categoryID}, '{namaKategori}')"
        try:
            self._session.execute(statement)
            self._connection.commit()
        except:
            print("Failed!")

# DRIVER CODE ----------------------------------------------------------------
## Initialization
cn1 = connector("localhost", "root", "password", "rpl")
cn1.openConnection()

## Add Activity --------------------------------------------------------------
# cn1.addActivity(3,"Bowling", "expired", "2020-1-10",1)
a = cn1.todayToDoList()
print(a)

# print(len(a))

# for i in a:
#     print(i[2])
## Del Activity --------------------------------------------------------------
# cn1.deleteKegiatan(1)
# b = cn1.allToDoList()
# print(b)








# cn1.showToDoList()
# a = "'Expired'"
# cn1._session.execute(f"SELECT * FROM Kegiatan WHERE jenisStatus = {a}")

# a = cn1._session.fetchall()
# print(a)
# print(type(a[0][2]))

# print(a[0][2].year)

# print("-----------------------------")
# query = f"DELETE FROM Kegiatan WHERE idKegiatan = 1"
# cn1._session.execute(query)
# cn1._connection.commit()
# cn1.selectToDoList()
# a = cn1._session.fetchall()
# print(a)


# cn1.filterStatus(a)
# result = cn1._session.fetchall()

# statement = "SELECT * FROM Kegiatan WHERE jenisStatus = 'On-Going'" 
# print(cn1.query("'Expired'"))

# some_name = 'On-Going'

# result = cn1.selectToDoList()
# print(result)