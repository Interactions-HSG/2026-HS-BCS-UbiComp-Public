# Part 1: The right way to sleep

## Task 1

### 1. Estimation of the power consumption

**_Example response_**
1. Estimation of the average current draw during the awake cycle (5s):
- The accelerometer is active and sampling data every 100ms.
- The NRF radio is advertising continuously with a tight interval of 30ms.
- Based on the hardware specifications, here are the estimated current draws:
  - Accelerometer active:... mA
  - NRF radio advertising:... mA
- Total average current draw during the awake cycle: ... mA

2. Estimation of the average current draw during the sleep cycle (5s):
- The accelerometer is turned off.
- The NRF radio is not advertising.
- Based on the hardware specifications, here are the estimated current draws:
  - Accelerometer off: 
  - NRF radio off: 
- Total average current draw during the sleep cycle:  mA

3. Estimation of the overall average current draw over a 10s cycle (5s awake + 5s asleep): 
- Average current draw = 
- Average current draw =  


### 2. Interpretation of the power consumption measurements
**_Example response_**

If the average current draw during the awake cycle is 10 mA and during the sleep cycle is 1 mA, then the overall average current draw over a 10s cycle would be:
- Average current draw = (10 mA * 5s + 1 mA * 5s) / 10s = (50 mAs + 5 mAs) / 10s = 55 mAs / 10s = 5.5 mA

Put screenshots of the current draw measurements in the report. Include the following information:
- The average current draw during the awake cycle (5s)
- The average current draw during the sleep cycle (5s)
- The overall average current draw over a 10s cycle (5s awake + 5s asleep)
(Store the screenshots in the `images` subdirectory.)

### 3. Question P1.Q1: How long would the CR2032 battery last in this scenario?
- The CR2032 battery has a typical capacity of 220 mAh.
- Using the overall average current draw calculated above, we can estimate the battery life as follows:

_(Focus on what happens during a cycle or sleep-wake and then estimate how many times this will happen during day/hour and then estimate battery life)_

## Task 2

### 1. Estimation of the power consumption

### 2. Interpretation of the power consumption measurements

### 3. Question P1.Q2: Why is the energy consumption not half of what you measured in P1.T1?

## Task 3

### 1. Estimation of the power consumption

### 2. Interpretation of the power consumption measurements

### 3. Question P1.Q3: (a) Is there a difference in sleep phase current and the current profile? If so why? (b) How long (days/months/years) will the CR2032 battery last if the puck is moved 10 times a day.