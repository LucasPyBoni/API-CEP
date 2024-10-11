#!/usr/bin/env python
# coding: utf-8

# ### Via CEP
# 
# https://viacep.com.br/

# #### Consulta de informações de um CEP

# In[ ]:


import pandas as pd
import requests

cep = input('insira seu cep: ')
cep = cep.replace('.','').replace('-','').replace(' ','')

if len(cep) == 8:
    
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(link)
    dic = requisicao.json()
    uf = dic['uf']
    bairro = dic['bairro']
    logra = dic['logradouro']
    print(uf, bairro, logra, sep='\n')
else:
    print('cep inválido')



# #### Busca de CEP a partir de endereço

# In[ ]:


uf = input('Digite o UF: ')
cidade = input('Digite a Cidade: ')
endereco = input('Digite o endereço: ')


cep = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'
requi = requests.get(cep)
dic_cep = requi.json()
print(dic_cep)


# In[ ]:


import pprint
tabela = pd.DataFrame(dic_cep)
display(tabela)


# In[ ]:


ceps = [cep['cep'] for cep in dic_cep]
print(ceps)


# In[ ]:





# In[ ]:




