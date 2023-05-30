# Elseve
# Trabalho final de programação sobre as linhas de cabelo Loreal Paris

print("Bem-vindo(a) ao teste de tipo de cabelo!")

resposta = input("Seu cabelo tem caspa? (1 - SIM, 2 - NÃO):")
if resposta == "1":
   print("LINHA HTDRA DETOX CASPA")

elif resposta == "2":
    resposta_adicional1 = input("Você quer usar antes da escova? (1 - sim, 2 - não): ")
    if resposta_adicional1 == "1": 
       print('LINHA QUERALISO')
    elif resposta_adicional1 == "2":
         resposta_adicional2 = input("Seu cabelo tem química? (1 - sim, 2 - não): ")
         if resposta_adicional2 == "1": 
            resposta_adicional3 = input("Ele é pintado? (1 - sim, 2 - não): ")
            if resposta_adicional3 == "1":
               print('LINHA COLORVIVE')
            elif resposta_adicional3 == "2":
               print('LINHA REPARAÇÃO TOTAL PÓS QUÍMICA')
         elif resposta_adicional2 == "2":
               resposta_adicional4 = input("Seu cabelo tem frizz? (1 - sim, 2 - não)")
               if resposta_adicional4 == "1":
                  print('SUPREME CONTROL')
               elif resposta_adicional4 == "2":
                    resposta_adicional5 = input("Ele tem queda? (1 - sim, 2 - não): ")
                    if resposta_adicional5 == "1":
                       print('LINHA ARGININA')
                    elif resposta_adicional5 == "2":
                           resposta_adicional6 = input("Ele está muito danificado? (1 - sim, 2 - não): ")
                           if resposta_adicional6 == '1':
                              resposta_adicional7 = input("Ele está muito ou pouco danificado? (1 - pouco, 2 - não): ")
                              if resposta_adicional7 == '1':
                                 print('REPARAÇÃO TOTAL 5 PROFUNDA')
                              elif resposta_adicional7 == '2':
                                 print('REPARAÇÃO TOTAL 5')
                           elif resposta_adicional6 == '2':
                                resposta_adicional8 = input('Ele está desidratado? (1 - sim, 2 - não): ')
                                if resposta_adicional8 == '1':
                                   resposta_adicional9 = input('Muito? (1 - sim, 2 - não): ')
                                   if resposta_adicional9 == '1':
                                      print('HIDRAIALURONICO')
                                   elif resposta_adicional9 == '2':
                                      resposta_adicional10 = input('Qual seu tipo de cabelo: 1 - oleoso, 2 - misto, 3 - seco:')
                                      if resposta_adicional10 == '1':
                                         print('PURE HIALURONICO')
                                      elif resposta_adicional10 == '2':
                                         print('HYDRA DETOX')
                                      elif resposta_adicional10 == '3':
                                         resposta_adicional11 = input('Textura do cabelo? 1 - liso, 2 - cacheado: ')
                                         if resposta_adicional11 == "1":
                                            print('OLEO EXTRAORDINARIO')
                                         elif resposta_adicional11 == "2":
                                            print('OLEO EXTRAORDINARIO CACHOS')
                                elif resposta_adicional8 == "2":
                                     resposta_adicional11 = input('Qual é seu tipo de cabelo? 1 - liso, 2 - cacheado?')
                                     if resposta_adicional11 == "1":
                                          resposta_adicional12 = input("Quer mais liso? 1, quer mais longo? 2")     
                                          if resposta_adicional12 == "1":
                                              print('LISO DOS SONHOS')
                                          elif resposta_adicional12 == '2':
                                              print('LONGO DOS SONHOS')
                                     elif resposta_adicional11 == "2":
                                          print('CACHOS DOS SONHOS')
        
