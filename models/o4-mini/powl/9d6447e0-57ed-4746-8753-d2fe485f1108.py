# Generated from: 9d6447e0-57ed-4746-8753-d2fe485f1108.json
# Description: This process outlines the establishment of a sustainable urban rooftop farming system designed to maximize limited space in metropolitan areas. It involves site assessment, structural analysis, soil preparation, hydroponic installation, seed selection, and environment control setup. The workflow integrates community engagement and digital monitoring to optimize crop yield while minimizing environmental impact. The process also includes regulatory compliance verification, pest management protocols, and periodic harvest scheduling, ensuring continuous production and quality assurance within an urban agricultural framework.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
load_testing     = Transition(label='Load Testing')
design_layout    = Transition(label='Design Layout')
soil_prep        = Transition(label='Soil Prep')
hydro_setup      = Transition(label='Hydro Setup')
seed_selection   = Transition(label='Seed Selection')
planting_seeds   = Transition(label='Planting Seeds')
irrigation_config= Transition(label='Irrigation Config')
sensor_install   = Transition(label='Sensor Install')
climate_control  = Transition(label='Climate Control')
regulation_check = Transition(label='Regulation Check')
community_meet   = Transition(label='Community Meet')
pest_inspection  = Transition(label='Pest Inspection')
growth_monitor   = Transition(label='Growth Monitor')
harvest_plan     = Transition(label='Harvest Plan')
yield_analysis   = Transition(label='Yield Analysis')

# Monitoring & harvest sub-process: Growth Monitor -> Harvest Plan -> Yield Analysis
monitoring_seq = StrictPartialOrder(nodes=[growth_monitor, harvest_plan, yield_analysis])
monitoring_seq.order.add_edge(growth_monitor, harvest_plan)
monitoring_seq.order.add_edge(harvest_plan, yield_analysis)

# Loop: Pest Inspection then choose to exit or do monitoring_seq then Pest Inspection again
loop_cycle = OperatorPOWL(operator=Operator.LOOP, children=[pest_inspection, monitoring_seq])

# Root process: initial setup, compliance & community, then the loop
root = StrictPartialOrder(nodes=[
    site_survey, load_testing, design_layout, soil_prep, hydro_setup,
    seed_selection, planting_seeds, irrigation_config, sensor_install,
    climate_control, regulation_check, community_meet, loop_cycle
])

# Sequential setup edges
root.order.add_edge(site_survey, load_testing)
root.order.add_edge(load_testing, design_layout)
root.order.add_edge(design_layout, soil_prep)
root.order.add_edge(soil_prep, hydro_setup)
root.order.add_edge(hydro_setup, seed_selection)
root.order.add_edge(seed_selection, planting_seeds)
root.order.add_edge(planting_seeds, irrigation_config)
root.order.add_edge(irrigation_config, sensor_install)
root.order.add_edge(sensor_install, climate_control)

# After climate control, do compliance check and community meet (concurrent)
root.order.add_edge(climate_control, regulation_check)
root.order.add_edge(climate_control, community_meet)

# Both compliance and community must complete before starting the pest/monitoring loop
root.order.add_edge(regulation_check, loop_cycle)
root.order.add_edge(community_meet, loop_cycle)