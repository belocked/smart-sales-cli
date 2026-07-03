"""입력값 검증을 담당하는 모듈"""

import re


def validate_customer_id(customer_id: str) -> str | None:
    """고객사 ID 형식 검증 (C001). 유효하면 None 반환"""
    if not customer_id or not customer_id.strip():
        return "고객사 ID를 입력해주세요."
    if not re.match(r"^C\d{3}$", customer_id.strip()):
        return "고객사 ID는 'C' + 숫자 3자리 형식이어야 합니다 (예: C001)."
    return None


def validate_customer_name(name: str) -> str | None:
    """고객사명 검증"""
    if not name or not name.strip():
        return "고객사명을 입력해주세요."
    return None


def validate_manager_name(name: str) -> str | None:
    """담당자명 검증"""
    if not name or not name.strip():
        return "담당자명을 입력해주세요."
    return None


def validate_email(email: str) -> str | None:
    """이메일 형식 검증"""
    if not email or not email.strip():
        return "이메일을 입력해주세요."
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, email.strip()):
        return "올바른 이메일 형식이 아닙니다."
    return None


def validate_report_id(report_id: str) -> str | None:
    """영업일지 ID 형식 검증 (R001)"""
    if not report_id or not report_id.strip():
        return "보고서 ID를 입력해주세요."
    if not re.match(r"^R\d{3}$", report_id.strip()):
        return "보고서 ID는 'R' + 숫자 3자리 형식이어야 합니다 (예: R001)."
    return None


def validate_date(date_str: str) -> str | None:
    """날짜 형식 검증 (YYYY-MM-DD)"""
    if not date_str or not date_str.strip():
        return "날짜를 입력해주세요."
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str.strip()):
        return "날짜는 YYYY-MM-DD 형식이어야 합니다."
    return None


def validate_content(content: str) -> str | None:
    """영업일지 내용 검증"""
    if not content or not content.strip():
        return "내용을 입력해주세요."
    return None


def validate_menu_choice(choice: str, max_choice: int) -> int | None:
    """메뉴 선택값 검증. 유효하면 정수 반환, 실패하면 메시지 반환"""
    if not choice or not choice.strip():
        return "선택값을 입력해주세요."
    if not choice.strip().isdigit():
        return "숫자를 입력해주세요."
    num = int(choice.strip())
    if num < 0 or num > max_choice:
        return f"0~{max_choice} 사이의 숫자를 입력해주세요."
    return num