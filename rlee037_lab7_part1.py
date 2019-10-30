# lab 7 part 1

import spidev

def createSPI(device):
  # Create the SPI object
  # Open the SPI object on bus 0 for the specified device (CE)
  # Set the max speed to 1 MHz
  spi.max_speed_hz=1000000
  # Set the mode to 0
  spi.mode = 0
  return spi

def WelfordsAlgorithm(val):
  # pp

if __name__ == '__main__':
  try:
    while True:
      # Receive data from microcontroller 1
      # Calculate running average using Welford's algorithm
      average = WelfordsAlgorithm(newLightValue)
      # Send new value to microcontroller 2
      # Delay for 1 second
  except KeyboardInterrupt:
      # Close all open SPI (spi.close())
      exit()


