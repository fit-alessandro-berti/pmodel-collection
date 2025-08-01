# Generated from: 62456c42-47de-4e2a-9066-fff64616273e.json
# Description: This process outlines the establishment of a vertical farming facility within an urban environment, integrating advanced hydroponic systems, renewable energy sources, and AI-driven crop monitoring. It begins with site analysis and structural assessment, followed by modular farm design and procurement of specialized equipment. Installation includes climate control setup, nutrient delivery systems, and automated lighting. Continuous data collection enables real-time adjustments to optimize growth cycles. The process incorporates waste recycling, pest management without chemicals, and community engagement initiatives to promote sustainable urban agriculture. Final stages involve yield analysis, distribution logistics, and scalability planning to expand operations efficiently.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis      = Transition(label='Site Analysis')
structure_check    = Transition(label='Structure Check')
design_farm        = Transition(label='Design Farm')
order_equipment    = Transition(label='Order Equipment')
install_hydroponics= Transition(label='Install Hydroponics')
setup_climate      = Transition(label='Setup Climate')
configure_lighting = Transition(label='Configure Lighting')
program_ai         = Transition(label='Program AI')
calibrate_sensors  = Transition(label='Calibrate Sensors')
nutrient_mix       = Transition(label='Nutrient Mix')
waste_recycling    = Transition(label='Waste Recycling')
pest_control       = Transition(label='Pest Control')
data_monitoring    = Transition(label='Data Monitoring')
community_outreach = Transition(label='Community Outreach')
yield_assessment   = Transition(label='Yield Assessment')
logistics_plan     = Transition(label='Logistics Plan')
scale_strategy     = Transition(label='Scale Strategy')

# Loop: continuous monitoring → nutrient mix → back to monitoring
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_monitoring, nutrient_mix]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    structure_check,
    design_farm,
    order_equipment,
    install_hydroponics,
    setup_climate,
    configure_lighting,
    program_ai,
    calibrate_sensors,
    monitoring_loop,
    waste_recycling,
    pest_control,
    community_outreach,
    yield_assessment,
    logistics_plan,
    scale_strategy
])

# Define the control-flow dependencies
o = root.order
o.add_edge(site_analysis,    structure_check)
o.add_edge(structure_check,  design_farm)
o.add_edge(design_farm,      order_equipment)
o.add_edge(order_equipment,  install_hydroponics)
o.add_edge(install_hydroponics, setup_climate)
o.add_edge(setup_climate,    configure_lighting)
o.add_edge(configure_lighting, program_ai)
o.add_edge(program_ai,       calibrate_sensors)
o.add_edge(calibrate_sensors, monitoring_loop)

# After exiting the monitoring loop, these run (in parallel)
o.add_edge(monitoring_loop, waste_recycling)
o.add_edge(monitoring_loop, pest_control)
o.add_edge(monitoring_loop, community_outreach)

# Once all finishing tasks complete, proceed to final stages
o.add_edge(waste_recycling,  yield_assessment)
o.add_edge(pest_control,     yield_assessment)
o.add_edge(community_outreach, yield_assessment)

o.add_edge(yield_assessment, logistics_plan)
o.add_edge(logistics_plan,   scale_strategy)