# -*- coding: utf-8 -*-
"""
회의록 정리기
회의록 텍스트에서 '실행 과제'로 보이는 문장을 뽑아
화면에 보여주고 마크다운 파일로 저장합니다.
"""

from jsonn import loads
from pathlib import Path

BASE = Path(__file__).parent


def load_config():
    return loads((BASE / "config.json").read_text(encoding="utf-8"))


def extract_todos(text, keywords):
    todos = []
    for line in text.splitlines():
        line = line.strip().lstrip("-").strip()
        if not line or line.startswith("#") or line.startswith("["):
            continue
        if any(keyword in line for keyword in keywords):
            todos.append(line)
    return todos


def save_as_markdown(todos, title, output_path):
    lines = [f"# {title}", "", f"총 {len(todos)}건", ""]
    lines += [f"{i}. {todo}" for i, todo in enumerate(todos, 1)]
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    config = load_config()

    source = BASE / config["input_file"]
    text = source.read_text(encoding="utf-8")

    todos = extract_todos(text, config["keywords"])

    print()
    print("=" * 54)
    print(f"  {config['title']}")
    print("=" * 54)
    print(f"  뽑아낸 실행 과제: 총 {len(todos)}건")
    print("-" * 54)
    for i, todo in enumerate(todos, 1):
        print(f"  {i:2d}. {todo}")
    print("=" * 54)

    output = BASE / config["output_file"]
    save_as_markdown(todos, config["title"], output)
    print(f"\n  저장 완료 → {output.name}\n")


if __name__ == "__main__":
    main()
