# PCB for Antenna Control and Sensor Interface
## What is the PCB Made For

The PCB designed for the antenna serves as a control card, providing essential functionality for the antenna system. It incorporates an STM32 microcontroller, six sensor inputs, and a CAN module for seamless communication with the host system. The antenna system is capable of detecting gases such as CO, CH4, and H2 using these sensors. Additionally, it can measure UV light intensity, airborne dust levels, and accurately determine air temperature and humidity. The STM32 processor reads and organizes the data from the sensors, which is then transmitted to the central control unit via the CAN module. From there, the data flows to the rover host (Nvidia Jetson TX2) and ultimately reaches the central control center with the assistance of Lora communication. The collected data is utilized for the projected thesis or other relevant purposes.

## PCB Description
The PCB designed for the antenna system exhibits a straightforward structure with the following features:

Sensor Inputs: The PCB provides six JST inputs for connecting the sensors. To ensure compatibility with the 3.3V operating voltage of the STM32 microcontroller, a voltage divider is implemented for sensor outputs that typically work with 5 volts.

Layer Structure: The PCB follows a 2-layer design. The first layer is dedicated to the 5V field, while the second layer is covered with the GND field, establishing a proper grounding structure.

Power Supply: Although the main power input to the PCB is 24V, a voltage regulator is employed to reduce the voltage to 5V, which is then supplied to the sensors. This ensures the sensors operate within their specified voltage range.

Interchangeability and Assembly: Instead of utilizing SMD components, the PCB is designed to accommodate female header pins, enabling easy assembly and interchangeability. This design choice allows the PCB to function as a basic breadboard and facilitates the placement of a ready-made STM32 Blue Pill module on it. 

As a result, the system can be used without the need for voltage level conversion from 5V to 3.3V for the STM32 microcontroller.
Please note that this is a summary of the key features of the antenna PCB. For more detailed technical specifications and information, please refer to the relevant documentation.


![Alt text](https://github.com/onurkarakoc79/METU-ROVER/blob/main/SCIENCE-CONTROL-UNIT/Science%20Control%20Unit%20Air%20Analysis%20Antenna%20PCB/Screenshots/Screenshot%20from%202023-07-14%2000-05-08.png)

![Alt text](https://github.com/onurkarakoc79/METU-ROVER/blob/main/SCIENCE-CONTROL-UNIT/Science%20Control%20Unit%20Air%20Analysis%20Antenna%20PCB/Screenshots/Screenshot%20from%202023-07-14%2000-05-01.png)
