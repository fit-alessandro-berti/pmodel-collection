# Generated from: 59916b4a-061d-4439-af0c-160418a477fd.json
# Description: This process outlines the establishment of a vertical urban farm in a densely populated city environment. It integrates unconventional site selection, modular hydroponic system design, and multi-tiered crop scheduling. The process requires coordination between environmental impact analysis, energy optimization, and community engagement to ensure sustainable urban agriculture. Activities include securing rooftop leases, customizing nutrient delivery, implementing AI-driven climate control, and managing crop rotation cycles. The process culminates in local distribution partnerships and continuous feedback integration to enhance yield and reduce waste in an atypical but scalable urban farming operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
lease           = Transition(label='Lease Negotiation')
design          = Transition(label='Design Layout')
energy_audit    = Transition(label='Energy Audit')
community_meet  = Transition(label='Community Meet')
system_build    = Transition(label='System Build')
climate_setup   = Transition(label='Climate Setup')
nutrient_prep   = Transition(label='Nutrient Prep')
seed_selection  = Transition(label='Seed Selection')
planting        = Transition(label='Planting Cycle')
ai_calibration  = Transition(label='AI Calibration')
growth_monitor = Transition(label='Growth Monitoring')
pest_control    = Transition(label='Pest Control')
harvest_plan    = Transition(label='Harvest Plan')
feedback_loop   = Transition(label='Feedback Loop')
local_partner   = Transition(label='Local Partner')
waste_recycle   = Transition(label='Waste Recycle')

# Concurrency block: design, energy audit, community engagement in parallel
concurrent_block = StrictPartialOrder(
    nodes=[design, energy_audit, community_meet]
)
# no edges => fully concurrent

# Loop for continuous crop cycles: calibrate AI, then monitor→pest→harvest→feedback, then back to calibration
loop_body = StrictPartialOrder(
    nodes=[growth_monitor, pest_control, harvest_plan, feedback_loop]
)
loop_body.order.add_edge(growth_monitor, pest_control)
loop_body.order.add_edge(pest_control, harvest_plan)
loop_body.order.add_edge(harvest_plan, feedback_loop)

loop_cycle = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ai_calibration, loop_body]
)

# Root partial order tying everything together
root = StrictPartialOrder(
    nodes=[
        site_survey,
        lease,
        concurrent_block,
        system_build,
        climate_setup,
        nutrient_prep,
        seed_selection,
        planting,
        loop_cycle,
        local_partner,
        waste_recycle
    ]
)

# Define the control-flow dependencies
# 1. Site survey → Lease negotiation
root.order.add_edge(site_survey, lease)
# 2. Lease → (design ∥ energy audit ∥ community meet)
root.order.add_edge(lease, concurrent_block)
# 3. After concurrent block → system build
root.order.add_edge(concurrent_block, system_build)
# 4. System build → climate setup
root.order.add_edge(system_build, climate_setup)
# 5. Climate setup → (nutrient prep ∥ seed selection)
root.order.add_edge(climate_setup, nutrient_prep)
root.order.add_edge(climate_setup, seed_selection)
# 6. Both nutrient prep & seed selection → planting
root.order.add_edge(nutrient_prep, planting)
root.order.add_edge(seed_selection, planting)
# 7. Planting → the crop‐cycle loop
root.order.add_edge(planting, loop_cycle)
# 8. After loop → local distribution partnerships → waste recycle
root.order.add_edge(loop_cycle, local_partner)
root.order.add_edge(local_partner, waste_recycle)