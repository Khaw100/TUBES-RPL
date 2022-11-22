import mariadb
import sys
from datetime import datetime

class connector2():
    def __init__(self):
        pass

    def allToDoList(self):
        conn = mariadb.connect(
                user = "wipiii",
                password = "miscrit10",
                host = "localhost",
                port = 3306,
                database = "rpl"
                )
        session = conn.cursor()
        statement = "SELECT * FROM Kegiatan"
        try:
            session.execute(statement)
            data = session.fetchall()
        except:
            print("Failed!")

        conn.close()
        return data
    
    def updateStatusOnGOing(self, activityID):
        conn = mariadb.connect(
                user = "wipiii",
                password = "miscrit10",
                host = "localhost",
                port = 3306,
                database = "rpl"
                )
        session = conn.cursor()
        statement = f"UPDATE Kegiatan SET status = 'ongoing' WHERE = {activityID}"
        try:
            session.execute(statement)
            conn.commit()
        except:
            print("Failed!") 
        conn.close()


    def autoUpdateStatusExpired(self, activityID):
        conn = mariadb.connect(
                user = "wipiii",
                password = "miscrit10",
                host = "localhost",
                port = 3306,
                database = "rpl"
                )
        session = conn.cursor()
        statement = f"UPDATE Kegiatan SET status = 'expired' WHERE idKegiatan = {activityID}"
        try:
            session.execute(statement)
            conn.commit()
        except:
            print("Failed!")
        conn.close()

    def addActivity(self, activityID, name, status, deadline, categoryID):
        conn = mariadb.connect(
                user = "wipiii",
                password = "miscrit10",
                host = "localhost",
                port = 3306,
                database = "rpl"
                )
        session = conn.cursor()
        statement = f"INSERT INTO Kegiatan (idKegiatan, namaKegiatan, jenisStatus, batasWaktu, idKategori) VALUES ({activityID}, '{name}', '{status}', '{deadline}', {categoryID})"
        try:
            session.execute(statement)
            conn.commit()
        except:
            print("Failed!")
        conn.close()

    def deleteKegiatan(self, activityID):
        conn = mariadb.connect(
                user = "wipiii",
                password = "miscrit10",
                host = "localhost",
                port = 3306,
                database = "rpl"
                )
        session = conn.cursor()
        statement = f"DELETE FROM Kegiatan WHERE idKegiatan = {activityID}"
        try:
            session.execute(statement)
            conn.commit()
        except:
            print("Failed!")
        conn.close()

    def filterKategori(self, selectedIDKategori):
        conn = mariadb.connect(
                user = "wipiii",
                password = "miscrit10",
                host = "localhost",
                port = 3306,
                database = "rpl"
                )
        session = conn.cursor()
        statement = f"SELECT idKegiatan, namaKegiatan, batasWaktu, jenisStatus, jenisKategori FROM Kegiatan INNER JOIN Kategori WHERE idKategori = '{selectedIDKategori}'"
        try:
            session.execute(statement)
            data = session.fetchall()
        except:
            print("Failed!")
        conn.close()
        return data

    def filterStatus(self,selectedstatus):
        conn = mariadb.connect(
                user = "wipiii",
                password = "miscrit10",
                host = "localhost",
                port = 3306,
                database = "rpl"
                )
        session = conn.cursor()
        statement = f"SELECT * FROM Kegiatan WHERE jenisStatus = '{selectedstatus}'"
        try:
            session.execute(statement)
            data = session.fetchall()
        except:
            print("Failed!")
        conn.close()
        return data

    def filterBatasWaktuToday(self):
        conn = mariadb.connect(
                user = "wipiii",
                password = "miscrit10",
                host = "localhost",
                port = 3306,
                database = "rpl"
                )
        session = conn.cursor()
        today = datetime.now()
        strToday = f"{today.year}-{today.month}-{today.day}"
        statement = f"SELECT * FROM Kegiatan WHERE batasWaktu = '{strToday}'"
        try:
            session.execute(statement)
            data = session.fetchall()
        except:
            print("Failed!")
        conn.close()
        return data