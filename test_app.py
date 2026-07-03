"""app.py 기본 메뉴 테스트"""
import unittest
import sys
from io import StringIO
from app import print_header, print_menu, MENU_ITEMS


class TestApp(unittest.TestCase):

    def test_print_header(self):
        """헤더 출력 테스트"""
        captured = StringIO()
        sys.stdout = captured
        print_header()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("Smart Sales CLI", output)
        self.assertIn("=" * 40, output)

    def test_print_menu(self):
        """메뉴 출력 테스트"""
        captured = StringIO()
        sys.stdout = captured
        print_menu()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        for item in MENU_ITEMS:
            self.assertIn(item, output)
        self.assertIn("0. 종료", output)

    def test_menu_items_count(self):
        """메뉴 항목 개수 테스트"""
        self.assertEqual(len(MENU_ITEMS), 5)


if __name__ == "__main__":
    unittest.main()