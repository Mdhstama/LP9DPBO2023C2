from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import Image, ImageTk

hunians = []
hunians.append(Apartemen("Adit", "assets/apart.jpg", 3, 3, 40, 500))
hunians.append(Rumah("Fahreza", "assets/home.jpg", 5, 2, 250, 2200))
hunians.append(Indekos("Nabhan", "Reydi", "assets/dorm.jpg", 35, 400))
hunians.append(Rumah("Fadhil", "assets/home.jpg", 1, 4, 175, 1300))

root = Tk()
root.title("2000360 - Muhammad Aditya C1 2020 | Praktikum LP9 DPBO Python 2023")

# ---------- Frame Detail ----------


def details(index):
    # frame detail
    top = Toplevel()
    top.title("Detail Residen " + hunians[index].get_jenis())

    # frame data residem
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # ---------- Data ----------

    # summary
    d_summary = Label(
        d_frame, text="Summary : " + hunians[index].get_summary(), anchor="w"
    ).grid(row=0, column=0, sticky="w")

    # pemilik hunian
    d_pemilik = Label(
        d_frame,
        text="Pemilik Hunian : " + hunians[index].get_nama_pemilik(),
        anchor="w",
    ).grid(row=1, column=0, sticky="w")

    # (hunian == indekos, tampilkan penghuni) dan (hunian != indekos, tampilkan jumlah kamar)
    if hunians[index].get_jenis() == "Indekos":
        d_penghuni = Label(
            d_frame, text="Penghuni : " + hunians[index].get_nama_penghuni(), anchor="w"
        ).grid(row=2, column=0, sticky="w")
    else:
        d_jml_kamar = Label(
            d_frame,
            text="Jumlah Kamar : " + str(hunians[index].get_jml_kamar()),
            anchor="w",
        ).grid(row=2, column=0, sticky="w")

    # luas hunian
    d_luasTanah = Label(
        d_frame,
        text="Luas Hunian : " + str(hunians[index].get_luas_hunian()) + " m^2",
        anchor="w",
    ).grid(row=3, column=0, sticky="w")

    # luas hunian
    d_listrik = Label(
        d_frame,
        text="Kapasitas Listrik : " + str(hunians[index].get_listrik()) + "VA",
        anchor="w",
    ).grid(row=4, column=0, sticky="w")

    # dokumen
    d_document = Label(
        d_frame, text="Dokumen : " + hunians[index].get_dokumen(), anchor="w"
    ).grid(row=5, column=0, sticky="w")

    # Load the image
    image_path = hunians[index].get_img()
    image = Image.open(image_path)
    resized_image = image.resize((100, 100))  # Resize the image if needed

    # Convert the image to PhotoImage
    photo = ImageTk.PhotoImage(resized_image)

    # Create a label to display the image
    image_label = Label(d_frame, image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection
    image_label.grid(row=6, column=0, sticky="w")

    # ---------- Button ----------
    opts = LabelFrame(top, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    # back button
    d_back = Button(opts, text="Back", command=top.destroy)
    d_back.grid(row=0, column=0)


# ---------- Landing Page ----------
def show_main_page():
    landing_frame.pack_forget()
    main_frame.pack(padx=10, pady=10)


landing_frame = Frame(root, padx=10, pady=10)
landing_frame.pack(padx=10, pady=10)

landing_label = Label(
    landing_frame, text="Welcome to Database Resident", font=("Arial", 18)
)
landing_label.pack(pady=10)

landing_button = Button(
    landing_frame, text="Detail Data Resident", command=show_main_page
)
landing_button.pack(pady=10)

# ---------- Main Page ----------
main_frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)

# Hide the main frame initially
main_frame.pack_forget()

# ---------- Data ----------
for index, h in enumerate(hunians):
    # iterasi nomor
    idx = Label(main_frame, text=str(index + 1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    # jenis hunian
    type = Label(
        main_frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid"
    )
    type.grid(row=index, column=1)

    # hunian nama pemilik
    if h.get_jenis() != "Indekos":
        name = Label(
            main_frame,
            text=" " + h.get_nama_pemilik(),
            width=40,
            borderwidth=1,
            relief="solid",
            anchor="w",
        )
        name.grid(row=index, column=2)
    else:
        name = Label(
            main_frame,
            text=" " + h.get_nama_penghuni(),
            width=40,
            borderwidth=1,
            relief="solid",
            anchor="w",
        )
        name.grid(row=index, column=2)

    # button detail
    b_detail = Button(
        main_frame, text="Details ", command=lambda index=index: details(index)
    )
    b_detail.grid(row=index, column=3)

root.mainloop()
