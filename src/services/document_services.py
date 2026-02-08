from src.core import doc_engine


class DocumentService:
    def __init__(self) -> None:
        self.template_path: str | None = None

    def generate_acts(self) -> None:
        doc_engine.create_files(self.template_path)

    def get_path_for_generate(self, path: str):

        self.template_path = path
