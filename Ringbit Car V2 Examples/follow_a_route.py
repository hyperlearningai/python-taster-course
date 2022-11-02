# Initialise the wheels
RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)

# Move forwards
RingbitCar.forward()

# Define the custom instructions in a custom function
def on_forever():

    # Left infrared sensor detects deviation from the black line.
    # Stop the right wheel and slow the left wheel in order to turn.
    if RingbitCar.tracking(RingbitCar.TrackingStateType.TRACKING_STATE_2):
        RingbitCar.freestyle(50, 0)
        basic.pause(100)

    # Right infrared sensor detects deviation from the black line.
    # Stop the left wheel and slow the right wheel in order to turn.
    if RingbitCar.tracking(RingbitCar.TrackingStateType.TRACKING_STATE_1):
        RingbitCar.freestyle(0, 50)
        basic.pause(100)

    # Normal moving speed
    RingbitCar.freestyle(100, 100)

# Run the function body continuously in an event-based forever loop
# Reference: https://makecode.microbit.org/reference/basic/forever
basic.forever(on_forever)

