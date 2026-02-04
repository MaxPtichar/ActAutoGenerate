if __name__ == "__main__":
    db = DBManager("database/organization.db")
    req = Requisites(
        unp="191380192",
        address="220037, г. Минск, ул. Багратиона, д. 62, комн. 7",
        bank_account="BY79BPSB30121754740119330000",
        name_of_bank= "ОАО 'СберБанк'",
        bic="BPSBBY2X",
        mobile_num="272-81-07",
        e_mail="vimalit@yandex.ru, buh.niitvs@gmail.com",
    )

    new_org = Organization(
        id=None,
        name="Вималит",
        manager_name="Семашко Алексей Сергеевич",
        agreement="3/0412 от 04 декабря 2023 года",
        fee=200,
        act_counter=26,
        date=date(2026, 1, 30),
        requisites=req,
    )
    db.insert_organization(new_org)



    if __name__ == "__main__":
    db = DBManager("database/organization.db")
    print(db.fetch_organization(1))
    req = Requisites(
        name="«Акрифор»",
        unp="193018622",
        address="220037, г. Минск, ул. Багратиона, д. 62, комн. 7",
        bank_account="BY59BPSB30123037360139330000",
        name_of_bank= "ОАО 'СберБанк'",
        bic="BPSBBY2X",
        mobile_num="80173735162",
        e_mail="akrifor2017@gmail.com",
    )

    new_org = Organization(
        id=None,
        name="«Акрифор»",
        manager_name="Клочко Дмитрия Владимировича",
        agreement="№ 1/0412 от 04 декабря 2023 года",
        fee=1801,
        act_counter=26,
        date=date(2026, 1, 30),
        requisites=req,
    )
    db.insert_organization(new_org)
