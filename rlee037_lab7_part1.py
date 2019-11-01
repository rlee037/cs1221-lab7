# lab 7 part 1

import time
import spidev

def createSPI(device):
  spi = spidev.SpiDev()    # Create the SPI object
  spi.open(0, device)      # Open the SPI object on bus 0 for the specified device (CE)
  spi.max_speed_hz=1000000 # Set the max speed to 1 MHz
  spi.mode = 0             # Set the mode to 0
  return spi

def WelfordsAlgorithm(val):
  # 
  return 1


if __name__ == '__main__':
  try:
    spi1 = createSPI(0)
    spi2 = createSPI(1)
    send = []
    while True:
      newLightValue = spi1.readbytes(1)          # Receive data from microcontroller 1
      average = WelfordsAlgorithm(newLightValue) # Calculate running average using Welford's algorithm
      send.append(average)
      spi2.xfer(send)                            # Send new value to microcontroller 2
      time.sleep(1)                              # Delay for 1 second
  except KeyboardInterrupt:
      # Close all open SPI (spi.close())
      spi1.close()
      spi2.close()
      exit()


