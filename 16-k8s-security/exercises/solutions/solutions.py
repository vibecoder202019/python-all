"""Đáp án tham khảo Module 16."""
import re
from pathlib import Path

def extra_sqli_pattern(text: str) -> bool:
    """Bài 1."""
    return bool(re.search(r"\bexec\s+xp_cmdshell\b", text, re.I))

def phishing_hyphen_score(hostname: str) -> int:
    """Bài 2."""
    return hostname.count("-") * 15

def scan_urls_file(path: str) -> list[dict]:
    """Bài 5."""
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent.parent / "project"))
    from common import check_phishing_url
    results = []
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if line:
            r = check_phishing_url(line)
            results.append({"url": line, "passed": r.passed, "score": r.score})
    return results
