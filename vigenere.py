import sys
def generate_table(SPARSE,letter):
    SPARSE="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?$&;:"
    position=SPARSE.find(letter)
    newsparse=SPARSE[position:]+SPARSE[:position]
    return newsparse


def print_table(key):
    SPARSE="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?$&;:"
    for letter in key:
        print(generate_table(SPARSE,letter))

def encryption(input_file,output_file,key):
    SPARSE="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?$&;:"
    try:
        fd=open(input_file,"r")
        newread=fd.read()
        fd.close()
    except:
        sys.exit("something wrong")
    result=""
    for i in range(len(newread)):
        j=i%len(key)
        newsparse=generate_table(SPARSE,key[j])
        letter=newread[i]
        encryletter=newsparse[SPARSE.find(letter)]
        result+=encryletter
    fd=open(output_file,"w")
    fd.write(result)
    fd.close()
    print ("Encoded:"+result)
    return

def decryption(input_file,output_file,key):
    SPARSE="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?$&;:"
    try:
        fd=open(input_file,"r")
        newread=fd.read()
        fd.close()
    except:
        sys.exit("something wrong")
    result=""
    for i in range(len(newread)):
        j=i%len(key)
        newsparse=generate_table(SPARSE,key[j])
        letter=newread[i]
        decryletter=SPARSE[newsparse.find(letter)]
        result+=decryletter
    fd=open(output_file,"w")
    fd.write(result)
    fd.close()
    print ("Decoded:"+result)
    return



input_file=sys.argv[2]
output_file=sys.argv[3]
key=sys.argv[4]
if len(key)<3:
    sys.exit("this is the wrong key")
if sys.argv[1]=="-e":
    encryption(input_file,output_file,key)
else:
    decryption(input_file,output_file,key)
print_table(key)
