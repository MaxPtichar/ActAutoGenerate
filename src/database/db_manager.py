import sqlite3
from datetime import date
from pathlib import Path

from src.models import Organization, Requisites


class DBManager:
    def __init__(self) -> None:
        self.base_dir = Path(__file__).parent.parent.parent
        self.db_path = self.base_dir / "data" / "organization.db"
        self.connect = sqlite3.connect(str(self.db_path.absolute()))
        self.cursor = self.connect.cursor()
        self.create_table()

    def execute_query(self, query, params=None):
        if not params:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.connect.commit()

    def create_table(self):
        query = """ CREATE TABLE IF NOT EXISTS organizations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        manager_name TEXT,
        agreement TEXT,
        fee REAL,
        act_counter INTEGER,
        date TEXT,
        last_issued_num INTEGER,
        -- Реквизиты (плоским списком)
        unp TEXT UNIQUE,
        address TEXT,
        bank_account TEXT,
        name_of_bank TEXT,
        bic TEXT,
        mobile_num TEXT,
        e_mail TEXT
    )
    """
        self.execute_query(query)

    def insert_organization(self, org: Organization):
        try:
            query = (
                "INSERT INTO organizations (name, manager_name, agreement, fee, act_counter, "
                "date, last_issued_num, unp, address, bank_account, name_of_bank, bic, mobile_num, e_mail) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            )

            values = (
                org.name,
                org.manager_name,
                org.agreement,
                org.fee,
                org.act_counter,
                org.date.isoformat(),
                org.last_issued_num,
                org.requisites.unp,
                org.requisites.address,
                org.requisites.bank_account,
                org.requisites.name_of_bank,
                org.requisites.bic,
                org.requisites.mobile_num,
                org.requisites.e_mail,
            )
            self.execute_query(query, params=values)

        except sqlite3.IntegrityError as e:
            print(f"Ошибка {e}. Такое значение унп {org.requisites.unp} уже есть")

    def update_data(self, org: Organization):
        query = """UPDATE organizations SET act_counter = ?, last_issued_num = ?, date = ? WHERE id = ?"""
        params = (org.act_counter, org.last_issued_num, org.date.isoformat(), org.id)
        self.execute_query(query, params)

    def fetch_organization(self):
        query = "SELECT * FROM organizations"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        organizations = []
        for row in rows:
            req = Requisites(
                unp=row[8],
                address=row[9],
                bank_account=row[10],
                name_of_bank=row[11],
                bic=row[12],
                mobile_num=row[13],
                e_mail=row[14],
            )
            org = Organization(
                id=row[0],
                name=row[1],
                manager_name=row[2],
                agreement=row[3],
                fee=row[4],
                act_counter=row[5],
                date=date.fromisoformat(row[6]),
                requisites=req,
                last_issued_num=row[7],
            )
            organizations.append(org)

        return organizations

    def delete_organization(self, org_unp):
        try:
            query = "DELETE FROM organizations WHERE unp = ?"
            val = (org_unp,)
            self.execute_query(query, params=val)
            print(f"Successfully deleted")
        except sqlite3.OperationalError as e:
            raise Exception(f"Ошибка {e}. Такого унп {org_unp} нет.") from e
