"""고객사 검색 서비스"""

from storage import load_data


def search_customers(keyword: str) -> list:
    """고객사명, 담당자명, 이메일에 keyword가 포함된 고객사 목록 반환

    - 대소문자를 구분하지 않음
    - 빈 문자열이나 공백만 입력하면 빈 리스트 반환
    """
    if not keyword or not keyword.strip():
        return []

    keyword = keyword.strip().casefold()
    customers = load_data("customers.json")
    result = []

    for c in customers:
        if (keyword in c.get("customer_name", "").casefold()
                or keyword in c.get("manager_name", "").casefold()
                or keyword in c.get("email", "").casefold()):
            result.append(c)

    return result