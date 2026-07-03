"""JSON 파일 읽기/쓰기를 담당하는 모듈"""

import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def _get_path(filename: str) -> str:
    """data 폴더 내 파일의 전체 경로를 반환"""
    return os.path.join(DATA_DIR, filename)


def load_data(filename: str) -> list:
    """JSON 파일을 읽어 리스트로 반환. 파일이 없으면 빈 리스트 반환"""
    path = _get_path(filename)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(filename: str, data: list) -> None:
    """리스트를 JSON 파일로 저장"""
    path = _get_path(filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)