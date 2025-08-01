# Generated from: 9480ef34-fdde-468a-ae28-220aeb4c0fda.json
# Description: This process outlines the establishment of an urban vertical farming system within a constrained city environment. It involves selecting appropriate modular structures, integrating smart IoT sensors for environmental control, sourcing sustainable nutrient solutions, and implementing automated seeding and harvesting mechanisms. The process further includes regulatory compliance checks, community engagement for local support, and post-deployment monitoring to optimize crop yield and energy efficiency. Each phase requires coordination between architects, agronomists, engineers, and urban planners to ensure the farm operates sustainably while maximizing limited urban space and reducing carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey      = Transition(label='Site Survey')
design_planning  = Transition(label='Design Planning')
modular_build    = Transition(label='Modular Build')
sensor_install   = Transition(label='Sensor Install')
nutrient_prep    = Transition(label='Nutrient Prep')
seed_loading     = Transition(label='Seed Loading')
climate_setup    = Transition(label='Climate Setup')
automation_cfg   = Transition(label='Automation Config')
regulation_check = Transition(label='Regulation Check')
staff_training   = Transition(label='Staff Training')
community_meet   = Transition(label='Community Meet')
growth_monitor   = Transition(label='Growth Monitor')
pest_control     = Transition(label='Pest Control')
harvest_cycle    = Transition(label='Harvest Cycle')
waste_manage     = Transition(label='Waste Manage')
energy_audit     = Transition(label='Energy Audit')

# Define the monitoring loop: do a Growth Monitor, then optionally do Pest Control -> Harvest -> Waste Manage, repeat
# Body of loop
monitor_body = StrictPartialOrder(nodes=[pest_control, harvest_cycle, waste_manage])
monitor_body.order.add_edge(pest_control, harvest_cycle)
monitor_body.order.add_edge(harvest_cycle, waste_manage)

# Loop operator: first child = Growth Monitor, second child = body
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, monitor_body])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_planning,
    modular_build,
    sensor_install,
    nutrient_prep,
    seed_loading,
    climate_setup,
    automation_cfg,
    regulation_check,
    staff_training,
    community_meet,
    monitor_loop,
    energy_audit
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,      design_planning)
root.order.add_edge(design_planning,  modular_build)
root.order.add_edge(modular_build,    sensor_install)
root.order.add_edge(sensor_install,   nutrient_prep)
root.order.add_edge(nutrient_prep,    seed_loading)
root.order.add_edge(seed_loading,     climate_setup)
root.order.add_edge(climate_setup,    automation_cfg)
root.order.add_edge(automation_cfg,   regulation_check)

# After regulation check, staff training and community meet can proceed in parallel
root.order.add_edge(regulation_check, staff_training)
root.order.add_edge(regulation_check, community_meet)

# Both training and community engagement must complete before entering the monitoring loop
root.order.add_edge(staff_training,   monitor_loop)
root.order.add_edge(community_meet,   monitor_loop)

# After the monitoring loop terminates, perform the final energy audit
root.order.add_edge(monitor_loop,     energy_audit)