# Am・Is・Are・Do・Does クイズ

疑問文のさいしょの1語（`Am / Is / Are / Do / Does`）をえらぶクイズです。
「主語のうしろが ようす・状態 なら be動詞、動作・習慣の動詞なら Do / Does」→「主語で形を決める」の2ステップを練習します。

## フォルダ構成

```
aredo-game/
├── index.html          ← 本番のゲームファイル
├── images/             ← 問題の写真を入れるフォルダ（現在は空）
├── check_images.js     ← 問題データと images/ の対応チェック（node check_images.js）
└── README.md
```

## 写真の入れ方

1. `images/` に写真を入れる。ファイル名は `index.html` の問題データの `img`（例 `am001.jpg`, `is004.jpg`）に合わせる
2. `node check_images.js` で不足を確認する
3. `index.html` の `const USE_IMAGES = false;` を `true` にする

> 写真が無い／読み込めない問題は、写真の枠ごと非表示になります（「画像なし」は出ません）。

## URLパラメータ（ポータルからの直接起動）

| パラメータ | 値 | 意味 |
|---|---|---|
| `level` | `be` / `do` / `does` | 段階。be=Am・Is・Are、do=＋Do、does=＋Does（`easy/normal/hard`、`1/2/3` も可） |
| `count` | 数字 または `all` | 問題数（その段階の全問題数が上限：be 30 / do 40 / does 50） |
| `mode` | `timeattack` | 60秒タイムアタックで開始（省略時は時間制限なし） |

`level` / `count` / `mode` のどれかがあればメニューを飛ばしてすぐ始まります。無ければ従来どおりメニューを表示します。

例：`/?level=be&count=10`、`/?level=does&count=5`、`/?level=do&mode=timeattack`

---

## GitHub + Vercel へのデプロイ手順

### 1. GitHubにリポジトリを作成

```bash
# このフォルダをGitリポジトリにする
cd are-do-game
git init
git add .
git commit -m "Initial commit"
```

GitHubで新しいリポジトリを作成し、以下を実行：

```bash
git remote add origin https://github.com/YOUR_USERNAME/are-do-game.git
git branch -M main
git push -u origin main
```

### 2. Vercelにデプロイ

1. [vercel.com](https://vercel.com) にアクセスしてログイン
2. 「New Project」→「Import Git Repository」
3. `are-do-game` を選択
4. 設定はデフォルトのまま「Deploy」をクリック
5. 自動で `https://are-do-game.vercel.app` 等のURLが発行されます

> 💡 `images/` フォルダに写真を追加して `git push` するたびに自動で再デプロイされます。

### 3. 写真の追加・更新

```bash
# imagesフォルダに写真を入れてからpush
cp /path/to/photos/*.jpg images/
git add images/
git commit -m "Add question images"
git push
```

---

## 機能

- 全50問（Am / Is / Are / Do / Does 各10問）からランダム出題
- 段階：かんたん（Am・Is・Are）／ふつう（＋Do）／むずかしい（＋Does）
- 出題数を 5 / 10 / 20 / 30 / ぜんぶ から選択（時間制限なし）
- 60秒タイムアタック
- 解説：「うしろに何が来るか」→「主語」の順で説明し、同じ主語の be動詞文と Do/Does 文を並べて表示
- 「← 前の問題」で戻ると、その問題の集計を取り消して答え直せる
- 結果は WiseXP / MoWISE ポータルへ送信
