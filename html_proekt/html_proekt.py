class Tags:
    def __init__(self):
        self.name = "tag"
        self.textfor = ""
        self.attribute = ""
        self.arrayinto = []

    def creation(self):
        answer = "<" + self.name + " " + self.attribute + ">" +self.textfor + " \n"
        for tag in self.arrayinto:
            answer = answer + tag.creation()
        answer = answer + "</" + self.name + "> \n"
        return answer
    
    def createFile(self, files):
        file = open(files, "w")
        file.write(self.creation())
        file.close()


class Html(Tags):
    def __init__(self, array):
        Tags.__init__(self)
        self.name = "html"
        self.arrayinto = array


class Head(Tags):
    def __init__(self, array):
        Tags.__init__(self)
        self.name = "head"
        self.arrayinto = array


class Body(Tags):
    def __init__(self, array, attribute):
        Tags.__init__(self)
        self.name = "body"
        self.arrayinto = array
        self.attribute = attribute


class Title(Tags):
    def __init__(self, text):
        Tags.__init__(self)
        self.name = "title"
        self.textfor = text


class Img(Tags):
    def __init__(self, attribute):
        Tags.__init__(self)
        self.name = "img"
        self.attribute = attribute


class H1(Tags):
    def __init__(self, text):
        Tags.__init__(self)
        self.name = "h1"
        self.textfor = text


class Video(Tags):
    def __init__(self, attribute):
        Tags.__init__(self)
        self.name = "video"
        self.attribute = attribute


class A(Tags):
    def __init__(self, text, attribute):
        Tags.__init__(self)
        self.name = "a"
        self.textfor = text
        self.attribute = attribute


class Em(Tags):
    def __init__(self, text):
        Tags.__init__(self)
        self.name = "em"
        self.textfor = text


class B(Tags):
    def __init__(self, text):
        Tags.__init__(self)
        self.name = "b"
        self.textfor = text


class Br(Tags):
    def __init__(self):
        Tags.__init__(self)
        self.name = "br"


site = Html([
    Head([Title("Экзаменационная работа")]),
    Body([
        H1("Что такое когнитивистика?"),
        Img("src='https://goroday.ru/data/photo/070919_057983544809.jpg' width='350 px' height='200 px'"),
        Br(),
        B("Когнитивистика (лат. cognitio — познание) — междисциплинарное научное направление, объединяющее теорию "
          "познания, когнитивную психологию, нейрофизиологию, когнитивную лингвистику и теорию искусственного "
          "интеллекта."),
        Br(),
        Video("src='https://youtu.be/Oztrq_Zx9X0' width='350 px' height='200 px' controls"),
        Br(),
        B("Если видео не загружается, "),
        A("перейдите по этой ссылке", "href='https://youtu.be/Oztrq_Zx9X0'"),
        Br(),
        Em("Чтобы узнать больше, нажмите"),
        A("здесь", "href='https://postnauka.ru/themes/brain'"),
        Br()
    ], "")
])

site.createFile("proekt.html")
