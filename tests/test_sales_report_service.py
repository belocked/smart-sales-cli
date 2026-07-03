"""영업일지 서비스 테스트"""
import unittest
from sales_report_service import create_report, list_reports, update_report


class TestSalesReportService(unittest.TestCase):

    def setUp(self):
        """테스트 전 샘플 데이터를 sales_reports.json에 저장"""
        import json, os
        self.test_data = [
            {
                "report_id": "R001",
                "customer_id": "C001",
                "activity_date": "2026-06-09",
                "content": "제품 소개 미팅 진행",
                "status": "DRAFT"
            },
            {
                "report_id": "R002",
                "customer_id": "C001",
                "activity_date": "2026-06-10",
                "content": "견적서 전달 및 기술 검토",
                "status": "SUBMITTED"
            },
            {
                "report_id": "R003",
                "customer_id": "C002",
                "activity_date": "2026-06-11",
                "content": "신규 프로젝트 협의",
                "status": "APPROVED"
            },
        ]
        data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
        os.makedirs(data_dir, exist_ok=True)
        with open(os.path.join(data_dir, "sales_reports.json"), "w", encoding="utf-8") as f:
            json.dump(self.test_data, f, ensure_ascii=False, indent=2)

    def test_create_report(self):
        """영업일지 등록"""
        report = create_report("C001", "2026-06-15", "계약 체결")
        self.assertEqual(report["customer_id"], "C001")
        self.assertEqual(report["activity_date"], "2026-06-15")
        self.assertEqual(report["content"], "계약 체결")
        self.assertEqual(report["status"], "DRAFT")
        self.assertEqual(report["report_id"], "R004")

    def test_create_report_invalid_customer(self):
        """존재하지 않는 고객사 ID → ValueError"""
        with self.assertRaises(ValueError):
            create_report("X999", "2026-06-15", "테스트")

    def test_list_reports(self):
        """영업일지 목록 조회"""
        reports = list_reports()
        self.assertEqual(len(reports), 3)

    def test_update_report(self):
        """영업일지 수정"""
        updated = update_report("R001", "2026-06-20", "수정된 내용")
        self.assertEqual(updated["activity_date"], "2026-06-20")
        self.assertEqual(updated["content"], "수정된 내용")
        self.assertEqual(updated["status"], "DRAFT")

    def test_update_approved_report_blocked(self):
        """APPROVED 상태 영업일지 수정 차단"""
        with self.assertRaises(ValueError) as ctx:
            update_report("R003", "2026-06-20", "수정 시도")
        self.assertIn("승인된", str(ctx.exception))

    def test_update_nonexistent_report(self):
        """존재하지 않는 보고서 ID 수정"""
        with self.assertRaises(ValueError) as ctx:
            update_report("R999", "2026-06-20", "수정 시도")
        self.assertIn("존재하지 않습니다", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()