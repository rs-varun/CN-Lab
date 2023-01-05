storage = 0
 
no_of_queries = 4
 
bucket_size = 10
 

input_pkt_size = 4
 

output_pkt_size = 1
for i in range(0, no_of_queries):  # space left
 
    size_left = bucket_size - storage
    if input_pkt_size <= size_left:
    
        storage += input_pkt_size
    else:
        print("Packet loss = ", input_pkt_size)
 
    print(f"Buffer size= {storage} out of bucket size = {bucket_size}")
 
    storage -= output_pkt_size
  
  
  OUTPUT:
    
    
Buffer size= 4 out of bucket size = 10
Buffer size= 7 out of bucket size = 10
Buffer size= 10 out of bucket size = 10
Packet loss =  4
Buffer size= 9 out of bucket size = 10
