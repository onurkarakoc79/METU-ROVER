# Metu Rover Soil Analysis PCB

## What the PCB is Designed For

The Soil Analysis Box is a crucial component of the Analysis Unit and is responsible for conducting soil analysis on the Metu Rover. The PCB (Printed Circuit Board) described here plays a significant role in controlling and managing various components within the Soil Analysis Box. The key features and functionalities of the Soil Analysis Box are as follows:

Drilling Mechanism: The box includes a driller for digging into the soil.

Vibration Motors: Four small vibration motors and three bmp280 pressure sensors are used to sift the earth and collect soil samples.

Servo Motors: Five servo motors are employed to pour certain chemicals into test tubes.

Stepper Motors: Five small stepper motors and one large stepper motor (Nema23) are used for precise movements and control.

Sensors: The analysis box incorporates three weight sensors, one soil moisture sensor, one temperature sensor, and three bmp280 pressure sensors to measure various soil properties

STM32 Microcontrollers: Two STM32 microcontrollers are utilized for faster processing and pin management. They are connected via UART communication protocol.

Data Transmission: The PCB facilitates the transmission of collected data from sensors to the main computer and subsequently to the base for further analysis.

Motor Control: The PCB determines the operating time of the motors and controls the number of steps the stepper motors will run.

## PCB Description

The PCB design takes into consideration the challenges associated with mounting SMD components and ensures easy replacement of the STM32 Blue Pill boards. The following key aspects are associated with the PCB design:

Dual STM32 Configuration: Two STM32 microcontrollers are utilized to distribute processing load and overcome pin shortage. UART communication is established between the two microcontrollers, with one acting as the primary communicator with the host while waking up the other for specific tasks.

Sensor Readings and Communication: The primary STM32 continuously reads data from the sensors and facilitates communication with the computer. It ensures a steady flow of information between the PCB and the host.

Motor Control: The secondary STM32, which is in a sleep state most of the time for power-saving purposes, determines the operating timing of the motors and controls the steps taken by the stepper motors.

Power and Ground Layers: The PCB consists of two layers, with the top layer dedicated to 5V, 3.3V, and VCC (24V) areas. The bottom layer is entirely covered by the GND line.

Power Supply: The PCB includes a voltage regulator to step down the primary 24V power input to 5V for the necessary sensors. The STM32's internal regulator provides the 3.3V line.

Communication: The PCB utilizes the CAN (Controller Area Network) module for communication with the host.

Motor Control and Integration: Vibration motors are controlled using transistors, while four stepper motor drivers are integrated directly into the circuit. Additionally, an external stepper driver stm is employed to activate the Nema23 large stepper motor.
Please note that this is a high-level overview of the Metu Rover Soil Analysis PCB. For more detailed information and technical specifications, please refer to the relevant documentation.

![Alt text](https://github.com/onurkarakoc79/METU-ROVER/blob/main/SCIENCE-CONTROL-UNIT/Science%20Control%20Unit%20Soil%20Analysis%20PCB/Screenshot%20from%202023-07-13%2023-53-51.png)
![Alt text]((https://github.com/onurkarakoc79/METU-ROVER/blob/main/SCIENCE-CONTROL-UNIT/Science%20Control%20Unit%20Soil%20Analysis%20PCB/Screenshot%20from%202023-07-13%2023-54-03.png)https://github.com/onurkarakoc79/METU-ROVER/blob/main/SCIENCE-CONTROL-UNIT/Science%20Control%20Unit%20Soil%20Analysis%20PCB/Screenshot%20from%202023-07-13%2023-54-03.png)
