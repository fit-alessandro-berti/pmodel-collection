# Generated from: 3c7762ee-2ab3-4766-81d4-8485cd76115e.json
# Description: This process outlines the intricate steps involved in assembling custom drones tailored to specific client requirements. It begins with component selection based on desired drone capabilities, followed by intricate circuit integration and firmware customization. Quality checks ensure compliance with safety and performance standards, while iterative flight testing validates operational stability. The process also includes environmental resilience testing, packaging with personalized branding, and coordination with logistics for expedited delivery. Throughout, detailed documentation and client feedback loops optimize future iterations and enhance overall product reliability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities as transitions
Component_Pick = Transition(label='Component Pick')
Circuit_Mount = Transition(label='Circuit Mount')
Firmware_Flash = Transition(label='Firmware Flash')
Sensor_Align = Transition(label='Sensor Align')
Propeller_Fit = Transition(label='Propeller Fit')
Battery_Install = Transition(label='Battery Install')
Signal_Test = Transition(label='Signal Test')
Calibrate_Gyro = Transition(label='Calibrate Gyro')
Flight_Trial = Transition(label='Flight Trial')
Data_Log = Transition(label='Data Log')
Stress_Test = Transition(label='Stress Test')
Weather_Proof = Transition(label='Weather Proof')
Package_Drone = Transition(label='Package Drone')
Brand_Label = Transition(label='Brand Label')
Shipping_Prep = Transition(label='Shipping Prep')
Client_Review = Transition(label='Client Review')

# Quality checks after assembly: Signal Test and Calibrate Gyro in parallel
quality_checks = StrictPartialOrder(nodes=[Signal_Test, Calibrate_Gyro])

# Order within quality checks (no order, so concurrent)

# Flight Trial + Data Log loop (iterative testing and logging)
test_loop_body = StrictPartialOrder(nodes=[Flight_Trial, Data_Log])
test_loop_body.order.add_edge(Flight_Trial, Data_Log)

# Loop: execute test_loop_body, then choice to exit or repeat
# B in loop: do Data Log, here we will use Data_Log as B, and Flight_Trial as A
# But because loop is defined as *(A,B) = execute A then choose exit or execute B then A again
# So we can set 
# A = Flight Trial
# B = Data Log
loop_testing = OperatorPOWL(operator=Operator.LOOP, children=[Flight_Trial, Data_Log])

# Environmental resilience testing after quality checks and flight testing
env_resilience = StrictPartialOrder(nodes=[Stress_Test, Weather_Proof])
# Stress_Test and Weather_Proof are concurrent (no edges)

# Assembly order: Component Pick -> Circuit Mount -> Firmware Flash -> Sensor Align -> Propeller Fit -> Battery Install
assembly = StrictPartialOrder(nodes=[Component_Pick, Circuit_Mount, Firmware_Flash, Sensor_Align, Propeller_Fit, Battery_Install])

assembly.order.add_edge(Component_Pick, Circuit_Mount)
assembly.order.add_edge(Circuit_Mount, Firmware_Flash)
assembly.order.add_edge(Firmware_Flash, Sensor_Align)
assembly.order.add_edge(Sensor_Align, Propeller_Fit)
assembly.order.add_edge(Propeller_Fit, Battery_Install)

# After assembly, proceed to quality checks then loop_testing then environmental resilience
# We combine quality_checks, loop_testing, env_resilience with ordering edges

post_assembly = StrictPartialOrder(nodes=[quality_checks, loop_testing, env_resilience])
post_assembly.order.add_edge(quality_checks, loop_testing)
post_assembly.order.add_edge(loop_testing, env_resilience)

# Packaging with personalized branding: Package Drone then Brand Label (order)
packaging = StrictPartialOrder(nodes=[Package_Drone, Brand_Label])
packaging.order.add_edge(Package_Drone, Brand_Label)

# Shipping Prep after packaging
shipping = StrictPartialOrder(nodes=[Shipping_Prep])
# client review concurrent with shipping prep (feedback loop)

# Client Review concurrent with Shipping_Prep
post_packaging = StrictPartialOrder(nodes=[packaging, shipping, Client_Review])
post_packaging.order.add_edge(packaging, shipping)
# Client Review concurrent with shipping (no edge)

# Final model
# Assembly -> post_assembly -> post_packaging

root = StrictPartialOrder(
    nodes=[assembly, post_assembly, post_packaging]
)

root.order.add_edge(assembly, post_assembly)
root.order.add_edge(post_assembly, post_packaging)