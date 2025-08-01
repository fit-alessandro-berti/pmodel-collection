# Generated from: 510d4214-7946-4c60-b6bd-f6b2f48122c6.json
# Description: This process outlines the complex steps required to establish an urban vertical farming system within a repurposed multi-story building. It involves site assessment, modular system design, climate control optimization, nutrient cycling integration, and automation deployment. The process must address sustainability metrics, regulatory compliance, and community engagement. It further includes supply chain coordination for specialized seeds, sensors installation, real-time data analysis for crop health, pest management without chemicals, and iterative system tuning to maximize yield while minimizing energy consumption and waste generation. The process culminates in establishing a market distribution network and continuous feedback loops for improvement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
System_Build = Transition(label='System Build')
Install_Sensors = Transition(label='Install Sensors')
Setup_Climate = Transition(label='Setup Climate')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Selection = Transition(label='Seed Selection')
Planting_Phase = Transition(label='Planting Phase')
Monitor_Growth = Transition(label='Monitor Growth')
Pest_Control = Transition(label='Pest Control')
Data_Analysis = Transition(label='Data Analysis')
Adjust_Parameters = Transition(label='Adjust Parameters')
Energy_Audit = Transition(label='Energy Audit')
Waste_Manage = Transition(label='Waste Manage')
Market_Setup = Transition(label='Market Setup')

skip = SilentTransition()

# Build partial orders and loops according to the process description

# Phase 1: Site survey --> design --> system build
phase1 = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, System_Build])
phase1.order.add_edge(Site_Survey, Design_Layout)
phase1.order.add_edge(Design_Layout, System_Build)

# Phase 2: Install sensors, setup climate, nutrient mix, seed selection in parallel after system build
install_related = StrictPartialOrder(
    nodes=[Install_Sensors, Setup_Climate, Nutrient_Mix, Seed_Selection]
)
# all parallel - no order edges

after_build = StrictPartialOrder(nodes=[phase1, install_related])
after_build.order.add_edge(phase1, install_related)

# Phase 3: Planting phase after seed selection
phase3 = StrictPartialOrder(nodes=[Planting_Phase])
# Planting depends on Seed Selection
# Need to connect from install_related (Seed_Selection) to Planting_Phase

# We can establish edges from install_related's Seed_Selection to Planting_Phase
# But since install_related is a PO, and Seed_Selection is inside it,
# we cannot add edges crossing StrictPartialOrder nodes.
# Instead, flatten the structure:

# Redefine a larger partial order that integrates phase1 and install_related, and Planting_Phase

setup_nodes = [
    Site_Survey,
    Design_Layout,
    System_Build,
    Install_Sensors,
    Setup_Climate,
    Nutrient_Mix,
    Seed_Selection,
    Planting_Phase,
]
setup = StrictPartialOrder(nodes=setup_nodes)

# Order edges
setup.order.add_edge(Site_Survey, Design_Layout)
setup.order.add_edge(Design_Layout, System_Build)

# System_Build --> all install related
setup.order.add_edge(System_Build, Install_Sensors)
setup.order.add_edge(System_Build, Setup_Climate)
setup.order.add_edge(System_Build, Nutrient_Mix)
setup.order.add_edge(System_Build, Seed_Selection)

# Seed_Selection --> Planting_Phase
setup.order.add_edge(Seed_Selection, Planting_Phase)

# Phase 4: Monitor Growth, Pest Control, Data Analysis - concurrent after Planting
monitoring = StrictPartialOrder(
    nodes=[Monitor_Growth, Pest_Control, Data_Analysis]
)
# all parallel after Planting_Phase

# connect Planting_Phase --> all three
# same as before, flatten nodes for edges crossing
mon_nodes = [
    Planting_Phase,
    Monitor_Growth,
    Pest_Control,
    Data_Analysis,
]
mon = StrictPartialOrder(nodes=mon_nodes)
mon.order.add_edge(Planting_Phase, Monitor_Growth)
mon.order.add_edge(Planting_Phase, Pest_Control)
mon.order.add_edge(Planting_Phase, Data_Analysis)

# Phase 5: Loop - adjust parameters, energy audit, waste manage, then back to monitoring or exit
# The loop body is B = StrictPartialOrder nodes=[Adjust_Parameters, Energy_Audit, Waste_Manage]
loop_body = StrictPartialOrder(nodes=[Adjust_Parameters, Energy_Audit, Waste_Manage])
# all parallel inside loop body, no internal order edges

# A = monitoring phase (Monitor Growth, Pest Control, Data Analysis)
# But we already defined 'mon' as containing Planting_Phase and monitoring nodes - 
# we want loop on monitoring activities only, not planting phase

mon_only = StrictPartialOrder(nodes=[Monitor_Growth, Pest_Control, Data_Analysis])

# loop = LOOP(A=mon_only, B=loop_body)
loop = OperatorPOWL(operator=Operator.LOOP, children=[mon_only, loop_body])

# Phase 6: Market Setup after loop exit
# So loop --> Market_Setup

# build top-level partial order:
# setup --> loop --> Market_Setup

root = StrictPartialOrder(nodes=[setup, loop, Market_Setup])
root.order.add_edge(setup, loop)
root.order.add_edge(loop, Market_Setup)