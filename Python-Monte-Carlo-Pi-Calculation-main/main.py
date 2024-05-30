import montecarlo as mc

circle_radius = 300 #radio del circulo en pixeles
window = (1200,1000) #resolucion de la pantalla
points = 1000000 #numero total de puntos a mostrar

montecarlo_simulation = mc.MonteCarlo(window, circle_radius, points)
montecarlo_simulation.loop()