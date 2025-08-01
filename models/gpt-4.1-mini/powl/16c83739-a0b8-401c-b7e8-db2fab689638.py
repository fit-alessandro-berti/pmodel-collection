# Generated from: 16c83739-a0b8-401c-b7e8-db2fab689638.json
# Description: This process outlines the complex and atypical workflow involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It includes site analysis, modular system design, climate control calibration, nutrient cycling optimization, automated pest management integration, and real-time crop monitoring. The process also involves securing local permits, community engagement for urban agriculture acceptance, energy-efficient lighting configuration, water recycling setup, and post-harvest logistics planning. Each step must be carefully coordinated to ensure sustainable production, minimal environmental impact, and scalability within dense city environments, addressing challenges unique to urban farming such as space constraints and regulatory compliance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
permit_review = Transition(label='Permit Review')
modular_design = Transition(label='Modular Design')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
pest_control = Transition(label='Pest Control')
lighting_config = Transition(label='Lighting Config')
water_cycle = Transition(label='Water Cycle')
energy_audit = Transition(label='Energy Audit')
sensor_install = Transition(label='Sensor Install')
crop_seeding = Transition(label='Crop Seeding')
growth_monitor = Transition(label='Growth Monitor')
harvest_prep = Transition(label='Harvest Prep')
waste_reuse = Transition(label='Waste Reuse')
delivery_plan = Transition(label='Delivery Plan')
community_meet = Transition(label='Community Meet')
data_analysis = Transition(label='Data Analysis')

# Construct partial orders reflecting logical dependencies with concurrency where possible

# Site analysis and permitting
site_permit = StrictPartialOrder(nodes=[site_survey, permit_review])
site_permit.order.add_edge(site_survey, permit_review)

# Modular Design after permit review and site survey
# But modular design also depends on energy audit and community meeting, so those are concurrent with site survey/permit review
energy_community = StrictPartialOrder(nodes=[energy_audit, community_meet])
# No order between energy_audit and community_meet, they are concurrent

# Create partial order joining all prerequisites before modular design
pre_modular = StrictPartialOrder(nodes=[site_permit, permit_review, energy_community, modular_design])

# Actually we need to unify these partial orders properly:
# site_permit has site_survey and permit_review with order survey-->permit
# energy_community has energy_audit and community_meet concurrent
# After all these, modular_design runs.

# So combined partial order with nodes:
# site_survey, permit_review, energy_audit, community_meet, modular_design
pre_modular2 = StrictPartialOrder(nodes=[site_survey, permit_review, energy_audit, community_meet, modular_design])
pre_modular2.order.add_edge(site_survey, permit_review)
pre_modular2.order.add_edge(permit_review, modular_design)
pre_modular2.order.add_edge(energy_audit, modular_design)
pre_modular2.order.add_edge(community_meet, modular_design)

# After modular design, parallel configuration of climate setup and water cycle and lighting
config_parallel = StrictPartialOrder(
    nodes=[climate_setup, water_cycle, lighting_config]
)
# no order edges means fully concurrent

# Nutrient mix depends on modular design and climate setup
nutrient_part = StrictPartialOrder(nodes=[modular_design, climate_setup, nutrient_mix])
nutrient_part.order.add_edge(modular_design, nutrient_mix)
nutrient_part.order.add_edge(climate_setup, nutrient_mix)

# Pest control depends on modular design and water cycle (pest control needs water cycle set)
pest_part = StrictPartialOrder(nodes=[modular_design, water_cycle, pest_control])
pest_part.order.add_edge(modular_design, pest_control)
pest_part.order.add_edge(water_cycle, pest_control)

# Sensor Install and Crop Seeding depend on pest control, lighting config and nutrient mix
sensor_crop = StrictPartialOrder(
    nodes=[pest_control, lighting_config, nutrient_mix, sensor_install, crop_seeding]
)
sensor_crop.order.add_edge(pest_control, sensor_install)
sensor_crop.order.add_edge(pest_control, crop_seeding)
sensor_crop.order.add_edge(lighting_config, sensor_install)
sensor_crop.order.add_edge(lighting_config, crop_seeding)
sensor_crop.order.add_edge(nutrient_mix, sensor_install)
sensor_crop.order.add_edge(nutrient_mix, crop_seeding)

# Growth monitor after crop seeding and sensor install
growth_part = StrictPartialOrder(nodes=[crop_seeding, sensor_install, growth_monitor])
growth_part.order.add_edge(crop_seeding, growth_monitor)
growth_part.order.add_edge(sensor_install, growth_monitor)

# Harvest prep after growth monitor
harvest_part = StrictPartialOrder(nodes=[growth_monitor, harvest_prep])
harvest_part.order.add_edge(growth_monitor, harvest_prep)

# Waste reuse can start after harvest prep
waste_part = StrictPartialOrder(nodes=[harvest_prep, waste_reuse])
waste_part.order.add_edge(harvest_prep, waste_reuse)

# Delivery plan depends on harvest prep and waste reuse (needs info from waste reuse)
delivery_part = StrictPartialOrder(nodes=[harvest_prep, waste_reuse, delivery_plan])
delivery_part.order.add_edge(harvest_prep, delivery_plan)
delivery_part.order.add_edge(waste_reuse, delivery_plan)

# Data analysis can be concurrent with delivery plan, after growth monitor
data_analysis_part = StrictPartialOrder(nodes=[growth_monitor, data_analysis])
data_analysis_part.order.add_edge(growth_monitor, data_analysis)

# Final model organizes the above partial orders and their dependencies
# Combine pre_modular2, config_parallel, nutrient_part, pest_part, sensor_crop, growth_part,
# harvest_part, waste_part, delivery_part, data_analysis_part with correct orders

# Root nodes:
# pre_modular2 finishes modular design -> config_parallel and nutrient_part and pest_part start
# nutrient_part and pest_part precede sensor_crop
# sensor_crop precedes growth_part
# growth_part precedes harvest_part and data_analysis_part
# harvest_part precedes waste_part and delivery_part

root = StrictPartialOrder(
    nodes=[
        pre_modular2,
        config_parallel,
        nutrient_part,
        pest_part,
        sensor_crop,
        growth_part,
        harvest_part,
        waste_part,
        delivery_part,
        data_analysis_part,
    ]
)

# Add control flow dependencies

# After pre_modular2 modular_design node is done, config_parallel, nutrient_part and pest_part can start concurrently
# modular_design node is inside pre_modular2, so link pre_modular2 -> config_parallel etc.

root.order.add_edge(pre_modular2, config_parallel)
root.order.add_edge(pre_modular2, nutrient_part)
root.order.add_edge(pre_modular2, pest_part)

# nutrient_part and pest_part precede sensor_crop
root.order.add_edge(nutrient_part, sensor_crop)
root.order.add_edge(pest_part, sensor_crop)

# sensor_crop precedes growth_part
root.order.add_edge(sensor_crop, growth_part)

# growth_part precedes harvest_part and data_analysis_part
root.order.add_edge(growth_part, harvest_part)
root.order.add_edge(growth_part, data_analysis_part)

# harvest_part precedes waste_part and delivery_part
root.order.add_edge(harvest_part, waste_part)
root.order.add_edge(harvest_part, delivery_part)