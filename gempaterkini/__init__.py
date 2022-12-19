import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
        Gempabumi Terkini
    Tanggal: 10 November 2022
    Waktu: 12:56:30 WIB
    Magnitudo: 4.9
    Kedalaman: 10 km
    Lokasi: 4.28 LU 96.72 BT
    Pusat Gempa: Pusat gempa berada di darat 40 km BaratDaya Takengon
    Dirasakan: Dirasakan (Skala MMI): III Nagan Raya, III Benermeriah, I-II Pidie, I-II Lhokseumawe
    :return:
    """
    global tanggal, waktu, magnitudo, kedalaman, ls, bt, lokasi, dirasakan
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        print('tidak dapat mengekstraks data')
        return None

    # print(content.status_code)
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")
        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1
    hasilnya = dict()
    hasilnya['tanggal'] = tanggal
    hasilnya['waktu'] = waktu
    hasilnya['magnitudo'] = magnitudo
    hasilnya['kedalaman'] = kedalaman
    hasilnya['lokasi'] = {'LS': ls, 'BT': bt}
    hasilnya['pusat gempa'] = lokasi
    hasilnya['dirasakan'] = dirasakan

    return hasilnya


def tampilkan_data(hasilnya):
    print('GEMPA TERAKHIR BERDASARKAN BMKG:')
    print(f"tanggal {hasilnya['tanggal']}")
    print(f"waktu {hasilnya['waktu']}")
    print(f"magnitudo {hasilnya['magnitudo']}")
    print(f"kedalaman {hasilnya['kedalaman']}")
    print('lokasi:')
    print(f"    LU= {hasilnya['lokasi']['LS']}")
    print(f"    BT= {hasilnya['lokasi']['BT']}")
    print(hasilnya['pusat gempa'])
    print(hasilnya['dirasakan'])

