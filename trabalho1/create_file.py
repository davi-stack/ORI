import os
for i in range(0, 20):
    #cria um arquivo docs{i}.txt
    with open(f'docs/docs{i}.txt', 'w') as f:
        f.write(f"Este é o documento {i}")