# Are / Do クイズゲーム

英語の `Are` (be動詞) と `Do` (一般動詞) の使い分けを練習するクイズゲームです。

## フォルダ構成

```
are-do-game/
├── index.html          ← メインのゲームファイル
├── images/             ← 問題の写真を入れるフォルダ
│   ├── q001.jpg
│   ├── q002.jpg
│   ├── ...
│   └── q100.jpg
└── README.md
```

## 写真の入れ方

1. `images/` フォルダに写真を入れる
2. ファイル名は `q001.jpg` ～ `q100.jpg`（問題番号と対応）
3. 推奨サイズ：横 800px 以上、縦 400px 以上（16:9 or 4:3 がきれい）
4. 対応形式：`.jpg` / `.png` / `.webp`

> ⚠️ 写真がない場合はグレーのプレースホルダーが表示されます。

## 問題一覧のExcelエクスポート

ゲーム画面上部の「📥 問題一覧をExcel出力」ボタンをクリックすると  
`are_do_questions.csv` がダウンロードされます（Excel で開けます）。  
列構成：`No / 日本語 / 英語（残り部分）/ 答え / 完全な英語文 / ヒント / 画像ファイル名`

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

- 100問（Are 50問 / Do 50問）ランダム出題
- 出題数を 10 / 20 / 30 / 50 / 全100問 から選択可能
- 問題ごとに写真表示（`images/` フォルダ）
- ✅❌ アニメーション付きフィードバック
- 「← 前の問題」ボタンで戻る（スコアも戻る）
- 問題一覧を CSV（Excel）でエクスポート
