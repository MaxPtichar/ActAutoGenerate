from pathlib import Path

from docxtpl import DocxTemplate

from src.core.paths import get_output_dir

from ..constants import MONTHS_RU
from ..database.db_manager import DBManager

db = DBManager()


def path_save(filename: str) -> Path:
    base_dir = get_output_dir()
    out_path = base_dir
    print(out_path / filename)
    return out_path / filename


def create_files(selected_template: str) -> None:
    template_path = Path(selected_template)

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
