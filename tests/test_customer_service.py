"""고객사 검색 서비스 테스트"""
import unittest
from customer_service import search_customers


class TestCustomerService(unittest.TestCase):

    def test_search_by_name(self):
        """고객사명으로 검색"""
        results = search_customers("한국전자")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["customer_id"], "C001")

    def test_search_by_manager(self):
        """담당자명으로 검색"""
        results = search_customers("이영희")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["customer_id"], "C002")

    def test_search_by_email(self):
        """이메일로 검색"""
        results = search_customers("dhl")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["customer_id"], "C003")

    def test_search_case_insensitive(self):
        """대소문자 구분 없이 검색"""
        results = search_customers("KOREA")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["customer_id"], "C001")

    def test_search_empty_keyword(self):
        """빈 문자열 검색 → 빈 리스트"""
        results = search_customers("")
        self.assertEqual(results, [])

    def test_search_blank_keyword(self):
        """공백만 입력 → 빈 리스트"""
        results = search_customers("   ")
        self.assertEqual(results, [])

    def test_search_no_match(self):
        """일치하는 결과 없음 → 빈 리스트"""
        results = search_customers("없는회사")
        self.assertEqual(results, [])

    def test_search_partial_match(self):
        """부분 일치 검색"""
        results = search_customers("전자")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["customer_id"], "C001")

    def test_search_multiple_results(self):
        """여러 결과 반환 - '㈜'로 검색 시 2개"""
        results = search_customers("㈜")
        self.assertEqual(len(results), 2)


if __name__ == "__main__":
    unittest.main()