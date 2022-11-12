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

    def selectToDoList(self):
        statement = "SELECT * FROM Kegiatan"
        try:
            self._session.execute(statement)
            data = self._session.fetchall()
        except:
            print("Failed!")
        return data

    def updateStatus(self):
        result = self._session.execute("UPDATE Kegiatan SET status = 'ongoing'")
        return result

    def autoUpdateStatus(self):
        result = self._session.execute("UPDATE Kegiatan SET status = 'expired'")
        return result
    
    def addActivity(self, activityID, name, status, deadline, categoryID):
        result = self._session.execute("INSERT INTO Kegiatan (idKegiatan, namaKegiatan, jenisStatus, batasWaktu, idKategori) VALUES (?, ?, ?, ?, ?)", (activityID, name, status, deadline, categoryID))
        return result

    def deleteKegiatan(self, activityID):
        result = self._sessionr.execute("DELETE FROM Kegiatan WHERE idKegiatan = ?", (activityID))
        return result

    def filterKategori(self, selectedIDKategori):
        statement = f"SELECT idKegiatan, namaKegiatan, batasWaktu, jenisStatus, jenisKategori FROM Kegiatan INNER JOIN Kategori WHERE idKategori = '{selectedIDKategori}'"
        try:
            self._session.execute(statement)
            data = self._session.fetchall()
        except:
            print("Failed!")
        return data

    def filterStatus(self,selectedstatus):
        statement = f"SELECT * FROM Kegiatan WHERE jenisStatus = '{selectedstatus}'"
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
        statement = f"SELECT * FROM Kegiatan WHERE batasWaktu = '{strToday}'"
        try:
            self._session.execute(statement)
            data = self._session.fetchall()
        except:
            print("Failed!")
        return data

cn1 = connector("localhost", "wipiii", "miscrit10", "rpl")
cn1.openConnection()
# cn1.selectToDoList()
a = "'Expired'"
cn1._session.execute(f"SELECT * FROM Kegiatan WHERE jenisStatus = {a}")

a = cn1._session.fetchall()
print(type(a[0][2]))

print(a[0][2].year)


# cn1.filterStatus(a)
# result = cn1._session.fetchall()

# statement = "SELECT * FROM Kegiatan WHERE jenisStatus = 'On-Going'" 
# print(cn1.query("'Expired'"))

# some_name = 'On-Going'

# result = cn1.selectToDoList()
# print(result)