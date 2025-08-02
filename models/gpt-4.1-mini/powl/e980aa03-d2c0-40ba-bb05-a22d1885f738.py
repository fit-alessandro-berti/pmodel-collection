# Generated from: e980aa03-d2c0-40ba-bb05-a22d1885f738.json
# Description: This process involves creating highly specialized drones tailored for environmental research missions. It begins with client consultation to define unique specifications, followed by custom component sourcing that requires vetting rare materials. The assembly phase incorporates precision calibration of sensors and propulsion systems, integrated software deployment, and rigorous flight testing in controlled environments. Post-assembly, the drone undergoes adaptive AI training based on mission parameters, final quality assurance checks, and packaging with mission-specific accessories. The process concludes with client training sessions and remote deployment support, ensuring the drone operates effectively in diverse and unpredictable field conditions. Continuous feedback loops help refine future builds and maintain long-term client satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
ClientBrief = Transition(label='Client Brief')
SpecAnalysis = Transition(label='Spec Analysis')
MaterialSourcing = Transition(label='Material Sourcing')
ComponentVetting = Transition(label='Component Vetting')
FrameAssembly = Transition(label='Frame Assembly')
SensorInstall = Transition(label='Sensor Install')
PropulsionSetup = Transition(label='Propulsion Setup')
Calibration = Transition(label='Calibration')
SoftwareLoad = Transition(label='Software Load')
FlightTest = Transition(label='Flight Test')
AITraining = Transition(label='AI Training')
QAReview = Transition(label='QA Review')
MissionPack = Transition(label='Mission Pack')
ClientTraining = Transition(label='Client Training')
DeploymentSupport = Transition(label='Deployment Support')

# Stage 1: Client consultation and specification analysis (sequential)
stage1 = StrictPartialOrder(nodes=[ClientBrief, SpecAnalysis])
stage1.order.add_edge(ClientBrief, SpecAnalysis)

# Stage 2: Custom component sourcing workflow:
# Material Sourcing --> Component Vetting (sequential)
stage2 = StrictPartialOrder(nodes=[MaterialSourcing, ComponentVetting])
stage2.order.add_edge(MaterialSourcing, ComponentVetting)

# Stage 3: Assembly phase with some partial order and some concurrency
# Frame Assembly first
# Sensor Install and Propulsion Setup in parallel (no order between them)
# Then Calibration, Software Load, Flight Test in sequence
sensor_and_propulsion = StrictPartialOrder(nodes=[SensorInstall, PropulsionSetup])
# no edges -> concurrent

post_install_seq = StrictPartialOrder(nodes=[Calibration, SoftwareLoad, FlightTest])
post_install_seq.order.add_edge(Calibration, SoftwareLoad)
post_install_seq.order.add_edge(SoftwareLoad, FlightTest)

# Combine assembly partial orders:
# Frame Assembly --> sensor_and_propulsion (concurrent nodes)
# sensor_and_propulsion --> post_install_seq (Calibration...)
assembly_nodes = [FrameAssembly, sensor_and_propulsion, post_install_seq]

# Because sensor_and_propulsion and post_install_seq are StrictPartialOrder themselves we can treat them as nodes in a higher PO
assembly = StrictPartialOrder(nodes=assembly_nodes)
assembly.order.add_edge(FrameAssembly, sensor_and_propulsion)
assembly.order.add_edge(sensor_and_propulsion, post_install_seq)

# Stage 4: Post-assembly: AI Training --> QA Review --> Mission Pack (sequential)
post_assembly = StrictPartialOrder(nodes=[AITraining, QAReview, MissionPack])
post_assembly.order.add_edge(AITraining, QAReview)
post_assembly.order.add_edge(QAReview, MissionPack)

# Stage 5: Final: Client Training and Deployment Support (can be concurrent)
final_stage = StrictPartialOrder(nodes=[ClientTraining, DeploymentSupport])
# no edges -> concurrent

# Main sequential ordering between stages:
# stage1 --> stage2 --> assembly --> post_assembly --> final_stage

main_nodes = [stage1, stage2, assembly, post_assembly, final_stage]
root = StrictPartialOrder(nodes=main_nodes)
root.order.add_edge(stage1, stage2)
root.order.add_edge(stage2, assembly)
root.order.add_edge(assembly, post_assembly)
root.order.add_edge(post_assembly, final_stage)

# Feedback loop: Continuous feedback loops help refine future builds and maintain long-term client satisfaction.
# Model as a loop: from final_stage back to stage2 (component sourcing) representing refinement

root = OperatorPOWL(operator=Operator.LOOP, children=[root, stage2])