import csv
from math import sqrt
from copy import deepcopy

class knn:

    def __init__(self):
        self.dados_treinamento = []
        self.testes = []
        self.rotulos = []
        self.rotulos_corretos = []
        self.precisao = 0

    def carregar_arquivo(self,nome_do_arquivo):
        return open(nome_do_arquivo, 'r').readlines()

    def limpar_dados(self, dados_carregados):
        saida = []
        for i in range(1,len(dados_carregados)):
            dados_carregados_temp = dados_carregados[i].replace('\n', '').split(',')
            dados = []
            for d in dados_carregados_temp:
                dados.append(float(d))
            saida.append(dados)
        return saida
        
    def gerar_dados(self, arquivo):
        return self.limpar_dados(self.carregar_arquivo(arquivo))

    def calcula_distancia(self, entrada):
        treinamento_distancia = deepcopy(self.dados_treinamento)
        teste = (entrada[0]-entrada[1]-entrada[2]-entrada[3])**2
        for i in range(len(treinamento_distancia)):
            distancia = 0
            for e in range(len(entrada)):
                distancia += (treinamento_distancia[i][e]-entrada[e])**2
            treinamento_distancia[i].append(distancia)
        return treinamento_distancia
        
    def chave(self, t):
        return t[5]

    def achar_k_menores(self, k, distancias):
        distancias.sort(key=self.chave)
        menores_tipos = []
        for i in range(k):
            menores_tipos.append(distancias[i][4])
        return menores_tipos

    def achar_tipo(self, kprimeiros):
        tipos = [0,0,0]
        tipos[0] = kprimeiros.count(0)
        tipos[1] = kprimeiros.count(1)
        tipos[2] = kprimeiros.count(2)
        return tipos.index(max(tipos))

    def escrever(self, arquivo, texto):
        arquivo = open(arquivo, 'w')
        for r in texto:
            arquivo.write(str(r)+'\n')
        arquivo.close()
            
    def definir_precisao(self,respostas):
        resultado = self.gerar_dados('resultado.txt')
        resposta = self.gerar_dados(respostas)
        count = 0
        for r in range(len(resposta)):
            if resposta[r] == resultado[r]:
                count+=1
        return count/float(len(resposta))*100
    
    def knn(self, treinamento, testes, respostas, k):
        self.dados_treinamento = self.gerar_dados(treinamento)
        self.testes = self.gerar_dados(testes)
        for i in a.testes:
            distancias = self.calcula_distancia(i)
            menores = self.achar_k_menores(k, distancias)
            tipo = self.achar_tipo(menores)
            self.rotulos.append(tipo)
        self.escrever('resultado.txt', self.rotulos)
        self.precisao = self.definir_precisao(respostas)
        print('obteve '+str(self.precisao)+' de precisao para o K = '+str(k))  
            
a = knn()
a.knn('treinamento.csv', 'teste.csv', 'rotulos-teste.txt', 3)
