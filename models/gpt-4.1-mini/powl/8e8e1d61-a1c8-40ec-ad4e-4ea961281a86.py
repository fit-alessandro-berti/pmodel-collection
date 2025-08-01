# Generated from: 8e8e1d61-a1c8-40ec-ad4e-4ea961281a86.json
# Description: This process outlines the steps required to establish an urban rooftop farming operation on a commercial building. It involves assessing structural integrity, selecting suitable crops for rooftop conditions, designing irrigation and nutrient delivery systems, obtaining necessary permits, installing solar-powered sensors for environmental monitoring, and launching a community engagement program to promote local produce. The process also incorporates waste recycling protocols, pest management without chemicals, and continuous yield optimization through data analysis, ensuring sustainability and profitability in an unconventional agriculture setting within a dense urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
load_testing = Transition(label='Load Testing')
crop_selection = Transition(label='Crop Selection')
design_layout = Transition(label='Design Layout')
permit_filing = Transition(label='Permit Filing')
sensor_setup = Transition(label='Sensor Setup')
irrigation_install = Transition(label='Irrigation Install')
nutrient_mix = Transition(label='Nutrient Mix')
solar_paneling = Transition(label='Solar Paneling')
waste_sorting = Transition(label='Waste Sorting')
pest_control = Transition(label='Pest Control')
data_collection = Transition(label='Data Collection')
community_meet = Transition(label='Community Meet')
yield_review = Transition(label='Yield Review')
report_draft = Transition(label='Report Draft')

# Step 1-2: Assess structural integrity as partial order (Site Survey -> Load Testing)
structural_check = StrictPartialOrder(nodes=[site_survey, load_testing])
structural_check.order.add_edge(site_survey, load_testing)

# Step 3-4: Crop Selection -> Design Layout (includes irrigation and nutrient mix)
# Irrigation Install and Nutrient Mix seem concurrent, both part of the layout design
# Since both irrigation_install and nutrient_mix are related closely, combine them in PO with design_layout following selection
crop_and_design = StrictPartialOrder(
    nodes=[crop_selection, design_layout, irrigation_install, nutrient_mix]
)
crop_and_design.order.add_edge(crop_selection, design_layout)
crop_and_design.order.add_edge(design_layout, irrigation_install)
crop_and_design.order.add_edge(design_layout, nutrient_mix)
# irrigation_install and nutrient_mix are concurrent (no order between them)

# Step 5: Permit Filing
# This probably must happen after structural checks and crop/design done
# We'll add permit filing after these activities

# Step 6-9: Sensor Setup and Solar Paneling
# sensor_setup and solar_paneling likely concurrent, both tech setup tasks
# Waste Sorting and Pest Control are sustainability measures, presumably concurrent and can happen after permit filing.
# Data Collection, Community Meet, Yield Review, Report Draft form the continuous yield optimization and community engagement loops
# We'll organize these next.

# Tech setup partial order: sensor_setup || solar_paneling
tech_setup = StrictPartialOrder(nodes=[sensor_setup, solar_paneling])
# no edges as they are concurrent

# Sustainability tasks: waste_sorting and pest_control concurrent
sustainability = StrictPartialOrder(nodes=[waste_sorting, pest_control])
# no edges

# Yield optimization process:
# Data Collection -> Yield Review -> Report Draft
# Community Meet is parallel to this, both presumably concurrent and possibly synchronize later

yield_optimization = StrictPartialOrder(nodes=[data_collection, yield_review, report_draft])
yield_optimization.order.add_edge(data_collection, yield_review)
yield_optimization.order.add_edge(yield_review, report_draft)

# Community engagement concurrent with yield optimization:
# We'll combine them by a partial order with concurrency (no ordering between community_meet and yield_optimization)

engagement = StrictPartialOrder(nodes=[community_meet, yield_optimization])
# no edges between community_meet and yield_optimization.nodes, so concurrent

# Now combine all major phases sequentially:
# Full partial order with edges:
# structural_check --> crop_and_design --> permit_filing --> tech_setup & sustainability concurrently --> engagement

# First create partial order nodes
# Use permit_filing as single transition

# Combine tech_setup and sustainability concurrently:
tech_and_sustain = StrictPartialOrder(nodes=[tech_setup, sustainability])
# no order edges => concurrent

# Now build the root partial order with nodes:
root = StrictPartialOrder(
    nodes=[structural_check, crop_and_design, permit_filing, tech_and_sustain, engagement]
)
root.order.add_edge(structural_check, crop_and_design)
root.order.add_edge(crop_and_design, permit_filing)
root.order.add_edge(permit_filing, tech_and_sustain)
root.order.add_edge(tech_and_sustain, engagement)