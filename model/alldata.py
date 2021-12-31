import http.client
import json

from flask import jsonify


def modelalldata():
    conn = http.client.HTTPSConnection("data.covid19.go.id")
    payload = ''
    headers = {}
    conn.request("GET", "/public/api/update.json", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))
    dataparse = json.loads(data)
    print(dataparse["data"])
    # penambahan
    total_positive = dataparse["update"]["total"]["jumlah_positif"]
    total_recovered = dataparse["update"]["total"]["jumlah_sembuh"]
    total_death = dataparse["update"]["total"]["jumlah_meninggal"]
    total_active = dataparse["update"]["total"]["jumlah_dirawat"]

    new_positif = dataparse["update"]["penambahan"]["jumlah_positif"]
    new_recovered = dataparse["update"]["penambahan"]["jumlah_sembuh"]
    new_death = dataparse["update"]["penambahan"]["jumlah_meninggal"]
    new_active = dataparse["update"]["penambahan"]["jumlah_dirawat"]

    datax = {
        "ok": True,
        "data": {
            "total_positive": total_positive,
            "total_recovered": total_recovered,
            "total_deaths": total_death,
            "total_active": total_active,

            "new_positive": new_positif,
            "new_recovered": new_recovered,
            "new_deaths": new_death,
            "new_active": new_active,
        },
        "message":"Data Berhasil Di get"

    }
    # “new_positive”: < value >,
    # “new_recovered”: < value >,,
    # “new_deaths”: < value >,
    # “new_active”: < value >,
    datay = json.dumps(datax)
    return datay
