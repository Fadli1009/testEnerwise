import pandas as pd

# membuat variable allDataKwh yang berisi dari soal
allDataKWH = [
    {
        "kwh_meter_id": 1,
        "kwh_usage": 10,
        "date": "5/10/2024 00:00:00",
    },
    {
        "kwh_meter_id": 1,
        "kwh_usage": 20,
        "date": "5/10/2024 01:00:00",
    },
    {
        "kwh_meter_id": 1,
        "kwh_usage": 33,
        "date": "5/10/2024 02:00:00",
        },
    {
        "kwh_meter_id": 1,
        "kwh_usage": 45,
        "date": "5/10/2024 03:00:00",
    },
    {
        "kwh_meter_id": 1,
        "kwh_usage": 51,
        "date": "5/10/2024 04:00:00",
    },
    {
        "kwh_meter_id": 1,
        "kwh_usage": 59,
        "date": "6/10/2024 00:00:00",
    },
    {
        "kwh_meter_id": 1,
        "kwh_usage": 65,
        "date": "6/10/2024 01:00:00",
    },
    {
        "kwh_meter_id": 1,
        "kwh_usage": 74,
        "date": "6/10/2024 02:00:00",
    },
    {
        "kwh_meter_id": 1,
        "kwh_usage": 89,
        "date": "6/10/2024 03:00:00",
    },
    {
        "kwh_meter_id": 1,
        "kwh_usage": 102,
        "date": "6/10/2024 04:00:00",
    },
    {
        "kwh_meter_id": 2,
        "kwh_usage": 8,
        "date": "5/10/2024 00:00:00",
    },
    {
        "kwh_meter_id": 2,
        "kwh_usage": 17,
        "date": "5/10/2024 01:00:00",
    },
    {
        "kwh_meter_id": 2,
        "kwh_usage": 27,
        "date": "5/10/2024 02:00:00",
    },
    {
        "kwh_meter_id": 2,
        "kwh_usage": 32,
        "date": "5/10/2024 03:00:00",
    },
    {
        "kwh_meter_id": 2,
        "kwh_usage": 44,
        "date": "5/10/2024 04:00:00",
    },
    {
        "kwh_meter_id": 2,
        "kwh_usage": 47,
        "date": "6/10/2024 00:00:00",
    },
    {
        "kwh_meter_id": 2,
        "kwh_usage": 51,
        "date": "6/10/2024 01:00:00",
    },
    {
        "kwh_meter_id": 2,
        "kwh_usage": 57,
        "date": "6/10/2024 02:00:00",
    },
    {
        "kwh_meter_id": 2,
        "kwh_usage": 61,
        "date": "6/10/2024 03:00:00",
    },
    {
        "kwh_meter_id": 2,
        "kwh_usage": 75,
        "date": "6/10/2024 04:00:00",
    },
]

# membuat frame yang berisi data dari variable allDataKWH (merapihkan)
pf = pd.DataFrame(allDataKWH)

# mengubah date dari allDataKWH menjadi datetime
pf['date'] = pd.to_datetime(pf['date'])

# mengonversikan date hanya mengambil date saja, tidak dengan waktunya
pf["date"] = pf['date'].dt.date

# mengelompokan berdasarkan kwh_meter_id dan juga tanggal, sekalian menambahkan hasil dari kwh usage
hasil = pf.groupby(['kwh_meter_id','date']).sum()

# menyetak hasil nya
print(hasil)