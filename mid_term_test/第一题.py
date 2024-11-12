import pyttsx3


class MyTTS:

    def __init__(self, rate=150, volume=1):

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", rate)

        self.engine.setProperty("volume", volume)

    def say(self, text):

        self.engine.say(text)

        self.engine.runAndWait()


if __name__ == "__main__":

    my_tts = MyTTS(rate=150, volume=1)

    text = "你好，欢迎使用文本转语音功能！"

    my_tts.say(text)
