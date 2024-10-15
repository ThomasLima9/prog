 programa para determinar a carteira de menor risco usando 
% o modelo da media variancia de Markowitz
clc  % limpa a tela
clear all % apaga as variaveis da workspace
close all

% matriz de retorno%s dos dados historicos de A1 e A2
%X=[6 8;2 -2]; % as colunas de X sao os retornos de A1 e A2

% matriz de retornos com correlacao -1 entre os ativos A1 e A2
%X=[6 -8;4 -2]; % as colunas de X sao os retornos de A1 e A2

% matriz de retornos com correlacao dif de 1 e -1 entre os ativos A1 e A2
X=[-2 4;4 8;5 3]; % as colunas de X sao os retornos de A1 e A2


Q=cov(X,1);  % matriz de covariancias dos retornos dados
[m,n]=size(X); % numero de periodos dos retornos
X0=zeros(n,1);

%[X, OBJ, INFO, LAMBDA] = qp (X0, H, q, A, B, LB, UB) chamada da rotina qp
[Car_ot,Sc]=qp(X0,2*Q,[],ones(1,n),1,zeros(n,1),[]); % Car_ot e' a carteira
% otima e Sc é o risco da carteira otima


% abaixo plotar carteiras individuais e carteira otima

Rma=(sum(X)')/n;  % retorno medio dos ativos Ai para i=1,2,...,n
Sa=sqrt(diag(Q)); % Risco dos ativos Ai para i=1,2,...,n
Rc=Rma'*Car_ot;  % retorno da carteira

for i=1:n
  plot(Sa(i,:),Rma(i,:),"r*")  % plota carteira investindo 100% em Ai
  hold on
  pause
end
  plot(sqrt(Sc),Rc,'b*')   % plota carteira otima
  pause
% proximo passo plotar fronteira eficiente
k=0.9;
while k >= 0.1
  Ck = k*Rma(1)+(1-k)*Rma(2); % carteira investindo k em A1 e (1-k) em A2
  Sk = sqrt(k^2*Q(1,1)+(1-k)^2*Q(2,2)+2*k*(1-k)*Q(1,2)); % idem para o risco 
  plot(Sk,Ck,'m+')
  pause
  k = k-0.1;
end
