class LzwAlgorithm:
    def __init__(self, texto = ''):
        self.dicionario_encode = {chr(i): i for i in range(256)}
        self.dicionario_decode = {i: chr(i) for i in range(256)}
        self.data_encoded = []
        self.data_decoded = []
        self.texto = texto
        self.encode()
        self.decode()

    def encode(self):
        buffer = ''
        ret = []
        for i in range(self.texto.__len__()):
            c = self.texto[i]
            if self.texto.__len__() == 0 or (buffer + c in self.dicionario_encode):
                buffer += c
            else:
                code = self.dicionario_encode[buffer]
                self.dicionario_encode.__setitem__(buffer + c, self.dicionario_encode.__len__()+1)
                buffer = c
                ret += [code]
        if buffer:
            ret += [self.dicionario_encode[buffer]]
        self.data_encoded = ret

    def decode(self):
        last_symbol = self.data_encoded[0]
        ret = self.dicionario_decode[last_symbol]
        for symbol in self.data_encoded[1:]:
            if symbol in self.dicionario_decode:
                atual = self.dicionario_decode[symbol]
                anterior = self.dicionario_decode[last_symbol]
                to_add = atual[0]
                self.dicionario_decode.__setitem__(self.dicionario_encode.__len__() + 1, anterior + to_add)
                ret += atual
            else:
                anterior = self.dicionario_decode[last_symbol]
                to_add = anterior[0]
                self.dicionario_decode.__setitem__(self.dicionario_encode.__len__() + 1, anterior + to_add)
                ret += anterior + to_add
            last_symbol = symbol
        self.data_decoded = ret


lzw = LzwAlgorithm('123abc')

print(lzw.data_encoded)
print(lzw.data_decoded)
