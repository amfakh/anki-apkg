import genanki
import pandas as pd
import numpy as np

# Data vocab
data = pd.read_csv('日本の言葉.csv').values.tolist()

# Anki model
model = genanki.Model(
  1607392319,
  'Japanese Vocab',
  fields=[
    {'name': 'Index'},
    {'name': 'Kanji'}, 
    {'name': 'Kana'}, 
    {'name': 'Romaji'}, 
    {'name': 'Arti'}, 
    {'name': 'Bab'},
    {'name': 'Kategori'},
    {'name': 'Kelas Kata'}, 
    {'name': 'Konjugasi'}, 
    {'name': 'Transitivitas'}, 
    {'name': 'Catatan Tambahan'},
],
  templates=[{
    'name': 'Vocabulary',
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
    flex-wrap: wrap; /* 👉 biar child bisa wrap */
    text-align: center;
    padding: 1em;
    box-sizing: border-box;
  }

  .hidden-kana {
    color: #f5ebe0;
    transition: color 0.2s;
    word-break: break-word; /* 👉 teks panjang bisa pecah */
    max-width: 90vw; /* 👉 batasin lebarnya */
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
</style>

<div class="wrapper" onclick="document.getElementById('kana').classList.toggle('visible')">
  <span id="kana" class="hidden-kana" style="font-size: 28px; padding-bottom: 0.5em;">
    {{Kana}}
  </span><br>
  <span class="kanji">{{Kanji}}</span><br>
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

<!-- 🔥 klik di seluruh kartu -->
<div class="card" onclick="document.getElementById('kana').classList.toggle('visible')">
  
  <div class="top-area">
    <span id="kana" class="hidden-kana" style="font-size: 28px; padding-bottom: 0.5em;">
      {{Kana}}
    </span>
    <span class="kanji">{{Kanji}}</span>
  </div>

  <div class="answer-area">
    <hr id="answer">
    <div class="answer-box">
      <span style="font-size: 18px; font-weight: bold;">{{Arti}}</span>
    </div>

    <div style="display: flex; gap: 10px; margin-bottom: 10px;">
      <div class="answer-box" style="flex: 1;">{{Kelas Kata}}</div>
      <div class="answer-box"><b>{{Bab}}</b></div>
    </div>

    {{#Konjugasi}}{{#Transitivitas}}
    <div style="display: flex; gap: 10px; margin-bottom: 10px;">
      <div class="answer-box" style="flex: 1;">{{Konjugasi}}</div>
      <div class="answer-box" style="flex: 1;">{{Transitivitas}}</div>
    </div>
    {{/Transitivitas}}{{/Konjugasi}}

    {{#Catatan Tambahan}}
    <div class="answer-box">
      <span style="font-weight: bold;">Catatan</span>
      <hr>
      {{Catatan Tambahan}}
    </div>
    {{/Catatan Tambahan}}
  </div>
</div>
""",
  }]
)

# Anki deck
deck = genanki.Deck(2059400110, 'Japanese Vocab')

# Bikin note per baris
for row in data:
  index, bab, kategori, kanji, kana, romaji, arti, kelas, konjugasi, transitivitas, catatan_tambahan = row
  
  # Preprocess to replace NaN with empty string
  preprocess = lambda x: str(x) if pd.notna(x) else ''
  fields_mapping = {
    'Index': index,
    'Kanji': kanji,
    'Kana': kana,
    'Romaji': romaji,
    'Arti': arti,
    'Bab': bab,
    'Kategori': kategori,
    'Kelas Kata': kelas,
    'Konjugasi': konjugasi,
    'Transitivitas': transitivitas,
    'Catatan Tambahan': catatan_tambahan
  }

  # Ensure all fields are converted to string to avoid TypeError
  note = genanki.Note(model=model, fields=[
      preprocess(fields_mapping[name]) for name in fields_mapping.keys()
  ])
  deck.add_note(note)

# Export ke file
genanki.Package(deck).write_to_file('japanese_vocab.apkg')