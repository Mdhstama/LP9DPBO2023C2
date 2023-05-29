import mysql.connector

# Konek ke dalam database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_test",
)

# Membuat kursor objek untuk menjalankan query SQL
cursor = db.cursor()


def insert_data(id, nama, umur):
    # insert datanya
    sql = "INSERT INTO user (id, nama, umur) VALUES (%s, %s, %s)"
    values = (id, nama, umur)

    try:
        # jalankan querynya
        cursor.execute(sql, values)
        db.commit()
        print("Data berhasil masuk kedalam database!!")
    except mysql.connector.Error as error:
        print("Terdapat error karena : ", error)


def show_data():
    # masukkan query
    sql = "SELECT * FROM user"

    try:
        # jalankan query
        cursor.execute(sql)

        # ambil data nya
        records = cursor.fetchall()

        # Print datanya
        for record in records:
            print("ID:", record[0])
            print("Nama:", record[1])
            print("Umur:", record[2])
            print("----------------")
    except mysql.connector.Error as error:
        print("\nTerdapat error karena : ", error)


def update_data(id, umur):
    # update datanya
    sql = "UPDATE user SET umur = %s WHERE id = %s"
    values = (umur, id)

    try:
        # jalankan querynya
        cursor.execute(sql, values)
        db.commit()
        print("\nData berhasil di update!!")
    except mysql.connector.Error as error:
        print("\nTerdapat error karena : ", error)


def delete_data(id):
    # delete datanya
    sql = "DELETE FROM user WHERE id = %s"
    value = (id,)

    try:
        # jalankan quernynya
        cursor.execute(sql, value)
        db.commit()
        print("\nData berhasil dihapus!!")
    except mysql.connector.Error as error:
        print("\nTerdapat error karena : ", error)


# Insert Data
insert_data(1, "Adit", 21)
insert_data(2, "Surya", 20)
print("\n------ Ini Data Insert ------")
show_data()

# Update Data Umur
update_data(2, 30)
print("\n------ Ini Update Data Ke-2 ------")
show_data()

# Delete Data
delete_data(1)
print("\n------ Ini Delete Data Ke-1 ------")
show_data()

# Tutup database
db.close()
