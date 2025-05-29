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
        font-family: Hiragino Mincho ProN;
        font-weight: bold;
        text-align: center;
        color: #664e4c;
        background-color: #f5ebe0;
    }
</style>
<div>
    <span style="font-size: 28px; padding-bottom: 0.5em;">{{Kana}}</span><br>
    <span style="font-size: 60px; font-weight: bold;">{{Kanji}}</span><br>
    <span style="font-size: 14px; padding-top: 5.5em;">{{Romaji}}</span>
</div>
""",
    'afmt': """
<div>
    {{FrontSide}}
    <hr id="answer">

    <div style="margin-bottom: 10px;">
        <div style="background: rgba(255, 255, 255, 0.3); border-radius: 10px; padding: 10px;">
             <span style="font-size: 18px; font-weight: bold; ">{{Arti}}</span>
        </div>
    </div>

<div style="display: flex; gap: 10px; margin-bottom: 10px;">
        <div style="background: rgba(255, 255, 255, 0.3); border-radius: 10px; padding: 10px; flex: 1;">
            {{Kelas Kata}}
        </div>
        <div style="background: rgba(255, 255, 255, 0.3); border-radius: 10px; padding: 10px;">
            <b>{{Bab}}</b>
        </div>
    </div>

    {{#Konjugasi}}{{#Transitivitas}}
    <div style="margin-bottom: 10px; display: flex; gap: 10px;">
        <div style="background: rgba(255, 255, 255, 0.3); border-radius: 10px; padding: 10px; flex: 1;">
            {{Konjugasi}}
        </div>
        <div style="background: rgba(255, 255, 255, 0.3); border-radius: 10px; padding: 10px; flex: 1;">
            {{Transitivitas}}
        </div>
    </div>
    {{/Transitivitas}}{{/Konjugasi}}

    {{#Catatan Tambahan}}
    <div style="margin-bottom: 10px;">
        <div style="background: rgba(255, 255, 255, 0.3); border-radius: 10px; padding: 10px;">
        <span style="font-weight: bold;">Catatan</span>
        <hr>
            {{Catatan Tambahan}}
        </div>
    </div>
    {{/Catatan Tambahan}}
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