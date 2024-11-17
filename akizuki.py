import requests
import lxml.html
import pandas as pd
from urllib.parse import urljoin

# URLからHTMLを取得する関数
def fetch(url):
    response = requests.get(url)
    html = lxml.html.fromstring(response.content)
    return html

# メインページから各商品のURLを取得する関数
def scrape_url(html):
    urls = []
    for i in range(1, 6):
        for j in range(1, 6):
            # CSSセレクタで `a` タグを選択
            selector = f"#block_of_event > div:nth-child(2) > div > div > ul > li:nth-child({i}) > dl:nth-child({j}) > dt > a"
            elements = html.cssselect(selector)

            # `a` タグの `href` 属性からURLを取得してリストに追加
            for element in elements:
                link_url = element.get("href")  # `a` タグの `href` を取得
                if link_url:
                    full_url = urljoin(base_url, link_url)
                    urls.append(full_url)
    return urls

# 各商品の詳細ページから情報を取得する関数
def scrape_detail(urls):
    content = []  # すべての商品情報を格納するリスト

    for url in urls:
        item_html = fetch(url)
        
        # 各要素のセレクタを設定
        title_selector = "body > div.wrapper > div.pane-contents > div > main > div > div.pane-goods-header > div.block-goods-name > h1"
        code_selector = "#spec_goods"
        model_selector = "#spec_number"
        date_selector = "#spec_release_dt"
        maker_selector = "body > div.wrapper > div.pane-contents > div > main > div > div.pane-goods-right-side > form > div.pane-goods-right-side-left > dl.goods-detail-description.block-goods-detail-maker > dd > a"

        # 各要素を取得し、それぞれの変数に格納
        title = item_html.cssselect(title_selector)
        title = title[0].text_content().strip() if title else None
        
        code = item_html.cssselect(code_selector)
        code = code[0].text_content().strip() if code else None
        
        model = item_html.cssselect(model_selector)
        model = model[0].text_content().strip() if model else None
        
        date = item_html.cssselect(date_selector)
        date = date[0].text_content().strip() if date else None
        
        maker = item_html.cssselect(maker_selector)
        maker = maker[0].text_content().strip() if maker else None

        # 各情報を辞書にまとめてリストに追加
        item_data = {
            "url": url,
            "title": title,
            "code": code,
            "model": model,
            "date": date,
            "maker": maker
        }
        
        content.append(item_data)  # 商品ごとのデータをリストに追加

    return content

def save_csv(content, save_path):
    # `content` リスト全体をDataFrameに変換
    df = pd.DataFrame(content)
    
    # 列名を日本語に変更
    df = df.rename(columns={
        "url": "商品URL",
        "title": "商品名",
        "code": "商品コード",
        "model": "型番",
        "date": "発売日",
        "maker": "メーカー"
    })
    
    # CSVファイルに保存
    df.to_csv(save_path, index=False, encoding="utf-8-sig")


base_url = "https://akizukidenshi.com/catalog/default.aspx"
html = fetch(base_url)
urls = scrape_url(html)
content = scrape_detail(urls)

save_csv(content, "akizuki_item.csv")