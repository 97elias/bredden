from elias import *
from bintreeFile import *
from IndexlistQFile import *
from lab4_fan_gud import *

def main():
  map = MapEdges()
  
  # Program som skriver ut stadsnamnen och dess koordinater på min ö
  for city in map.cities:
    #print(city)
    pass #ta bort denna senare

  # Program som skriver ut index av staden givet dess namn
  index = map.getIndexFromCity('Advertisement')
  #print(index)


  breddenForstSokning('Ashdrift', 'Cullfield', map)


def breddenForstSokning(startstad, slutstad, map):
  # skapa en kö för att hålla reda på städer som ska undersökas
  startstadIndex = map.getIndexFromCity(startstad)
  slutstadIndex = map.getIndexFromCity(slutstad)
  queue = IndexlistQ() # gör en instans som en kö (lab4)
  queue.enqueue(startstadIndex) # lägg till startstaden i kön
  visitedCities = Bintree() # skapa en bintree för att hålla reda på besökta städer
  myTrip = Travel()
  i = 0
  while not queue.isEmpty() and i<500:
    i += 1
    nuvarande_stad = queue.dequeue()
    parentCity = City(startstad, nuvarande_stad) 
    #print(f'det här är nuvarande stad: {nuvarande_stad}')

    # Om vi har nått slutstaden, avsluta sökningen
    if nuvarande_stad == slutstadIndex:
      print('vi har nått slutstaden')
      slutstad = City(map.getCityName(nuvarande_stad), nuvarande_stad)
      return myTrip.writechain(slutstad)
    

    else:
      newCities = map.getNeighborsTo(nuvarande_stad)
      for city in newCities:
        if city in visitedCities:
          pass
        else:
          queue.enqueue(city)
          cityNode = City(map.getCityName(city), city)
          cityNode.parent = parentCity
          visitedCities.store(city)
      

      if queue.isEmpty():
        return False


main()