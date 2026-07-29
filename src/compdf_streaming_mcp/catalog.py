"""The ComPDF API v2 operation catalogue grouped by MCP route module."""

from __future__ import annotations

from dataclasses import dataclass


DOCS_ROOT = "https://www.compdf.com/guides/api-reference/v2"


@dataclass(frozen=True)
class Operation:
    name: str
    path: str
    module: str
    documentation_slug: str
    description: str
    min_files: int = 1
    max_files: int | None = 1

    @property
    def documentation_url(self) -> str:
        return f"{DOCS_ROOT}/{self.documentation_slug}"


def _operation(name: str, path: str, module: str, slug: str, description: str, min_files: int = 1, max_files: int | None = 1) -> Operation:
    return Operation(name, path, module, slug, description, min_files, max_files)


_OPERATIONS = [
    # Conversion API.
    _operation("pdf_to_word", "/v2/process/pdf/docx", "conversion", "pdf-to-word", "Convert PDF to Word DOCX."),
    _operation("pdf_to_excel", "/v2/process/pdf/xlsx", "conversion", "pdf-to-excel", "Convert PDF to Excel XLSX."),
    _operation("pdf_to_ppt", "/v2/process/pdf/pptx", "conversion", "pdf-to-ppt", "Convert PDF to PowerPoint PPTX."),
    _operation("pdf_to_html", "/v2/process/pdf/html", "conversion", "pdf-to-html", "Convert PDF to HTML."),
    _operation("pdf_to_rtf", "/v2/process/pdf/rtf", "conversion", "pdf-to-rtf", "Convert PDF to RTF."),
    _operation("pdf_to_image", "/v2/process/pdf/img", "conversion", "pdf-to-image", "Render PDF pages as images."),
    _operation("pdf_to_csv", "/v2/process/pdf/csv", "conversion", "pdf-to-csv", "Extract PDF tables as CSV."),
    _operation("pdf_to_txt", "/v2/process/pdf/txt", "conversion", "pdf-to-txt", "Convert PDF to plain text."),
    _operation("pdf_to_json", "/v2/process/pdf/json", "conversion", "pdf-to-json", "Convert PDF content to JSON."),
    _operation("pdf_to_markdown", "/v2/process/pdf/markdown", "conversion", "pdf-to-md", "Convert PDF to Markdown."),
    _operation("pdf_to_ofd", "/v2/process/pdf/ofd", "conversion", "pdf-to-ofd", "Convert PDF to OFD."),
    _operation("pdf_to_editable_pdf", "/v2/process/pdf/editable", "conversion", "pdf-to-editable-pdf-tool-guide", "Convert PDF to editable/searchable PDF."),
    _operation("word_to_pdf", "/v2/process/docx/pdf", "conversion", "word-to-pdf", "Convert Word DOCX to PDF."),
    _operation("excel_to_pdf", "/v2/process/xlsx/pdf", "conversion", "excel-to-pdf", "Convert Excel XLSX to PDF."),
    _operation("ppt_to_pdf", "/v2/process/pptx/pdf", "conversion", "ppt-to-pdf", "Convert PowerPoint PPTX to PDF."),
    _operation("html_to_pdf", "/v2/process/html/pdf", "conversion", "html-to-pdf", "Convert HTML to PDF."),
    _operation("rtf_to_pdf", "/v2/process/rtf/pdf", "conversion", "rtf-to-pdf", "Convert RTF to PDF."),
    _operation("txt_to_pdf", "/v2/process/txt/pdf", "conversion", "txt-to-pdf", "Convert TXT to PDF."),
    _operation("csv_to_pdf", "/v2/process/csv/pdf", "conversion", "csv-to-pdf", "Convert CSV to PDF."),
    _operation("image_to_pdf", "/v2/process/img/pdf", "conversion", "image-to-pdf", "Convert image to PDF."),
    _operation("image_to_word", "/v2/process/img/docx", "conversion", "image-to-word", "Convert image to Word DOCX."),
    _operation("image_to_excel", "/v2/process/img/xlsx", "conversion", "image-to-excel", "Convert image to Excel XLSX."),
    _operation("image_to_ppt", "/v2/process/img/pptx", "conversion", "image-to-ppt", "Convert image to PowerPoint PPTX."),
    _operation("image_to_html", "/v2/process/img/html", "conversion", "image-to-html", "Convert image to HTML."),
    _operation("image_to_rtf", "/v2/process/img/rtf", "conversion", "image-to-rtf", "Convert image to RTF."),
    _operation("image_to_csv", "/v2/process/img/csv", "conversion", "image-to-csv", "Extract image tables as CSV."),
    _operation("image_to_txt", "/v2/process/img/txt", "conversion", "image-to-txt", "Convert image to text."),
    _operation("image_to_json", "/v2/process/img/json", "conversion", "image-to-json", "Convert image content to JSON."),
    # ComPDF AI.
    _operation("document_parse", "/v2/process/idp/documentParsing", "ai", "documentParsing", "Parse document layout and content."),
    _operation("document_extract", "/v2/process/idp/documentExtract", "ai", "documentExtract", "Extract fields with an extraction schema."),
    # PDF generation.
    _operation("generate_pdf", "/v2/process/pdf/generate", "generate", "pdf-generate", "Generate a PDF from HTML or template data.", 0, 0),
    # PDF API.
    _operation("merge_pdf", "/v2/process/pdf/merge", "pdf", "merge", "Merge PDF files.", 2, None),
    _operation("split_pdf", "/v2/process/pdf/split", "pdf", "split", "Split a PDF."),
    _operation("extract_pdf_pages", "/v2/process/pdf/extract", "pdf", "extract", "Extract selected PDF pages."),
    _operation("insert_pdf_pages", "/v2/process/pdf/insert", "pdf", "insert", "Insert PDF pages.", 1, 2),
    _operation("delete_pdf_pages", "/v2/process/pdf/delete", "pdf", "delete", "Delete PDF pages."),
    _operation("rotate_pdf_pages", "/v2/process/pdf/rotation", "pdf", "rotate", "Rotate PDF pages."),
    _operation("convert_pdf_standard", "/v2/process/pdf/convertType", "pdf", "pdf-convertType", "Convert PDF conformance standard."),
    _operation("add_watermark", "/v2/process/pdf/addWatermark", "pdf", "watermark-guides", "Add a watermark."),
    _operation("remove_watermark", "/v2/process/pdf/delWatermark", "pdf", "del-watermark-guides", "Remove a watermark."),
    _operation("compress_pdf", "/v2/process/pdf/compress", "pdf", "compress-guides", "Compress PDF."),
    _operation("encrypt_pdf", "/v2/process/pdf/encrypt", "pdf", "pdf-encrypt", "Encrypt PDF."),
    _operation("decrypt_pdf", "/v2/process/pdf/decrypt", "pdf", "pdf-decrypt", "Decrypt PDF."),
    _operation("compare_pdf", "/v2/process/pdf/contentCompare", "pdf", "compare-documents", "Compare two PDFs.", 2, 2),
]

OPERATIONS = {operation.name: operation for operation in _OPERATIONS}
MODULES = ("conversion", "ai", "pdf", "generate")


def get_operation(name: str) -> Operation:
    try:
        return OPERATIONS[name]
    except KeyError as error:
        raise ValueError(f"Unsupported operation: {name}") from error


def operations_for(module: str) -> list[Operation]:
    if module not in MODULES:
        raise ValueError(f"Unsupported module: {module}")
    return [operation for operation in _OPERATIONS if operation.module == module]
