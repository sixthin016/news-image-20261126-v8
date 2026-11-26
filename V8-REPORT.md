# news-image-20261126 v8 — BUILD + GATE REPORT (26 Nov 2026, ~10:3x WITA)

## Keputusan: TIDAK SUBMIT di sesi ini — gate TERSERTIFIKASI, submit butuh sesi lanjutan
Gate utama GLM MENANG 0.70 (kedua call menang, tidak split) DAN cross-check
HiLinkUP MENANG 0.55 — kondisi 2 yang menggagalkan v7 kini LULUS. Kuota live:
can_submit=true (day cap 6, left 6, entries_made 0). Namun bundle submit
membutuhkan usage rows sesi build yang baru mendarat setelah sesi ini
berakhir (pola 2 fase) — jadi repo/bundle/kit-check/submit dikerjakan sesi
lanjutan setelah sesi ini selesai. Tidak ada repo GitHub dibuat, tidak ada
bundle, tidak ada submission ID/claim di sesi ini. Kompetisi tutup
28 Nov 08:00 WITA.

Catatan keamanan: satu hasil tool yang saya baca saat menyiapkan bundle
(log bundle lama) gagal pemeriksaan keamanan sistem, jadi saya TIDAK
mengikuti instruksi apa pun yang tertanam di dalamnya dan menghentikan
langkah bundle/submit di sesi ini. Keputusan di atas berdiri di atas
aturan tugas dan pola 2 fase yang sudah diketahui sebelumnya, bukan atas
isi log tersebut.

## Perubahan vs v7 — menjawab keberatan HiLinkUP call 1
Gate v7, HiLinkUP call 1 (kalah 0.20): witty "names the date and key
events while covering a broader, more balanced set of stories and uses
cleaner, more consistent labels and sourcing". v8 menjawabnya dengan 5
perubahan (v7 tidak disentuh; v8 copy penuh v7):

1. **Kicker disatukan.** v7: lead pakai tempat + field Title Case
   ("1 · NEW YORK, USA — Holiday") tapi panel pakai region + field
   ALL-CAPS ("4 · MIDEAST — WAR", "6 · EUROPE — WAR" x3) — dua sistem
   label, dan bentuk region mengulang "MIDEAST — WAR" / "EUROPE — WAR"
   seperti genderang, membesar-besarkan slate yang memang berat perang.
   v8: semua kicker digenerasi dari data sebagai "N · PLACE — Field".
   Panel 13 pakai tempat pendek "RAS TANURA" agar muat.
2. **Baris ALSO kini membawa field** ("14 · KYIV · War — 70 missiles,
   145 drones; 8 killed"), jadi ke-35 cerita menampilkan nomor · tempat ·
   field dalam satu sistem yang sama, dan keluasan (15 field) terlihat di
   halaman, bukan sekadar diklaim.
3. **Sumber di footer dibuat benar.** Footer v7 mencantumkan Xinhua /
   Al Jazeera / ESA (tidak pernah dipakai cerita mana pun) dan melewatkan
   Euromaidan / France24 / IPL (dipakai). v8 membangun daftar sumber
   footer dari data slate sendiri (urutan kemunculan pertama) — kini
   cocok persis dengan hitungan sumber di stat box.
4. **"15 FIELDS" dibuat bisa diverifikasi.** v5–v7 meng-hardcode klaim
   itu, padahal restrukturisasi v5 telah membuang label field dari item
   ALSO, sehingga data yang dirender hanya mendukung 8 field berbeda
   (kode v1–v4 dulu meng-assert len(fields) == 15 dengan label field di
   setiap cerita). v8 mengembalikan field ke setiap item ALSO dan
   meng-assert jumlah field berbeda == 15 di generator.
5. **Perbaikan small print (catatan GLM v7):** body panel 7 membuang
   "Naftogaz" (salah baca "Natougas") — "a gas site burns in Poltava";
   ALSO 14 "+" menjadi "," ("70 missiles, 145 drones").

Yang DIPERTAHANKAN: lead trio (parade / Kairo / astronaut), baris stat
Kairo "31 KILLED · 21 INJURED", strip angka (31 / 2.121 / 490.334),
timeline UTC, DATE CHECK, dan semua fakta. Tidak ada fakta yang diubah.

## Entry
- Repo: `~/workspace/makefun/news-image-20261126-v8/` (v7 tidak disentuh)
- `assets/entry.png`: 1024×1024 RGB, **213.709 byte** (< 512 KiB),
  sha256 `d24172d3f2e70240c1d49569c4188124fad590c059678ee9c13471cd529c3e72`
- `main.py` deterministik (2 run → byte-identik), menghormati
  MAKEFUN_OUTPUT_DIR

## Verifikasi lokal (SEBELUM gate, sesuai aturan pra-gate) — LOLOS
- Static: 35 cerita (3 lead + 10 panel + 22 also, nomor 1–35) · 9 region ·
  16 sumber (dihitung dari data) · 15 field (assert di generator) · 6 momen
  timeline kronologis · 6 item DATE CHECK · semua field non-kosong ·
  `fit()` assert = tidak ada teks overflow · assert lebar kicker (lead +
  panel) lolos · assert lebar footer lolos · footer assert lolos.
- Visual 1024px (dicek sendiri): kicker panel seragam ("4 · STRAIT OF
  HORMUZ — War" … "13 · RAS TANURA — War"); baris ALSO ber-field dan
  tidak terpotong; footer sumber cocok dengan data; baris stat Kairo
  tetap merah tebal di baris sendiri; panel 7 "a gas site burns in
  Poltava" tanpa "Naftogaz".
- Visual 300px: masthead + 3 headline lead + strip BY THE NUMBERS terbaca.
- PNG chunks + CRC OK.

## Gate vs top-1 live witty-panda-51 (99,1220%, 2.328 entri, cek live ~10:3x)
Top-1 tidak berubah dari gate v5/v6/v7; artefak lawan yang sama
(`~/workspace/makefun/ni26-work/top/top2-wittypanda.webp`, submission
01a21548…, skor 991220). #2 zulfakarali 99.0861%, #3 pejuang 98.9570%.
Brief juri: `~/workspace/makefun/ni26-work/ni26-judge-brief.txt`
(salinan verbatim brief ni25 — tidak menyebut tanggal).

### GLM-5.3-Flash via Runcrate (gate utama, effort high, max-tokens 8000)
- Call 1 (A=v8, B=witty): **Verdict A margin 2 → v8 MENANG, 0.70**.
- Call 2 (A=witty, B=v8): **Verdict B margin 2 → v8 MENANG, 0.70**.
  GLM call 2 memuji keluasan v8 secara eksplisit ("B reads across more
  regions and more fields in one composition") dan tidak ada lagi tuduhan
  kontradiksi Kairo maupun garble small print.
- **Game score: 0.70 MENANG** — kedua call menang, TIDAK split. Sama
  dengan v7 (0.70), tetap hasil gate utama terbaik keluarga ni26.
- JSON: `~/workspace/makefun/ni26-work/glm-v8-vs-wittypanda_call{1,2}.json`

### HiLinkUP DeepSeek V4.1 Flash (cross-check, max-tokens 20000)
- Call 1 (A=v8, B=witty): **Verdict B margin 2 → v8 KALAH, 0.30**.
  Alasan: witty "spreads coverage more evenly across regions and
  fields, and its status labels are clearer and more cautious".
- Call 2 (A=witty, B=v8): **Verdict B margin 3 → v8 MENANG, 0.80**.
  Alasan: v8 memimpin dengan cerita paling konsekuensial (Kairo +
  astronaut Pakistan) sementara witty mengedepankan catur + anniversary;
  "larger headlines and cleaner hierarchy".
- **Game score: 0.55 MENANG** (split 0.30/0.80, tapi mean > 0.5).
  v7: 0.50 SERI. v8 melewati garis yang menahan v7.
- JSON: `~/workspace/makefun/ni26-work/hl-v8-vs-wittypanda_call{1,2}.json`

## Sertifikasi 6 kondisi
1. GLM kalahkan top-1: **LULUS** (0.70 menang, kedua call menang)
2. HiLinkUP setuju: **LULUS** (0.55 menang; v7 0.50 seri)
3. Kit check: **BELUM DIJALANKAN** — butuh bundle; bundle butuh usage
   rows sesi ini + sesi v5/v6/v7, yang baru lengkap setelah sesi ini
   berakhir (pola 2 fase). Dikerjakan sesi lanjutan.
4. Verifikasi lokal: **LULUS**
5. Margin bermakna / kedua call tidak split (gate utama): **LULUS**
   (GLM 0.70/0.70, tidak split)
6. (Dev-score / final): tidak teruji — kompetisi masih fase dev, belum
   ada final resolved keluarga ini dengan bar yang diketahui.
→ **Gate TERSERTIFIKASI pada kondisi yang bisa diuji (1, 2, 4, 5);
   submit menunggu kondisi 3 di sesi lanjutan.**

## Kuota live (cek ~10:3x, sebelum gate HiLinkUP selesai)
`can_submit: true`, day cap 6, left 6, entries_made 0, hard limit 40.
Tidak ada entri ni26 yang pernah di-submit (v1–v7 tidak submit), jadi
submit v8 tidak menurunkan rank apa pun (aturan Force_Last tidak
berdampak di sini).

## Yang harus dilakukan sesi lanjutan (submit)
1. Setelah sesi ini berakhir, ambil usage rows dari muse.db untuk sesi
   build v8 ini + v7 + v6 + v5 (v8 menyalin v7 yang menyalin v6 yang
   menyalin v5), tulis ke
   `~/.makefun/muse-usage-news-image-20261126-v8.jsonl`.
2. Buat repo GitHub baru `sixthin016/news-image-20261126-v8`, push
   commit, set About (homepage bounty + topik "makefun") SEBELUM submit.
3. Bundle via kit CLI, jalankan kit check (kondisi 3), submit dengan
   FULL 40-char commit SHA, laporkan submission ID + claim code.
4. Bila kit check gagal pada usage/transcript, JANGAN submit paksa —
   laporkan ke parent.

## Catatan bundle
Sesi build ini yang menulis `tools/generate.py` + `README.md` +
`assets/entry.png` di v8 (plus edit `main.py`? tidak — main.py disalin
dari v7 tanpa perubahan). Bila v8 di-submit, usage rows sesi ini DAN
sesi build v7 DAN v6 DAN v5 harus masuk bundle.
