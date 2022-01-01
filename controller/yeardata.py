import model.yeardata
import json


def yearcontroller(since, upto):
    data = model.yeardata.modelyeardata()
    # print(data)
    datafx = []
    dataparse = json.loads(data)
    # print(dataparse["data"])
    for i in dataparse["update"]["harian"]:
        # print(i['key_as_string'])
        year = i['key_as_string'][:4]
        # print(year)

        if year >= since and year <= upto:
            # print(i['jumlah_dirawat']['value'])
            data = {
                "year": year,
                "positive": i['jumlah_positif']['value'],
                "recovered": i['jumlah_sembuh']['value'],
                "deaths": i['jumlah_meninggal']['value'],
                "active": i['jumlah_dirawat']['value'],
            }
            datafx.append(data)

    datax = {
        "ok": True,
        "data": datafx,
        "message": "Data Berhasil Di get"
    }
    datay = json.dumps(datax)
    return datay
