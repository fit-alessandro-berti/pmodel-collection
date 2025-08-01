# Generated from: 510d4214-7946-4c60-b6bd-f6b2f48122c6.json
# Description: This process outlines the complex steps required to establish an urban vertical farming system within a repurposed multi-story building. It involves site assessment, modular system design, climate control optimization, nutrient cycling integration, and automation deployment. The process must address sustainability metrics, regulatory compliance, and community engagement. It further includes supply chain coordination for specialized seeds, sensors installation, real-time data analysis for crop health, pest management without chemicals, and iterative system tuning to maximize yield while minimizing energy consumption and waste generation. The process culminates in establishing a market distribution network and continuous feedback loops for improvement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
system_build    = Transition(label='System Build')
install_sensors = Transition(label='Install Sensors')
setup_climate   = Transition(label='Setup Climate')
nutrient_mix    = Transition(label='Nutrient Mix')
seed_selection  = Transition(label='Seed Selection')
planting_phase  = Transition(label='Planting Phase')
monitor_growth  = Transition(label='Monitor Growth')
data_analysis   = Transition(label='Data Analysis')
adjust_parameters = Transition(label='Adjust Parameters')
pest_control    = Transition(label='Pest Control')
energy_audit    = Transition(label='Energy Audit')
waste_manage    = Transition(label='Waste Manage')
market_setup    = Transition(label='Market Setup')

# Define the iterative tuning loop: A = Monitor Growth, B = analysis → adjust → pest → energy audit → waste manage
A_seq = StrictPartialOrder(nodes=[monitor_growth])

B_seq = StrictPartialOrder(nodes=[
    data_analysis,
    adjust_parameters,
    pest_control,
    energy_audit,
    waste_manage
])
B_seq.order.add_edge(data_analysis, adjust_parameters)
B_seq.order.add_edge(adjust_parameters, pest_control)
B_seq.order.add_edge(pest_control, energy_audit)
B_seq.order.add_edge(energy_audit, waste_manage)

loop_tuning = OperatorPOWL(operator=Operator.LOOP, children=[A_seq, B_seq])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    system_build,
    install_sensors,
    setup_climate,
    nutrient_mix,
    seed_selection,
    planting_phase,
    loop_tuning,
    market_setup
])

# Sequential and concurrent dependencies
root.order.add_edge(site_survey,   design_layout)
root.order.add_edge(design_layout, system_build)

# After build, perform concurrent setup steps
root.order.add_edge(system_build, install_sensors)
root.order.add_edge(system_build, setup_climate)
root.order.add_edge(system_build, nutrient_mix)
root.order.add_edge(system_build, seed_selection)

# All setup tasks must complete before planting
root.order.add_edge(install_sensors, planting_phase)
root.order.add_edge(setup_climate,   planting_phase)
root.order.add_edge(nutrient_mix,    planting_phase)
root.order.add_edge(seed_selection,  planting_phase)

# After planting, begin the iterative monitoring loop
root.order.add_edge(planting_phase, loop_tuning)

# Once tuning loop exits, finalize with market setup
root.order.add_edge(loop_tuning, market_setup)