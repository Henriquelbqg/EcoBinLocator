import folium
import webbrowser

latitude_padrao = -8.0476
longitude_padrao = -34.8770

mapa = folium.Map(location=[latitude_padrao, longitude_padrao], zoom_start=12)

latitude1 = -8.08715
longitude1 = -34.8885
latitude2 = -8.02751
longitude2 = -34.9136
latitude3 = -8.03047
longitude3 = -34.9230
latitude4 = -8.03174
longitude4 = -34.9597
coordenadas_lixo1 = [latitude1, longitude1]
icon1 = folium.CustomIcon(icon_image='imagem_lixo.png', icon_size=(30, 30))
lixo1 = folium.Marker(coordenadas_lixo1, icon=icon1, popup='R. Manoel de Brito, 871')
lixo1.add_to(mapa)
coordenadas_lixo2 = [latitude2, longitude2]
icon2 = folium.CustomIcon(icon_image='imagem_lixo.png', icon_size=(30, 30))
lixo2 = folium.Marker(coordenadas_lixo2, icon=icon2, popup='Estr. do Arraial, 4469')
lixo2.add_to(mapa)
coordenadas_lixo3 = [latitude3, longitude3]
icon3 = folium.CustomIcon(icon_image='imagem_lixo.png', icon_size=(30, 30))
lixo3 = folium.Marker(coordenadas_lixo3, icon=icon3, popup='R. Silveira Lôbo, 32')
lixo3.add_to(mapa)
coordenadas_lixo4 = [latitude4, longitude4]
icon4 = folium.CustomIcon(icon_image='imagem_lixo.png', icon_size=(30, 30))
lixo4 = folium.Marker(coordenadas_lixo4, icon=icon4, popup='R. Gov. Leopoldo Neves, 271')
lixo4.add_to(mapa)

mapa.save('mapa_sem_endereco.html')

webbrowser.open('mapa_sem_endereco.html')