x=0
while x==0:
    op1=input("Pressione Enter para começar: ")
    if op1=="":
        # Aqui se encontra a variável que inicia o menu do sistema
    	a=0
        # Listas que armazena os cadastros
    	nome=[]
    	email=[]
    	data=[]
    	cpf=[]
    	tell=[]
    	print("-----------------------------------------------------------------------\n")
    	print("                         Bem Vindo ao Programa CRUD")
    	print("                                      de")
    	print("             💻   Anderson Melo da Silva  N.º05 1°B 2022     💻")
    	print("             💻   Fr. Emerson Marques Araújo  N.º17 1°B 2022 💻")
    	print("\n-----------------------------------------------------------------------")
    	# Aqui vai se iniciar a repetição de informações do sistema
    	inf=0
    	while inf == 0:
    		print("__"*35)
	    	info=int(input(" Digite sua escolha:\n 1-Começar\n 2-Informações sobre o sistema\n "))
	    	if info == 1:
	    		print("Iniciando sistema...")
	    		inf=1
	    	elif info == 2:
	    		print("=="*8,"Informações sobre o Menu do Sistema","=="*7)
	    		print("--"*35)
	    		print("°-°Opção Cadastrar:\n -Nessa opção o individuo podera escolher a quantidade de cadastros que serão feitos e em seguida cadastrara suas informações com forme for pedido;")
	    		print("--"*35)
	    		print("°-°Opção Ler:\n -Nessa opção o individuo poderar Ler suas informações que foram registradas na opção Cadastrar;")
	    		print("--"*35)
	    		print("°-°Opção Deletar:\n -Nessa opção é possivel Deletar qualquer informação Cadastrada que desejar;")
	    		print("--"*35)
	    		print("°-°Opção Atualizar:\n -Nessa opção é possivel auterar qualquer informação Cadastrada, assim o individuo poderar Atualizar suas informações;")
	    		print("--"*35)
	    		print("°-°Opção Sair:\n -Nessa opção o individuo podera Sair do sistema que sera fechado e finalizado.")
	    		print("--"*35)
	    		inf2=0
	    		while inf2 == 0:
	    		    info=int(input(" Digite sua escolha:\n 1-Começar\n 2-Fechar o programa\n "))
	    		    if info == 1:
	    		        print("Iniciando sistema...")
	    		        inf2=1
	    		        inf=1
	    		    elif info == 2:
	    		        print("Fechando sistema...")
	    		        print("Fim do programa")
	    		        print("     ┏( ͡ᵔ ͜ʖ ͡ᵔ)┛")
	    		        a=1
	    		        inf2=1
	    		        inf=1
	    		        x=1
	    		    else:
	    		        print("__"*35)
	    		        print("!!Essa opção não existe!!")
	    	else:
	    		print("__"*35)
	    		print("!!Essa opção não existe!!")
    	# Variável que representa o Número de Cadastros
    	qtc=0
    	while a==0:
    		print("-=" *35)
    		print("=="*14,"Menu do Sistema","=="*13)
    		print("1-Cadastrar")
    		print("2-ler")
    		print("3-Deletar")
    		print("4-Atualizar")
    		print("5-Sair")
    		esc=input("Escolha a opção que deseja:\n")
    		# Se o usuário escolhe a opção 1 cadastrar
    		if esc=="1":
    		    # Variável que uso nos while
    			c=0
    			#Se você não tiver nenhum cadastro
    			if qtc==0:
        			while c==0:
        				print("__"*35)
        				qtc=int(input(' Digite: "0" se quiser voltar\n ou\n Quantos cadastros você quer fazer:\n '))
        				if qtc>0:
        				    print("-=" *35)
        				    print("Preencha os espaços abaixo para fazer o seu cadastro:")
        				    print("__"*35)
        				    # Variável que conta a quantidade de cadastros
        				    qt=1
        				    registro=0
        				    while  registro<qtc:
        				        print("-="*5,"Cadastro %s"%qt,"-="*5)
        				        no=input("Digite seu nome completo: ")
        				        e=input("Digite seu e-mail: ")
        				        d=input("Digite sua data de nascimento: ")
        				        cpf1=input("Digite seu CPF: ")
        				        t=input("Digite seu Telefone: ")
        				        print("__" *35)
        				        print("Deseja continuar o cadastro com essas informações ou deseja refazer? ")
        				        l=0
        				        while l==0:
        				            print("1-Salvar")
        				            print("2-Refazer")
        				            i=int(input("Digite sua escolha: "))
        				            print("__"*35)
        				            # Caso o usuário queira salvar os dados
        				            if i==1:
        				                # Verificar se o usuário colocou pelomenos algo.
        				                if no=="" or e=="" or d=="" or cpf1=="" or t=="":
        				                    print("!!Há campos vazios!!")
        				                    print("Por favor preencha os campos corretamente")
        				                    print("__" *35)
        				                    l=1
        				                # Se nada tiver errado, entra nesse else
        				                else:
        				                    print("  "*13 ,"Dados salvos")
        				                    # Junta o que o usuário cadastrou nas listas
        				                    nome.append(no)
        				                    email.append(e)
        				                    data.append(d)
        				                    cpf.append(cpf1)
        				                    tell.append(t)
        				                    # Caso o contador for igual ao número de cadastros feitos, o programaa vouta ao menu inicial
        				                    if qt==qtc:
        				                        l=1
        				                        c=1
        				                        registro+=1
        				                    # Caso ainda falte cadastros o programa continua
        				                    else:
        				                        l=1
        				                        qt+=1
        				                        registro+=1
        				            # Caso ele decida refazer
        				                # Ele so retorna aos dados que o usuário vai digitar 
        				            elif i==2:
        				                    print("Refazer cadastro")
        				                    l=1
        				                    registro=registro
        				            # Caso ele digite uma função que não existe
        				            else:
        				                print("  "*13 ,"Sem função")
        				# Ele não faz nada, só reza a quantidade de cadastro (qtc) e acaba com a repetição 'c'
        				elif qtc==0:
        				    qtc=0
        				    c=1
        				# Caso ele digite um opção inexistente
        				else:
        					print("Número de cadastros invalido")
        					c=0
    			# Se você tiver cadastros já feitos antes
    			elif qtc!=0:
    			    print("-=" *35)
    			    print("Você já tem cadastros feitos!!")
    			    print("-=" *35)
    			    k=0
    			    while k==0:
    			        print("Você deseja: ")
    			        print("1-Adicionar cadastros")
    			        print("2-Valtar ao menu inicial")
    			        i=int(input("Escolha sua opção: "))
    			        print("-=" *35)
    			        # Se escolhido 1, o programa funciona igal a o anterior ↑
    			        if i==1:
    			            while c==0:
                				print("__"*35)
                				qtc2=int(input('Digite:\n "0" se quiser voltar ao menu\n ou\n Quantos cadastros você quer fazer:\n '))
                				if qtc2>0:
                						print("-=" *35)
                						print("Preencha os espaços abaixo para fazer o seu cadastro:")
                						print("__"*35)
                						qtc3=qtc2+qtc
                						qt2=qtc+1
                						registro=0
                						while  registro<qtc2:
                							print("-="*5,"Cadastro %s"%qt2,"-="*5)
                							no=input("Digite seu nome completo: ")
                							e=input("Digite seu e-mail: ")
                							d=input("Digite sua data de nascimento: ")
                							cpf1=input("Digite seu CPF: ")
                							t=input("Digite seu Telefone: ")
                							print("__" *35)
                							print("Deseja continuar o cadastro com essas informações ou deseja refazer? ")
                							l=0
                							while l==0:
                							    print("1-Salvar")
                							    print("2-Refazer")
                							    # È string mas funciona como um inteiro
                							    d=input("Digite sua escolha: ")
                							    print("__"*35)
                							    # Mesma coisa que o cadastro anterior
                							    if d=="1":
                							        if i==1:
                							            if no=="" or e=="" or d=="" or cpf1=="" or t=="":
                							                print("!!Há campos vazios!!")
                							                print("Por favor preencha os campos corretamente")
                							                print("__" *35)
                							                l=1
                							            else:
                							            	print("  "*13 ,"Dados salvos")
                							            	nome.append(no)
                							            	email.append(e)
                							            	data.append(d)
                							            	cpf.append(cpf1)
                							            	tell.append(t)
                							            	qtc+=1
                							            	qt2+=1
                							            	if qt2==qtc3+1:
                							            	    registro+=1
                							            	    l=1
                							            	    c=1
                							            	    k=1
                							            	else:
                							            	    registro+=1
                							            	    l=1
                							    elif d=="2":
                							        print("Refazer cadastro")
                							        registro=registro
                							        l=1
                							    else:
                							        print("  "*13 ,"Sem função")
                	            # Acaba com as repetições
                				elif qtc2==0:
                				    c=1
                				    k=1
                				else:
                				    print("Número de cadastros invalido")
                				    c=0
    			        elif i==2:
    			            k=1
    			        else:
    			            print("  "*13 ,"Sem função")
    		# Se o usuário escolhe a opção 2 ler
    		elif esc=="2":
    			if qtc!=0:
    				registro=0
    				print("=="*12,"Cadastros Registrados","=="*12)
    				while registro<qtc:
    					print("-="*5,"Cadastro ",registro+1,"-="*5)
    					print("Nome: ",nome[registro])
    					print("E-mail: ",email[registro])
    					print("Data de nascimento: ",data[registro])
    					print("CPF: ",cpf[registro])
    					print("Telefone: ",tell[registro])
    					print("--"*35)
    					registro+=1
    				e=0
    				while e==0:
    					enter=input("Pressione 'Enter' para voltar ao menu:\n")
    					if enter=="":
    						e=1
    					else:
    						print("__"*35)
    						print("!!Erro na tecla digitada tente novamente!!")
    						print("--"*35)
    			elif qtc==0:
    				print("__"*35)
    				print("  "*13 ,"Sem cadastro")
    				print("__"*35)
    		# Se o usuário escolhe a opção 3 deletar
    		elif esc=="3":
    			print("-=" *35)
    			if qtc!=0:
    				u=0
    				while u==0:
    					registro=0
    					print("=="*12,"Cadastros Registrados","=="*12)
    					# Printa os cadastros faitos antes
    					while registro<qtc:
    						print("-="*5,"Cadastro ",registro+1,"-="*5)
    						print("Nome: ",nome[registro])
    						print("E-mail: ",email[registro])
    						print("Data de nascimento: ",data[registro])
    						print("CPF: ",cpf[registro])
    						print("Telefone: ",tell[registro])
    						print("--"*35)
    						registro+=1
    					qcd=int(input('Digite:\n"-1" para deletar todos\nou\n"0" para voltar ao menu inicial\nou\nQual cadastro você quer deletar\n'))
    					if qcd<=qtc and qcd>0:
    					    print("Cadastro deletado")
    					    qcd-=1
    					    del nome[qcd]
    					    del email[qcd]
    					    del data[qcd]
    					    del cpf[qcd]
    					    del tell[qcd]
    					    qtc=qtc-1
    					    # Caso não tenha mais cadastros
    					    if qtc==0:
    					        u=1
    					elif qcd==0:
    						u=1
    					# Caso o usuário queira deletar todos os cadastros de
    					elif qcd==-1:
    					    # Todos as listas perdem todo.
    					    print("-"*35)
    					    print("                           Todos os cadastros foram deletados")
    					    print("-"*35)
    					    nome=[]
    					    emai=[]
    					    data=[]
    					    cpf=[]
    					    tell=[]
    					    qtc=0
    					    u=1
    					else:
    						print("__"*35)
    						print("Não á esse cadastro/Função")
    						print("__"*35)
    			else:
    				print("__"*35)
    				print("  "*13 ,"Sem cadastro")
    				print("__"*35)
    		# Se o usuário escolhe a opção 4 Atualizar
    		elif esc=="4":
    			print("-=" *35)
    			# Caso o usuário tenha cadastros qtc vai ser diferente de zero
    			if qtc!=0:
    				u=0
    				while u==0:
    					registro=0
    					print("=="*12,"Cadastros Registrados","=="*12)
    					# Vai printar todos os cadastros
    					while registro<qtc:
    						print("-="*5,"Cadastro ",registro+1,"-="*5)
    						print("Nome: ",nome[registro])
    						print("E-mail: ",email[registro])
    						print("Data de nascimento: ",data[registro])
    						print("CPF: ",cpf[registro])
    						print("Telefone: ",tell[registro])
    						print("--"*35)
    						registro+=1
    					qcd=int(input('Digite "-1" para atualizar todos\nou\nDigite "0" para voltar ao menu inicial\nou\nDigite qual cadastro você quer atualizar\n'))
    					# Caso o usuário digite um número de cadastro que exista
    					if qcd<=qtc and qcd>0:
    						t=0
    						while t==0:
    						    h=0
    						    print("-"*5,"Você está atualizado o cadastro ",qcd,"-"*5)
    						    # Várias que vai fazer a troca das informações
    						    inp=input("Digite seu novo nome: ")
    						    inp2=input("Digite seu novo e-mail: ")
    						    inp3=input("Digite sua nova data de nascimento: ")
    						    inp4=input("Digite seu novo CPF: ")
    						    inp5=input("Digite seu novo telefone: ")
    						    while h==0:
    						        vcd=int(input("Você deseja:\n1-Salvar\n2-Refazer\n3-Voltar sem salvar\n"))
    						        # Casno escolha 1
    						        if vcd==1:
    						            # Impede que o usuário não digite nada
    						            if inp=="" or inp2=="" or inp3=="" or inp4=="" or inp5=="":
    						                print("!!Há campos vazios!!")
    						                print("Por favor preencha os campos corretamente")
    						                print("--"*35)
    						            # Caso esteja tudo OK
    						            else:
    						                qcd-=1
    						                # Substitui que foi digitado antes, no local dos dados anteriores
    						                nome[qcd]=inp
    						                email[qcd]=inp2
    						                data[qcd]=inp3
    						                cpf[qcd]=inp4
    						                tell[qcd]=inp5
    						                print("!!Todas as informações foram atualizadas!!")
    						                print("__"*35)
    						                h=1
    						                t=1
    						                u=0
    						        # Casno escolha 2
    						        elif vcd==2:
    						            h=1
    						            t=1
    						            u=0
    						        # Casno escolha 3
    						        elif vcd==3:
    						            h=1
    						            t=1
    						        # Casno escolha uma função indisponível
    						        else:
    						            print("  "*13 ,"Sem função")
    					elif qcd==0:
    					    u=1
    					# Entra no elif se o usuário digitar '-1' e a quantidade de cadastros seja diferente de zero
    					elif qcd==-1 and qtc!=0:
    					    # o contador 3 vai subsistir os registros da listas se o usuário deseja
    					    qt3=0
    					    # enquanto não percorrer todos os cadastos o programa repetirá
    					    while qt3<qtc:
    					        print("-"*5,"Você está atualizado o cadastro ",qt3+1,"-"*5)
    					        # Várias que vai fazer a troca das informações
    					        inp=input("Digite seu novo nome: ")
    					        inp2=input("Digite seu novo e-mail: ")
    					        inp3=input("Digite sua nova data de nascimento: ")
    					        inp4=input("Digite seu novo CPF: ")
    					        inp5=input("Digite seu novo telefone: ")
    					        h=0
    					        while h==0:
    					            vcd=int(input("Você deseja:\n1-Salvar\n2-Refazer\n"))
    					            # Casno escolha 1
    					            if vcd==1:
    					                # Impede que o usuário não digite nada
    					                if inp=="" or inp2=="" or inp3=="" or inp4=="" or inp5=="":
    						                print("!!Há campos vazios!!")
    						                print("Por favor preencha os campos corretamente")
    						                h=1
    						                print("--"*35)
    						            # Caso esteja tudo OK
    					                else:
    						                # Substitui que foi digitado antes, no local dos dados anteriores
    						                nome[qt3]=inp
    						                email[qt3]=inp2
    						                data[qt3]=inp3
    						                cpf[qt3]=inp4
    						                tell[qt3]=inp5
    						                print("!!As informações foram atualizadas!!")
    						                print("__"*35)
    						                h=1
    						                qt3+=1
    					            # Casno escolha 2
    					            elif vcd==2:
    					                h=1
    						        # Casno escolha uma função indisponível
    					            else:
    						            print("  "*13 ,"Sem função")
    					else:
    						print("_"*35)
    						print("Não á esse cadastro")
    						print("_"*35)
    			# Caso o usuário não tenha cadastros
    			else:
    				print("__"*35)
    				print( "  "*13 ,"Sem cadastro")
    				print("__"*35)
    		# Se o usuário escolhe a opção 5
    		elif esc=="5":
    			ops=int(input("Quer mesmo sair:\n 1-Sim\n 2-Não\n "))
    			if ops==1:
    				print("Fechando sistema...")
    				print("Fim do programa")
    				print("     ┏( ͡ᵔ ͜ʖ ͡ᵔ)┛")
    				a=1
    				x=1
    			if ops>2 or ops<1:
    				print("!!Essa opção não existe!!")
    		# Easter egg
    		elif esc=="0":
    			print("==Sistema 99% funcional==\n==Criado por: Anderson e Emerson==\n_(っ ͡ᵔ ͜ʖ͡ᵔ )っ")
    		# Se o usuário escolhe uma opção que não existe
    		else:
    			print("!!Essa opção não existe!!\n==Por favor digite uma opção do menu==\n====¯\_( ಠ ₒ ಠ )_/¯====")
    # Se o usuário não digitar Enter para iniciar programa
    else:
    	print("===Enter não pressionado===\n!!Você digito:%s!!"%op1)