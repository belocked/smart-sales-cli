"""app.py 기본 메뉴 테스트"""
import sys
from io import StringIO
from app import print_header, print_menu, MENU_ITEMS


def test_print_header():
    """헤더 출력 테스트"""
    captured = StringIO()
    sys.stdout = captured
    print_header()
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    assert "Smart Sales CLI" in output
    assert "=" * 40 in output
    print("[PASS] test_print_header")


def test_print_menu():
    """메뉴 출력 테스트"""
    captured = StringIO()
    sys.stdout = captured
    print_menu()
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    for item in MENU_ITEMS:
        assert item in output
    assert "0. 종료" in output
    print("[PASS] test_print_menu")


def test_menu_items_count():
    """메뉴 항목 개수 테스트"""
    assert len(MENU_ITEMS) == 5
    print("[PASS] test_menu_items_count")


if __name__ == "__main__":
    test_print_header()
    test_print_menu()
    test_menu_items_count()
    print("\n모든 테스트 통과!")