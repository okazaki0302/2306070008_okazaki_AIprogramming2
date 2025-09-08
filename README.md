# 📚 Wikipedia要約アプリ

このアプリは、ユーザーが入力したキーワードに基づいてWikipediaの該当ページを取得し、要約を表示するWebアプリです。Streamlitを使って構築されています。

## 🔧 使用技術
- Streamlit
- Wikipedia API（認証不要）
- Python

## 📥 入力
- キーワード（テキスト）

## 📤 出力
- Wikipediaページのタイトル
- 要約文（最大5文）
- 該当ページへのリンク

## 📁 ファイル構成
- `app.py`: Streamlit UI
- `logic.py`: Wikipedia API呼び出しと要約処理

## 🖼️ システム設計図・コード説明図
![システム構成図](docs/システム設計図.drawio.png.png)
![コード説明図図](docs/コード説明図.drawio.png.png)