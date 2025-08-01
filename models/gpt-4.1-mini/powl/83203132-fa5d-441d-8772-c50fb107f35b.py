# Generated from: 83203132-fa5d-441d-8772-c50fb107f35b.json
# Description: This process outlines the end-to-end setup of an urban vertical farming facility designed to maximize crop yield in limited city spaces by integrating hydroponics, automated climate control, and renewable energy sources. It begins with site analysis and ends with real-time monitoring system deployment. The workflow includes critical steps such as equipment sourcing, nutrient solution formulation, and staff training for operational efficiency. Uniquely, it incorporates waste recycling loops from local restaurants as organic input and engages with city planners for regulatory compliance. This atypical business process blends agriculture, technology, and sustainability to meet growing urban food demands while minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
PermitObtain = Transition(label='Permit Obtain')
SupplierVetting = Transition(label='Supplier Vetting')
EquipmentOrder = Transition(label='Equipment Order')
InstallRacks = Transition(label='Install Racks')
SetupLighting = Transition(label='Setup Lighting')
NutrientMix = Transition(label='Nutrient Mix')
WaterTesting = Transition(label='Water Testing')
ClimateConfig = Transition(label='Climate Config')
WasteIntake = Transition(label='Waste Intake')
SystemIntegration = Transition(label='System Integration')
StaffTraining = Transition(label='Staff Training')
TrialGrowth = Transition(label='Trial Growth')
ComplianceCheck = Transition(label='Compliance Check')
LaunchMonitor = Transition(label='Launch Monitor')
DataLogging = Transition(label='Data Logging')

# Waste recycling loop:
# Loop body: WasteIntake (B) and then SystemIntegration (A)
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[SystemIntegration, WasteIntake])

# Setup phase partial order after equipment order:
# Install Racks, Setup Lighting, Nutrient Mix, Water Testing, Climate Config are partially concurrent after EquipmentOrder
setup_nodes = [InstallRacks, SetupLighting, NutrientMix, WaterTesting, ClimateConfig]

setup_PO = StrictPartialOrder(nodes=setup_nodes)
# No order edges inside setup => all concurrent

# NutrientMix and WaterTesting can be considered order-free but usually NutrientMix before WaterTesting is logical,
# but since no explicit order given, leave unordered.

# StaffTraining must follow SystemIntegration
# TrialGrowth follows StaffTraining
# ComplianceCheck and LaunchMonitor follow TrialGrowth
# ComplianceCheck and LaunchMonitor can be concurrent or sequential.
# DataLogging after LaunchMonitor and ComplianceCheck.

# Build partial order

nodes = [
    SiteSurvey,
    DesignLayout,
    PermitObtain,
    SupplierVetting,
    EquipmentOrder,
    waste_loop,
    *setup_nodes,
    StaffTraining,
    TrialGrowth,
    ComplianceCheck,
    LaunchMonitor,
    DataLogging
]

root = StrictPartialOrder(nodes=nodes)

# Orders (dependencies):

# Start: Site Survey --> Design Layout --> Permit Obtain
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, PermitObtain)

# Permit Obtain --> Supplier Vetting
root.order.add_edge(PermitObtain, SupplierVetting)

# Supplier Vetting --> Equipment Order
root.order.add_edge(SupplierVetting, EquipmentOrder)

# Equipment Order --> Setup phase (Install Racks, Setup Lighting, Nutrient Mix, Water Testing, Climate Config)
for setup_node in setup_nodes:
    root.order.add_edge(EquipmentOrder, setup_node)

# Setup phase --> Waste Loop and Staff Training depends on SystemIntegration which is after WasteIntake loop

# Waste Loop depends on WasteIntake (loop) and SystemIntegration
# waste_loop = LOOP(SystemIntegration (A), WasteIntake (B))

# EquipmentOrder --> waste_loop (waste recycling from restaurants), assumed after equipment ordered
root.order.add_edge(EquipmentOrder, waste_loop)

# Wait for both SystemIntegration and setup before Staff Training
# Since SystemIntegration is part of waste_loop, and setup phase nodes all must complete before Staff Training
# To encode concurrency between setup and waste_loop before StaffTraining,
# add edges from last activities to StaffTraining.

# Constraints:
# Staff Training after SystemIntegration and after all setup nodes
root.order.add_edge(waste_loop, StaffTraining)
for setup_node in setup_nodes:
    root.order.add_edge(setup_node, StaffTraining)

# Staff Training --> Trial Growth
root.order.add_edge(StaffTraining, TrialGrowth)

# Trial Growth --> Compliance Check and Launch Monitor (choice or concurrency? Assume concurrency)
root.order.add_edge(TrialGrowth, ComplianceCheck)
root.order.add_edge(TrialGrowth, LaunchMonitor)

# Compliance Check and Launch Monitor --> Data Logging
root.order.add_edge(ComplianceCheck, DataLogging)
root.order.add_edge(LaunchMonitor, DataLogging)