'''
ATCG count
       

1.0
        

Mario Alberto Limón Hernández
        

DESCRIPTION: Counts number of ATCG nucleotides
        

CATEGORY
        

USAGE

    % python programName
    

ARGUMENTS


METHOD


SEE ALSO


        
'''
nA = 0
nC = 0
nG = 0
nT = 0
with open('archivo.txt', 'r') as file:
    lines = file.read()
sequence = lines.upper()
for base in sequence:
    if base == 'A':
        nA+=1
    elif base == 'C':
        nC+=1
    elif base == 'G':
        nG+=1
    elif base == 'T':
        nT+=1
# Posteriormente se imprime

# ¿Donde lo imprimes? jajaja 
# Te dejo una versión de código más simple, aún no hemos visto métodos en clase, pero son una cosa maravillosa que permite que puedas hacer un monton de cosas 
# En este caso usé el método count:
with open(archivo, 'r') as file:
    DNA = file.read()
# Obtenemos la frecuencia de aparicion de cad aletra.
print(f"El total por base es: A:{ADN.count('A')} C:{ADN.count('C')} T:{ADN.count('T')} G:{ADN.count('G')}")

# ===========================================================================
# = File                            imports
# ===========================================================================





# ===========================================================================
# =                            Command Line Options
# ===========================================================================






# ===========================================================================
# =                            functions
# ===========================================================================





# ===========================================================================
# =                            main
# ===========================================================================


# step 1.


# step 2.


# step 3.



