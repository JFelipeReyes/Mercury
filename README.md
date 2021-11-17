# CFJ Explorer
In this repository you can find all the relevant information for the development of this project, we have made use of the Python language to develop a client-server communication and through this execute the different functions that allow the movement of the device, and the native library of Linux motion to transmit what is captured by the camera through a port of the IP assigned to the Raspberry Pi.

## What's the use?

La idea del desarrollo del proyecto es poder explorar lugares estrechos no menores a 17 cm de alto y 15 de ancho ya que el dispositivo cuenta con una cámara montada en el chasis, con la cual se puede monitorear la ubicación del dispositivo y posibles obstáculos con los que pueda encontrarse.

## How to use?

Steps to use the device :
1) Connect the Raspberry Pi to the power supply (Powerbank).
2) Connect the L298n diver to the Lipo battery.
3) Using the Linux terminal access the Raspberry Pi using SSH :
pi@ASSIGNED_IP.
4) Execute the Server.py file in the path it is stored:

```
  $ python3 Server.py
```

5) In the Linux terminal of the device that will act as a client, run the file Client.py:

```
  $ python3 Cliente.py
```

It is time to control the device:
The Client.py file runs a keylogger that detects the characters entered and sends a message that the Server.py file decodes and executes as a function.

W - This letter sends the command to advance to 25% power.

S - This letter sends the backward command at 25% power.

A - This letter sends the command to turn left at 40% power.

S - This letter sends the command to turn right at 40% power.

Q - This letter sends the command to stop.

Y - This letter sends the command to go forward at 100% power.

H - This letter sends the command to reverse at 100% power.

K - This letter disables the Server.

The power of the device is limited because in the transmission of the camera there is a delay of at least 0.5 seconds, therefore, by giving full power to the motors it is not possible to know with certainty the position of the device.


## How to install it?

* Download the APK of the application, go to the file manager to find the APK previously downloaded (if it is the first time you are going to install an APK from the file manager it will ask for permissions to do the installation, follow the steps that appear on the screen), at the end of the installation go to the main screen to start the application.

![APP](https://i.imgur.com/hbXglhE.jpg)

* Para visualizar la comunicación serial se utilizo la aplicación "Bluetooth SPP".

![Bluetooth SPP](https://i.imgur.com/JQsUVjX.jpg)



##  Information about PIC16F15244 Curiosity Nano Evaluation Kit

![PIC16F15244](https://i.imgur.com/DyVkeEG.jpg?1)

* [PIC16F15244](https://www.microchip.com/wwwproducts/en/PIC16F15244).

* [PIC16F15244 Curiosity Nano Evaluation Kit](https://www.microchip.com/Developmenttools/ProductDetails/EV09Z19A).

* [PIC16F15244 Curiosity Nano Hardware User Guide](https://ww1.microchip.com/downloads/en/DeviceDoc/PIC16F15244-Curiosity-Nano-Hardware-User-Guide-DS50003045A.pdf).

* [PIC16F15244 Curiosity Nano Schematics](https://ww1.microchip.com/downloads/en/DeviceDoc/PIC16F15244_Curiosity_Nano_Schematics.pdf).

* [PIC16F15244 Curiosity Nano Design Documentation](https://ww1.microchip.com/downloads/en/DeviceDoc/PIC16F15244_Curiosity_Nano_Design_Documentation.zip).

* [PIC16F15244 Curiosity Nano Altium Project](https://ww1.microchip.com/downloads/en/DeviceDoc/PIC16F15244_Curiosity_Nano_Altium_Project.zip).

## Software

* This MPU operates with the compiler [XC8](http://ww1.microchip.com/downloads/en/DeviceDoc/MPLAB_XC8_C_Compiler_User_Guide_for_PIC.pdf)of microchip.

* [MPLAB-X-IDE](https://www.microchip.com/en-us/development-tools-tools-and-software/mplab-x-ide).

* [Code Configurator](https://www.microchip.com/en-us/development-tools-tools-and-software/embedded-software-center/mplab-code-configurator).

*[Data Visualizer](https://www.microchip.com/en-us/development-tools-tools-and-software/embedded-software-center/mplab-data-visualizer).

## Schematic circuit
![Schematic circuit](https://i.imgur.com/u8DykT3.jpg)
