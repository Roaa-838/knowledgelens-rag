
from collections.abc import Iterator
from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import (
    CSVLoader,
    DirectoryLoader,
    PyPDFLoader,
    TextLoader,
    WebBaseLoader,
)


def test_load_text_file(file_path: str | Path) -> list[Document]:
    pass


def test_load_csv_file(file_path: str | Path) -> list[Document]:
    pass

def test_load_pdf_file(file_path: str | Path) -> list[Document]:
    pass

def test_load_web_page(url: str) -> list[Document]:
    pass


def test_load_directory(
    directory_path: str | Path,
    glob: str = "*.txt",
) -> list[Document]:
    pass


def test_iter_directory_documents(
    directory_path: str | Path,
    glob: str = "*.txt",
) -> Iterator[Document]:
    pass


def test_create_document(
    page_content: str,
    metadata: dict | None = None,
) -> Document:
    pass
