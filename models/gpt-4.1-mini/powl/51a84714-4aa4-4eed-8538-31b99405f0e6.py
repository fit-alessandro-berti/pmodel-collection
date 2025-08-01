# Generated from: 51a84714-4aa4-4eed-8538-31b99405f0e6.json
# Description: This process describes the complex setup and operational launch of an urban vertical farm integrating hydroponics, IoT monitoring, and sustainable energy systems. It involves site analysis, modular infrastructure assembly, nutrient solution formulation, environmental calibration, and continuous crop monitoring. The process also includes stakeholder coordination, regulatory compliance checks, and iterative optimization of growth parameters to maximize yield and minimize resource consumption in a confined urban environment. Post-launch activities encompass data analytics integration, pest control automation, and community engagement to ensure long-term sustainability and scalability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
ProcureModules = Transition(label='Procure Modules')
AssembleFramework = Transition(label='Assemble Framework')
InstallSensors = Transition(label='Install Sensors')
SetupIrrigation = Transition(label='Setup Irrigation')
FormulateNutrients = Transition(label='Formulate Nutrients')
CalibrateClimate = Transition(label='Calibrate Climate')
SeedPlanting = Transition(label='Seed Planting')
MonitorGrowth = Transition(label='Monitor Growth')
PestInspection = Transition(label='Pest Inspection')
DataIntegration = Transition(label='Data Integration')
EnergySync = Transition(label='Energy Sync')
ComplianceCheck = Transition(label='Compliance Check')
StakeholderMeet = Transition(label='Stakeholder Meet')
YieldAnalysis = Transition(label='Yield Analysis')
SystemOptimization = Transition(label='System Optimization')

# Build partial orders for subprocesses

# 1. Site setup and infrastructure
po_infra = StrictPartialOrder(nodes=[SiteSurvey, DesignLayout, ProcureModules, AssembleFramework])
po_infra.order.add_edge(SiteSurvey, DesignLayout)
po_infra.order.add_edge(DesignLayout, ProcureModules)
po_infra.order.add_edge(ProcureModules, AssembleFramework)

# 2. Installation and calibration
po_install = StrictPartialOrder(nodes=[InstallSensors, SetupIrrigation, FormulateNutrients, CalibrateClimate])
po_install.order.add_edge(InstallSensors, SetupIrrigation)
po_install.order.add_edge(SetupIrrigation, FormulateNutrients)
po_install.order.add_edge(FormulateNutrients, CalibrateClimate)

# 3. Pre-planting steps: seed planting after calibration
po_preplant = StrictPartialOrder(nodes=[CalibrateClimate, SeedPlanting])
po_preplant.order.add_edge(CalibrateClimate, SeedPlanting)

# 4. Growth monitoring loop:
# Loop: MonitorGrowth, then choice:
# - exit loop
# - or PestInspection then MonitorGrowth again

growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[MonitorGrowth, PestInspection]
)

# 5. Coordination and compliance as a choice after infrastructure and installation:
coordination_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[StakeholderMeet, ComplianceCheck]
)

# 6. Post-launch activities partial order: DataIntegration, EnergySync, PestInspection (already in loop), and community engagement approximated by StakeholderMeet (already as choice)
# We'll put DataIntegration and EnergySync concurrent after growth loop ends

post_launch = StrictPartialOrder(nodes=[DataIntegration, EnergySync])
# No ordering: concurrent

# 7. Optimization loop:
# Loop: YieldAnalysis then choose exit or SystemOptimization then YieldAnalysis again
optimization_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[YieldAnalysis, SystemOptimization]
)

# Compose whole process in partial order

# Nodes of root:
#   - po_infra
#   - po_install
#   - po_preplant
#   - growth_loop
#   - coordination_choice
#   - post_launch
#   - optimization_loop

nodes = [po_infra, po_install, po_preplant, growth_loop, coordination_choice, post_launch, optimization_loop]
root = StrictPartialOrder(nodes=nodes)

# Order edges:

# Infra --> Install
root.order.add_edge(po_infra, po_install)

# Install --> Preplant
root.order.add_edge(po_install, po_preplant)

# Preplant --> Growth loop
root.order.add_edge(po_preplant, growth_loop)

# Growth loop --> Coordination choice (stakeholder and compliance)
root.order.add_edge(growth_loop, coordination_choice)

# Coordination choice --> Post launch activities
root.order.add_edge(coordination_choice, post_launch)

# Post launch --> Optimization loop
root.order.add_edge(post_launch, optimization_loop)