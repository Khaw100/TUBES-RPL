from datetime import datetime

today = datetime.now()
print(today)

print(type(today.year))
a = f"{today.year}-{today.month}-{today.day}"
print(a)
print(type(a))

strToday = f"{today.year}-{today.month}-{today.day}"
statement = f"SELECT * FROM Kegiatan WHERE batasWaktu = '{strToday}'"
print(statement)

