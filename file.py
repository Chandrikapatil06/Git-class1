limit = 100


parents, babies = (1, 1)


while babies < limit:
    print(f'This generation has {babies} babies')
    
    parents, babies = (babies, parents + babies)