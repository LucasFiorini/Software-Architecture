from Similaridade import Similaridade

def main():
    s = Similaridade("exemplo.py")
    a, b, c, d = s.calcular_a_b_c_d("Teste", "Util")
    print(a, b, c, d)


if __name__ == '__main__':
    main()
