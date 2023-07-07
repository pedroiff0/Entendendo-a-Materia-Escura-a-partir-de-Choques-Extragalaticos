#<--28/02/2023
#<--graficos da saida do codigo do Dawson
#<--author: Pedro Henrique Rocha de Andrade

#importando bibliotecas para uso
import numpy as np #cálculos
import pandas as pd #leitura de dados
import matplotlib.pyplot as plt #plotagem de graficos


#definindo os arquivos que serão usados
local  = "/home/pedro/Documents/bolsa icj/"
dir_cat = local + "Resultados/"

files = []

#intervalo de massas de 1 pra 1
files.append('zh_1to1_b0_z_updated')
#files.append('zh_1to1_b0.5_z_updated') 
#files.append('zh_1to1_b1_z_updated')

#intervalo de massas de 1 pra 3
files.append('zh_1to3_b0_z_updated')
#files.append('zh_1to3_b0.5_z_updated') #parametro de impacto 0.5
#files.append('zh_1to3_b1_z_updated') #parametro de impacto 1

#intervalo de massas de 1 pra 10
files.append('zh_1to10_b0_z_updated')
#files.append('zh_1to10_b0.5_z_updated')
#files.append('zh_1to10_b1_z_updated')



#Nomeando as saídas do zuhone
out1 = [] 

out1.append('zh_1to1_b0_z.png')
out1.append('zh_1to3_b0_z.png')
out1.append('zh_1to10_b0_z.png')

#Nomeando as saídas da comparação do ZuHone com Dawson
out2 = []
out2.append('dw_1to1_b0_z.png')
out2.append('dw_1to3_b0_z.png')
out2.append('dw_1to10_b0_z.png')

out3 = []
out3.append('dw_1to1_b0_z_zoom.png')
out3.append('dw_1to3_b0_z_zoom.png')
out3.append('dw_1to10_b0_z_zoom.png')


#Definindo o tempo das colisões (menor separação em parsec)
CT=[1.32,1.20,1.04]

#Titulos dos gráficos
names=['1 para 1','1 para 3','1 para 10']


for i in range(0, len(files)): 

	print(files[i])

	filename = dir_cat + files[i] + '.txt'
	df = pd.read_csv(filename, sep='\t')

#plotando os graficos iniciais

#zoomplot
#xmin, xmax, ymin, ymax = 0, 1, 0, 3

	plt.scatter(df['age']-CT[i],df['sep.kpc'],c='red') #definindo o tipo do gráfico pra pontos (dispersão XY) na cor vermelha
	plt.plot([0, 0], [0, 3100], 'k-') #Plotando o gráfico
	plt.title(names[i]) #definindo o titulo
	plt.xlabel('tempo (Ganos)') #titulo do eixo x
	
	plt.ylabel('Separação (kpc)') #titulo do eixo y
	#plt.show() #mostrando o grafico
	plt.savefig(dir_cat + out1[i]) #salvando o grafico 
	plt.clf() #limpando os graficos
	
#comparação
	plt.scatter(df['age']-CT[i],df['sep.Mpc'],c='red') #ZuHone 
	plt.scatter(df['TSC0'],df['d.proj.out'],c='blue') #Dawson
	
	y_error = [df['TSC0.lower'], df['TSC0.upper']]  #margem de erro (Dawson)
	plt.errorbar(df['TSC0'],df['d.proj.out'], yerr=y_error, fmt='o')  #plotagem da barra de erro nos gŕaficos
	
#graficos finais 
	plt.title(names[i]) #definindo o titulo do grafico
	plt.xlabel('tempo (Ganos)') #identificando o eixo x
	plt.ylabel('Separação (Mpc)') #identificando o eixo y
	#plt.show() #mostrando o gráfico
	plt.savefig(dir_cat + out2[i]) #salvando o gŕafico
	plt.clf() #limpando 
	
#comparação zoom
	plt.scatter(df['age']-CT[i],df['sep.Mpc'],c='red') #ZuHone 
	plt.scatter(df['TSC0'],df['d.proj.out'],c='blue') #Dawson
	
	y_error = [df['TSC0.lower'], df['TSC0.upper']]  #margem de erro (Dawson)
	plt.errorbar(df['TSC0'],df['d.proj.out'], yerr=y_error, fmt='o')  #plotagem da barra de erro nos gŕaficos
	
#graficos finais 
	plt.title(names[i]) #definindo o titulo do grafico
	plt.xlabel('tempo (Ganos)') #identificando o eixo x
	plt.ylabel('Separação (Mpc)') #identificando o eixo y
	plt.ylim(0,3) #zoom 
	plt.xlim(0,1) #zoom
	#plt.show() #mostrando o gráfico
	plt.savefig(dir_cat + out3[i]) #salvando o gŕafico
	plt.clf() #limpando
