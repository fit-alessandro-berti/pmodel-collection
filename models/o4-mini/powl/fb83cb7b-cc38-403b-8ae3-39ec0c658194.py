# Generated from: fb83cb7b-cc38-403b-8ae3-39ec0c658194.json
# Description: This process outlines the complex steps involved in establishing an urban rooftop farming system. It begins with site assessment and structural analysis to ensure the roof can support the load. Next, permits and zoning approvals are secured, followed by sourcing sustainable materials and soil mixtures tailored for rooftop environments. Installation involves waterproofing, irrigation setup, and modular planting bed assembly. Ongoing activities include crop planning, pest monitoring using integrated pest management techniques, and automated nutrient delivery calibration. The process concludes with harvest scheduling, community engagement for education, and data collection for yield optimization and environmental impact assessment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_assess       = Transition(label='Site Assess')
structure_check   = Transition(label='Structure Check')
permit_obtain     = Transition(label='Permit Obtain')
material_source   = Transition(label='Material Source')
soil_prepare      = Transition(label='Soil Prepare')
waterproof_roof   = Transition(label='Waterproof Roof')
irrigation_setup  = Transition(label='Irrigation Setup')
bed_assemble      = Transition(label='Bed Assemble')
crop_plan         = Transition(label='Crop Plan')
pest_monitor      = Transition(label='Pest Monitor')
nutrient_calibrate= Transition(label='Nutrient Calibrate')
harvest_schedule  = Transition(label='Harvest Schedule')
community_train   = Transition(label='Community Train')
yield_record      = Transition(label='Yield Record')
impact_review     = Transition(label='Impact Review')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_assess, structure_check,
    permit_obtain,
    material_source, soil_prepare,
    waterproof_roof, irrigation_setup, bed_assemble,
    crop_plan, pest_monitor, nutrient_calibrate,
    harvest_schedule, community_train, yield_record, impact_review
])

# 1. Site assessment and structural analysis precede permit obtaining
root.order.add_edge(site_assess,    permit_obtain)
root.order.add_edge(structure_check, permit_obtain)

# 2. Obtaining permits precedes sourcing materials and soil
root.order.add_edge(permit_obtain, material_source)
root.order.add_edge(permit_obtain, soil_prepare)

# 3. Sourcing precedes installation steps
for src in (material_source, soil_prepare):
    root.order.add_edge(src, waterproof_roof)
    root.order.add_edge(src, irrigation_setup)
    root.order.add_edge(src, bed_assemble)

# 4. Installation steps precede ongoing activities
for inst in (waterproof_roof, irrigation_setup, bed_assemble):
    root.order.add_edge(inst, crop_plan)
    root.order.add_edge(inst, pest_monitor)
    root.order.add_edge(inst, nutrient_calibrate)

# 5. Ongoing activities precede concluding tasks
for ongoing in (crop_plan, pest_monitor, nutrient_calibrate):
    for final in (harvest_schedule, community_train, yield_record, impact_review):
        root.order.add_edge(ongoing, final)