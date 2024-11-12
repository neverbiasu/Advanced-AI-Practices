from gtts import gTTS
import os

# 建立数据字典
hanzi_dict = {
    "明": {"部件1": "日", "部件2": "月"},
    "张": {"部件1": "弓", "部件2": "长"},
    "和": {"部件1": "禾", "部件2": "口"},
    "吴": {"部件1": "口", "部件2": "天"},
}

# 生成句子
sentences = []
for hanzi, parts in hanzi_dict.items():
    sentence = f"汉字{hanzi}由{parts['部件1']}和{parts['部件2']}两部分组成，{parts['部件1']}{parts['部件2']}为{hanzi}。"
    sentences.append(sentence)

# 合并所有句子
full_sentence = " ".join(sentences)

# 语音合成
tts = gTTS(text=full_sentence, lang="zh-cn")
tts.save("hanzi_analysis.mp3")

# 播放语音文件（仅限Linux系统）
os.system("mpg321 hanzi_analysis.mp3")
