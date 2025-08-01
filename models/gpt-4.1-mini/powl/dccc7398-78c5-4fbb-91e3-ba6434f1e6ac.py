# Generated from: dccc7398-78c5-4fbb-91e3-ba6434f1e6ac.json
# Description: This process outlines the complex steps involved in establishing a fully automated urban vertical farm within a metropolitan area. It begins with site evaluation and ends with ongoing crop optimization. The workflow integrates architectural design, environmental control installation, nutrient cycling, robotic planting, AI-based growth monitoring, pest management using bio-controls, and energy-efficient harvesting. Stakeholders coordinate across disciplines including agronomy, engineering, logistics, and IT to ensure sustainable production in limited urban spaces while minimizing water and energy usage. The process also involves regulatory compliance checks, community engagement, and market integration for fresh produce distribution, making it a multifaceted endeavor requiring precise orchestration of technology and human expertise.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Design_Draft = Transition(label='Design Draft')
Permit_Review = Transition(label='Permit Review')
Structure_Build = Transition(label='Structure Build')
Enviro_Setup = Transition(label='Enviro Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Selection = Transition(label='Seed Selection')
Plant_Robots = Transition(label='Plant Robots')
Sensor_Install = Transition(label='Sensor Install')
Data_Sync = Transition(label='Data Sync')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Quality_Check = Transition(label='Quality Check')
Market_Launch = Transition(label='Market Launch')
Feedback_Loop = Transition(label='Feedback Loop')

# Site evaluation and design sequence
site_and_design = StrictPartialOrder(
    nodes=[Site_Survey, Design_Draft, Permit_Review],
)
site_and_design.order.add_edge(Site_Survey, Design_Draft)
site_and_design.order.add_edge(Design_Draft, Permit_Review)

# Structure build and setup sequence
build_and_setup = StrictPartialOrder(
    nodes=[Structure_Build, Enviro_Setup, Nutrient_Mix],
)
build_and_setup.order.add_edge(Structure_Build, Enviro_Setup)
build_and_setup.order.add_edge(Enviro_Setup, Nutrient_Mix)

# Planting and installation partial order (these can be concurrent)
planting_and_install = StrictPartialOrder(
    nodes=[Seed_Selection, Plant_Robots, Sensor_Install],
)
# No order edges - all concurrent

# Data and monitoring partial order (data sync before monitoring)
data_and_monitor = StrictPartialOrder(
    nodes=[Data_Sync, Growth_Monitor],
)
data_and_monitor.order.add_edge(Data_Sync, Growth_Monitor)

# Pest control branch
pest_control = Pest_Control

# Harvest and quality check sequence
harvest_and_check = StrictPartialOrder(
    nodes=[Harvest_Plan, Quality_Check],
)
harvest_and_check.order.add_edge(Harvest_Plan, Quality_Check)

# Market launch after quality check
market_launch = Market_Launch

# Feedback loop is looping on Growth Monitor and Pest Control (monitoring ongoing),
# representing ongoing crop optimization with feedback.
# We'll create a loop: 
# A = Growth Monitor + Pest Control concurrent partial order
# B = Feedback Loop (silent or labeled) to represent possible iterations

# Concurrent Growth_Monitor and Pest_Control
monitor_and_pest = StrictPartialOrder(
    nodes=[Growth_Monitor, Pest_Control],
)
# No order edges - concurrent

# Loop modeled as LOOP(A=monitor_and_pest, B=Feedback_Loop)
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_and_pest, Feedback_Loop]
)

# Now combine all main phases in partial order:

# First phase: site_and_design --> build_and_setup
# Then --> planting_and_install
# Then --> data_and_monitor
# Then --> loop (growth monitoring + pest with feedback)
# Then --> harvest_and_check --> market_launch

# Create partial order with all nodes:
root = StrictPartialOrder(
    nodes=[
        site_and_design,
        build_and_setup,
        planting_and_install,
        data_and_monitor,
        loop,
        harvest_and_check,
        market_launch
    ],
)

# Define ordering edges:
root.order.add_edge(site_and_design, build_and_setup)
root.order.add_edge(build_and_setup, planting_and_install)
root.order.add_edge(planting_and_install, data_and_monitor)
root.order.add_edge(data_and_monitor, loop)
root.order.add_edge(loop, harvest_and_check)
root.order.add_edge(harvest_and_check, market_launch)