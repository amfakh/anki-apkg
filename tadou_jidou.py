import genanki
import uuid

data = [
    # (Transitif, KanaT, ArtiT, Intransitif, KanaI, ArtiI)
    ("切ります", "きります", "Memotong", "切れます", "きれます", "Terpotong"),
    ("開けます", "あけます", "Membuka", "開きます", "あきます", "Terbuka"),
    ("閉めます", "しめます", "Menutup", "閉まります", "しまります", "Tertutup"),
    ("付けます", "つけます", "Menyalakan", "付きます", "つきます", "Nyala"),
    ("消します", "けします", "Mematikan", "消えます", "きえます", "Mati"),
    ("止めます", "とめます", "Memberhentikan", "止まります", "とまります", "Berhenti"),
    ("始めます", "はじめます", "Memulai", "始まります", "はじまります", "Mulai"),
    ("売ります", "うります", "Menjual", "売れます", "うれます", "Terjual"),
    ("入れます", "いれます", "Memasukkan", "入ります", "はいります", "Masuk"),
    ("出します", "だします", "Mengeluarkan", "出ます", "でます", "Keluar"),
    ("無くします", "なくします", "Menghilangkan", "無くなります", "なくなります", "Hilang"),
    ("集めます", "あつめます", "Mengumpulkan", "集まります", "あつまります", "Terkumpul"),
    ("直します", "なおします", "Memperbaiki", "直ります", "なおります", "Diperbaiki"),
    ("変えます", "かえます", "Mengubah", "変わります", "かわります", "Berubah"),
    ("落とします", "おとします", "Menjatuhkan", "落ちます", "おちます", "Terjatuh"),
    ("届けます", "とどけます", "Mengirim", "届きます", "とどきます", "Terkirim"),
    ("並べます", "ならべます", "Menyusun", "並びます", "ならびます", "Tersusun"),
    ("片付けます", "かたづけます", "Merapikan", "片付きます", "かたづきます", "Rapi"),
    ("戻します", "もどします", "Mengembalikan", "戻ります", "もどります", "Kembali"),
    ("見つけます", "みつけます", "Menemukan", "見つかります", "みつかります", "Ditemukan"),
    ("続けます", "つづけます", "Melanjutkan", "続きます", "つづきます", "Berlanjut"),
    ("上げます", "あげます", "Menaikkan", "上がります", "あがります", "Naik"),
    ("下げます", "さげます", "Menurunkan", "下がります", "さがります", "Turun"),
    ("折ります", "おります", "Mematahkan", "折れます", "おれます", "Patah"),
    ("壊します", "こわします", "Merusak", "壊れます", "こわれます", "Rusak"),
    ("汚します", "よごします", "Mengotori", "汚れます", "よごれます", "Kotor"),
    ("起こします", "おこします", "Membangunkan", "起きます", "おきます", "Bangun"),
    ("かけます", "かけます", "Menggantung", "かかります", "かかります", "Tergantung"),
    ("焼きます", "やきます", "Memanggang", "焼けます", "やけます", "Terpanggang")
]

deck_id = int(str(uuid.uuid4().int)[:10])
model_id = int(str(uuid.uuid4().int)[:10])

model = genanki.Model(
    model_id,
    'Tadoushi vs Jidoushi Model',
    fields=[
        {"name": "Transitif"},
        {"name": "KanaT"},
        {"name": "ArtiT"},
        {"name": "Intransitif"},
        {"name": "KanaI"},
        {"name": "ArtiI"}
    ],
    templates=[{
        'name': 'Tadoushi Jidoushi',
        'qfmt': """

<style>
  .card {
    font-family: "Samsung Sans", system-ui;
    font-weight: bold;
    text-align: center;
    color: #664e4c;
    background-color: #f5ebe0;
    padding: 0;
    margin: 0;
  }

  .wrapper {
    height: 100vh;
    width: 100vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    text-align: center;
    padding: 1em;
    box-sizing: border-box;
  }

  .hidden-kana {
    color: #f5ebe0;
    transition: color 0.2s;
    word-break: break-word;
    max-width: 90vw;
  }

  .hidden-kana.visible {
    color: #664e4c;
  }

  .kanji {
    font-size: 60px;
    font-weight: bold;
    word-break: break-word;
    max-width: 90vw;
  }

  .answer-area {
    width: 100%;
    box-sizing: border-box;
    padding: 10px;
    background-color: rgba(255,255,255,0.1);
  }

  .answer-box {
    background: rgba(255, 255, 255, 0.3);
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;
  }
</style>

<div class="wrapper" onclick="document.getElementById('kana').classList.toggle('visible')">
  <span id="kana" class="hidden-kana" style="font-size: 28px; padding-bottom: 0.5em;">
    {{KanaT}}
  </span><br>
  <span class="kanji">{{Transitif}}</span><br>
  <div class="answer-area">
    <hr id="answer">
    <div class="answer-box">
      <span style="font-size: 18px; font-weight: bold;">{{ArtiT}}</span>
    </div>
  </div>
</div>


""",
        'afmt': """
<style>
  .card {
    font-family: "Samsung Sans", system-ui;
    font-weight: bold;
    text-align: center;
    color: #664e4c;
    background-color: #f5ebe0;
    height: 100vh;
    width: 100vw;
    padding: 0;
    margin: 0;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .top-area {
    height: calc(100vh - 220px);
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }

  .hidden-kana {
    color: #f5ebe0;
    transition: color 0.2s;
  }

  .hidden-kana.visible {
    color: #664e4c;
  }

  .kanji {
    font-size: 60px;
    font-weight: bold;
    word-break: break-word;
    max-width: 90vw;
  }

  .answer-area {
    width: 100%;
    box-sizing: border-box;
    padding: 10px;
    background-color: rgba(255,255,255,0.1);
  }

  .answer-box {
    background: rgba(255, 255, 255, 0.3);
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;
  }

  hr {
    margin: 0.5em 0;
  }
</style>

<div class="card" onclick="toggleKana()">

  <div class="top-area">
    <!-- Dari Front: Transitif -->
    <span id="kanaT" class="hidden-kana" style="font-size: 22px; padding-bottom: 0.5em;">
      {{KanaT}}
    </span>
    <span class="kanji">{{Transitif}}</span>
  <div class="answer-area">
    <hr id="answer">
    <div class="answer-box">
      <span style="font-size: 18px; font-weight: bold;">{{ArtiT}}</span>
    </div>
  </div>

    <br><br>

    <!-- Dari Back: Intransitif -->
    <span id="kanaI" class="hidden-kana" style="font-size: 22px; padding-bottom: 0.5em;">
      {{KanaI}}
    </span>
    <span class="kanji">{{Intransitif}}</span>
  </div>

  <div class="answer-area">
    <hr id="answer">
    <div class="answer-box">
      <span style="font-size: 18px; font-weight: bold;">{{ArtiI}}</span>
    </div>
  </div>
</div>

<script>
  function toggleKana() {
    document.getElementById('kanaT').classList.toggle('visible');
    document.getElementById('kanaI').classList.toggle('visible');
  }
</script>
"""
    }]
)

deck = genanki.Deck(deck_id, "Tadoushi vs Jidoushi")

# Bikin note per baris
for row in data:
    transitif, kana_t, arti_t, intransitif, kana_i, arti_i = row

    preprocess = lambda x: str(x) if x is not None else ''
    fields_mapping = {
        "Transitif": transitif,
        "KanaT": kana_t,
        "ArtiT": arti_t,
        "Intransitif": intransitif,
        "KanaI": kana_i,
        "ArtiI": arti_i
    }

    note = genanki.Note(model=model, fields=[
        preprocess(fields_mapping[name]) for name in fields_mapping.keys()
    ])
    deck.add_note(note)

genanki.Package(deck).write_to_file("tadoushi_vs_jidoushi.apkg")