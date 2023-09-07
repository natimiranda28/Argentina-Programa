def calcula_promedio():
    
    for i in range(1,12,1):
        if i<=6:
            sum=sum+300
    else:
        if i>=7 and i<10:
            sum=sum+500
        else:
            sum=sum+700
            
            
    prom= sum//12
    return prom
 
 
 
 
 def sueldo():
     
    if calcula_promedio()<300:
         return "Sueldo bajo"
    else: 
         if (calcula_promedio()>=300 and calcula_promedio()≤=900):
             
             return "Sueldo medio"
         
         else:
             return "Sueldo mejor de lo normal"  
            


            