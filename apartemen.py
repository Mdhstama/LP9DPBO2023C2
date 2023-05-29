from hunian import Hunian


class Apartemen(Hunian):
    def __init__(
        self, nama_pemilik, img_path, jml_penghuni, jml_kamar, luas_hunian, listrik
    ):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, luas_hunian, listrik)
        self.nama_pemilik = nama_pemilik
        self.img_path = img_path

    def get_dokumen(self):
        return (
            "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n "
            + self.nama_pemilik
            + "."
        )

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_img(self):
        return self.img_path
