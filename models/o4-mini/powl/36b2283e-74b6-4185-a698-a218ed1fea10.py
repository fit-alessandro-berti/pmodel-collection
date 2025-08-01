# Generated from: 36b2283e-74b6-4185-a698-a218ed1fea10.json
# Description: This process outlines the complex sequence involved in establishing a sustainable urban rooftop farm on a commercial building. It includes initial site assessment for structural integrity and sunlight exposure, securing permits from local authorities, designing modular planting beds adapted to rooftop constraints, sourcing organic soil and seeds, installing automated drip irrigation systems powered by solar panels, integrating pest management strategies minimizing chemical use, scheduling crop rotation plans to optimize yield, training maintenance staff on crop care and system monitoring, implementing data collection for environmental factors, coordinating waste composting onsite, and finally launching a direct-to-consumer sales platform that connects urban residents with fresh produce. This atypical business process demands multidisciplinary coordination among architects, agronomists, engineers, and marketers to ensure both environmental sustainability and commercial viability in a constrained urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_assess       = Transition(label='Site Assess')
permit_acquire    = Transition(label='Permit Acquire')
design_layout     = Transition(label='Design Layout')
soil_source       = Transition(label='Soil Source')
seed_select       = Transition(label='Seed Select')
install_irrigation= Transition(label='Install Irrigation')
solar_setup       = Transition(label='Solar Setup')
pest_control      = Transition(label='Pest Control')
crop_rotate       = Transition(label='Crop Rotate')
staff_train       = Transition(label='Staff Train')
data_monitor      = Transition(label='Data Monitor')
waste_compost     = Transition(label='Waste Compost')
market_outreach   = Transition(label='Market Outreach')
sales_launch      = Transition(label='Sales Launch')
feedback_collect  = Transition(label='Feedback Collect')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_assess, permit_acquire, design_layout,
    soil_source, seed_select,
    install_irrigation, solar_setup,
    pest_control, crop_rotate, staff_train, data_monitor, waste_compost,
    market_outreach, sales_launch, feedback_collect
])

# Sequential dependencies
root.order.add_edge(site_assess,    permit_acquire)
root.order.add_edge(permit_acquire, design_layout)

# After layout, soil and seed sourcing can run in parallel
root.order.add_edge(design_layout, soil_source)
root.order.add_edge(design_layout, seed_select)

# Irrigation install and solar setup start only once soil and seed sourcing finish
for prep in (soil_source, seed_select):
    root.order.add_edge(prep, install_irrigation)
    root.order.add_edge(prep, solar_setup)

# Once infrastructure is in place, operational tasks run in parallel
for op in (pest_control, crop_rotate, staff_train, data_monitor, waste_compost):
    root.order.add_edge(install_irrigation, op)
    root.order.add_edge(solar_setup,       op)

# Market outreach follows staff training
root.order.add_edge(staff_train, market_outreach)

# Sales launch waits for operational readiness and outreach
for prereq in (pest_control, crop_rotate, data_monitor, waste_compost, market_outreach):
    root.order.add_edge(prereq, sales_launch)

# Feedback collection after sales launch
root.order.add_edge(sales_launch, feedback_collect)