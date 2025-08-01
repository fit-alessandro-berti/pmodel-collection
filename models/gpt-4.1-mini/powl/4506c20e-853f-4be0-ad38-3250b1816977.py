# Generated from: 4506c20e-853f-4be0-ad38-3250b1816977.json
# Description: This process involves the bespoke assembly of drones tailored to unique client specifications. It begins with detailed requirement gathering followed by prototype design and component sourcing from specialized suppliers. Each drone undergoes precision frame construction, intricate wiring, and sensor calibration. Software integration and flight algorithm customization follow, requiring iterative testing and real-time adjustments. Quality assurance includes environmental stress testing and safety certification. The final steps cover packaging, client training, and post-delivery support to ensure optimal drone operation under varied conditions and use cases.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Requirement_Analysis = Transition(label='Requirement Analysis')
Prototype_Design = Transition(label='Prototype Design')
Component_Sourcing = Transition(label='Component Sourcing')
Frame_Assembly = Transition(label='Frame Assembly')
Wiring_Setup = Transition(label='Wiring Setup')
Sensor_Calibration = Transition(label='Sensor Calibration')
Software_Loading = Transition(label='Software Loading')
Algorithm_Tuning = Transition(label='Algorithm Tuning')
Flight_Testing = Transition(label='Flight Testing')
Stress_Testing = Transition(label='Stress Testing')
Safety_Review = Transition(label='Safety Review')
Packaging_Prep = Transition(label='Packaging Prep')
Client_Training = Transition(label='Client Training')
Delivery_Scheduling = Transition(label='Delivery Scheduling')
Support_Setup = Transition(label='Support Setup')

# Loop for iterative testing and adjustment:
# Loop body: Algorithm_Tuning (B)
# Loop do part: Flight_Testing and adjustments cycle represented by Algorithm_Tuning
# So a loop executing Flight_Testing and real-time adjustments modeled as (A=Flight_Testing, B=Algorithm_Tuning)
# According to the description, first execute Flight_Testing, then choose to exit or execute Algorithm_Tuning then Flight_Testing again.
test_loop = OperatorPOWL(operator=Operator.LOOP, children=[Flight_Testing, Algorithm_Tuning])

# Quality assurance activities sequentially: Stress_Testing, Safety_Review
quality_assurance = StrictPartialOrder(nodes=[Stress_Testing, Safety_Review])
quality_assurance.order.add_edge(Stress_Testing, Safety_Review)

# Final delivery steps including packaging, training, delivery scheduling and support setup.
final_steps = StrictPartialOrder(
    nodes=[Packaging_Prep, Client_Training, Delivery_Scheduling, Support_Setup]
)
final_steps.order.add_edge(Packaging_Prep, Client_Training)
final_steps.order.add_edge(Client_Training, Delivery_Scheduling)
final_steps.order.add_edge(Delivery_Scheduling, Support_Setup)

# Assembly steps partial order: Frame_Assembly, Wiring_Setup, Sensor_Calibration (concurrent)
assembly = StrictPartialOrder(
    nodes=[Frame_Assembly, Wiring_Setup, Sensor_Calibration]
)
# No order edges mean these three can be done concurrently

# Ordering the main process:
# Requirement Analysis -> Prototype Design -> Component Sourcing ->
# Assembly (Frame/Wire/Sensor) ->
# Software Loading ->
# Loop (Flight Testing and Algorithm Tuning) ->
# Quality Assurance (Stress Testing, Safety Review) ->
# Final Steps (Packaging, Client Training, Delivery Scheduling, Support Setup)

root = StrictPartialOrder(
    nodes=[
        Requirement_Analysis,
        Prototype_Design,
        Component_Sourcing,
        assembly,
        Software_Loading,
        test_loop,
        quality_assurance,
        final_steps,
    ]
)

root.order.add_edge(Requirement_Analysis, Prototype_Design)
root.order.add_edge(Prototype_Design, Component_Sourcing)
root.order.add_edge(Component_Sourcing, assembly)
root.order.add_edge(assembly, Software_Loading)
root.order.add_edge(Software_Loading, test_loop)
root.order.add_edge(test_loop, quality_assurance)
root.order.add_edge(quality_assurance, final_steps)