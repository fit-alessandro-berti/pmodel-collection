# Generated from: 8bcdec4b-ec04-490e-a686-557154b07e74.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm on a commercial building. It includes site analysis considering structural integrity and sunlight exposure, procurement of specialized soil and hydroponic systems, coordination with city authorities for permits, installation of irrigation and energy-efficient lighting, selection and planting of diverse crops suited for urban climates, ongoing monitoring for pest control using organic methods, integration of data-driven growth analytics, and finally, the distribution of produce through local markets and community-supported agriculture programs. The process requires collaboration between architects, agronomists, environmental engineers, and logistics teams to ensure a viable, eco-friendly, and profitable urban farming operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
site_survey = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
sunlight_map = Transition(label='Sunlight Map')

permit_request = Transition(label='Permit Request')

soil_sourcing = Transition(label='Soil Sourcing')
hydroponics_setup = Transition(label='Hydroponics Setup')

irrigation_install = Transition(label='Irrigation Install')
lighting_setup = Transition(label='Lighting Setup')

crop_selection = Transition(label='Crop Selection')
planting_seeds = Transition(label='Planting Seeds')

pest_monitoring = Transition(label='Pest Monitoring')
organic_treatment = Transition(label='Organic Treatment')

data_analytics = Transition(label='Data Analytics')

harvest_planning = Transition(label='Harvest Planning')

market_delivery = Transition(label='Market Delivery')
community_outreach = Transition(label='Community Outreach')

# Site Analysis partial order (Site Survey -> Structural Check and Sunlight Map concurrent after Structural Check)
site_analysis = StrictPartialOrder(
    nodes=[site_survey, structural_check, sunlight_map]
)
site_analysis.order.add_edge(site_survey, structural_check)
site_analysis.order.add_edge(structural_check, sunlight_map)

# Procurement partial order (Soil Sourcing and Hydroponics Setup in parallel)
procurement = StrictPartialOrder(
    nodes=[soil_sourcing, hydroponics_setup]
)
# no order edges, concurrent procurement

# Installation partial order (Irrigation Install and Lighting Setup in parallel)
installation = StrictPartialOrder(
    nodes=[irrigation_install, lighting_setup]
)
# no order edges, concurrent installation

# Crop establishment partial order (Crop Selection -> Planting Seeds)
crop_establishment = StrictPartialOrder(
    nodes=[crop_selection, planting_seeds]
)
crop_establishment.order.add_edge(crop_selection, planting_seeds)

# Pest control loop: Pest Monitoring followed optionally by Organic Treatment,
# model the loop: do Pest Monitoring, then choose either exit or Organic Treatment then repeat
organic_treatment_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pest_monitoring, organic_treatment]
)

# Monitoring branch includes the pest control loop and then Data Analytics
monitoring = StrictPartialOrder(
    nodes=[organic_treatment_loop, data_analytics]
)
monitoring.order.add_edge(organic_treatment_loop, data_analytics)

# Coordination: site_analysis must finish before permit_request
coordination = StrictPartialOrder(
    nodes=[site_analysis, permit_request]
)
coordination.order.add_edge(site_analysis, permit_request)

# Overall setup partial order:
# Coordination -> Procurement and Installation (concurrent)
# Procurement and Installation must finish before Crop Establishment
setup = StrictPartialOrder(
    nodes=[coordination, procurement, installation]
)
setup.order.add_edge(coordination, procurement)
setup.order.add_edge(coordination, installation)

# Crop Establishment depends on setup completion
crop_phase = StrictPartialOrder(
    nodes=[setup, crop_establishment]
)
crop_phase.order.add_edge(setup, crop_establishment)

# Harvest Planning after Data Analytics and Crop Establishment
harvest_prep = StrictPartialOrder(
    nodes=[monitoring, crop_phase, harvest_planning]
)
harvest_prep.order.add_edge(crop_phase, monitoring)
# harvest_planning depends on monitoring and crop_phase
harvest_prep.order.add_edge(monitoring, harvest_planning)

# Final distribution: Market Delivery and Community Outreach concurrent after Harvest Planning
distribution = StrictPartialOrder(
    nodes=[harvest_prep, market_delivery, community_outreach]
)
distribution.order.add_edge(harvest_prep, market_delivery)
distribution.order.add_edge(harvest_prep, community_outreach)

# Root node includes all and partial orders already handle dependencies
root = distribution