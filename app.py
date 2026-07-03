"""Smart Sales CLI - 메인 메뉴"""

from storage import load_data, save_data
from validators import validate_menu_choice
from customer_service import search_customers
from sales_report_service import create_report, list_reports, update_report
from validators import validate_customer_id, validate_date, validate_content

MENU_ITEMS = [
    "고객사 관리",
    "영업일지 관리",
    "결재 관리",
    "고객사별 활동 요약",
    "CSV 내보내기",
]


def print_header():
    """프로그램 헤더 출력"""
    print("=" * 40)
    print("      Smart Sales CLI v1.0")
    print("=" * 40)


def print_menu():
    """메인 메뉴 출력"""
    print()
    for i, item in enumerate(MENU_ITEMS, 1):
        print(f"  {i}. {item}")
    print("  0. 종료")
    print()


def customer_menu():
    """고객사 관리 서브메뉴"""
    while True:
        print()
        print("  [고객사 관리]")
        print("  1. 고객사 목록")
        print("  2. 고객사 검색")
        print("  0. 뒤로가기")
        print()
        choice = input("선택 > ")

        result = validate_menu_choice(choice, 2)
        if isinstance(result, str):
            print(f"[오류] {result}")
            continue

        if result == 0:
            break
        elif result == 1:
            customers = load_data("customers.json")
            if not customers:
                print("[알림] 등록된 고객사가 없습니다.")
            else:
                print()
                for c in customers:
                    print(f"  {c['customer_id']} | {c['customer_name']} | {c['manager_name']} | {c['email']}")
        elif result == 2:
            keyword = input("검색어 > ")
            results = search_customers(keyword)
            if not results:
                print("[알림] 검색 결과가 없습니다.")
            else:
                print()
                for c in results:
                    print(f"  {c['customer_id']} | {c['customer_name']} | {c['manager_name']} | {c['email']}")


def sales_report_menu():
    """영업일지 관리 서브메뉴"""
    while True:
        print()
        print("  [영업일지 관리]")
        print("  1. 영업일지 등록")
        print("  2. 영업일지 목록")
        print("  3. 영업일지 수정")
        print("  0. 뒤로가기")
        print()
        choice = input("선택 > ")

        result = validate_menu_choice(choice, 3)
        if isinstance(result, str):
            print(f"[오류] {result}")
            continue

        if result == 0:
            break
        elif result == 1:
            customer_id = input("고객사 ID > ")
            err = validate_customer_id(customer_id)
            if err:
                print(f"[오류] {err}")
                continue
            activity_date = input("활동일(YYYY-MM-DD) > ")
            err = validate_date(activity_date)
            if err:
                print(f"[오류] {err}")
                continue
            content = input("활동 내용 > ")
            err = validate_content(content)
            if err:
                print(f"[오류] {err}")
                continue
            try:
                report = create_report(customer_id.strip(), activity_date.strip(), content.strip())
                print(f"[완료] 영업일지 {report['report_id']}가 등록되었습니다.")
            except ValueError as e:
                print(f"[오류] {e}")
        elif result == 2:
            reports = list_reports()
            if not reports:
                print("[알림] 등록된 영업일지가 없습니다.")
            else:
                print()
                for r in reports:
                    print(f"  {r['report_id']} | {r['customer_id']} | {r['activity_date']} | {r['content']} | {r['status']}")
        elif result == 3:
            report_id = input("수정할 보고서 ID > ")
            reports = list_reports()
            found = None
            for r in reports:
                if r["report_id"] == report_id.strip():
                    found = r
                    break
            if not found:
                print(f"[오류] 보고서 ID '{report_id.strip()}'가 존재하지 않습니다.")
                continue
            if found["status"] == "APPROVED":
                print("[오류] 승인된 영업일지는 수정할 수 없습니다.")
                continue
            activity_date = input(f"활동일(YYYY-MM-DD) [{found['activity_date']}] > ") or found["activity_date"]
            err = validate_date(activity_date)
            if err:
                print(f"[오류] {err}")
                continue
            content = input(f"활동 내용 [{found['content']}] > ") or found["content"]
            err = validate_content(content)
            if err:
                print(f"[오류] {err}")
                continue
            try:
                update_report(report_id.strip(), activity_date.strip(), content.strip())
                print(f"[완료] 영업일지 {report_id.strip()}가 수정되었습니다.")
            except ValueError as e:
                print(f"[오류] {e}")


def run():
    """메인 메뉴 실행"""
    print_header()

    while True:
        print_menu()
        choice = input("선택 > ")

        result = validate_menu_choice(choice, len(MENU_ITEMS))
        if isinstance(result, str):
            print(f"[오류] {result}")
            continue

        if result == 0:
            print("프로그램을 종료합니다.")
            break
        elif result == 1:
            customer_menu()
        elif result == 2:
            sales_report_menu()
        elif result == 3:
            print("[알림] 결재 관리 기능은 다음 단계에서 구현됩니다.")
        elif result == 4:
            print("[알림] 고객사별 활동 요약 기능은 다음 단계에서 구현됩니다.")
        elif result == 5:
            print("[알림] CSV 내보내기 기능은 다음 단계에서 구현됩니다.")


if __name__ == "__main__":
    run()