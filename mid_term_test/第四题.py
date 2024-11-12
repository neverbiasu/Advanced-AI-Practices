import pyttsx3


# 创建一个字典来存储汉字及其组成部分

hanzi_parts = {"明": ["日", "月"], "张": ["弓", "长"], "和": [], "吴": ["口", "天"]}


# 初始化语音合成器

engine = pyttsx3.init()


# 遍历字典并生成句子

sentences = []

for hanzi, parts in hanzi_parts.items():

    if parts:

        part_str = "和".join(parts)

        sentence = f"汉字{hanzi}由{part_str}两部分组成，{part_str}为{hanzi}。"

        sentences.append(sentence)

    else:

        sentence = f"汉字{hanzi}无法分解。"

        sentences.append(sentence)


# 合并所有句子

final_sentence = " ".join(sentences)


# 输出句子

print(final_sentence)


# 将句子转化为语音

engine.say(final_sentence)

engine.runAndWait()
