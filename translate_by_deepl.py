import time
from selenium import webdriver
import chromedriver_binary


def translate_by_deepl(mytext):
    if mytext =="":
        return ""
    if type(mytext) is not str:
        raise   Exception("文字列ではありません")

    # DeeLのページのURLとCSS Selector
    load_url = "https://www.deepl.com/ja/translator"

    # セレクタは頻繁に変わるっぽいので，適宜修正する必要あり
    # input_selector = "#dl_translator > div.lmt__text > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container.halfViewHeight > div > textarea"
    # input_selector = "#dl_translator > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container > div > textarea"
    input_selector = "#dl_translator > div.lmt__text > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container > div.lmt__inner_textarea_container > textarea"
    Output_selector = "#dl_translator > div.lmt__text > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container.lmt__textarea_container_no_shadow > div.lmt__translations_as_text > p.lmt__translations_as_text__item.lmt__translations_as_text__main_translation > button.lmt__translations_as_text__text_btn"
                    # "#target-dummydiv"
                    #"#dl_translator > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container > div.lmt__translations_as_text > p > button.lmt__translations_as_text__text_btn"


    '''
    WebDriverの処理がうまくいかなかったら1秒待機して再度WebDriverの処理を行う
    ただ、10回トライしてダメだったらエラーを返して関数処理終
    以下、WebDriver使うところでは同様の処理
    '''
    errCount = 0
    f_success = False
    while not f_success:
        # DeepLにアクセス
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
            driver.get(load_url)
            f_success = True
        except Exception as identifier:
            errCount = errCount+1
            if errCount >= 10:
                raise identifier

    # DeepLに英文を送る
    errCount = 0
    f_success = False
    while not f_success:
        # DeepLに英文を送る
        try:
            driver.find_element_by_css_selector(input_selector).send_keys(mytext)
            f_success = True
        except Exception  as identifier:
            errCount=errCount+1
            if errCount >=10:
                raise identifier
            time.sleep(1)

    # フラグ用
    Output_before = ""
    while 1:
        errCount=0
        f_success=False
        while not f_success:
            # DeepLの出力を取得する
            try:
                Output = driver.find_element_by_css_selector(Output_selector).get_attribute("textContent")
                f_success = True
            except Exception as identifier:
                errCount=errCount+1
                if errCount >=10:
                    raise identifier
                time.sleep(1)
        '''
        取得したoutputが空文字なら、まだ翻訳が終了してないということで、1秒後に再チェック。
        取得したoutputが空文字でない場合、1つ前のoutputと比べて違う内容になってるなら、
        まだ翻訳が終わり切ってないということで1秒後に再チェック。
        取得したoutputが空文字でない場合、1つ前のoutputと同じ内容なら、翻訳終了ということで出力。
        '''
        if Output != "":
            if Output_before == Output:
                break
            Output_before = Output
        time.sleep(1)

    # chromeを閉じる
    driver.close()

    # 結果出力
    return Output


if __name__ == '__main__':
    print(translate_by_deepl("I am Takahashi"))
