# Generated from: dc6f61b8-19c8-4468-848c-82b674ca2558.json
# Description: This process outlines the complex and atypical steps involved in setting up an urban vertical farm within a repurposed skyscraper. It includes securing partnerships for sustainable energy, integrating AI-driven climate control systems, sourcing modular hydroponic units, obtaining multi-level zoning permits, and coordinating logistics for the installation of automated nutrient delivery systems. The process also involves community engagement initiatives to promote local produce, testing crop yield optimization algorithms, and establishing carbon offset programs to ensure environmental compliance. Continuous monitoring and iterative adjustments ensure the farm remains efficient and scalable, addressing urban food security challenges innovatively.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
site_survey = Transition(label='Site Survey')
energy_partner = Transition(label='Energy Partner')
permit_filing = Transition(label='Permit Filing')
hydro_unit = Transition(label='Hydro Unit')
ai_setup = Transition(label='AI Setup')
nutrient_plan = Transition(label='Nutrient Plan')
system_install = Transition(label='System Install')
crop_testing = Transition(label='Crop Testing')
data_analysis = Transition(label='Data Analysis')
community_meet = Transition(label='Community Meet')
yield_adjust = Transition(label='Yield Adjust')
carbon_audit = Transition(label='Carbon Audit')
logistics_plan = Transition(label='Logistics Plan')
quality_check = Transition(label='Quality Check')
scale_review = Transition(label='Scale Review')

# Silent transition for looping choice
skip = SilentTransition()

# Loop for continuous monitoring and iterative adjustments:
# Loop( (Data Analysis + Yield Adjust) , (Quality Check + Scale Review) )
# We'll model the monitoring and adjustments as a PO of Data Analysis and Yield Adjust,
# and the iteration loop applies Quality Check and Scale Review repeatedly before returning to monitor
monitoring = StrictPartialOrder(nodes=[data_analysis, yield_adjust])
# no order between Data Analysis and Yield Adjust, they are concurrent

adjustments = StrictPartialOrder(nodes=[quality_check, scale_review])
# no order between Quality Check and Scale Review, concurrent

loop_adjust = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitoring, adjustments]
)

# Setup phase - parallel tasks that all depend on Site Survey
setup_dependencies = StrictPartialOrder(
    nodes=[energy_partner, permit_filing, hydro_unit, ai_setup, nutrient_plan, logistics_plan]
)
# No internal order, all concurrent

# After Site Survey, these setup tasks run concurrently
initial_po = StrictPartialOrder(nodes=[site_survey, setup_dependencies])
initial_po.order.add_edge(site_survey, setup_dependencies)

# The setup_dependencies is a POWL node, so must be a single node.
# We'll just flatten by combining them into a POWL node and linking as needed.
# But pm4py's StrictPartialOrder.nodes expects single nodes, so we need to model setup_dependencies as a PO node (StrictPartialOrder)

# Since StrictPartialOrder cannot be nested inside, we keep setup_dependencies as a single node.
# But we want to have the nodes independent inside setup_dependencies.
# So we redefine to keep all nodes flat at root level, and order edges to express concurrency and order.

# We'll proceed with flat model

# Build full PO root including setup parallel tasks between them (no order edges)
# And edges from Site Survey to each setup activity (to enforce they occur after Site Survey)

nodes = [
    site_survey,
    energy_partner,
    permit_filing,
    hydro_unit,
    ai_setup,
    nutrient_plan,
    logistics_plan,
    system_install,
    community_meet,
    crop_testing,
    carbon_audit,
    crop_testing,  # repeat in code: to note only once, remove duplicate
    community_meet,
    crop_testing,
    loop_adjust
]

# Remove duplicates above
nodes = [
    site_survey,
    energy_partner,
    permit_filing,
    hydro_unit,
    ai_setup,
    nutrient_plan,
    logistics_plan,
    system_install,
    community_meet,
    crop_testing,
    carbon_audit,
    loop_adjust
]

root = StrictPartialOrder(nodes=nodes)

# Add edges representing order dependency

# Site Survey --> all setup activities (energy_partner, permit_filing, hydro_unit, ai_setup, nutrient_plan, logistics_plan)
root.order.add_edge(site_survey, energy_partner)
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(site_survey, hydro_unit)
root.order.add_edge(site_survey, ai_setup)
root.order.add_edge(site_survey, nutrient_plan)
root.order.add_edge(site_survey, logistics_plan)

# All setup activities --> system_install
root.order.add_edge(energy_partner, system_install)
root.order.add_edge(permit_filing, system_install)
root.order.add_edge(hydro_unit, system_install)
root.order.add_edge(ai_setup, system_install)
root.order.add_edge(nutrient_plan, system_install)
root.order.add_edge(logistics_plan, system_install)

# system_install --> community_meet (for engagement after installation)
root.order.add_edge(system_install, community_meet)

# community_meet --> crop_testing
root.order.add_edge(community_meet, crop_testing)

# crop_testing --> carbon_audit (to ensure compliance after testing)
root.order.add_edge(crop_testing, carbon_audit)

# carbon_audit --> loop_adjust (monitoring and iterative adjustments)
root.order.add_edge(carbon_audit, loop_adjust)