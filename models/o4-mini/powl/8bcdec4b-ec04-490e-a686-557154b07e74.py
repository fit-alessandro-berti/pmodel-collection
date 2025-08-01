# Generated from: 8bcdec4b-ec04-490e-a686-557154b07e74.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm on a commercial building. It includes site analysis considering structural integrity and sunlight exposure, procurement of specialized soil and hydroponic systems, coordination with city authorities for permits, installation of irrigation and energy-efficient lighting, selection and planting of diverse crops suited for urban climates, ongoing monitoring for pest control using organic methods, integration of data-driven growth analytics, and finally, the distribution of produce through local markets and community-supported agriculture programs. The process requires collaboration between architects, agronomists, environmental engineers, and logistics teams to ensure a viable, eco-friendly, and profitable urban farming operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
struct_check     = Transition(label='Structural Check')
sunlight_map     = Transition(label='Sunlight Map')
permit_request   = Transition(label='Permit Request')
soil_sourcing    = Transition(label='Soil Sourcing')
hydroponics_setup= Transition(label='Hydroponics Setup')
irrigation_install = Transition(label='Irrigation Install')
lighting_setup   = Transition(label='Lighting Setup')
crop_selection   = Transition(label='Crop Selection')
planting_seeds   = Transition(label='Planting Seeds')
pest_monitoring  = Transition(label='Pest Monitoring')
organic_treatment= Transition(label='Organic Treatment')
data_analytics   = Transition(label='Data Analytics')
harvest_planning = Transition(label='Harvest Planning')
market_delivery  = Transition(label='Market Delivery')
community_outreach = Transition(label='Community Outreach')

# Loop for ongoing monitoring and treatment
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitoring, organic_treatment])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, struct_check, sunlight_map,
    permit_request, soil_sourcing, hydroponics_setup,
    irrigation_install, lighting_setup,
    crop_selection, planting_seeds,
    monitor_loop, data_analytics,
    harvest_planning, market_delivery, community_outreach
])

# Site survey feeds into the two parallel checks
root.order.add_edge(site_survey, struct_check)
root.order.add_edge(site_survey, sunlight_map)

# Both checks must finish before procurement and permit request
root.order.add_edge(struct_check, permit_request)
root.order.add_edge(sunlight_map, permit_request)
root.order.add_edge(struct_check, soil_sourcing)
root.order.add_edge(sunlight_map, soil_sourcing)
root.order.add_edge(struct_check, hydroponics_setup)
root.order.add_edge(sunlight_map, hydroponics_setup)

# Permit and hydroponics setup precede installation tasks
root.order.add_edge(permit_request, irrigation_install)
root.order.add_edge(hydroponics_setup, irrigation_install)
root.order.add_edge(permit_request, lighting_setup)
root.order.add_edge(hydroponics_setup, lighting_setup)

# Installation feeds into crop selection
root.order.add_edge(irrigation_install, crop_selection)
root.order.add_edge(lighting_setup, crop_selection)
# Soil sourcing is required before crop selection
root.order.add_edge(soil_sourcing, crop_selection)

# Crop selection -> planting seeds
root.order.add_edge(crop_selection, planting_seeds)

# After planting, start the monitoring loop and data analytics in parallel
root.order.add_edge(planting_seeds, monitor_loop)
root.order.add_edge(planting_seeds, data_analytics)

# Both monitoring analytics and loop completion lead to harvest planning
root.order.add_edge(monitor_loop, harvest_planning)
root.order.add_edge(data_analytics, harvest_planning)

# Final distribution tasks in parallel after planning
root.order.add_edge(harvest_planning, market_delivery)
root.order.add_edge(harvest_planning, community_outreach)