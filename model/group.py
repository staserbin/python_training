from sys import maxsize

class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    #__repr__ - определяет как будет выглядеть объект при выводе на консоль, каково его строковое представление
    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.name, self.header, self.footer)  # данная строка выводит в формате "id:name"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    #функция, которая вычисляет ключ, по которому мы сравниваем группы
    def id_or_max(self):
        if self.id:
            #gr.id - строка, поэтому преобразуем его в число, чтобы можно было сравнивать с maxsize
            return int(self.id)
        else:
            # максимальное целочисленное
            return maxsize