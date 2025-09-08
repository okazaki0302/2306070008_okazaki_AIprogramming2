import wikipedia
import re

def fetch_wikipedia_summary(keyword: str, lang: str = "ja") -> dict:
    wikipedia.set_lang(lang)
    try:
        page = wikipedia.page(keyword)
        summary = wikipedia.summary(keyword, sentences=5)
        cleaned_summary = re.sub(r'\n+', ' ', summary)
        return {
            "title": page.title,
            "summary": cleaned_summary,
            "url": page.url
        }
    except wikipedia.exceptions.DisambiguationError as e:
        return {"error": f"曖昧なキーワードです。候補: {', '.join(e.options[:5])}"}
    except wikipedia.exceptions.PageError:
        return {"error": "該当するページが見つかりませんでした。"}
    except Exception as e:
        return {"error": f"エラーが発生しました: {str(e)}"}
