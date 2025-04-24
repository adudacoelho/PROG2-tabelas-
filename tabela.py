def lerTabProp():

    tabela = []
    for i in range(7):
        tabela.append(input().split(','))
        
    return tabela

def lerTabVeiculos():
    v = []
    for i in range(23):
        v.append(input().split(','))
    return v

def relatorio(tabV, tabP):

    tabR = []
    for i in range(len(tabP)):
        p = []
        p.append(tabP[i][1])
        p.append(tabP[i][2])
        c = []
        for j in range(len(tabV)):
            carros = []
            if tabP[i][0] == tabV[j][3]:
                carros.append(tabV[j][0])
                carros.append(tabV[j][1])
                carros.append(tabV[j][2])
                c.append(carros)
        p.append(c)
        tabR.append(p)
    return tabR


def main():
    
    tabV = lerTabVeiculos()
    tabP = lerTabProp()

    tabR = relatorio(tabV, tabP)
    print(tabR)
main()
