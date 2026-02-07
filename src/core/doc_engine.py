from pathlib import Path

from docxtpl import DocxTemplate

from ..constants import MONTHS_RU
from ..database.db_manager import DBManager

db = DBManager()


def path_save(filename: str) -> Path:
    base_dir = Path(__file__).parent.parent
    out_path = base_dir / "output"
    out_path.mkdir(exist_ok=True)
    return out_path / filename


def create_files() -> None:
    base_dir = Path(__file__).parent.parent
    template_path = base_dir / "template" / "template1.docx"
    if not template_path.exists():
        print(f"ERRROR: Шаблон не найден по пути {template_path}")
        return
    all_fetch = db.fetch_organization()
    if all_fetch:
        try:
            for org in all_fetch:
                doc = DocxTemplate(str(template_path))
                context = {"org": org}

                doc.render(context)

                filename = f"{org.name} Акт за {MONTHS_RU[org.date.month][0]} № {org.act_counter}.docx"
                doc.save(path_save(filename))
                print(f"Успех: {filename}")
                org.prepare_next_period()
                db.update_data(org)
        except Exception as e:
            print(f"Ошибка при обработке {org}: {e}")
