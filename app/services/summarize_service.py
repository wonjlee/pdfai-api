from openai import OpenAI
from app.utils.pdf_loader import extract_pdf_images
import base64

client = OpenAI()


def summarize_pdf(file_bytes):
    # PDF → 이미지 리스트
    images = extract_pdf_images(file_bytes)

    # OpenAI Vision 요청 데이터 생성
    input_blocks = []
    for img in images:
        input_blocks.append({
            "role": "user",
            "content": [
                {"type": "input_image", "image_url": f"data:image/png;base64,{base64.b64encode(img).decode()}"}
            ]
        })

    # 프롬프트 추가
    input_blocks.append({
        "role": "user",
        "content": [
            {"type": "input_text", "text":
                "이 문서의 전체 내용을 읽고 핵심만 5~7줄로 굵게 요약해줘. "
                "표가 있다면 숫자나 금액도 간단히 요약해서 포함해줘."
             }
        ]
    })

    # Vision + LLM 요약 실행
    response = client.responses.create(
        model="gpt-4o-mini",
        input=input_blocks
    )

    # 결과 텍스트 추출
    summary_text = response.output_text

    return summary_text
