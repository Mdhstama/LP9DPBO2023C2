from hunian import Hunian


class Rumah(Hunian):
    def __init__(
        self, nama_pemilik, img_path, jml_penghuni, jml_kamar, luas_hunian, listrik
    ):
        super().__init__("Rumah", jml_penghuni, jml_kamar, luas_hunian, listrik)
        self.nama_pemilik = nama_pemilik
        self.img_path = img_path

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_img(self):
        return self.img_path
