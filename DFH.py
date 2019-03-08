def power(a,b,P):
    if (b == 1):
        return a;
    else:
        return ((pow(a, b)) % P);
P = int(input("Enter the prime number :"))
print("The value of P :", P)
G = int(input("Enter the primitve root for pervious prime number :"))
print("The value of G :", G)  
a = int(input("Enter the chosen private key A :"))
print("The private key a :", a) 
x = power(G, a, P)
b = int(input("Enter the chosen private key B :"))
print("The private key b :", b) 
y = power(G, b, P)
ka = power(y, a, P)
kb = power(x, b, P)
print("Secret key for a is :", ka) 
print("Secret Key for b is :", kb)
