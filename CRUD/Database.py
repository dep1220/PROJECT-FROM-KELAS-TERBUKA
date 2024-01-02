from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
  "pk": "XXXXXX",
  "date_add": "yyyy-mm-dd",
  "judul": 255*" ",
  "penulis": 100*" ",
  "tahun": "yyyy"
} 

def init_console():
  try:
    with open("data.txt", "r") as file:
      print("Database tersedia, init done!")
  except:
    print("Database tidak ditemukan, silahkan membuat database baru")
    Operasi.create_first_data()