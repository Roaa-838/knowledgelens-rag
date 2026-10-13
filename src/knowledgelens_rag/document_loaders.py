
from collections.abc import Iterator
from pathlib import Path

from langchain_community.document_loaders import (
    CSVLoader,
    DirectoryLoader,
    PyPDFLoader,
    TextLoader,
    WebBaseLoader,
)
from langchain_core.documents import Document


def _validate_file(file_path: str | Path) -> Path:
    """Validate and return an existing file path."""
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    return path


def load_text_file(file_path: str | Path) -> list[Document]:
    """Load a plain-text file."""
    path = _validate_file(file_path)
    return TextLoader(str(path), encoding="utf-8").load()


def load_csv_file(file_path: str | Path) -> list[Document]:
    """Load a CSV file, producing documents from its rows."""
    path = _validate_file(file_path)
    return CSVLoader(str(path)).load()


def load_pdf_file(file_path: str | Path) -> list[Document]:
    """Load a PDF file, producing documents from its pages."""
    path = _validate_file(file_path)
    return PyPDFLoader(str(path)).load()


def load_web_page(url: str) -> list[Document]:
    """Load and parse a webpage."""
    if not url.startswith(("https://", "http://")):
        raise ValueError("URL must start with http:// or https://")

    return WebBaseLoader(url).load()


def load_directory(
    directory_path: str | Path,
    glob: str = "*.txt",
) -> list[Document]:
    """Load matching text files from a directory."""
    path = Path(directory_path)

    if not path.is_dir():
        raise NotADirectoryError(f"Directory not found: {path}")

    loader = DirectoryLoader(
        str(path),
        glob=glob,
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )
    return loader.load()


def iter_directory_documents(
    directory_path: str | Path,
    glob: str = "*.txt",
) -> Iterator[Document]:
    """Yield matching documents incrementally."""
    path = Path(directory_path)

    if not path.is_dir():
        raise NotADirectoryError(f"Directory not found: {path}")

    loader = DirectoryLoader(
        str(path),
        glob=glob,
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )
    yield from loader.lazy_load()


def create_document(
    page_content: str,
    metadata: dict[str, object] | None = None,
) -> Document:
    """Create a LangChain Document from text and optional metadata."""
    return Document(
        page_content=page_content,
        metadata={} if metadata is None else metadata,
    )
