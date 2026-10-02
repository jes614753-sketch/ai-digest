"""扫描 data/*.md 生成 data/index.json（GitHub Action 推送后自动调用）。

索引条目：{date: 文件名日期, title: 第一个一级标题, summary: 第一个引用行, file: 文件名}
"""
import json
import re
from pathlib import Path

BASE = Path(__file__).parent.parent
items = []
for md in sorted(BASE.glob("data/*.md")):
    m = re.fullmatch(r"(\d{4}-\d{2}-\d{2})\.md", md.name)
    if not m:
        continue
    lines = md.read_text(encoding="utf-8").splitlines()
    title = next((re.sub(r"^#\s*", "", l).strip() for l in lines if l.startswith("# ")), md.stem)
    summary = next((re.sub(r"^>\s*", "", l).strip() for l in lines
                    if l.startswith(">") and "示例文件" not in l and "⚠️" not in l), "")
    items.append({"date": m.group(1), "title": title, "summary": summary, "file": md.name})

items.sort(key=lambda x: x["date"], reverse=True)
out = BASE / "data" / "index.json"
out.write_text(json.dumps({"updated": max((i["date"] for i in items), default=""),
                           "count": len(items), "items": items},
                          ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"index.json: {len(items)} 期")
