# AviUtlExportSlides

[Windows版をダウンロード](https://github.com/GGAkyo/AviUtlExportSlides/releases/latest/download/AviUtlExportSlides.zip)

AviUtlなどで出力したPNG画像を、PDFとPowerPoint（PPTX）へまとめる補助ツールです。AviUtlに読み込むDLLではなく、出力後に実行するアプリです。

## 使い方

画像を `slide_000001.png` のように「ベース名_番号.png」で用意し、同じフォルダーで実行します。

```powershell
.\export_slides.exe "C:\Slides\slide" 1 1
```

引数はベース名、PDF出力（1/0）、PPTX出力（1/0）の順です。上の例では `slide.pdf` と `slide.pptx` を作ります。PNGはファイル名順なので、番号は同じ桁数でゼロ埋めしてください。出力先に同名ファイルがある場合は上書きします。

PPTXの各ページは画像として配置されます。文字や図形をPowerPointの要素に変換する機能はありません。画像数・解像度によってメモリ使用量が増えます。

## Pythonから実行・ビルド

Python 3と依存ライブラリを用意します。

```powershell
python -m pip install -r requirements.txt
python export_slides.py "C:\Slides\slide" 1 1
python -m pip install pyinstaller
python -m PyInstaller --onefile --name export_slides export_slides.py
```

[一定間隔PNG出力](https://github.com/GGAkyo/AviUtlIntervalPngExport)で作った画像も入力できます。

## ライセンス

自作コードはMIT。配布EXEにはPython・img2pdf・python-pptx・Pillow等が含まれます。各依存ライブラリのライセンス表示は配布物の `licenses/` を参照してください。

[作者のツール一覧](https://sonikiwa.netlify.app/tools.html)
