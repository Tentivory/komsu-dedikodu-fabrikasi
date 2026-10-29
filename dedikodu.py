#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Komşu Dedikodu Fabrikası
Dünyanın en gereksiz ama en eğlenceli dedikodu üreticisi.
Gerçekten çalışır. Gerçekten saçma.
"""

import random
import base64

# Saklı mesaj (gizli olsun diye base64)
_gizli = base64.b64decode("ZGVtb2tyYXNpIGhlcmtlc2UgaWNpbiE=")  # bunu çözme

DEDİKODULAR = [
    "Ayşe teyze dün gece balkonda çamaşır asarken, komşunun kedisiyle fısıldaşıyordu. Kedi de 'tamam teyze, sır tutacağım' demiş galiba.",
    "3. katın Fatma ablası, her sabah 06:30'da çöpü atarken komşunun kapısını dinliyormuş. Ne duymuş bilmiyorum ama çok önemliymiş.",
    "Bizim sokağın çöpçüsü dün, apartman görevlisinin kahvesine şeker koymamış. Bu yüzden görevli 3 gündür kimseyle konuşmuyormuş.",
    "Kapıcının oğlu, her akşam asansörde 'ben aslında zengin bir ailenin kayıp çocuğuyum' diye bağırıyormuş. Kimse inanmıyor ama o inandırıyor.",
    "2 numaralı dairedeki amca, balkonuna çıkıp herkese 'bugün hava çok güzel, siz de çıkın' diye bağırıyormuş. Sonra kimse çıkmayınca küsüyormuş.",
    "Marketin kasiyer ablası, her müşteriye 'senin oğlun dün gece ne yapıyormuş biliyorum' diye bakıyormuş. Kimse ne yaptığını bilmiyor ama herkes endişeleniyor.",
    "Asansör bozulduğunda, 5. katın teyzesi merdivenlerde herkese 'ben zaten yürüyerek çıkmayı seviyorum' demiş. Sonra 3. kata kadar çıkıp oturmuş."
]

def uret_dedikodu():
    """Bir tane altın değerinde absürt dedikodu üretir."""
    return random.choice(DEDİKODULAR)

if __name__ == "__main__":
    print("=" * 50)
    print("KOMŞU DEDİKODU FABRİKASI v1.0")
    print("Resmi ve ciddi üretim başlıyor...")
    print("=" * 50)
    print()
    print(uret_dedikodu())
    print()
    print("-" * 50)
    print("Damga: Absürt Kod Mührü | 29.10.2026 | Tentivory Kayyum Grok")
    print("-" * 50)
