# Generated from: 5c0964cc-03e8-438b-9125-153d34538c78.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming facility within a densely populated city. It includes site selection based on sunlight and accessibility, modular system design for space optimization, installation of controlled environment agriculture technologies such as LED lighting and hydroponic systems, integration of IoT sensors for real-time monitoring of humidity, temperature, and nutrient levels, and development of automated irrigation and nutrient delivery schedules. The process further covers staff training for specialized urban farming techniques, implementation of waste recycling protocols, coordination with local suppliers for organic inputs, compliance with municipal agricultural regulations, and marketing strategies tailored for urban consumers. Finally, it involves continuous performance evaluation and system upgrades to maximize yield and sustainability in a challenging urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteSurvey = Transition(label='Site Survey')
LightAnalysis = Transition(label='Light Analysis')
SystemDesign = Transition(label='System Design')
TechInstall = Transition(label='Tech Install')
SensorSetup = Transition(label='Sensor Setup')
IrrigationPlan = Transition(label='Irrigation Plan')
NutrientMix = Transition(label='Nutrient Mix')
StaffTraining = Transition(label='Staff Training')
WasteProtocol = Transition(label='Waste Protocol')
SupplierSync = Transition(label='Supplier Sync')
RegulationCheck = Transition(label='Regulation Check')
MarketStudy = Transition(label='Market Study')
LaunchEvent = Transition(label='Launch Event')
PerformanceAudit = Transition(label='Performance Audit')
SystemUpgrade = Transition(label='System Upgrade')

# Build partial orders for the main flow components:

# Site selection branch: Site Survey -> Light Analysis
site_selection = StrictPartialOrder(nodes=[SiteSurvey, LightAnalysis])
site_selection.order.add_edge(SiteSurvey, LightAnalysis)

# System design branch: Light Analysis -> System Design
system_design = StrictPartialOrder(nodes=[LightAnalysis, SystemDesign])
system_design.order.add_edge(LightAnalysis, SystemDesign)

# Tech install branch: System Design -> Tech Install -> Sensor Setup
tech_install = StrictPartialOrder(nodes=[SystemDesign, TechInstall, SensorSetup])
tech_install.order.add_edge(SystemDesign, TechInstall)
tech_install.order.add_edge(TechInstall, SensorSetup)

# Irrigation and nutrient plans in parallel (can run concurrently)
irrigation_and_nutrient = StrictPartialOrder(nodes=[IrrigationPlan, NutrientMix])

# Staff training branch
staff_training = StrictPartialOrder(nodes=[StaffTraining])

# Waste protocol branch
waste_protocol = StrictPartialOrder(nodes=[WasteProtocol])

# Supplier sync branch
supplier_sync = StrictPartialOrder(nodes=[SupplierSync])

# Regulation check branch
regulation_check = StrictPartialOrder(nodes=[RegulationCheck])

# Market study branch
market_study = StrictPartialOrder(nodes=[MarketStudy])

# Launch event node (after all preparations)
launch_event = StrictPartialOrder(nodes=[LaunchEvent])

# Performance audit and system upgrade loop
perf_audit_upgrade_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[PerformanceAudit, SystemUpgrade]
)

# Compose partial order of all preparatory branches before launch

# Multiple preparatory branches can run concurrently after Sensor Setup:
# - Irrigation + Nutrient plans (parallel)
# - Staff Training
# - Waste Protocol
# - Supplier Sync
# - Regulation Check
# - Market Study

preparations = StrictPartialOrder(nodes=[
    irrigation_and_nutrient,
    staff_training,
    waste_protocol,
    supplier_sync,
    regulation_check,
    market_study
])

# "StrictPartialOrder" nodes can contain other STRICT partial orders or Operators or Transitions,
# so to add dependencies between compound nodes we treat them as single nodes.

# The order is: 
# SensorSetup --> all preparations (concurrent) --> LaunchEvent --> perf_audit_upgrade_loop (loop)

# root PO nodes: site_selection, system_design, tech_install, preparations, launch_event, perf_audit_upgrade_loop

# But site_selection and system_design overlap (LightAnalysis common),
# so we merge and keep dependencies correctly:

# Actually we link as:
# SiteSurvey --> LightAnalysis --> SystemDesign --> TechInstall --> SensorSetup --> preparations --> LaunchEvent --> loop

# Define main linear partial order nodes:
linear_nodes = [SiteSurvey, LightAnalysis, SystemDesign, TechInstall, SensorSetup]

linear_flow = StrictPartialOrder(nodes=linear_nodes)
linear_flow.order.add_edge(SiteSurvey, LightAnalysis)
linear_flow.order.add_edge(LightAnalysis, SystemDesign)
linear_flow.order.add_edge(SystemDesign, TechInstall)
linear_flow.order.add_edge(TechInstall, SensorSetup)

# Now the root node includes:
# linear_flow, preparations (collection of 6 parallel branches), launch_event, and perf_audit_upgrade_loop

# collect all prep branch nodes individually for the root, since we need to add edges from SensorSetup to each:

prep_branches = [
    irrigation_and_nutrient,
    staff_training,
    waste_protocol,
    supplier_sync,
    regulation_check,
    market_study
]

all_nodes = [linear_flow] + prep_branches + [launch_event, perf_audit_upgrade_loop]

root = StrictPartialOrder(nodes=all_nodes)

# add linear flow order edges within linear_flow are already set internally,
# now add dependency from linear_flow -> all prep branches
for prep in prep_branches:
    root.order.add_edge(linear_flow, prep)

# all prep branches must complete before launch event
for prep in prep_branches:
    root.order.add_edge(prep, launch_event)

# Launch event before loop
root.order.add_edge(launch_event, perf_audit_upgrade_loop)