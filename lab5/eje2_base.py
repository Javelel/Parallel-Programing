from mpi4py import MPI 

 
comm = MPI.COMM_WORLD 
rank = comm.Get_rank()  
size = comm.Get_size() 

if rank == 0: 
   mensaje_enviado = "Mensaje desde 0"  

else: 
   mensaje_enviado = "" 

if rank == 0: 
   for i in range(1,size): 
       print("Enviando a", i)  
       comm.send(mensaje_enviado, dest=i) 

else: 
   mensaje_recibido = comm.recv() 
   print("Recibido por", rank, ":", mensaje_recibido)