"""insert_data_word_table

Revision ID: 3
Revises: 2
Create Date: 2023-07-16 12:29:30.552654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3'
down_revision = '2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('''
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (1, '男性', 'Nam tính', 'だんせい', 3, '{}', '{}', '{"男女": "nam nữ",
    "性別": "giới tính"}', 
    '{}', 
    '{}',
     '{}',  '[{"type":"Danh từ","sen_1":"理想の 男性 と結婚する","mean_1":"Kết hôn với người đàn ông lý tưởng.","sen_2":"","mean_2":""}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (2, '女性', 'Nữ tính', 'じょせい', 3, '{}', '{}', '{"男女": "nam nữ",
    "性別": "giới tính"}', 
    '{}', 
    '{}',
     '{}',  '[{"type":"Danh từ","sen_1":"理想の 女性 と結婚する","mean_1":"Kết hôn với người phụ nữ lý tưởng.","sen_2":"あの女性・女の人・女は誰ですか。","mean_2":"Người con gái/ người phụ nữ đó là ai?"}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (3, '高齢', 'Cao linh', 'こうれい', 3, '{}', '{}', '{}', 
    '{}', 
    '{"__者": "người cao tuổi", "__化社会":"Xã hội già hóa"}',
     '{}',  '[{"type":"Danh từ","sen_1":"祖母は高齢だが、まだとても元気だ。","mean_1":"Tuy bà tôi đã già nhưng bà vẫn rất khỏe mạnh.","sen_2":"","mean_2":""}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (4, '年上', 'Niên thượng', 'としうえ', 3, '{}', '{"年下":"Kém tuổi hơn"}', '{"年長": "Lớn tuổi"}', 
    '{}', 
    '{}',
     '{}',  '[{"type":"Danh từ","sen_1":"年上の友達。","mean_1":"Người bạn lớn tuổi hơn","sen_2":"彼女は私より三つ年上だ。","mean_2":"Cô ấy lớn hơn tôi ba tuổi."}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (5, '目上', 'Mục thượng', 'めうえ', 3, '{}', '{"目下":"Cấp dưới"}', '{}', 
    '{}', 
    '{}',
     '{}',  '[{"type":"Danh từ","sen_1":"目上の人には敬語で話した方がいい。","mean_1":"Tốt hơn là nên nói bằng kính ngữ với cấp trên.","sen_2":"","mean_2":""}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (6, '先輩', 'Tiền bối', 'せんぱい', 3, '{}', '{}', '{}', 
    '{}', 
    '{}',
     '{}',  '[{"type":"Danh từ","sen_1":"田中さんと私は同じ年だが、職場では彼の方が先輩だ。","mean_1":"Anh Tanaka và tôi bằng tuổi nhau, nhưng ở nơi làm việc anh ấy là tiền bối.","sen_2":"","mean_2":""}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (7, '後輩', 'Hậu bối', 'こうはい', 3, '{}', '{}', '{}', 
    '{}', 
    '{}',
     '{}',  '[{"type":"Danh từ","sen_1":"田中さんと私は同じ年だが、職場では彼の方が先輩だ。","mean_1":"Anh Tanaka và tôi bằng tuổi nhau, nhưng ở nơi làm việc anh ấy là tiền bối.","sen_2":"","mean_2":""}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (8, '上司', 'Thượng ty', 'じょうし', 3, '{}', '{"部下":"Cấp dưới"}', '{"同僚":"Đồng nghiệp"}', 
    '{}', 
    '{}',
     '{}',  '[{"type":"Danh từ","sen_1":"上司に相談してから決定する。","mean_1":"Tôi sẽ trao đổi với cấp trên rồi quyết định.","sen_2":"","mean_2":""}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (9, '相手', 'Tương thủ', 'あいて', 3, '{}', '{}', '{}', 
    '{}', 
    '{"話＿＿":"Đối phương (khi nghe, nói chuyện)", "結婚＿＿":"Hôn phu", "相談＿＿":"Người thảo luận cùng"}',
     '{}',  '[{"type":"Danh từ","sen_1":"相手の目を見て話す。","mean_1":"Nhìn vào mắt đối phương khi nói chuyện.","sen_2":"今度の試合の相手は強そうだ。","mean_2":"Đối thủ trong trận đấu này có vẻ mạnh."}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (10, '知り合い', 'Tri hợp', 'しりあい', 3, '{"知人":"Người quen"}', '{}', '{"友達":"Bạn ", "友人":"Người bạn", "親友":"Bạn thân"}', 
    '{}', 
    '{}',
     '{}',  '[{"type":"Danh từ","sen_1":"知り合いに息子の就職を頼む。","mean_1":"Tôi nhờ người quen tìm việc cho con trai.","sen_2":"","mean_2":""}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (11, '友人', 'Hữu nhân', 'ゆうじん', 3, '{"知人":"Người quen"}', '{}', '{ "親友":"Bạn thân", "知り合い":"Người quen"}', 
    '{}', 
    '{}',
     '{}',  '[{"type":"Danh từ","sen_1":"「田中さんを知っていますか。」「学生時代の友人です。」","mean_1":"Bạn có biết anh Tanaka không? - Có, anh ý là bạn từ thời đại học của mình.","sen_2":"","mean_2":""}]',
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (12, '仲', 'Trọng', 'なか', 3, '{}', '{}', '{}', 
    '{ "＿＿がいい":"Quan hệ tốt", "__が悪い":"Quan hệ xấu"}', 
    '{ "＿＿間":"Đồng minh, bạn bè", "__良し":"Bạn bè tốt"}',
     '{}',  '[{"type":"Danh từ","sen_1":"私は山本さんと仲がいい。","mean_1":"Tôi có mối quan hệ tốt với anh Yamamoto.","sen_2":"","mean_2":""}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (13, '生年月日', 'Sinh Niên Nguyệt Nhật', 'せいねんがっぴ', 3, '{}', '{}', '{"誕生日":"Ngày sinh nhật"}', 
    '{}', 
    '{}',
     '{}',  '[{"type":"Danh từ","sen_1":"書類に生年月日を記入する。","mean_1":"Điền ngày tháng vào tài liệu.","sen_2":"","mean_2":""}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (14, '誕生', 'Đản sinh', 'たんじょう', 3, '{}', '{}', '{}', 
    '{}', 
    '{"__日":"Ngày sinh"}',
     '{}',  '[{"type":"Danh từ","sen_1":"新しい命の誕生を祝う。","mean_1":"Tôi cầu chúc cho sự ra đời của sinh mệnh mới.","sen_2":"新政権が誕生する。","mean_2":"Chính quyền mới được thành lập"}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (15, '年', 'Niên', 'とし', 3, '{"年齢":"Tuổi đời"}', '{}', '{}', 
    '{ "＿＿が始まる<ｰ>終わる":"Bắt đầu năm mới <-> Kết thúc năm", "__が開ける":"Bắt đầu năm mới",  "__が過ぎる":"Trải qua một năm",  "＿＿を取る":"Thêm tuổi"}', 
    '{"__開け":"Năm mới", "お＿＿寄り":"Người già"}',
     '{}',  '[{"type":"Danh từ","sen_1":"年の初めてに一年の計画を立てる。","mean_1":"Lập kế hoạch cho một năm mới vào dịp đầu năm.","sen_2":"父は歳より若く見える。","mean_2":"Bố tôi trông trẻ hơn so với tuổi."}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (16, '出身', 'Xuất thân', 'しゅっしん', 3, '{}', '{}', '{}', 
    '{}', 
    '{"＿＿地":"Nơi sinh", "＿＿校":"Trường xuất thân"}',
     '{}',  '[{"type":"Danh từ","sen_1":"「ご出身はどちらですか。」","mean_1":"Bạn đến từ đâu.","sen_2":"私は｛東京・東京大学｝の出身です。","mean_2":"Tôi đến từ Tokyo/ đại học Tokyo."}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (17, '故郷', 'Cố hương', 'こきょう', 3, '{"ふるさと":"Quê hương"}', '{}', '{}', 
    '{}', 
    '{}',
     '{}',  '[{"type":"Danh từ","sen_1":"仕事が忙しくてもう何年も故郷に帰っていない。","mean_1":"Đã nhiều năm tôi không về quê vì bận công việc.","sen_2":"","mean_2":""}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (18, '成長する', 'Thành trường', 'せいちょうする', 3, '{}', '{}', '{}', 
    '{}', 
    '{"高度経済＿＿":"Tăng trưởng kinh tế mạnh", "＿＿率":"Tỷ lệ tăng trưởng mạnh"}',
     '{}',  '[{"type":"Danh từ","sen_1":"子供の成長を喜ぶ。","mean_1":"Tôi vui mừng vì sự trưởng thành của các con.","sen_2":"事業の成長。","mean_2":"Phát triển sự nghiệp."}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (19, '成人する', 'Thành nhân', 'せいじんする', 3, '{}', '{"未成年":"Vị thành niên"}', '{}', 
    '{}', 
    '{"＿＿式":"Lễ thành nhân"}',
     '{}',  '[{"type":"Danh từ","sen_1":"日本では二十歳以上の人を成人と言う。","mean_1":"Ở Nhật Bản, những người trên 20 tuổi được gọi là người lớn.","sen_2":"息子は成人して働いている。","mean_2":"Con trai tôi đã trưởng thành và đi làm."}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (20, '合格する', 'Hợp cách', 'ごうかくする', 3, '{}', '{"不合格（になる・だ）":"Trượt, không đỗ"}', '{}', 
    '{}', 
    '{"＿＿者":"Người trúng tuyển", "＿＿率":"Tỷ lệ đỗ"}',
     '{}',  '[{"type":"Danh từ","sen_1":"大学・入学・検査に合格する。","mean_1":"Đậu đại học/đầu vào/kỳ thi.","sen_2":"","mean_2":""}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (21, '進学する', 'Tiến học', 'しんがくする', 3, '{}', '{}', '{}', 
    '{}', 
    '{ "＿＿率":"Tỷ lệ  học lên"}',
     '{}',  '[{"type":"Danh từ","sen_1":"子供の進学について考える。","mean_1":"Tôi suy nghĩ về việc học lên cao của con.","sen_2":"大学院に進学する。","mean_2":"Đi học cao học."}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (22, '退学する', 'Thoái học', 'たいがくする', 3, '{}', '{}', '{"中退（をする）":"Nghỉ học giữa chừng"}', 
    '{}', 
    '{"＿＿届け":"Đơn nghỉ học", "＿＿処分":"Xử lý thôi học"}',
     '{}',  '[{"type":"Danh từ","sen_1":"退学の理由を説明する。","mean_1":"Giải thích lý do nghỉ học.","sen_2":"病気で大学を退学した。","mean_2":"Bị ốm nên phải nghỉ đại học."}]', 
    'true');
    INSERT INTO word (code, name, kanji, yomi, level, synonym, antonym, kanren, usage_pattern, compound_word, common_word, meaning, active) 
    VALUES (23, '就職する', 'Tựu chức', 'しゅうしょくする', 3, '{}', '{"退職":"Bỏ việc"}', '{"履歴書":"Sơ yếu lý lịch"}', 
    '{}', 
    '{"＿＿活動":"Hoạt động tìm việc", "＿＿試験":"Kỳ thi xin việc", "＿＿難":"Khó xin việc"}',
     '{}',  '[{"type":"Danh từ","sen_1":"旅行会社に就職する。","mean_1":"Xin việc tại một công ty du lịch","sen_2":"","mean_2":""}]', 
    'true');
    
    ''')


def downgrade() -> None:
    pass
