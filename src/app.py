import sqlite3

#create a db
DBNAME = 'moviesInfo.db'
def init_db():
    conn = sqlite3.connect(DBNAME)
    conn.close()

#===============================================
init_db()








def  create_table():
    query = '''

        CREATE TABLE IF  NOT EXISTS movies 
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        title TEXT NOT NULL,
        country  TEXT, 
        year TEXT , 
        imdb_rate REAL
        )
            '''

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

#====================================================
#create_table()








def insert_recort(title, counrty, year, imdb_rate ):
    query = '''
        INSERT INTO movies (title, country, year, imdb_rate )
        VALUES (?, ? ,? ,?)

        '''     

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query, (title, counrty, year, imdb_rate ))
    conn.commit()
    conn.close()

#========================================================

#insert_recort('odyse', 'usa', '2026', '9.7')
#insert_recort('openhimer', 'usa, ireland', '2025', '8.5')







def select_all_recorde():
    #query = 'SELECT * FROM  movies'
    query_2 =  'SELECT title, country  FROM  movies'
# this up is two query example  

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    #rows = cursor.execute(query).fetchall()
    rows = cursor.execute(query_2).fetchall()


    conn.close()
    return rows

#=============================================================
#print(select_all_recorde())







def  select_record_by_id(id):
    query = 'SELECT * FROM  movies WHERE  id = ?'
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    rows = cursor.execute(query, (id,)).fetchone()


    conn.close()
    return rows

#===================================
#print(select_record_by_id(2))






def  select_record_by_title(title):
    query = 'SELECT * FROM  movies  WHERE title = ?'
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    rows = cursor.execute(query, (title,)).fetchone()


    conn.close()
    return rows

#==================================================
#print(select_record_by_title('odyse'))






def delete_record_by_id(id):

    query = 'DELETE FROM movies  WHERE id = ?'
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query,(id,))
    conn.commit()
    conn.close()
    #return if we put this its just can tell us seccess or not 
    #return id we want to return something
#====================================================================
#delete_record_by_id(2)














def update_record_by_id (id,imdb_rate, year):
    query = 'UPDATE movies SET   imdb_rate = ? , year = ? WHERE id = ?'
    
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query,(imdb_rate, year, id))
    conn.commit()
    conn.close()
#khate 160 bayad az khat  157  olgo begire faghat!!!!!!!!!!!!!!
#=================

#update_record_by_id(1, 4.5, '2020')