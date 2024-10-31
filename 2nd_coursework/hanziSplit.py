import matplotlib.pyplot as plt

class Word:
    def __init__(self, data):
        """
        初始化 Word 对象
        :param data: 汉字矢量图的点坐标数据
        """
        self.data = data
        self.strokes = []

    def split_dot(self):
        """
        将汉字矢量图的点坐标数据切分成笔画
        """
        total_length = self.data[0]
        index = 3
        current_stroke = []

        while index + 1 <= total_length:
            x, y = self.data[index], self.data[index + 1]

            if x == -64 and y == -64:
                break
            if x == -64 and y == 0:
                self.strokes.append(current_stroke)
                current_stroke = []
            else:
                current_stroke.append((x, y))

            index += 2

        if current_stroke:
            self.strokes.append(current_stroke)

    def draw_stroke(self, stroke):
        """
        绘制单个笔画
        :param stroke: 笔画的点坐标列表
        """
        for i in range(len(stroke) - 1):
            x1, y1 = stroke[i]
            x2, y2 = stroke[i + 1]
            plt.plot([x1, x2], [-y1, -y2], marker='.', color='k')
            plt.pause(0.2)

    def draw(self, draw_all, stroke_index):
        """
        绘制汉字矢量图
        :param draw_all: 是否绘制所有笔画
        :param stroke_index: 要绘制的单个笔画的索引
        """
        plt.figure(figsize=(10, 10))
        plt.xlim(-20, 20)
        plt.ylim(-20, 20)

        if draw_all:
            for stroke in self.strokes:
                self.draw_stroke(stroke)
        else:
            self.draw_stroke(self.strokes[stroke_index])

        plt.axis('equal')
        plt.show()

def run(file_path, word_index, draw_all, stroke_index):
    """
    运行汉字矢量图切分和绘制
    :param file_path: 汉字矢量图点坐标文件路径
    :param word_index: 要处理的汉字索引
    :param draw_all: 是否绘制所有笔画
    :param stroke_index: 要绘制的单个笔画的索引
    """
    words = []

    with open(file_path, 'r') as file:
        for line in file.readlines():
            data = list(map(int, line.strip(',,,,,,\n').split(',')))
            words.append(Word(data))

    words[word_index].split_dot()
    words[word_index].draw(draw_all, stroke_index)

if __name__ == '__main__':
    run(r"hz（去噪声）.txt", 1, True, 2)