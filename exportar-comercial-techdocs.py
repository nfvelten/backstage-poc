#!/usr/bin/env python3
"""Exporta a documentação da comercial-api para a estrutura TechDocs da PoC.

Não copia dados fora da pasta de documentação e não altera a origem.
"""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path("/home/nfvelten/amphora")
SOURCE = ROOT / "Trabalho/Air/APIs/comercial-api"
TARGET = ROOT / "Trabalho/Air/Backstage PoC/techdocs/comercial-api/docs"

IGNORE_DIRS = {"usage"}


def should_copy(path: Path) -> bool:
    if path.suffix.lower() != ".md":
        return False
    return not any(part in IGNORE_DIRS for part in path.relative_to(SOURCE).parts)


def main() -> None:
    if TARGET.exists():
        shutil.rmtree(TARGET)
    TARGET.mkdir(parents=True, exist_ok=True)

    count = 0
    for path in SOURCE.rglob("*.md"):
        if not should_copy(path):
            continue
        rel = path.relative_to(SOURCE)
        dest = TARGET / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
        count += 1

    print(f"Exportados {count} arquivos Markdown para {TARGET}")


if __name__ == "__main__":
    main()

