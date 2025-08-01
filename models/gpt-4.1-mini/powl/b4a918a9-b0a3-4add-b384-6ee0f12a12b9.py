# Generated from: b4a918a9-b0a3-4add-b384-6ee0f12a12b9.json
# Description: This process outlines the comprehensive steps required to launch a vertical farming operation within an urban environment, integrating advanced hydroponic systems, AI-driven climate control, and community engagement initiatives. The process begins with site acquisition and feasibility analysis, followed by modular farm design and procurement of specialized equipment. Installation involves setting up climate sensors, nutrient delivery systems, and automated harvesting robots. Concurrently, regulatory compliance and sustainability certification are secured. Marketing strategies focus on local partnerships and transparent supply chain communication. Training programs for staff emphasize technology operation and crop management. The process concludes with pilot harvests, data-driven optimization, and phased scaling to meet urban food demands sustainably.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
SiteAcquire = Transition(label='Site Acquire')
FeasibilityCheck = Transition(label='Feasibility Check')
DesignFarm = Transition(label='Design Farm')
EquipmentOrder = Transition(label='Equipment Order')
InstallSensors = Transition(label='Install Sensors')
SetupHydroponics = Transition(label='Setup Hydroponics')
IntegrateAI = Transition(label='Integrate AI')
RobotDeploy = Transition(label='Robot Deploy')
ComplianceReview = Transition(label='Compliance Review')
CertifySustain = Transition(label='Certify Sustain')
LaunchMarketing = Transition(label='Launch Marketing')
PartnerOutreach = Transition(label='Partner Outreach')
StaffTraining = Transition(label='Staff Training')
PilotHarvest = Transition(label='Pilot Harvest')
DataOptimize = Transition(label='Data Optimize')
ScaleOperations = Transition(label='Scale Operations')

# Partial order for site acquisition and feasibility
po1 = StrictPartialOrder(nodes=[SiteAcquire, FeasibilityCheck])
po1.order.add_edge(SiteAcquire, FeasibilityCheck)

# Partial order for design and equipment procurement
po2 = StrictPartialOrder(nodes=[DesignFarm, EquipmentOrder])
po2.order.add_edge(DesignFarm, EquipmentOrder)

# Partial order for installation sequence
install_nodes = [
    InstallSensors,
    SetupHydroponics,
    IntegrateAI,
    RobotDeploy
]
po3 = StrictPartialOrder(nodes=install_nodes)
po3.order.add_edge(InstallSensors, SetupHydroponics)
po3.order.add_edge(SetupHydroponics, IntegrateAI)
po3.order.add_edge(IntegrateAI, RobotDeploy)

# Partial order for regulatory and certification - concurrent
reg_cert = StrictPartialOrder(nodes=[ComplianceReview, CertifySustain])

# Partial order for marketing
marketing = StrictPartialOrder(nodes=[LaunchMarketing, PartnerOutreach])
marketing.order.add_edge(LaunchMarketing, PartnerOutreach)

# Training alone (no order)
training = StaffTraining

# Partial order for final phase
final_phase = StrictPartialOrder(nodes=[PilotHarvest, DataOptimize, ScaleOperations])
final_phase.order.add_edge(PilotHarvest, DataOptimize)
final_phase.order.add_edge(DataOptimize, ScaleOperations)

# Combine installation and regulatory/concurrent activities in partial order (concurrent)
install_and_reg = StrictPartialOrder(nodes=[po3, reg_cert])
# No order edges between po3 and reg_cert to allow concurrency

# Combine marketing and training in parallel (concurrent)
marketing_training = StrictPartialOrder(nodes=[marketing, training])
# No order edges for concurrency

# Combine installation+regulatory and marketing+training in parallel
mid_phase = StrictPartialOrder(nodes=[install_and_reg, marketing_training])
# No order edges - concurrent

# Combine all phases with dependencies:
# site and feasibility --> design and equipment --> mid_phase --> final_phase

root = StrictPartialOrder(
    nodes=[po1, po2, mid_phase, final_phase]
)
root.order.add_edge(po1, po2)
root.order.add_edge(po2, mid_phase)
root.order.add_edge(mid_phase, final_phase)