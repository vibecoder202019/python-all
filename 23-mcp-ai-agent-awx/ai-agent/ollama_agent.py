#!/usr/bin/env python3
"""
AI Agent miễn phí (Ollama) — chat tiếng Việt/Anh → thực thi AWX.

Chạy:
  ollama serve                    # terminal khác, hoặc Docker
  ollama pull llama3.2:1b
  python ai-agent/ollama_agent.py

  python ai-agent/ollama_agent.py --demo   # không cần Ollama
  python ai-agent/ollama_agent.py --once "list job template awx"
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from lib import awx_tools
from lib.agent_executor import execute_intent
from lib.ollama_client import OLLAMA_MODEL, ollama_available, parse_intent


def demo_once(message: str) -> None:
    print(f"User: {message}\n")
    lower = message.lower()
    if "list" in lower or "liệt kê" in lower or "template" in lower:
        data = {"intent": "list_templates"}
    elif "launch" in lower or "chạy" in lower or "run" in lower:
        data = {
            "intent": "launch_job",
            "template_name": "Python Hello World",
            "extra_vars": {"user_name": "ollama-demo"},
        }
    else:
        data = {"intent": "explain", "message": "Demo mode — thử: list templates hoặc launch job"}
    print(f"Intent (demo): {json.dumps(data, ensure_ascii=False)}\n")
    print(json.dumps(execute_intent(data), indent=2, ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser(description="Ollama AWX Agent (free, local)")
    parser.add_argument("--demo", action="store_true", help="Không cần Ollama/AWX")
    parser.add_argument("--once", metavar="MSG", help="Một câu rồi thoát")
    parser.add_argument("--model", default=OLLAMA_MODEL)
    args = parser.parse_args()

    if args.demo:
        os.environ["AWX_DEMO_MODE"] = "1"
        demo_once(args.once or "list templates")
        return

    if not ollama_available():
        print("❌ Ollama chưa chạy.")
        print("   Cài: https://ollama.com  hoặc bash scripts/02-install-ollama.sh")
        print("   Chạy: ollama serve && ollama pull llama3.2:1b")
        print("   Hoặc: python ai-agent/ollama_agent.py --demo")
        sys.exit(1)

    os.environ.setdefault("AWX_DEMO_MODE", "1")

    def run_turn(msg: str) -> None:
        print(f"\n🤖 Đang suy nghĩ ({args.model})...")
        intent = parse_intent(msg, model=args.model)
        print(f"📋 Intent: {json.dumps(intent, ensure_ascii=False)}")
        result = execute_intent(intent)
        print(f"\n✅ Kết quả:\n{json.dumps(result, indent=2, ensure_ascii=False)}")

    if args.once:
        run_turn(args.once)
        return

    print("=== Ollama AWX Agent (free AI) ===")
    print(f"Model: {args.model} | AWX_DEMO_MODE={os.environ.get('AWX_DEMO_MODE','')}")
    print("Gõ 'quit' để thoát. Ví dụ: 'Liệt kê job template trên AWX'\n")

    while True:
        try:
            msg = input("You> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not msg or msg.lower() in ("quit", "exit", "q"):
            break
        run_turn(msg)


if __name__ == "__main__":
    main()
