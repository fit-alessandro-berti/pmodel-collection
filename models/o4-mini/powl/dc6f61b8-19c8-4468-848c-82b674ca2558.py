# Generated from: dc6f61b8-19c8-4468-848c-82b674ca2558.json
# Description: This process outlines the complex and atypical steps involved in setting up an urban vertical farm within a repurposed skyscraper. It includes securing partnerships for sustainable energy, integrating AI-driven climate control systems, sourcing modular hydroponic units, obtaining multi-level zoning permits, and coordinating logistics for the installation of automated nutrient delivery systems. The process also involves community engagement initiatives to promote local produce, testing crop yield optimization algorithms, and establishing carbon offset programs to ensure environmental compliance. Continuous monitoring and iterative adjustments ensure the farm remains efficient and scalable, addressing urban food security challenges innovatively.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey    = Transition(label='Site Survey')
energy_partner = Transition(label='Energy Partner')
permit_filing  = Transition(label='Permit Filing')
hydro_unit     = Transition(label='Hydro Unit')
ai_setup       = Transition(label='AI Setup')
nutrient_plan  = Transition(label='Nutrient Plan')
logistics_plan = Transition(label='Logistics Plan')
system_install = Transition(label='System Install')
crop_testing   = Transition(label='Crop Testing')
data_analysis  = Transition(label='Data Analysis')
yield_adjust   = Transition(label='Yield Adjust')
quality_check  = Transition(label='Quality Check')
carbon_audit   = Transition(label='Carbon Audit')
community_meet = Transition(label='Community Meet')
scale_review   = Transition(label='Scale Review')

# Build the loop body: Crop Testing -> Data Analysis -> Yield Adjust
loop_body = StrictPartialOrder(nodes=[crop_testing, data_analysis, yield_adjust])
loop_body.order.add_edge(crop_testing, data_analysis)
loop_body.order.add_edge(data_analysis, yield_adjust)

# Define the LOOP: first do loop_body, then either exit or do quality_check then loop_body again
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, quality_check])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    energy_partner,
    permit_filing,
    hydro_unit,
    ai_setup,
    nutrient_plan,
    logistics_plan,
    system_install,
    loop_node,
    carbon_audit,
    community_meet,
    scale_review
])

# Specify the sequencing constraints
root.order.add_edge(site_survey,    energy_partner)
root.order.add_edge(site_survey,    permit_filing)
root.order.add_edge(energy_partner, hydro_unit)
root.order.add_edge(permit_filing,  hydro_unit)
root.order.add_edge(hydro_unit,     ai_setup)
root.order.add_edge(ai_setup,       nutrient_plan)
root.order.add_edge(nutrient_plan,  logistics_plan)
root.order.add_edge(logistics_plan, system_install)
root.order.add_edge(system_install, loop_node)
root.order.add_edge(loop_node,      carbon_audit)
root.order.add_edge(carbon_audit,   community_meet)
root.order.add_edge(community_meet, scale_review)