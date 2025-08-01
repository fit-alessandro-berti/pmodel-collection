# Generated from: f5d74bd9-51d4-4906-9dac-77112ec1d4d0.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes site analysis, environmental impact assessment, structural modifications, hydroponic system installation, crop selection, nutrient management, pest control, automated monitoring integration, staff training, regulatory compliance checks, product packaging design, distribution channel setup, community engagement, and ongoing sustainability evaluations. The goal is to create a highly efficient, scalable, and sustainable urban farm that maximizes yield while minimizing resource consumption and environmental footprint in a dense city environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_review       = Transition(label='Site Review')
impact_study      = Transition(label='Impact Study')
design_plan       = Transition(label='Design Plan')
structure_mod     = Transition(label='Structure Mod')
hydroponics_setup = Transition(label='Hydroponics Setup')
crop_select       = Transition(label='Crop Select')
nutrient_mix      = Transition(label='Nutrient Mix')
pest_control      = Transition(label='Pest Control')
sensor_install    = Transition(label='Sensor Install')
staff_train       = Transition(label='Staff Train')
compliance_audit  = Transition(label='Compliance Audit')
packaging_dev     = Transition(label='Packaging Dev')
logistics_plan    = Transition(label='Logistics Plan')
community_engage  = Transition(label='Community Engage')
sustainability_check = Transition(label='Sustainability Check')

# Main workflow as a strict partial order (everything before the sustainability loop)
main_seq = StrictPartialOrder(nodes=[
    site_review, impact_study, design_plan, structure_mod, hydroponics_setup,
    crop_select, nutrient_mix, pest_control, sensor_install,
    staff_train, compliance_audit, packaging_dev, logistics_plan, community_engage
])

# Define the precedence relations
main_seq.order.add_edge(site_review, impact_study)
main_seq.order.add_edge(impact_study, design_plan)
main_seq.order.add_edge(design_plan, structure_mod)
main_seq.order.add_edge(structure_mod, hydroponics_setup)

# After hydroponics setup, the following four can run in parallel
main_seq.order.add_edge(hydroponics_setup, crop_select)
main_seq.order.add_edge(hydroponics_setup, nutrient_mix)
main_seq.order.add_edge(hydroponics_setup, pest_control)
main_seq.order.add_edge(hydroponics_setup, sensor_install)

# All four must complete before staff training
for t in (crop_select, nutrient_mix, pest_control, sensor_install):
    main_seq.order.add_edge(t, staff_train)

# Then compliance audit, packaging, logistics, and community engagement
main_seq.order.add_edge(staff_train, compliance_audit)
main_seq.order.add_edge(compliance_audit, packaging_dev)
main_seq.order.add_edge(packaging_dev, logistics_plan)
main_seq.order.add_edge(logistics_plan, community_engage)

# Wrap the core workflow in a loop for ongoing sustainability checks
# Loop children: [A, B] means A executes, then repeat (B -> A) zero or more times.
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_seq, sustainability_check]
)