from datetime import datetime

from src.database.db_manager import DBManager
from src.models import Organization, Requisites


class OrgServices:
    def __init__(self) -> None:
        self.db = DBManager()

    def add_org(self, org: Organization) -> None:
        self.db.insert_organization(org)

    def list_all(self) -> List[Organization]:
        return self.db.fetch_organization()

    def deleted_org(self, org: Organization) -> None:
        return self.db.delete_organization(org)

    def edit_org(self, org: Organization):
        return self.db.edit_organization(org)

    @staticmethod
    def build_org(data: dict) -> Organization:
        return Organization(
            id=data["id"],
            name=data["name"],
            manager_name=data["manager_name"],
            agreement=data["agreement"],
            fee=float(data["fee"]),
            act_counter=int(data["act_counter"]),
            date=datetime.strptime(data["date"], "%d.%m.%Y").date(),
            requisites=Requisites(
                unp=data["unp"],
                address=data["address"],
                bank_account=data["bank_account"],
                name_of_bank=data["name_of_bank"],
                bic=data["bic"],
                mobile_num=data["mobile_num"],
                e_mail=data["e_mail"],
            ),
        )
