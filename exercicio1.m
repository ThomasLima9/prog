# . exercicio da aula 1 de modelos  
# calcular os retornos e os riscos de 2 ativoes e depois formar uma carteira combinando 2 ativos,

A1=[2;4;-10;2;7;8]; #RETORNOS PASSADOS DO ATIVO 1
A2=[-3;7;0;-5;8;10]; #RETORNOS PASSADOS DO ATIVO 2
n= length(A1); #TAMANHO DO ATIVO 1
R1= sum(A1)/n; #RETORNO MEDIO DO ATIVO 1
R2= sum(A2)/n; #RETORNO MEDIO DO ATIVO 2
aux1 = (A1-R1).^2; #variavel auxiliar
v1 = sum(aux1)/n;  #variancia do ativo1
s1 = sqrt(v1);  # risco do ativo 1
###### PLOT DA CARTEIRA (RISCO ATIVO 1 E RISCO MEDIO DO ATIVO 1 ######
plot(s1,R1,'r*') # risco do ativo 1
hold on

aux2=(A2-R2).^2; # variavel auxiliar do ativo 2
v2 = sum(aux2)/n;  #variancia do ativo 2
s2 = sqrt(v2); # risco do ativo 2
plot(s2,R2,'b*')
aux3 = 0.5*(A1); #variavel auxiliar 50% do ativo1
aux4 = 0.5*(A2); #variavel auxiliar 50% do ativo2
rc = sum(aux3+aux4)/n; %Retorno da carteira comp com 50 porcento de cada ativo
vc = (sum((aux3-rc).^2+(aux4-rc).^2))/n; #Variancia da carteira composta
sc = sqrt(vc); #risco da carita composta por 50% de A1 e 50% de A2

######### PLOT DA CARTEIRA 50% DE A1 E 50% DE A2 E  RISCO DE 50% ATIVO1 E 50% ATIVO2 ######
plot(sc,rc,'m*')

###### outra maneira #################

aux5= 0.3*(A1); #variavel auxiliar 30% do ativo1
aux6 = 0.7*(A2); #variavel auxiliar 70% do ativo2

rc = sum(aux5+aux6)/n; %Retorno da carteira comp com 50 porcento de cada ativo
vc = (sum((aux5-rc).^2+(aux6-rc).^2))/n; #Variancia da carteira composta
sc = sqrt(vc); #risco da carita composta por 50% de A1 e 50% de A2
plot(sc,rc,'g*')

#############################################

aux5= 0.7*(A1); #variavel auxiliar 30% do ativo1
aux6 = 0.3*(A2); #variavel auxiliar 70% do ativo2

rc = sum(aux5+aux6)/n; %Retorno da carteira comp com 50 porcento de cada ativo
vc = (sum((aux5-rc).^2+(aux6-rc).^2))/n; #Variancia da carteira composta
sc = sqrt(vc); #risco da carita composta por 50% de A1 e 50% de A2
plot(sc,rc,'y*')
###################################################3

aux5= 0.6*(A1); #variavel auxiliar 30% do ativo1
aux6 = 0.4*(A2); #variavel auxiliar 70% do ativo2

rc = sum(aux5+aux6)/n; %Retorno da carteira comp com 50 porcento de cada ativo
vc = (sum((aux5-rc).^2+(aux6-rc).^2))/n; #Variancia da carteira composta
sc = sqrt(vc); #risco da carita composta por 50% de A1 e 50% de A2
plot(sc,rc,'c*')


