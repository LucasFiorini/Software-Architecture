from Similaridade import Similaridade
from Coefficients import Statistics

def main():
    s = Similaridade("exemplo.py")
    a, b, c, d = s.calcular_a_b_c_d("Teste", "Util")
    st = Statistics()
    st.generateValues(a, b, c, d)


if __name__ == '__main__':
    main()
