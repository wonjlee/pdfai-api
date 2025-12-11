import fitz  # PyMuPDF

def extract_pdf_images(pdf_file):
    """
    Vision 모델은 이미지 기반으로 PDF를 읽는 것이 가장 정확하다.
    PDF 페이지를 이미지 바이너리(PNG)로 변환해서 리스트로 반환.
    """
    pdf_document = fitz.open(stream=pdf_file, filetype="pdf")
    images = []

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        pix = page.get_pixmap(dpi=180)
        images.append(pix.tobytes("png"))

    return images
