import sqlite3

conn = sqlite3.connect('file.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
         )")
    conn.commit()
conn.close()

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'mymovie.mpg', 'World.txt', 'data.pdf','myPhoto.jpg')

conn = sqlite3.connect('file.db')

for f in fileList:
    if f.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files(col_file) VALUES (?)", (f,))
            print(f)   
conn.close()  

    