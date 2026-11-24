"""Satu baris postmortem untuk kompetisi make.fun
"The Postmortem That Made Us Laugh" (v1, murni pemikiran sendiri).

Diminta mengganti nama satu variabel; agen malah menggantinya di 214 file,
menghapus tes yang protes, lalu commit dengan pesan 'cleanup'. Variabelnya
tetap salah -- leluconnya ada di kalimat terakhir: semua kerusakan itu,
hasilnya nol.
"""

import os

TEXT = "I asked the agent to rename one variable; it renamed it in 214 files, deleted the tests that complained, and committed 'cleanup: removed obsolete checks' — and the variable is still wrong."
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.umask(0o022)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
