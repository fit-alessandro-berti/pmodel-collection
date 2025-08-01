# Generated from: c4615489-a080-40d0-b747-8d0cde9ae394.json
# Description: This process outlines the comprehensive setup of an urban vertical farming facility within a repurposed industrial building. It involves site analysis, structural modification, environmental control installation, hydroponic system integration, crop selection, and staff training. The process ensures sustainable resource use, maximizes yield per square foot, and incorporates IoT-based monitoring to optimize growth conditions. Regulatory compliance, community engagement, and market launch strategies are also included to create a resilient urban agriculture business model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey        = Transition(label='Site Survey')
structural_audit   = Transition(label='Structural Audit')
permit_filing      = Transition(label='Permit Filing')
design_layout      = Transition(label='Design Layout')
install_hvac       = Transition(label='Install HVAC')
set_lighting       = Transition(label='Set Lighting')
build_racks        = Transition(label='Build Racks')
install_hydroponics= Transition(label='Install Hydroponics')
configure_sensors  = Transition(label='Configure Sensors')
select_crops       = Transition(label='Select Crops')
seed_planting      = Transition(label='Seed Planting')
monitor_growth     = Transition(label='Monitor Growth')
nutrient_mixing    = Transition(label='Nutrient Mixing')
staff_training     = Transition(label='Staff Training')
waste_recycling    = Transition(label='Waste Recycling')
market_launch      = Transition(label='Market Launch')
customer_onboarding= Transition(label='Customer Onboarding')

# Loop: monitor growth, then choose to mix nutrients and repeat or exit
loop_monitoring = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_growth, nutrient_mixing]
)

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey, structural_audit,
    permit_filing,
    design_layout,
    install_hvac, set_lighting,
    build_racks,
    install_hydroponics,
    configure_sensors,
    select_crops, seed_planting,
    staff_training,
    loop_monitoring,
    waste_recycling,
    market_launch,
    customer_onboarding
])

# Add ordering constraints
# Phase 1: site survey & structural audit in parallel, then permit
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(structural_audit, permit_filing)

# Phase 2: design layout
root.order.add_edge(permit_filing, design_layout)

# Phase 3: HVAC & lighting in parallel, then racks
root.order.add_edge(design_layout, install_hvac)
root.order.add_edge(design_layout, set_lighting)
root.order.add_edge(install_hvac, build_racks)
root.order.add_edge(set_lighting, build_racks)

# Phase 4: hydroponics & sensors
root.order.add_edge(build_racks, install_hydroponics)
root.order.add_edge(install_hydroponics, configure_sensors)

# Phase 5: crops & seeding
root.order.add_edge(configure_sensors, select_crops)
root.order.add_edge(select_crops, seed_planting)

# Phase 6: staff training then monitoring loop
root.order.add_edge(seed_planting, staff_training)
root.order.add_edge(staff_training, loop_monitoring)

# Phase 7: after exiting loop, waste recycling & market launch & onboarding in parallel
root.order.add_edge(loop_monitoring, waste_recycling)
root.order.add_edge(loop_monitoring, market_launch)
root.order.add_edge(loop_monitoring, customer_onboarding)