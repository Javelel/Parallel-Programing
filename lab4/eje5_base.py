from mpi4py import MPI  
import random 

comm = MPI.COMM_WORLD 
rank = comm.Get_rank() 
size = comm.Get_size() 

numero = random.random()  

print("Procesador", rank, ":", numero) 

valor = comm.reduce(numero, root=0) 

print("Valor ", valor) 