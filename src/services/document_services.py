from src.core import doc_engine


class DocumentService:
    def generate_acts(self) -> None:
        doc_engine.create_files()
