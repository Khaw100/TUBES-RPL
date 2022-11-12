import mariadb
import sys

def connector():
    try:
        conn = mariadb.connect(
            user = "wipiii",
            password = "miscrit10",
            host = "localhost",
            port = 3306,
            database = "rpl"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn

a = connector()
curr = a.cursor()

# someName = input("Nama:")

# curr.execute(
#     "SELECT * FROM Kegiatan WHERE namaKegiatan=?",(someName,))

# result = curr.fetchall()

# print(result)
# # for i in result:
#     print(i)

def selectToDoList():
    result = curr.execute("SELECT * FROM Kegiatan")
    return result

def updateKegiatan():
    result = curr.execute("UPDATE Kegiatan SET jenisStatus = 'expired'")
    return result

def autoUpdateKegiatan():
    result = curr.execute("UPDATE Kegiatan SET jenisStatus = 'on-going'")
    return result

def addActivity(activityID, name, status, deadline, categoryID):
    result = curr.execute("INSERT INTO Kegiatan (idKegiatan, namaKegiatan, jenisStatus, batasWaktu, idKategori) VALUES (?, ?, ?, ?, ?)", (activityID, name, status, deadline, categoryID))
    return result

def deleteKegiatan(activityID):
    result = curr.execute("DELETE FROM Kegiatan WHERE idKegiatan = ?", (activityID))
    return result

def filterKategori(selectedIDKategori):
    result = curr.execute("SELECT idKegiatan, namaKegiatan, batasWaktu, jenisStatus, idKategori FROM Kegiatan INNER JOIN Kategori WHERE jenisKategori =?", (selectedIDKategori))
    return result

def filterStatus(selectedStatus):
    result = curr.execute("SELECT * FROM jenisStatus = ?", (selectedStatus))
    return result

# def filterBatasWaktu(selectedWaktu):
    # result
    # return result

selectToDoList()
result = curr.fetchall()
print(result)



# idA = int(input("ID Kegiatan: "))
# nama = input("Nama Kegiatan: ")
# status = input("Status: ")
# waktu = input("BatasWaktu: ")
# idC = int(input("ID Kategori: "))
# addActivity(idA, nama, status, waktu, idC)
# result = curr.fetchall()
# print(result)

