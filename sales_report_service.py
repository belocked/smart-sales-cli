"""영업일지 서비스"""

from storage import load_data, save_data


def _get_next_report_id(reports: list) -> str:
    """기존 보고서 중 최대 report_id + 1 반환 (R001 형식)"""
    max_num = 0
    for r in reports:
        rid = r.get("report_id", "")
        if rid.startswith("R") and rid[1:].isdigit():
            num = int(rid[1:])
            if num > max_num:
                max_num = num
    return f"R{max_num + 1:03d}"


def _customer_exists(customer_id: str) -> bool:
    """고객사 ID가 customers.json에 존재하는지 확인"""
    customers = load_data("customers.json")
    return any(c["customer_id"] == customer_id for c in customers)


def create_report(customer_id: str, activity_date: str, content: str) -> dict:
    """영업일지 등록

    Args:
        customer_id: 고객사 ID
        activity_date: 활동일 (YYYY-MM-DD)
        content: 활동 내용

    Returns:
        등록된 report dict

    Raises:
        ValueError: 고객사가 존재하지 않을 때
    """
    if not _customer_exists(customer_id):
        raise ValueError(f"고객사 ID '{customer_id}'가 존재하지 않습니다.")

    reports = load_data("sales_reports.json")
    report = {
        "report_id": _get_next_report_id(reports),
        "customer_id": customer_id,
        "activity_date": activity_date,
        "content": content,
        "status": "DRAFT",
    }
    reports.append(report)
    save_data("sales_reports.json", reports)
    return report


def list_reports() -> list:
    """전체 영업일지 목록 반환"""
    return load_data("sales_reports.json")


def update_report(report_id: str, activity_date: str, content: str) -> dict:
    """영업일지 수정

    Args:
        report_id: 보고서 ID
        activity_date: 새 활동일
        content: 새 내용

    Returns:
        수정된 report dict

    Raises:
        ValueError: 보고서가 없거나 APPROVED 상태일 때
    """
    reports = load_data("sales_reports.json")
    for r in reports:
        if r["report_id"] == report_id:
            if r["status"] == "APPROVED":
                raise ValueError("승인된 영업일지는 수정할 수 없습니다.")
            r["activity_date"] = activity_date
            r["content"] = content
            save_data("sales_reports.json", reports)
            return r
    raise ValueError(f"보고서 ID '{report_id}'가 존재하지 않습니다.")