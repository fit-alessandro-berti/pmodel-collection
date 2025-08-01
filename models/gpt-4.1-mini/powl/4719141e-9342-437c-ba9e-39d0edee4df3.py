# Generated from: 4719141e-9342-437c-ba9e-39d0edee4df3.json
# Description: This process involves the design, customization, and assembly of bespoke drones tailored to specific client requirements. It includes initial consultation to determine unique operational needs, iterative prototype development, component sourcing from multiple suppliers, software customization, rigorous testing under various environmental conditions, regulatory compliance verification, and final quality assurance before delivery. Post-delivery support and firmware updates are also integrated into the process to ensure optimal performance and client satisfaction over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
ClientConsult = Transition(label='Client Consult')
NeedsAnalysis = Transition(label='Needs Analysis')
DesignDraft = Transition(label='Design Draft')
ComponentSourcing = Transition(label='Component Sourcing')
PrototypeBuild = Transition(label='Prototype Build')
SoftwareSetup = Transition(label='Software Setup')
FirmwareInstall = Transition(label='Firmware Install')
InitialTesting = Transition(label='Initial Testing')
DesignReview = Transition(label='Design Review')
ComplianceCheck = Transition(label='Compliance Check')
EnvironmentalTest = Transition(label='Environmental Test')
QualityAudit = Transition(label='Quality Audit')
FinalAssembly = Transition(label='Final Assembly')
ClientTraining = Transition(label='Client Training')
DeliverySchedule = Transition(label='Delivery Schedule')
PostSupport = Transition(label='Post Support')
FirmwareUpdate = Transition(label='Firmware Update')

# Loop to model iterative prototype development and possible repeated software setup, testing, review and re-design:
# Loop body:
#   B = 
#     PartialOrder(
#       nodes={ComponentSourcing, PrototypeBuild, SoftwareSetup, FirmwareInstall, InitialTesting, EnvironmentalTest, DesignReview, ComplianceCheck, QualityAudit},
#       with partial order reflecting the described control flow
#     )
#   A =
#     PartialOrder(nodes={DesignDraft}, order={})
# Loop = *(A, B)

# Construct B partial order for iterative development cycle
# Order:
# ComponentSourcing -> PrototypeBuild -> SoftwareSetup -> FirmwareInstall -> InitialTesting
# InitialTesting -> EnvironmentalTest -> DesignReview -> ComplianceCheck -> QualityAudit
# DesignReview -> SoftwareSetup (feedback loop within the loop body, to model redesign or fixes)
B_nodes = [
    ComponentSourcing,
    PrototypeBuild,
    SoftwareSetup,
    FirmwareInstall,
    InitialTesting,
    EnvironmentalTest,
    DesignReview,
    ComplianceCheck,
    QualityAudit,
]

B = StrictPartialOrder(nodes=B_nodes)
B.order.add_edge(ComponentSourcing, PrototypeBuild)
B.order.add_edge(PrototypeBuild, SoftwareSetup)
B.order.add_edge(SoftwareSetup, FirmwareInstall)
B.order.add_edge(FirmwareInstall, InitialTesting)
B.order.add_edge(InitialTesting, EnvironmentalTest)
B.order.add_edge(EnvironmentalTest, DesignReview)
B.order.add_edge(DesignReview, ComplianceCheck)
B.order.add_edge(ComplianceCheck, QualityAudit)
# Feedback edge to SoftwareSetup from DesignReview (review feedback)
B.order.add_edge(DesignReview, SoftwareSetup)

# A is just DesignDraft as preparation before iterative cycles
A = StrictPartialOrder(nodes=[DesignDraft])

loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# After loop, next steps are final assembly, client training, delivery schedule
# plus post support and firmware update possibly concurrent after delivery

# Partial order after the loop:
# loop --> FinalAssembly --> ClientTraining --> DeliverySchedule
# DeliverySchedule --> XOR(PostSupport, FirmwareUpdate)
PostSupport_FirmwareUpdate = OperatorPOWL(operator=Operator.XOR, children=[PostSupport, FirmwareUpdate])

post_delivery_PO = StrictPartialOrder(
    nodes=[FinalAssembly, ClientTraining, DeliverySchedule, PostSupport_FirmwareUpdate]
)
post_delivery_PO.order.add_edge(FinalAssembly, ClientTraining)
post_delivery_PO.order.add_edge(ClientTraining, DeliverySchedule)
post_delivery_PO.order.add_edge(DeliverySchedule, PostSupport_FirmwareUpdate)

# Front part partial order: Client Consult -> Needs Analysis -> loop
front_PO = StrictPartialOrder(nodes=[ClientConsult, NeedsAnalysis, loop])
front_PO.order.add_edge(ClientConsult, NeedsAnalysis)
front_PO.order.add_edge(NeedsAnalysis, loop)

# Combine front_PO and post_delivery_PO in a top-level partial order
root = StrictPartialOrder(
    nodes=[ClientConsult, NeedsAnalysis, loop, FinalAssembly, ClientTraining, DeliverySchedule, PostSupport_FirmwareUpdate]
)

# Add edges for front portion
root.order.add_edge(ClientConsult, NeedsAnalysis)
root.order.add_edge(NeedsAnalysis, loop)

# Add edges for post loop portion
root.order.add_edge(loop, FinalAssembly)
root.order.add_edge(FinalAssembly, ClientTraining)
root.order.add_edge(ClientTraining, DeliverySchedule)
root.order.add_edge(DeliverySchedule, PostSupport_FirmwareUpdate)