# Generated from: 9725c04e-86a4-4e10-aa32-4ff30950bbe0.json
# Description: This process outlines the complex steps involved in launching an urban vertical farming operation within a densely populated city environment. It includes site analysis, regulatory compliance, technology integration, crop selection, and community engagement to ensure sustainable food production. The process addresses challenges such as limited space, energy efficiency, and supply chain logistics, while incorporating advanced hydroponic systems, IoT monitoring, and local distribution networks. Collaboration with city planners, environmental experts, and marketing teams is crucial to balance innovation with urban ecosystem demands, leading to a scalable, eco-friendly farming solution that supports local economies and reduces carbon footprints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities as Transitions
Site_Survey = Transition(label='Site Survey')
Permit_Filing = Transition(label='Permit Filing')
Tech_Setup = Transition(label='Tech Setup')
Crop_Research = Transition(label='Crop Research')
Vendor_Selection = Transition(label='Vendor Selection')
System_Build = Transition(label='System Build')
Seed_Sourcing = Transition(label='Seed Sourcing')
Nutrient_Mix = Transition(label='Nutrient Mix')
IoT_Config = Transition(label='IoT Config')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Packaging = Transition(label='Packaging')
Market_Launch = Transition(label='Market Launch')
Community_Meet = Transition(label='Community Meet')
Logistics_Map = Transition(label='Logistics Map')
Feedback_Loop = Transition(label='Feedback Loop')

# Loop: Pest control and feedback loop monitoring repeated during growth monitoring
pest_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Growth_Monitor,
    OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, Feedback_Loop])
])

# Partial order for system setup and tech integration
tech_integration = StrictPartialOrder(nodes=[Tech_Setup, IoT_Config])
tech_integration.order.add_edge(Tech_Setup, IoT_Config)

# Partial order for crop preparation: Seed Sourcing and Nutrient Mix concurrent
crop_prep = StrictPartialOrder(nodes=[Seed_Sourcing, Nutrient_Mix])

# Partial order for packaging and market launch
pack_market = StrictPartialOrder(nodes=[Packaging, Market_Launch])
pack_market.order.add_edge(Packaging, Market_Launch)

# Partial order for community engagement and logistics mapping
community_logistics = StrictPartialOrder(nodes=[Community_Meet, Logistics_Map])

# Partial order for system build after vendor selection and tech integration
system_build_phase = StrictPartialOrder(nodes=[Vendor_Selection, tech_integration, System_Build])
system_build_phase.order.add_edge(Vendor_Selection, System_Build)
system_build_phase.order.add_edge(tech_integration, System_Build)

# Partial order for site survey leading to permit filing and crop research
site_permit_crop = StrictPartialOrder(nodes=[Site_Survey, Permit_Filing, Crop_Research])
site_permit_crop.order.add_edge(Site_Survey, Permit_Filing)
site_permit_crop.order.add_edge(Site_Survey, Crop_Research)

# Harvest plan after pest/feedback loop
harvest_section = StrictPartialOrder(nodes=[pest_feedback_loop, Harvest_Plan])
harvest_section.order.add_edge(pest_feedback_loop, Harvest_Plan)

# Top-level partial order for entire process
root = StrictPartialOrder(nodes=[
    site_permit_crop,
    system_build_phase,
    crop_prep,
    harvest_section,
    pack_market,
    community_logistics
])

# Define dependencies (partial order edges) between major phases
root.order.add_edge(site_permit_crop, system_build_phase)  # Site/permit/crop before system build
root.order.add_edge(system_build_phase, crop_prep)         # System build before crop prep
root.order.add_edge(crop_prep, harvest_section)            # Crop prep before harvest
root.order.add_edge(harvest_section, pack_market)          # Harvest before packaging and market
root.order.add_edge(pack_market, community_logistics)      # Packaging and market before community/logistics