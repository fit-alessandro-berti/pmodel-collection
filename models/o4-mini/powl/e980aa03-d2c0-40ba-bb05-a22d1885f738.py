# Generated from: e980aa03-d2c0-40ba-bb05-a22d1885f738.json
# Description: This process involves creating highly specialized drones tailored for environmental research missions. It begins with client consultation to define unique specifications, followed by custom component sourcing that requires vetting rare materials. The assembly phase incorporates precision calibration of sensors and propulsion systems, integrated software deployment, and rigorous flight testing in controlled environments. Post-assembly, the drone undergoes adaptive AI training based on mission parameters, final quality assurance checks, and packaging with mission-specific accessories. The process concludes with client training sessions and remote deployment support, ensuring the drone operates effectively in diverse and unpredictable field conditions. Continuous feedback loops help refine future builds and maintain long-term client satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
client_brief    = Transition(label='Client Brief')
spec_analysis   = Transition(label='Spec Analysis')
material_source = Transition(label='Material Sourcing')
component_vet   = Transition(label='Component Vetting')
frame_assembly  = Transition(label='Frame Assembly')
sensor_install  = Transition(label='Sensor Install')
propulsion_setup= Transition(label='Propulsion Setup')
calibration     = Transition(label='Calibration')
software_load   = Transition(label='Software Load')
flight_test     = Transition(label='Flight Test')
ai_training     = Transition(label='AI Training')
qa_review       = Transition(label='QA Review')
mission_pack    = Transition(label='Mission Pack')
client_train    = Transition(label='Client Training')
deployment_supp = Transition(label='Deployment Support')

# Silent transition for loop feedback
tau = SilentTransition()

# Define the main subprocess (A) from Spec Analysis through Deployment Support
A = StrictPartialOrder(nodes=[
    spec_analysis,
    material_source,
    component_vet,
    frame_assembly,
    sensor_install,
    propulsion_setup,
    calibration,
    software_load,
    flight_test,
    ai_training,
    qa_review,
    mission_pack,
    client_train,
    deployment_supp
])
# Sequential ordering inside A
A.order.add_edge(spec_analysis,   material_source)
A.order.add_edge(material_source, component_vet)
A.order.add_edge(component_vet,   frame_assembly)
A.order.add_edge(frame_assembly,  sensor_install)
A.order.add_edge(frame_assembly,  propulsion_setup)
A.order.add_edge(sensor_install,  calibration)
A.order.add_edge(propulsion_setup,calibration)
A.order.add_edge(calibration,     software_load)
A.order.add_edge(software_load,   flight_test)
A.order.add_edge(flight_test,     ai_training)
A.order.add_edge(ai_training,     qa_review)
A.order.add_edge(qa_review,       mission_pack)
A.order.add_edge(mission_pack,    client_train)
A.order.add_edge(client_train,    deployment_supp)

# Define the loop: after completion, either exit or take a silent step and repeat A
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, tau])

# Top‐level model: Client Brief followed by the loop
root = StrictPartialOrder(nodes=[client_brief, loop])
root.order.add_edge(client_brief, loop)