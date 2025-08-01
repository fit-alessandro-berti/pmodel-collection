# Generated from: 36b2283e-74b6-4185-a698-a218ed1fea10.json
# Description: This process outlines the complex sequence involved in establishing a sustainable urban rooftop farm on a commercial building. It includes initial site assessment for structural integrity and sunlight exposure, securing permits from local authorities, designing modular planting beds adapted to rooftop constraints, sourcing organic soil and seeds, installing automated drip irrigation systems powered by solar panels, integrating pest management strategies minimizing chemical use, scheduling crop rotation plans to optimize yield, training maintenance staff on crop care and system monitoring, implementing data collection for environmental factors, coordinating waste composting onsite, and finally launching a direct-to-consumer sales platform that connects urban residents with fresh produce. This atypical business process demands multidisciplinary coordination among architects, agronomists, engineers, and marketers to ensure both environmental sustainability and commercial viability in a constrained urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
site_assess = Transition(label='Site Assess')
permit_acquire = Transition(label='Permit Acquire')
design_layout = Transition(label='Design Layout')
soil_source = Transition(label='Soil Source')
seed_select = Transition(label='Seed Select')
install_irrigation = Transition(label='Install Irrigation')
solar_setup = Transition(label='Solar Setup')
pest_control = Transition(label='Pest Control')
crop_rotate = Transition(label='Crop Rotate')
staff_train = Transition(label='Staff Train')
data_monitor = Transition(label='Data Monitor')
waste_compost = Transition(label='Waste Compost')
sales_launch = Transition(label='Sales Launch')
market_outreach = Transition(label='Market Outreach')
feedback_collect = Transition(label='Feedback Collect')

# The process description implies a partial order with some concurrency and sequencing:
# 1. Initial assessment (site_assess) then permit_acquire
# 2. After permit, design layout
# 3. Then soil and seed sourcing can occur concurrently
# 4. After soil and seed ready, install irrigation and solar setup run concurrently
# 5. Pest control follows installation concurrently with crop rotation planning
# 6. Staff training can overlap with data monitoring and waste composting
# 7. Finally sales_launch after market_outreach and feedback_collect (feedback_collect after sales_launch implied)
#
# Some concurrency and partial orders:
# "market_outreach" before "sales_launch"
# "feedback_collect" after "sales_launch"
# Also, loop could model crop_rotate repeated could be extended with repeat loop, but the prompt does not explicitly require loops
# We'll keep Crop Rotate once for optimization plan, no loop

# Define partial orders:

# First partial order: site_assess --> permit_acquire --> design_layout
phase1 = StrictPartialOrder(nodes=[site_assess, permit_acquire, design_layout])
phase1.order.add_edge(site_assess, permit_acquire)
phase1.order.add_edge(permit_acquire, design_layout)

# Second partial order: soil_source and seed_select concurrent after design_layout
soil_seed = StrictPartialOrder(nodes=[design_layout, soil_source, seed_select])
# design_layout -> soil_source, design_layout -> seed_select
soil_seed.order.add_edge(design_layout, soil_source)
soil_seed.order.add_edge(design_layout, seed_select)

# Third partial order: install_irrigation and solar_setup concurrent after soil_source and seed_select completed
irrigation_solar = StrictPartialOrder(
    nodes=[soil_source, seed_select, install_irrigation, solar_setup]
)
# soil_source and seed_select both before install_irrigation and solar_setup
irrigation_solar.order.add_edge(soil_source, install_irrigation)
irrigation_solar.order.add_edge(seed_select, install_irrigation)
irrigation_solar.order.add_edge(soil_source, solar_setup)
irrigation_solar.order.add_edge(seed_select, solar_setup)

# Fourth partial order: pest_control and crop_rotate run concurrently after installation done
pest_crop = StrictPartialOrder(
    nodes=[install_irrigation, solar_setup, pest_control, crop_rotate]
)
pest_crop.order.add_edge(install_irrigation, pest_control)
pest_crop.order.add_edge(solar_setup, pest_control)
pest_crop.order.add_edge(install_irrigation, crop_rotate)
pest_crop.order.add_edge(solar_setup, crop_rotate)

# Fifth partial order: staff_train, data_monitor and waste_compost concurrent after pest_control and crop_rotate
staff_data_waste = StrictPartialOrder(
    nodes=[pest_control, crop_rotate, staff_train, data_monitor, waste_compost]
)
staff_data_waste.order.add_edge(pest_control, staff_train)
staff_data_waste.order.add_edge(crop_rotate, staff_train)
staff_data_waste.order.add_edge(pest_control, data_monitor)
staff_data_waste.order.add_edge(crop_rotate, data_monitor)
staff_data_waste.order.add_edge(pest_control, waste_compost)
staff_data_waste.order.add_edge(crop_rotate, waste_compost)

# Sixth partial order: market_outreach before sales_launch, feedback_collect after sales_launch
market_sales_feedback = StrictPartialOrder(
    nodes=[market_outreach, sales_launch, feedback_collect]
)
market_sales_feedback.order.add_edge(market_outreach, sales_launch)
market_sales_feedback.order.add_edge(sales_launch, feedback_collect)

# Compose major phases together respecting ordering:
# phase1 -> soil_seed -> irrigation_solar -> pest_crop -> staff_data_waste -> market_sales_feedback

root = StrictPartialOrder(
    nodes=[
        phase1,
        soil_seed,
        irrigation_solar,
        pest_crop,
        staff_data_waste,
        market_sales_feedback,
    ]
)
root.order.add_edge(phase1, soil_seed)
root.order.add_edge(soil_seed, irrigation_solar)
root.order.add_edge(irrigation_solar, pest_crop)
root.order.add_edge(pest_crop, staff_data_waste)
root.order.add_edge(staff_data_waste, market_sales_feedback)