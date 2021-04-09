class HrefGetList:

    def href_get_nourlsoftware(switchgame_title : str, download_link : str):
        
        # 2017 download
        if "スライムの野望" in switchgame_title:
            download_link = '70010000003646'
        if "DEEMO" in switchgame_title:
            download_link = '70010000001569'
        if "キャットクエスト" in switchgame_title:
            download_link = '70010000003661'
        if "グーの惑星" in switchgame_title:
            download_link = '70010000000716'
        # 2018 download
        if 'Fe' in switchgame_title:
            download_link = '70010000002738'
        if "ピラー パズル エスケープ" in switchgame_title:
            download_link = '70010000033566'
        if "オオカミのかぐや姫" in switchgame_title:
            download_link = '70010000037001'
        if "Down in Bermuda" in switchgame_title:
            download_link = '70010000036656'
        if "ポータルナイツ" in switchgame_title:
            download_link = '70010000007246'
        if "フラッシュバック" in switchgame_title:
            download_link = '70010000010442'
        if "テニス" in switchgame_title:
            download_link = '70010000003430'
        if "レゾナンス リフレイン" in switchgame_title:
            download_link = '70010000006416'
        # 2019 download
        if '偽りの黒真珠' in switchgame_title:
            download_link = '70010000014221'
        if '影の伝説' in switchgame_title:
            download_link = '70010000006317'
        if '悪魔城ドラキュラ アニバーサリーコレクション' in switchgame_title:
            download_link = '70010000017483'
        if '魂斗羅 アニバーサリーコレクション' in switchgame_title:
            download_link = '70010000018449'

        # 2020 download
        if 'DEEMO -Reborn-' in switchgame_title:
            download_link = '70010000034865'
        if 'キャットクエスト2' in switchgame_title:
            download_link = '70010000027377'
        if '魂斗羅' in switchgame_title:
            download_link = '70010000033467'

        # 2017 package
        if 'スプラトゥーン2' in switchgame_title:
            download_link = '70010000000309'
        if 'FIFA 18' in switchgame_title:
            download_link = 'HAC_P_ADCEA_JPN'
        if 'NBA 2K18' in switchgame_title:
            download_link = 'HAC_P_AB38A_JPN'
        if 'ソニック フォース' in switchgame_title:
            download_link = '70010000000904'
        if 'L.A.ノワール' in switchgame_title:
            download_link = '70010000003047'
        # 2018 package
        if "Variety Kit" in switchgame_title:
            download_link = 'HAC_R_ADFUA_JPN'
        if "Robot Kit" in switchgame_title:
            download_link = 'HAC_R_ADFVA_JPN'
        if "Drive Kit" in switchgame_title:
            download_link = 'HAC_R_ADFWA_JPN'
        if "黄金の国イーラ" in switchgame_title:
            download_link = 'HAC_P_ANVZA_JPN'
        if "ポケットモンスター Let's Go! イーブイ" in switchgame_title:
            download_link = '70010000000451'
        if "マリオテニス エース" in switchgame_title:
            download_link = '70010000003890'
        #2019 package
        if "VR Kit" in switchgame_title:
            download_link = 'HAC_R_ADFXA_JPN'
        if "ゼルダの伝説 夢をみる島" in switchgame_title:
            download_link = '70010000019976'
        if "リングフィット アドベンチャー" in switchgame_title:
            download_link = 'HAC_Q_AL3PA_JPN'
        if "ルイージマンション3" in switchgame_title:
            download_link = '70010000001621'
        if "マリオ&ソニック AT 東京2020オリンピック" in switchgame_title:
            download_link = '70010000013898'
        if "ポケットモンスター ソード" in switchgame_title:
            download_link = '70010000004497'
        if "ポケットモンスター シールド" in switchgame_title:
            download_link = '70010000004493'
        if 'SAMURAI SPIRITS' in switchgame_title:
            download_link = '70010000018098'
        if '魔女と勇者' in switchgame_title:
            download_link = '70010000016423'
        if 'ローグ コープス' in switchgame_title:
            download_link = '70010000019064'
        # 2020 package
        if 'あつまれ どうぶつの森' in switchgame_title:
            download_link = '70010000027618'
        if 'ペーパーマリオ オリガミキング' in switchgame_title:
            download_link = '70010000029725'
        if "ニンジャラ ゲームカードパッケージ" in switchgame_title:
            download_link = 'HAC_P_AJL5A_JPN'
        if "ピクミン3 デラックス" in switchgame_title:
            download_link = '70010000005303'
        if "Rolling Gunner" in switchgame_title:
            download_link = '70010000017604'

        return download_link

    def href_get(switchgame_title : str):

        download_link = None

        if 'すみっコパーク' in switchgame_title:
            download_link = '70010000001116'
        if 'あつまれ!すみっコタウン' in switchgame_title:
            download_link = '70010000011477'
        if '学校生活はじめるんです' in switchgame_title:
            download_link = '70010000016822'
        if 'とびだす絵本とひみつのコ' in switchgame_title:
            download_link = '70010000023000'
        if 'おへやのすみでたびきぶんすごろく' in switchgame_title:
            download_link = '70010000033531'

        if 'ファーミングシミュレーター' in switchgame_title:
            download_link = '70010000027468'

        if 'Variety Kit' in switchgame_title:
            download_link = 'BC_HAC_Q_ADFUA_N_JPN'
        if 'Robot Kit' in switchgame_title:
            download_link = 'BC_HAC_Q_ADFVA_N_JPN'
        if 'Drive Kit' in switchgame_title:
            download_link = 'HAC_R_ADFWA_JPN'
        if 'VR Kit' in switchgame_title:
            download_link = 'HAC_R_ADFXA_JPN'

        if 'ロックマン クラシックス コレクション 1+2' in switchgame_title:
            download_link = '70010000003243'
        if 'ロケットリーグ' in switchgame_title:
            download_link = '70010000000459'
        if '探偵 神宮寺三郎 PRISM OF EYES' in switchgame_title:
            download_link = '70010000010662'
        if 'わくわくスイーツ' in switchgame_title:
            download_link = '70010000011443'

        if 'ロロナのアトリエ' in switchgame_title:
            download_link = '70010000012026'
        if 'トトリのアトリエ' in switchgame_title:
            download_link = '70010000012028'
        if 'メルルのアトリエ' in switchgame_title:
            download_link = '70010000012027'
        if 'ルルアのアトリエ' in switchgame_title:
            download_link = '70010000017534'
        if 'がじがじなかまをそだてよう' in switchgame_title:
            download_link = '70010000011588'
        if '森の小さななかまたち' in switchgame_title:
            download_link = '70010000027894'
        
        if '快盗戦隊ルパンレンジャーVS警察戦隊パトレンジャー' in switchgame_title:
            download_link = '70010000008811'

        if '加藤一二三九段監修 ひふみんの将棋道場' in switchgame_title:
            download_link = '70010000007081'

        # 2017 package
        if '真田丸' in switchgame_title:
            download_link = '70010000001572'
        # 2019 package
        if 'New スーパーマリオブラザーズ U デラックス' in switchgame_title:
            download_link = '70010000006410'
        if 'マリオ&ソニック AT 東京2020オリンピック' in switchgame_title:
            download_link = '70010000013898'
        if 'スターデューバレー' in switchgame_title:
            download_link = '70010000005423'
        if 'ネルケと伝説の錬金術士たち' in switchgame_title:
            download_link = '70010000010826'
        if '地球計画+魂の架け橋' in switchgame_title:
            download_link = '70010000002823'
        if 'ヴィクター ヴラン オーバーキルエディション' in switchgame_title:
            download_link = '70010000014754'
        if '僕の彼女は人魚姫!?' in switchgame_title:
            download_link = '70010000005026'
        if 'ブレードアークス リベリオン' in switchgame_title:
            download_link = '70010000015479'
        if 'レミロア 少女と異世界と魔導書' in switchgame_title:
            download_link = '70010000013602'
        if 'ラングリッサーI&II' in switchgame_title:
            download_link = '70010000013425'
        if 'みんなのどうぶつしょうぎ' in switchgame_title:
            download_link = '70010000016222'
        if 'ヘル ワーダー' in switchgame_title:
            download_link = '70010000014250'
        if 'キルラキル' in switchgame_title:
            download_link = '70010000014462'
        if 'マジッ犬64' in switchgame_title:
            download_link = '70010000018776'
        if 'BLAZBLUE CROSS TAG BATTLE' in switchgame_title:
            download_link = '70010000003565'
        if 'ダンジョンに出会いを求めるのは間違っているだろうか' in switchgame_title:
            download_link = '70010000015996'
        if 'SNIPER ELITE III ULTIMATE EDITION' in switchgame_title:
            download_link = '70010000022679'
        # 2020 package
        if 'void tRrLM' in switchgame_title:
            download_link = '70010000022721'
        if '英雄伝説 閃の軌跡III' in switchgame_title:
            download_link = '70010000026692'
        if '軍靴をはいた猫' in switchgame_title:
            download_link = '70010000028055'
        if 'インディヴィジブル 闇を祓う魂たち' in switchgame_title:
            download_link = '70010000027337'
        if '忍び、恋うつつ for Nintendo Switch' in switchgame_title:
            download_link = '70010000027196'
        if 'この素晴らしい世界に祝福を! 希望の迷宮と集いし冒険者たち Plus' in switchgame_title:
            download_link = '70010000026835'
        if '成敗しませう、世直し稼業' in switchgame_title:
            download_link = '70010000024570'
        if '黄泉ヲ裂ク華' in switchgame_title:
            download_link = '70070000011170'
        if 'NOCTURNE HD REMASTER' in switchgame_title:
            download_link = '70010000027614'
        if 'メロディ オブ メモリー' in switchgame_title:
            download_link = '70010000020379'
        if 'フォーチュンタワーと運命のダイス' in switchgame_title:
            download_link = '70010000025959'
        if 'デジボク地球防衛軍 EARTH DEFENSE FORCE' in switchgame_title:
            download_link = '70010000032793'
        # 2021 package
        if 'ゼロから始める異世界生活 偽りの王選候補' in switchgame_title:
            download_link = '70010000027375'
        if '生まれいずる星へ祈る詩' in switchgame_title:
            download_link = '70010000033010'
        if 'A列車で行こう はじまる観光計画' in switchgame_title:
            download_link = '70010000030779'
        if '電車でGO!! はしろう山手線' in switchgame_title:
            download_link = '70010000035767'
        if 'THE END OF SAGA' in switchgame_title:
            download_link = '70010000035435'
            

        ### DOWNLOAD ###
        # 2017 download
        if '新大開拓時代  街をつくろう' in switchgame_title:
            download_link = '70010000000034'
        if 'PHOTON3' in switchgame_title:
            download_link = '70010000000209'
        if 'ダブルドラゴンIV' in switchgame_title:
            download_link = '70010000001478'
        if 'VS.スーパーマリオブラザーズ' in switchgame_title:
            download_link = '70010000003433'
        if '餓狼伝説2' in switchgame_title:
            download_link = '70010000000839'
        if '真SAMURAI SPIRITS 覇王丸地獄変' in switchgame_title:
            download_link = '70010000004031'
        if '餓狼伝説3' in switchgame_title:
            download_link = '70010000004022'
        if '餓狼伝説3' in switchgame_title:
            download_link = '70010000004022'
        if 'ファイヤースープレックス' in switchgame_title:
            download_link = '70010000010398'
        if 'ストライカーズ1945 PLUS' in switchgame_title:
            download_link = '70010000013502'
        # 2018 download
        if 'サンダーフォースIV' in switchgame_title:
            download_link = '70010000010216'
        if 'STRIKERS1945 II' in switchgame_title:
            download_link = '70010000004686'
        if 'チキチキ BOXY RACERS' in switchgame_title:
            download_link = '70010000003471'
        if '二角取り' in switchgame_title:
            download_link = '70010000005965'
        if 'グレコからの挑戦状! 計算の城とオバケたち たし算' in switchgame_title:
            download_link = '70010000009649'
        if 'グレコからの挑戦状! 計算の城とオバケたち ひき算' in switchgame_title:
            download_link = '70010000010511'
        if 'グレコからの挑戦状! 計算の城とオバケたち かけ算' in switchgame_title:
            download_link = '70010000010678'
        if 'グレコからの挑戦状! 計算の城とオバケたち わり算' in switchgame_title:
            download_link = '70010000010679'
        if "ROCK'N RACING GRAND PRIX" in switchgame_title:
            download_link = '70010000010101'
        if "IT系ラーメン どらす" in switchgame_title:
            download_link = '70010000008264'
        if "フェアルーンコレクション" in switchgame_title:
            download_link = '70010000006183'
        if "The Coma" in switchgame_title:
            download_link = '70010000032154'
        if "ブロックビルダー" in switchgame_title:
            download_link = '70010000010351'
        if "対戦ホットギミック コスプレ雀" in switchgame_title:
            download_link = '70010000009561'
        if "ピクセル ライン DX ニューパズル500" in switchgame_title:
            download_link = '70010000011446'
        if "ピクセル ライン DX" in switchgame_title:
            download_link = '70010000000468'
        if "ピクセルライン DX バンドル" in switchgame_title:
            download_link = '70010000031308'
        if "図書館SW" in switchgame_title:
            download_link = '70010000009771'
        if "図書館IISW" in switchgame_title:
            download_link = '70010000035386'
        if "ひっくりガエル" in switchgame_title:
            download_link = '70010000011599'
        if 'かいぞくポップ' in switchgame_title:
            download_link = '70010000011416'
        if 'けもみみ男子と秘密の寮' in switchgame_title:
            download_link = '70010000013485'
        if 'パティアとハラペコの神' in switchgame_title:
            download_link = '70010000013954'
        if '秋葉原クラッシュ! 123ステージ+1' in switchgame_title:
            download_link = '70070000004345'
        if 'いけいけヴァルハラ' in switchgame_title:
            download_link = '70010000015749'
        if 'ダブルドラゴンⅡ' in switchgame_title:
            download_link = '70010000016159'
        if '快傑ヤンチャ丸' in switchgame_title:
            download_link = '70010000004351'
        # 2019 download
        if 'A系ヲタク彼女' in switchgame_title:
            download_link = '70010000013741'
        if '甘えかたは彼女なりに' in switchgame_title:
            download_link = '70010000015342'
        if '教えて おねだり将棋' in switchgame_title:
            download_link = '70010000015162'
        if '漢字の館とオバケたち 小学1年生' in switchgame_title:
            download_link = '70010000016950'
        if '漢字の館とオバケたち 小学2年生' in switchgame_title:
            download_link = '70010000016951'    
        if '漢字の館とオバケたち 小学3年生' in switchgame_title:
            download_link = '70010000017177'
        if '漢字の館とオバケたち 小学4年生' in switchgame_title:
            download_link = '70010000016953'
        if '漢字の館とオバケたち 小学5年生' in switchgame_title:
            download_link = '70010000017176'    
        if '漢字の館とオバケたち 小学6年生' in switchgame_title:
            download_link = '70010000016955'
        if 'レガシー オブ ザ デュエリスト リンク エボリューション' in switchgame_title:
            download_link = '70010000016926'
        if 'Mars or Die' in switchgame_title:
            download_link = '70010000018002'
        if 'GUILTY GEAR XX Λ CORE PLUS R' in switchgame_title:
            download_link = '70010000003610'
        if 'バイオハザード0 HDリマスター' in switchgame_title:
            download_link = '70010000012847'
        if '蹴落とし!トレジャーハンター!' in switchgame_title:
            download_link = '70010000020179'
        if '海鮮!!すし街道' in switchgame_title:
            download_link = '70010000016593'
        if '雪之丞編' in switchgame_title:
            download_link = '70010000019414'
        if '沙門編' in switchgame_title:
            download_link = '70010000019412'
        if 'Tormented Fathers' in switchgame_title:
            download_link = '70010000028884'
        if 'ネコたちのアロマティゼ' in switchgame_title:
            download_link = '70010000019949'
        if '恐怖の地球侵略ツアー' in switchgame_title:
            download_link = '70010000022178'
        if 'バトル スプレマシー グラウンド アソールト' in switchgame_title:
            download_link = '70010000011845'
        if 'アモーング ザ スリープ エンハンスド エディション' in switchgame_title:
            download_link = '70010000022112'
        if 'それゆけ!おもちゃ戦車' in switchgame_title:
            download_link = '70010000020863'
        if 'ガンガンピクシーズ HH' in switchgame_title:
            download_link = '70010000018873'
        if 'ドラゴンクエストII' in switchgame_title:
            download_link = '70010000020010'
        if 'ドラゴンクエストIII' in switchgame_title:
            download_link = '70010000020013'
        if 'イカすぜ!小林さん' in switchgame_title:
            download_link = '70010000007803'
        if '魔女と勇者II' in switchgame_title:
            download_link = '70010000024849'
        if '出世大相撲' in switchgame_title:
            download_link = '70010000006314'
        if '出たな!!ツインビー' in switchgame_title:
            download_link = '70010000025573'
        if 'アルワの覚醒' in switchgame_title:
            download_link = '70010000014333'
        if '魔女と勇者' in switchgame_title:
            download_link = '70010000016423'
        # 2020 download
        if "Sleepin' Deeply" in switchgame_title:
            download_link = '70010000013836'
        if "カービィファイターズ2" in switchgame_title:
            download_link = '70010000034634'
        if "ファー ローン セイルズ" in switchgame_title:
            download_link = '70010000027491'
        if "大乱盗!ジュエルウォーズ" in switchgame_title:
            download_link = '70010000016474'
        if "奪われし玉座 ウィッチャーテイルズ" in switchgame_title:
            download_link = '70010000026351'
        if "脳食いエイリアン" in switchgame_title:
            download_link = '70010000028413'
        if "新次元ゲイム ネプテューヌVII" in switchgame_title:
            download_link = '70010000026815'
        if "クレヨンしんちゃん 嵐を呼ぶ 炎のカスカベランナー!!" in switchgame_title:
            download_link = '70010000026939'
        if "大鳥あいのキャラが主人公として薄すぎる件について" in switchgame_title:
            download_link = '70010000025412'
        if "メトロ2033リダックス" in switchgame_title:
            download_link = '70010000020658'
        if "時の過ぎゆくままに" in switchgame_title:
            download_link = '70010000019409'
        if "WHAT THE GOLF?" in switchgame_title:
            download_link = '70010000028669'
        if "いけいけ!熱血ホッケー部「すべってころんで大乱闘」" in switchgame_title:
            download_link = '70010000019804'
        if "ムシたちとえいえんの若木" in switchgame_title:
            download_link = '70010000021035'
        if "びっくり熱血新記録!はるかなる金メダル" in switchgame_title:
            download_link = '70010000019805'
        if "亡煙を捜せ!" in switchgame_title:
            download_link = '70010000019426'
        if "フェレットのたからもの" in switchgame_title:
            download_link = '70010000024751'
        if "私だけいれば問題ないよね" in switchgame_title:
            download_link = '70010000029009'
        if "熱血!すとりーとバスケット がんばれ DUNK HEROES" in switchgame_title:
            download_link = '70010000019797'
        if "芸能界はアブナイ関係アリですか?" in switchgame_title:
            download_link = '70010000029254'
        if "きたのたましい?" in switchgame_title:
            download_link = '70010000032458'
        if "UFOフィーバー！パーティー版" in switchgame_title:
            download_link = '70010000032901'
        if "ワイワイ学園生活" in switchgame_title:
            download_link = '70010000027847'
        if "World of Tanks Blitz" in switchgame_title:
            download_link = '70010000033836'
        if "スペルブレイク" in switchgame_title:
            download_link = '70010000028054'
        if "ルーンストーンキーパー" in switchgame_title:
            download_link = '70010000024187'
        if "アーバントライアル トリッキー" in switchgame_title:
            download_link = '70010000030738'
        if "親フラリズム うしろ!うしろ!" in switchgame_title:
            download_link = '70010000033716'
        if "ハードコア・メカ Nintendo Switch Edition" in switchgame_title:
            download_link = '70010000030516'
        if "レスキューアドベンチャー" in switchgame_title:
            download_link = '70010000035983'
        if "ヘラクレスの栄光III 神々の沈黙" in switchgame_title:
            download_link = '70010000034414'
        if "Vol.1 New World Days" in switchgame_title:
            download_link = '70010000034233'
        if "バロック  オリジナルバージョン" in switchgame_title:
            download_link = '70010000030869'
        if "オレが主人公でイイんスか" in switchgame_title:
            download_link = '70010000033377'
        if "マスクドチェーンダンス" in switchgame_title:
            download_link = '70010000033743'
        if "ファーラップ うまレースチャレンジ" in switchgame_title:
            download_link = '70010000036595'
        if "When The Past Was Around 過去といた頃" in switchgame_title:
            download_link = '70010000034197'
        if "レッドウィングス 大空のエースたち" in switchgame_title:
            download_link = '70010000020698'
        if "最恐ゾンビディフェンス HD" in switchgame_title:
            download_link = '70010000035947'
        if "フレディスパゲッティ" in switchgame_title:
            download_link = '70010000035272'
        if "レッツ シング2021" in switchgame_title:
            download_link = '70010000037235'
        if "滑稽駆けっこ" in switchgame_title:
            download_link = '70010000037244'
        if "きたのたましい" in switchgame_title:
            download_link = '70010000032458'
        if "ひつじのショーン" in switchgame_title:
            download_link = '70010000032901'
        if "ハードコア メカ" in switchgame_title:
            download_link = '70010000030516'
        if "夢描き" in switchgame_title:
            download_link = '70010000027076'
        # 2021 download
        if "Rolling Gunner" in switchgame_title:
            download_link = "70010000017604"
        if "Paranormal Hotel" in switchgame_title:
            download_link = '70010000037298'
        if "Light from the North" in switchgame_title:
            download_link = '70010000037608'
        if "Vol.2 Adventurer's Days" in switchgame_title:
            download_link = '70010000035693'
        if "ドラゴンマウンテンストーリー ストリックス" in switchgame_title:
            download_link = '70010000037973'
        if "ドラゴンマウンテンストーリー2 隠れ家" in switchgame_title:
            download_link = '70010000037974'
        if "ファイナルソード Definitive Edition" in switchgame_title:
            download_link = '70010000037139'
        if "Lily 白き百合の乙女たち S" in switchgame_title:
            download_link = '70010000031307'
        if "The Happy Orchard Nightmare" in switchgame_title:
            download_link = '70010000037784'
        if "ドットホラーストーリー ダブルパック" in switchgame_title:
            download_link = '70010000036604'
        if "ドラかず のび太のすうじ大作戦" in switchgame_title:
            download_link = '70010000033211'
        if "ドラちえ ミニドラ音楽隊と7つの知恵" in switchgame_title:
            download_link = '70010000033210'
        if "ザフライングトラベラー リトルバードアドベンチャー" in switchgame_title:
            download_link = '70010000037909'
        if "サイバーパニック!" in switchgame_title:
            download_link = '70010000037557'
        if "Red Crow Mysteries" in switchgame_title:
            download_link = '70010000037752'
        if "ダブルクロス" in switchgame_title:
            download_link = '70010000017121'


        if download_link is None:
            download_link = 'nolink'

        return download_link