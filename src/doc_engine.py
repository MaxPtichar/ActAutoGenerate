from datetime import date

from docxtpl import DocxTemplate

from constants import MONTHS_RU
from database import DBManager
from models import Organization, Requisites

db = DBManager("database/organization.db")


all_fetch = db.fetch_organization()
if all_fetch:
    for org in all_fetch:
        doc = DocxTemplate("template//template1.docx")
        context = {"org": org}
        print(org)
        doc.render(context)

        doc.save(
            f"{org.name} Акт за {MONTHS_RU[org.date.month][0]} № {org.act_counter}.docx"
        )
        org.prepare_next_period()
        db.update_data(org)
