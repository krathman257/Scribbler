# authors
# Kyle Rathman
# Kendall Black
# 4-29-2020

from controller import Robot, Pen
import math

#Initialize variables
TIME_STEP = 64
MAX_SPEED = 7

#Create Robot instance
robot = Robot()

#Initialize devices
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']

for i in range(4):
    wheels.append(robot.getMotor(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)

pen = Pen('pen')
pen.write(True)

ticker = 0

#Feedback loop: Step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:

    #Calculate cosine wave, step ticker
    motorAngle = math.cos(ticker/10)
    ticker += 1

    #Initialize motor speeds
    leftSpeed = 0.5 * MAX_SPEED
    rightSpeed = 0.5 * MAX_SPEED

    #If between threshold, scribble
    if ticker > 32 and ticker < 285:
        leftSpeed += -1 * motorAngle * 0.5 * MAX_SPEED
        rightSpeed += motorAngle * 0.5 * MAX_SPEED
    if ticker > 320:
        #brake robot
        for wheel in wheels:
            wheel.setVelocity(0)
        #break loop
        break

    #Write motor speeds
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
