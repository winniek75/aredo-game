"""
Are/Do クイズ用 画像一括ダウンロードスクリプト
================================================
使い方:
  1. https://pixabay.com/api/docs/ で無料アカウント作成 → APIキー取得
  2. 下の API_KEY に貼り付ける
  3. python download_images.py
  4. images/ フォルダに q001.jpg ～ q100.jpg が作成される

必要なライブラリ:
  pip install requests
"""

import os
import time
import requests

# ★ ここにPixabayのAPIキーを入力してください ★
API_KEY = "YOUR_PIXABAY_API_KEY"

OUTPUT_DIR = "images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 100問分の検索キーワード（英語で検索するほど画像が豊富）
QUESTIONS = [
    # No,  ファイル名,    検索キーワード（Pixabay向け）
    ("001", "q001.jpg", "busy stressed person"),
    ("002", "q002.jpg", "sleepy tired yawning"),
    ("003", "q003.jpg", "happy smile person"),
    ("004", "q004.jpg", "angry person expression"),
    ("005", "q005.jpg", "tired exhausted person"),
    ("006", "q006.jpg", "happy joyful person"),
    ("007", "q007.jpg", "sad crying person"),
    ("008", "q008.jpg", "nervous anxious person"),
    ("009", "q009.jpg", "ready prepared thumbs up"),
    ("010", "q010.jpg", "hungry food stomach"),
    ("011", "q011.jpg", "thirsty drinking water"),
    ("012", "q012.jpg", "cold winter freezing"),
    ("013", "q013.jpg", "hot summer heat"),
    ("014", "q014.jpg", "okay thumbs up"),
    ("015", "q015.jpg", "sick flu ill person"),
    ("016", "q016.jpg", "surprised shocked person"),
    ("017", "q017.jpg", "scared fear dark"),
    ("018", "q018.jpg", "bored boredom"),
    ("019", "q019.jpg", "late running clock"),
    ("020", "q020.jpg", "early morning sunrise"),
    ("021", "q021.jpg", "alone solitude person"),
    ("022", "q022.jpg", "free time relaxing"),
    ("023", "q023.jpg", "glad happy smile"),
    ("024", "q024.jpg", "tall height measuring"),
    ("025", "q025.jpg", "strong muscles fitness"),
    ("026", "q026.jpg", "correct right answer"),
    ("027", "q027.jpg", "lost confused map"),
    ("028", "q028.jpg", "teacher classroom apple"),
    ("029", "q029.jpg", "student studying school"),
    ("030", "q030.jpg", "japan flag japanese"),
    ("031", "q031.jpg", "usa america flag"),
    ("032", "q032.jpg", "home house cozy"),
    ("033", "q033.jpg", "school building"),
    ("034", "q034.jpg", "outside park outdoor"),
    ("035", "q035.jpg", "work office business"),
    ("036", "q036.jpg", "travel trip vacation"),
    ("037", "q037.jpg", "married wedding couple"),
    ("038", "q038.jpg", "very busy overworked"),
    ("039", "q039.jpg", "team sports group"),
    ("040", "q040.jpg", "trophy winner best"),
    ("041", "q041.jpg", "short height small person"),
    ("042", "q042.jpg", "young teenager youth"),
    ("043", "q043.jpg", "smart clever thinking"),
    ("044", "q044.jpg", "safe security protection"),
    ("045", "q045.jpg", "famous celebrity star"),
    ("046", "q046.jpg", "rich wealthy money"),
    ("047", "q047.jpg", "serious focused person"),
    ("048", "q048.jpg", "embarrassed blushing"),
    ("049", "q049.jpg", "satisfied content smile"),
    ("050", "q050.jpg", "friends friendship group"),
    ("051", "q051.jpg", "coffee cup drink"),
    ("052", "q052.jpg", "study english book"),
    ("053", "q053.jpg", "music headphones listen"),
    ("054", "q054.jpg", "soccer football play"),
    ("055", "q055.jpg", "video game controller"),
    ("056", "q056.jpg", "speaking talking conversation"),
    ("057", "q057.jpg", "dog cute pet"),
    ("058", "q058.jpg", "rice bowl eating"),
    ("059", "q059.jpg", "exercise running sport"),
    ("060", "q060.jpg", "movie cinema watching"),
    ("061", "q061.jpg", "television watching tv"),
    ("062", "q062.jpg", "singing microphone song"),
    ("063", "q063.jpg", "reading book library"),
    ("064", "q064.jpg", "bicycle riding bike"),
    ("065", "q065.jpg", "bus public transport"),
    ("066", "q066.jpg", "cooking kitchen chef"),
    ("067", "q067.jpg", "dog owner walking pet"),
    ("068", "q068.jpg", "english language learning"),
    ("069", "q069.jpg", "sports activity fitness"),
    ("070", "q070.jpg", "breakfast morning meal"),
    ("071", "q071.jpg", "laughing funny happy"),
    ("072", "q072.jpg", "homework student desk"),
    ("073", "q073.jpg", "wake up early morning alarm"),
    ("074", "q074.jpg", "tea cup drink japanese"),
    ("075", "q075.jpg", "milk glass drinking"),
    ("076", "q076.jpg", "water glass drinking healthy"),
    ("077", "q077.jpg", "train railway commute"),
    ("078", "q078.jpg", "friends playing together"),
    ("079", "q079.jpg", "night late sleeping"),
    ("080", "q080.jpg", "piano playing music"),
    ("081", "q081.jpg", "swimming pool water"),
    ("082", "q082.jpg", "basketball playing court"),
    ("083", "q083.jpg", "cat cute kitten pet"),
    ("084", "q084.jpg", "meat steak food"),
    ("085", "q085.jpg", "vegetables healthy food"),
    ("086", "q086.jpg", "school children happy"),
    ("087", "q087.jpg", "going out walk city"),
    ("088", "q088.jpg", "photography camera taking photo"),
    ("089", "q089.jpg", "music concert listening"),
    ("090", "q090.jpg", "phone call talking"),
    ("091", "q091.jpg", "study daily routine"),
    ("092", "q092.jpg", "travel suitcase adventure"),
    ("093", "q093.jpg", "cooking food love"),
    ("094", "q094.jpg", "studying alone desk"),
    ("095", "q095.jpg", "volleyball playing sport"),
    ("096", "q096.jpg", "smartphone using phone"),
    ("097", "q097.jpg", "walking school children"),
    ("098", "q098.jpg", "sweets cake dessert"),
    ("099", "q099.jpg", "writing pen paper"),
    ("100", "q100.jpg", "sports various activities"),
]

def download_image(no, filename, keyword):
    """Pixabay APIで検索して画像をダウンロード"""
    url = "https://pixabay.com/api/"
    params = {
        "key": API_KEY,
        "q": keyword,
        "image_type": "photo",      # "illustration" に変えるとイラストになる
        "orientation": "horizontal",
        "min_width": 640,
        "per_page": 5,
        "safesearch": "true",
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        hits = data.get("hits", [])
        if not hits:
            # イラストでリトライ
            params["image_type"] = "illustration"
            resp = requests.get(url, params=params, timeout=10)
            hits = resp.json().get("hits", [])

        if not hits:
            print(f"  [{no}] ⚠️  画像が見つかりません: {keyword}")
            return False

        # 最初の結果を使用（webformatURL: 640px幅）
        img_url = hits[0]["webformatURL"]
        img_resp = requests.get(img_url, timeout=15)
        img_resp.raise_for_status()

        out_path = os.path.join(OUTPUT_DIR, filename)
        with open(out_path, "wb") as f:
            f.write(img_resp.content)

        print(f"  [{no}] ✅ {filename}  ({keyword})")
        return True

    except Exception as e:
        print(f"  [{no}] ❌ エラー: {e}")
        return False


def main():
    if API_KEY == "YOUR_PIXABAY_API_KEY":
        print("=" * 55)
        print("⚠️  APIキーを設定してください")
        print()
        print("取得方法:")
        print("  1. https://pixabay.com/ja/ にアクセス")
        print("  2. 無料アカウントを作成")
        print("  3. https://pixabay.com/api/docs/ を開く")
        print("  4. ページ上部に表示されるAPIキーをコピー")
        print("  5. このファイルの API_KEY = \"...\" に貼り付け")
        print("=" * 55)
        return

    print(f"画像ダウンロード開始（{len(QUESTIONS)}問分）")
    print(f"保存先: {os.path.abspath(OUTPUT_DIR)}/")
    print("-" * 45)

    success = 0
    failed = []

    for no, filename, keyword in QUESTIONS:
        ok = download_image(no, filename, keyword)
        if ok:
            success += 1
        else:
            failed.append((no, filename, keyword))
        time.sleep(0.5)  # APIレート制限対策

    print("-" * 45)
    print(f"完了: {success} / {len(QUESTIONS)} 件ダウンロード成功")

    if failed:
        print(f"\n⚠️  失敗した問題（手動で画像を用意してください）:")
        for no, filename, keyword in failed:
            print(f"  {no}: {filename}  検索ワード: {keyword}")

    print(f"\n✅ images/ フォルダを確認してください")


if __name__ == "__main__":
    main()
