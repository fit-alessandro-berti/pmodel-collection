# Generated from: 11707635-a7a9-4da6-87a1-91228671398b.json
# Description: This process outlines the establishment of an urban vertical farm designed to optimize space utilization in dense city environments. It involves initial site assessment, modular structure assembly, hydroponic system installation, environmental control calibration, crop selection tailored to microclimates, nutrient solution formulation, automated monitoring setup, staff training on specialized equipment, pest management planning using integrated pest management techniques, scheduling of planting and harvesting cycles, data analytics for yield optimization, waste recycling integration, community engagement for local sourcing, compliance verification with urban agricultural regulations, and final operational handover ensuring sustainability and scalability of the farm infrastructure.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
site_survey        = Transition(label='Site Survey')
structure_build    = Transition(label='Structure Build')
hydroponic_setup   = Transition(label='Hydroponic Setup')
climate_control    = Transition(label='Climate Control')
crop_selection     = Transition(label='Crop Selection')
nutrient_mix       = Transition(label='Nutrient Mix')
sensor_install     = Transition(label='Sensor Install')
staff_training     = Transition(label='Staff Training')
pest_planning      = Transition(label='Pest Planning')
plant_scheduling   = Transition(label='Plant Scheduling')
yield_analysis     = Transition(label='Yield Analysis')
waste_recycle      = Transition(label='Waste Recycle')
community_meet     = Transition(label='Community Meet')
regulation_check   = Transition(label='Regulation Check')
operation_handover = Transition(label='Operation Handover')

# Build a strict partial order representing the sequence of activities
root = StrictPartialOrder(nodes=[
    site_survey,
    structure_build,
    hydroponic_setup,
    climate_control,
    crop_selection,
    nutrient_mix,
    sensor_install,
    staff_training,
    pest_planning,
    plant_scheduling,
    yield_analysis,
    waste_recycle,
    community_meet,
    regulation_check,
    operation_handover
])

# Add sequential dependencies
root.order.add_edge(site_survey,        structure_build)
root.order.add_edge(structure_build,    hydroponic_setup)
root.order.add_edge(hydroponic_setup,   climate_control)
root.order.add_edge(climate_control,    crop_selection)
root.order.add_edge(crop_selection,     nutrient_mix)
root.order.add_edge(nutrient_mix,       sensor_install)
root.order.add_edge(sensor_install,     staff_training)
root.order.add_edge(staff_training,     pest_planning)
root.order.add_edge(pest_planning,      plant_scheduling)
root.order.add_edge(plant_scheduling,   yield_analysis)
root.order.add_edge(yield_analysis,     waste_recycle)
root.order.add_edge(waste_recycle,      community_meet)
root.order.add_edge(community_meet,     regulation_check)
root.order.add_edge(regulation_check,   operation_handover)