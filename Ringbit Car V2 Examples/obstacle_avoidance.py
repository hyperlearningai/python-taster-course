# Initialise the sonar variable
sonar = 0

# Initialise the wheels
RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)

# Move forwards
RingbitCar.forward()

# Define the custom instructions in a custom function
def on_forever():

    # Read the distance (cm) to an object detected by the ultrasonic sensor 
    # that is connected to the 0VS GVS pin.
    # Store the distance in the global sonar variable.
    global sonar
    sonar = sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_CM, DigitalPin.P0)

    # If the distance to the object is less than 10cm and is not 0cm 
    # then avoid the object.
    # Otherwise continue to move forwards.
    if sonar < 10 and sonar != 0:
        RingbitCar.freestyle(0, 100)
        basic.pause(500)
    else:
        RingbitCar.forward()

# Run the function body continuously in an event-based forever loop
# Reference: https://makecode.microbit.org/reference/basic/forever
basic.forever(on_forever)

