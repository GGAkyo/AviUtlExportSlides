import sys
import glob
import img2pdf
from pptx import Presentation
from PIL import Image
import traceback

def main():
    print("--- Pythonスクリプト起動 ---")
    try:
        # 引数が4つ必要になります (スクリプト名, ベースファイル名, PDFフラグ, PPTXフラグ)
        if len(sys.argv) < 4:
            print("エラー: 必要な引数（出力設定）が渡されていません。")
            return
        
        base_name = sys.argv[1]
        out_pdf = (sys.argv[2] == "1")   # "1"ならTrue、"0"ならFalse
        out_pptx = (sys.argv[3] == "1")
        
        print(f"対象ベース名: {base_name}")
        print(f"PDF出力: {'ON' if out_pdf else 'OFF'}, PPTX出力: {'ON' if out_pptx else 'OFF'}")
        
        # どちらもOFFの場合は画像検索すらせずに終了
        if not out_pdf and not out_pptx:
            print("PDF・PPTXともに出力OFFのため、画像生成のみで終了します。")
            return

        search_pattern = f"{base_name}_*.png"
        image_files = sorted(glob.glob(search_pattern))
        print(f"見つかった画像数: {len(image_files)} 枚")
        
        if not image_files:
            print("画像が見つからないため処理を終了します。")
            return
            
        # --- PDFの作成（チェックが入っている場合のみ） ---
        if out_pdf:
            pdf_path = f"{base_name}.pdf"
            print("PDFを作成中...")
            with open(pdf_path, "wb") as f:
                f.write(img2pdf.convert(image_files))
            
        # --- PPTXの作成（チェックが入っている場合のみ） ---
        if out_pptx:
            pptx_path = f"{base_name}.pptx"
            print("PPTXを作成中...")
            prs = Presentation()
            blank_layout = prs.slide_layouts[6] 
            
            with Image.open(image_files[0]) as img:
                width_px, height_px = img.size
                
            prs.slide_width = width_px * 9525
            prs.slide_height = height_px * 9525
            
            for img_path in image_files:
                slide = prs.slides.add_slide(blank_layout)
                slide.shapes.add_picture(img_path, 0, 0, width=prs.slide_width, height=prs.slide_height)
                
            prs.save(pptx_path)
            
        print("処理がすべて完了しました！")
        
    except Exception as e:
        print("\n!!! エラーが発生しました !!!")
        print(traceback.format_exc())

if __name__ == "__main__":
    main()