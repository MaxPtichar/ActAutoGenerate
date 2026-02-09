from src.database.db_manager import DBManager
from src.models import Organization


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
