import time
from ReconhecedorFacade import ReconhecedorFacade
from ReconhecedorSingleton import ReconhecedorSingleton
from ReconhecedorDecorator import ReconhecedorDecorator

recF = ReconhecedorFacade("Exemplo.py")
recF.reconhecer_facade()
print()
recS = ReconhecedorSingleton("Exemplo.py")
recS.reconhecer_singleton()
print()
recD = ReconhecedorDecorator("Exemplo.py")
recD.reconhecer_decorator()
