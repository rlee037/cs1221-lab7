# lab 7 part 1

import time
import spidev

def createSPI(device):
  spi = spidev.SpiDev()    # Create the SPI object
  spi.open(0, device)      # Open the SPI object on bus 0 for the specified device (CE)
  spi.max_speed_hz=1000000 # Set the max speed to 1 MHz
  spi.mode = 0             # Set the mode to 0 (master)
  return spi

_numVals = 0
_mean    = 0
_s       = 0
def WelfordsAlgorithm(newVal):
  # computes running average
  global _numVals
  global _mean
  global _s
  _numVals += 1
  if _numVals == 1:
    _mean = newVal
    _s    = 0
  else:
    _oldMean = _mean
    _mean    = _oldMean + (newVal - _oldMean) / _numVals
    _s       = _s + ((newVal - _oldMean) * (newVal - _mean))
  return _mean


if __name__ == '__main__':
  try:
    spi1 = createSPI(0)
    spi2 = createSPI(1)
    while True:
      newLightValue = spi1.readbytes(1)             # Receive data from microcontroller 1
      print(newLightValue[0])
      average = WelfordsAlgorithm(newLightValue[0]) # Calculate running average using Welford's algorithm
      send = []
      send.append(average)
      spi2.xfer(send)                               # Send new value to microcontroller 2
      time.sleep(1)                                 # Delay for 1 second
  except KeyboardInterrupt:
      # Close all open SPI (spi.close())
      spi1.close()
      spi2.close()
      exit()


