# Generated from: 8cdb6c9a-21bc-4ad5-834d-f2cf76a4c97b.json
# Description: This process involves the complex coordination of multiple stakeholders and resources to establish an urban vertical farm within a densely populated city. It begins with site identification and environmental impact assessments, followed by securing permits and designing modular vertical farming units. The process includes sourcing specialized hydroponic equipment, integrating IoT-based monitoring systems, and implementing energy-efficient LED lighting. Staff recruitment focuses on agronomists and technicians trained in controlled environment agriculture. Concurrently, partnerships with local markets and distributors are negotiated to ensure product flow. The process also covers sustainable waste management, water recycling systems, and community engagement initiatives. Quality control protocols and crop cycle optimization are continuously refined to maximize yield and minimize resource consumption. Finally, a phased product launch is executed alongside ongoing data analytics to adapt operations dynamically.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
site_survey = Transition(label='Site Survey')
impact_study = Transition(label='Impact Study')
permit_filing = Transition(label='Permit Filing')
unit_design = Transition(label='Unit Design')
equip_sourcing = Transition(label='Equip Sourcing')
system_setup = Transition(label='System Setup')
lighting_install = Transition(label='Lighting Install')
staff_hiring = Transition(label='Staff Hiring')
training_session = Transition(label='Training Session')
market_outreach = Transition(label='Market Outreach')
waste_setup = Transition(label='Waste Setup')
water_recycle = Transition(label='Water Recycle')
community_meet = Transition(label='Community Meet')
quality_check = Transition(label='Quality Check')
cycle_review = Transition(label='Cycle Review')
launch_phase = Transition(label='Launch Phase')
data_monitor = Transition(label='Data Monitor')

# 1) Site identification and environmental impact assessments (serial)
site_assessment = StrictPartialOrder(nodes=[site_survey, impact_study])
site_assessment.order.add_edge(site_survey, impact_study)

# 2) Securing permits and designing modular units (serial)
permits_and_design = StrictPartialOrder(nodes=[permit_filing, unit_design])
permits_and_design.order.add_edge(permit_filing, unit_design)

# 3) Sourcing hydroponic equipment, integrating IoT monitoring, and installing LED lighting (partial order)
# Equip Sourcing -> System Setup -> Lighting Install
equip_system_lighting = StrictPartialOrder(nodes=[equip_sourcing, system_setup, lighting_install])
equip_system_lighting.order.add_edge(equip_sourcing, system_setup)
equip_system_lighting.order.add_edge(system_setup, lighting_install)

# 4) Staff recruitment: hiring and training (serial)
staff_recruitment = StrictPartialOrder(nodes=[staff_hiring, training_session])
staff_recruitment.order.add_edge(staff_hiring, training_session)

# 5) Concurrent partnerships with markets and distributors (single activity: Market Outreach)
# 6) Concurrent sustainable waste management, water recycling, and community engagement
# (Waste Setup, Water Recycle, Community Meet) concurrent

# Grouping waste, water, community parallel
sustain_ops = StrictPartialOrder(nodes=[waste_setup, water_recycle, community_meet])
# no edges => fully concurrent

# 7) Quality control protocols and crop cycle optimization (serial)
quality_and_cycle = StrictPartialOrder(nodes=[quality_check, cycle_review])
quality_and_cycle.order.add_edge(quality_check, cycle_review)

# Step grouping of parallel activities:
# Market outreach runs concurrently with sustain_ops (waste+water+community)
market_sustain = StrictPartialOrder(nodes=[market_outreach, sustain_ops])
# no ordering edges, fully concurrent

# Assemble all main phases into the process

# Phase 1: site_assessment
# Phase 2: permits_and_design (after phase 1)
# Phase 3: equip_system_lighting (after phase 2)
# Phase 4: staff_recruitment (after phase 3)
# Phase 5: market_sustain (after phase 3) -- concurrent with staff_recruitment
# So market_sustain and staff_recruitment start after phase 3, concurrently

# Phase 6: quality_and_cycle (after staff recruitment and market_sustain complete)
# For safety, require market_sustain and staff_recruitment before quality_and_cycle
# So edges: staff_recruitment->quality_and_cycle, market_sustain->quality_and_cycle

# Phase 7: launch_phase and data_monitor run concurrently after quality_and_cycle
launch_and_monitor = StrictPartialOrder(nodes=[launch_phase, data_monitor])
# no edges => concurrent

# Now put all major blocks in a PO:
root = StrictPartialOrder(
    nodes=[
        site_assessment,
        permits_and_design,
        equip_system_lighting,
        staff_recruitment,
        market_sustain,
        quality_and_cycle,
        launch_and_monitor,
    ]
)

# Define order edges to reflect process flow and concurrency as described

# Phase 1 -> Phase 2
root.order.add_edge(site_assessment, permits_and_design)
# Phase 2 -> Phase 3
root.order.add_edge(permits_and_design, equip_system_lighting)
# Phase 3 -> staff_recruitment and market_sustain (concurrent start)
root.order.add_edge(equip_system_lighting, staff_recruitment)
root.order.add_edge(equip_system_lighting, market_sustain)
# staff_recruitment and market_sustain must finish before quality_and_cycle
root.order.add_edge(staff_recruitment, quality_and_cycle)
root.order.add_edge(market_sustain, quality_and_cycle)
# quality_and_cycle -> launch_and_monitor
root.order.add_edge(quality_and_cycle, launch_and_monitor)