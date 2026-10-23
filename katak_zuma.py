
class KatakZuma:

    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True

    def ganti_warna(self, warna_baru):
        warna_lama = self.warna_peluru
        self.warna_peluru = warna_baru
        print(f"Warna peluru berhasil diubah: '{warna_lama}' -> '{self.warna_peluru}'")

    def tembak(self):
        self.skor += 50
        print(f"piuwww {self.warna_peluru} kena bola, skor jadi +50: {self.skor}")

    def info_status(self):
        print("\n" + "=" * 45)
        print("       STATUS KATAK ZUMA")
        print("=" * 45)
        print(f"  Warna Peluru  : {self.warna_peluru}")
        print(f"  Skor          : {self.skor}")
        print(f"  Status Aktif  : {self.is_active}")
        print("=" * 45 + "\n")


if __name__ == "__main__":

    print("\nSelamat Datang di Game Zuma!\n")

    katak_player = KatakZuma(warna_awal="Kuning")

    print("[1] Info status awal katak:")
    katak_player.info_status()

    print("[2] Mengganti warna peluru menjadi 'Merah':")
    katak_player.ganti_warna("Merah")

    print("\n[3] Menembakkan peluru:")
    katak_player.tembak()

    print("\n[4] Info status akhir katak setelah perubahan:")
    katak_player.info_status()
