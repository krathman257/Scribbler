from controller import Robot
import math

#Time in milliseconds of a simulation step
TIME_STEP = 64

#Create Robot instance
robot = Robot()

#Initialize devices
ds = []
dsNames = ['ds_right', 'ds_left']

for i in range(2):
    ds.append(robot.getDistanceSensor(dsNames[i]))
    ds[i].enable(TIME_STEP)
    
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']

for i in range(4):
    wheels.append(robot.getMotor(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)

ticker = 0

#Feedback loop: Step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:

    #Step ticker
    motorAngle = math.cos(ticker/10)
    ticker += 1

    #Initialize motor speeds
    leftSpeed = 1.0
    rightSpeed = 1.0

    #If between threshold, calculate cosine wave
    if ticker > 32 and ticker < 224:
        leftSpeed += motorAngle * 0.5 * MAX_SPEED
        rightSpeed += -1 * motorAngle * 0.5 * MAX_SPEED

    #Write motor speeds
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
