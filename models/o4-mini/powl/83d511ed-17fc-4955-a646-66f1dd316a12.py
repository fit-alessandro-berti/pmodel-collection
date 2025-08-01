# Generated from: 83d511ed-17fc-4955-a646-66f1dd316a12.json
# Description: This process outlines the detailed steps involved in establishing an urban vertical farm within a repurposed commercial building. It includes activities such as site analysis, structural retrofitting, environmental control installation, crop selection, hydroponic system design, nutrient formulation, automated monitoring setup, pest management planning, labor training, and market integration. Each phase is critical to ensure sustainable production, optimize yield, and minimize environmental impact while addressing urban food security challenges through innovative farming techniques and technology integration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey   = Transition(label='Site Survey')
struct_check  = Transition(label='Structural Check')
retrofitting  = Transition(label='Retrofitting')
env_control   = Transition(label='Env Control')
crop_research = Transition(label='Crop Research')
system_design = Transition(label='System Design')
nutrient_mix  = Transition(label='Nutrient Mix')
sensor_setup  = Transition(label='Sensor Setup')
irrigation    = Transition(label='Irrigation Plan')
pest_control  = Transition(label='Pest Control')
staff_training= Transition(label='Staff Training')
energy_audit  = Transition(label='Energy Audit')
waste_recycle = Transition(label='Waste Recycle')
market_study  = Transition(label='Market Study')
launch_prep   = Transition(label='Launch Prep')
yield_monitor = Transition(label='Yield Monitor')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, struct_check, retrofitting, env_control,
    crop_research, system_design, nutrient_mix,
    sensor_setup, irrigation, pest_control,
    staff_training, energy_audit, waste_recycle,
    market_study, launch_prep, yield_monitor
])

# Phase 1: site survey -> structural check -> retrofitting -> env control
root.order.add_edge(site_survey, struct_check)
root.order.add_edge(struct_check, retrofitting)
root.order.add_edge(retrofitting, env_control)

# Phase 2: env control -> crop research -> system design -> nutrient mix
root.order.add_edge(env_control, crop_research)
root.order.add_edge(crop_research, system_design)
root.order.add_edge(system_design, nutrient_mix)

# Phase 3: after nutrient mix, three tasks run in parallel:
#   sensor setup, irrigation plan, pest control
for nxt in [sensor_setup, irrigation, pest_control]:
    root.order.add_edge(nutrient_mix, nxt)

# Phase 4: they all join into staff training
for prev in [sensor_setup, irrigation, pest_control]:
    root.order.add_edge(prev, staff_training)

# Phase 5: after training, energy audit and waste recycle in parallel
root.order.add_edge(staff_training, energy_audit)
root.order.add_edge(staff_training, waste_recycle)

# Phase 6: audit and recycle join into market study
root.order.add_edge(energy_audit, market_study)
root.order.add_edge(waste_recycle, market_study)

# Phase 7: market study -> launch prep -> yield monitor
root.order.add_edge(market_study, launch_prep)
root.order.add_edge(launch_prep, yield_monitor)