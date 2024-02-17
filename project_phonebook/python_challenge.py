import sqlite3


with sqlite3.connect(':memory:') as conn:
  cur= conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS Roster(\
              col_Name TEXT,\
              col_Species TEXT, \
              col_IQ INT \
            )")
  Roster_values = (('Jean-Baptiste Zorg','Human', 122),('Korben Dallas','Meat Popsicle', 100),('Ak not','Mangalore',-5))
  cur.executemany("INSERT INTO Roster(col_Name, col_Species, col_IQ) VALUES (?,?,?)", Roster_values)
  cur.execute("UPDATE Roster SET col_Species =? WHERE col_Name=? AND col_IQ=?",('Human','Korben Dallas',100) )
  cur.execute("SELECT col_Name , ]col_IQ FROM Roster WHERE col_Species = 'Human'")
  for row in cur.fetchall():
    print(row)
 