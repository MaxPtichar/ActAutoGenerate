from src.database.db_manager import DBManager
from src.models import Organization


class OrgServices:
    def __init__(self) -> None:
        self.db = DBManager()

    def add(self, org: Organization) -> None:
        self.db.insert_organization(org)

    def list_all(self) -> List[Organization]:
        return self.db.fetch_organization()
