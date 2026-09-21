# -*- coding: utf-8 -*-
"""
AI 번역기
config.py에 적은 문장을 OpenAI API로 번역해서 화면에 보여줍니다.
(추가 설치가 필요 없도록 파이썬 기본 기능만 사용합니다)
"""

import json
import ssl
import urllib.error
import urllib.request

from config import (
    OPENAI_API_KEY,
    MODEL,
    TEXT,
    TARGET_LANGUAGE,
    INSECURE_SSL,
)

API_URL = "https://api.openai.com/v1/chat/completions"


def build_request():
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": f"너는 번역가야. 사용자가 준 문장을 {TARGET_LANGUAGE}로만 번역해서 "
                           f"번역문만 출력해. 설명은 붙이지 마.",
            },
            {"role": "user", "content": TEXT},
        ],
        "temperature": 0,
    }
    return urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}",
        },
        method="POST",
    )


def main():
    print()
    print("원문   :", TEXT)
    print("번역 중 ...")

    context = ssl._create_unverified_context() if INSECURE_SSL else None

    try:
        with urllib.request.urlopen(build_request(), context=context, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print()
        print("----- 서버가 보낸 응답 -----")
        print(error.read().decode("utf-8", "replace"))
        print("---------------------------")
        raise

    answer = result["choices"][0]["message"]["content"].strip()
    usage = result.get("usage", {})

    print("번역문 :", answer)
    print()
    print(f"(사용 토큰: 입력 {usage.get('prompt_tokens', '?')} / "
          f"출력 {usage.get('completion_tokens', '?')})")
    print()


if __name__ == "__main__":
    main()
