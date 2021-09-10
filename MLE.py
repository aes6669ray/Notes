# def mlemu(X):
#     n=len(X)
#     return sum(X)/n

# def mlesigma(X):
#     n=len(X)
#     mu=mlemu(X)
#     s=sum([(x-mu)**2 for x in X])
#     return s/n

a=sum([(x-5)**2 for x in range(5)])
print(a)
