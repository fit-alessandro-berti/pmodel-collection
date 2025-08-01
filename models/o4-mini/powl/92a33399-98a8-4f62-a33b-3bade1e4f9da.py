# Generated from: 92a33399-98a8-4f62-a33b-3bade1e4f9da.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm in a dense metropolitan area. It includes initial site assessment, securing permits, soil testing, modular bed construction, irrigation system design, selecting climate-resilient crops, integrating renewable energy sources, pest management planning, community engagement, and ongoing yield optimization. The workflow balances environmental, regulatory, and social factors to promote urban agriculture as a viable food source while minimizing ecological footprint and maximizing space utilization on rooftops with structural and safety constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey       = Transition(label="Site Survey")
permit_filing     = Transition(label="Permit Filing")
soil_testing      = Transition(label="Soil Testing")
bed_assembly      = Transition(label="Bed Assembly")
irrigation_setup  = Transition(label="Irrigation Setup")
crop_selection    = Transition(label="Crop Selection")
energy_integration= Transition(label="Energy Integration")
pest_control      = Transition(label="Pest Control")
community_meet    = Transition(label="Community Meet")
nutrient_planning = Transition(label="Nutrient Planning")
water_recycling   = Transition(label="Water Recycling")
growth_monitoring = Transition(label="Growth Monitoring")
yield_analysis    = Transition(label="Yield Analysis")
safety_inspection = Transition(label="Safety Inspection")
waste_composting  = Transition(label="Waste Composting")

# Build the loop body: after each Growth Monitoring, we perform Yield Analysis,
# Nutrient Planning and Water Recycling (these can be concurrent after the analysis)
loop_body = StrictPartialOrder(nodes=[yield_analysis, nutrient_planning, water_recycling])
loop_body.order.add_edge(yield_analysis, nutrient_planning)
loop_body.order.add_edge(yield_analysis, water_recycling)

# LOOP node: A = Growth Monitoring, B = loop_body
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring, loop_body])

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        permit_filing,
        soil_testing,
        bed_assembly,
        irrigation_setup,
        crop_selection,
        energy_integration,
        pest_control,
        community_meet,
        monitoring_loop,
        safety_inspection,
        waste_composting
    ]
)

# Define the sequence/dependencies
root.order.add_edge(site_survey,       permit_filing)
root.order.add_edge(permit_filing,     soil_testing)
root.order.add_edge(soil_testing,      bed_assembly)
root.order.add_edge(bed_assembly,      irrigation_setup)
root.order.add_edge(irrigation_setup,  crop_selection)
root.order.add_edge(crop_selection,    energy_integration)
root.order.add_edge(energy_integration,pest_control)
root.order.add_edge(pest_control,      community_meet)
root.order.add_edge(community_meet,    monitoring_loop)
root.order.add_edge(monitoring_loop,   safety_inspection)
root.order.add_edge(safety_inspection, waste_composting)