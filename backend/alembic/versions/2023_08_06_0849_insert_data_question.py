"""insert_data_question

Revision ID: 55e822140c8c
Revises: 5
Create Date: 2023-08-06 08:49:02.444328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6'
down_revision = '5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('''
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('幸せ', 'hiragana', 'これからのお二人の(幸せ)祈っております。', '{"1":"しあわせ","2":"こうせ","3":"しああせ","4":"さちせ"}', '1', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('留学生', 'hiragana', '金曜日に(留学生)の友達とパーティーをするんだけど、来る?', '{"1":"りうがくせい","2":"りゅうがくせい","3":"りゅがくせい","4":"りゅうかくせい"}', '2', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('経験', 'hiragana', '彼は新入社員だから、まだ(経験)も少ない。', '{"1":"けいけ","2":"けいげん","3":"けいけん","4":"けけん"}', '3', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('自由', 'hiragana', '就職してからは、(自由)な時間が少なくなった。', '{"1":"じゆう","2":"じゆ","3":"じゅう","4":"じいう"}', '1', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('映画', 'hiragana', '川上さんの好きな(映画)は何ですか。', '{"1":"えか","2":"えが","3":"えいか","4":"えいが"}', '4', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('宝物', 'hiragana', '孫と撮ったこの写真は、私の(宝物)です。', '{"1":"たからぶつ","2":"たからもつ","3":"たからもち","4":"たからもの"}', '4', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('決する', 'hiragana', 'あなたのやさしさは(決して)忘れない。', '{"1":"けつして","2":"けっして","3":"きして","4":"げして"}', '2', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('訪ねる', 'hiragana', '千葉にある友達のアパートを(訪ねた)。', '{"1":"おとずれた","2":"ほうねた","3":"たずねた","4":"たすねた"}', '3', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('涙', 'kanji', '映画に感動して、(なみだ)が止まらなかった。', '{"1":"深","2":"涙","3":"泳","4":"泣"}', '2', '{"1":"Thâm - sâu","2":"Lệ - nước mắt","3":"Vịnh - lặn, đi ngầm dưới đáy nước","4":"Khấp - khóc"}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('観光', 'kanji', '地方の都市でも、外国人のかんこう"客が増えている。', '{"1":"観好","2":"勧好","3":"観光","4":"勧光"}', '3', '{"1":"quan hảo","2":"khuyến hảo","3":"quan quang - thăm quan","4":"khuyến quang"}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('閉める', 'kanji', '出かける前に、すべての窓を(しめ)。', '{"1":"開めた","2":"閉めた","3":"門めた","4":"問めた"}', '2', '{"1":"khai - mở ra","2":"bế - đóng lại ","3":"môn - cái cổng","4":"vấn - nghi vấn"}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('寝る', 'kanji', '子犬たちが気持ちよさそうに(ねて)いる。', '{"1":"睡て","2":"眼て","3":"寝て","4":"値て"}', '3', '{"1":"Thụy - ngủ","2":"Nhãn - mắt","3":"Tẩm - ngủ","4":"Trị - giá trị"}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('お湯', 'kanji', '急にシャワーのお(ゆ)が出なくなった。', '{"1":"油","2":"熱","3":"温","4":"湯"}', '4', '{"1":"Du - dầu, dầu ăn, xăng dầu","2":"Nhiệt - nóng","3":"Ôn - ôn hòa, ấm áp","4":"Thang - nước nóng"}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('連絡', 'kanji', 'ホテルのフロントに(れんらく)した。', '{"1":"連絡","2":"連格","3":"練格","4":"練絡"}', '1', '{"1":"liên lạc","2":"liên cách","3":"luyện cách","4":"luyện lạc"}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('指示', 'missing_word', 'マンションの下の階の人から、「うるさい」と＿＿＿が来た。', '{"1":"確認","2":"指示","3":"評判","4":"苦情"}', '4', '{"1":"xác nhận","2":"chỉ thị","3":"bình phán","4":"khổ tình"}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('動かす', 'missing_word', '最近太ってきたので、少し体を＿＿＿。', '{"1":"休めよう","2":"動かそう","3":"見てみよう","4":"治そう"}', '2', '{"1":"Hưu - nghỉ","2":"Động - hoạt động","3":"Kiến - nhìn thấy","4":"Trị - trị liệu"}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('屋外', 'missing_word', '午前は学校の＿＿＿コートでテニスをする。', '{"1":"室外","2":"課外","3":"場外","4":"屋外"}', '4', '{"1":"thât ngoại - ngoài phòng","2":"khóa ngoại","3":"trường ngoại","4":"ốc ngoại"}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('決める', 'missing_word', '週刊誌の記事が広がり、大臣が職を＿＿＿。', '{"1":"とびだした","2":"やすんだ","3":"はなれた","4":"きめた"}', '3', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('そっくり', 'missing_word', '川村さんはお母さんと顔が＿＿＿だ。', '{"1":"しっかり","2":"そっくり","3":"びっくり","4":"こっそり"}', '2', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('悪い', 'missing_word', '時間に遅れて、みんなには＿＿＿。', '{"1":"悪かった","2":"難しかった","3":"痛かった","4":"良かった"}', '1', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('バーゲン', 'missing_word', '明日から一週間、デパートで＿＿＿が行われる。', '{"1":"バーゲン","2":"デリバリー","3":"ミーティング","4":"コマーシャル"}', '1', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('無事', 'missing_word', '入学式は予定どおり、＿＿＿に終わった。', '{"1":"無理","2":"無断","3":"無事","4":"無視"}', '3', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('たんす', 'missing_word', '洋服が増えたので、新しい＿＿＿を買った。', '{"1":"押入れ","2":"引き出し","3":"あみだな","4":"たんす"}', '4', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('グラス', 'missing_word', 'さあ、乾杯、皆さん＿＿＿を持って下さい。', '{"1":"はいざら","2":"グラス","3":"はし","4":"タイマー"}', '2', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('アルバト', 'missing_word', '大野さんは学費と生活費のため、＿＿＿をしている。', '{"1":"ボランティア","2":"トレーニング","3":"カウンセリング","4":"アルバト"}', '4', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('構う', 'synonym', '参加費の支払いは、後で(構いません)。', '{"1":"あまります","2":"大丈夫です","3":"集めます","4":"同じです"}', '2', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('張り切る', 'synonym', '彼は最近仕事に(張り切って)いる。', '{"1":"努力して","2":"苦力して","3":"手を出して","4":"やる気を出して"}', '4', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('早め', 'synonym', 'この仕事は(早目に)やってください。', '{"1":"今すぐ","2":"なるべく急いで","3":"いつでも","4":"今日中に"}', '2', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('変換', 'synonym', 'パソコンでローマ字から漢字に(変換する)。', '{"1":"直す","2":"見せる","3":"返す","4":"落とす"}', '1', '{"1":"","2":"","3":"","4":""}', '3','true');
        INSERT INTO question (name, type, content, choices, answer, explanation, level_id, active)
        VALUES ('親戚', 'synonym', 'お正月で実家に(しんせき)が集まった。', '{"1":"両親","2":"新子","3":"親類","4":"兄弟"}', '3', '{"1":"","2":"","3":"","4":""}', '3','true');
    ''')

    op.execute('''
        UPDATE question
        SET search_str = concat(type, '|', lower(name), '|', content, CASE
        WHEN code IS NOT NULL THEN concat('|', code) END )
        WHERE TRUE;
    ''')


def downgrade() -> None:
    pass
