# Generated from: 16c83739-a0b8-401c-b7e8-db2fab689638.json
# Description: This process outlines the complex and atypical workflow involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It includes site analysis, modular system design, climate control calibration, nutrient cycling optimization, automated pest management integration, and real-time crop monitoring. The process also involves securing local permits, community engagement for urban agriculture acceptance, energy-efficient lighting configuration, water recycling setup, and post-harvest logistics planning. Each step must be carefully coordinated to ensure sustainable production, minimal environmental impact, and scalability within dense city environments, addressing challenges unique to urban farming such as space constraints and regulatory compliance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions for each activity
site          = Transition(label='Site Survey')
permit        = Transition(label='Permit Review')
community     = Transition(label='Community Meet')
modular       = Transition(label='Modular Design')
climate       = Transition(label='Climate Setup')
nutrient      = Transition(label='Nutrient Mix')
pest          = Transition(label='Pest Control')
lighting      = Transition(label='Lighting Config')
water         = Transition(label='Water Cycle')
energy        = Transition(label='Energy Audit')
sensor        = Transition(label='Sensor Install')
seeding       = Transition(label='Crop Seeding')
monitor       = Transition(label='Growth Monitor')
analysis      = Transition(label='Data Analysis')
harvest       = Transition(label='Harvest Prep')
waste         = Transition(label='Waste Reuse')
delivery      = Transition(label='Delivery Plan')

# Build the strict partial order
root = StrictPartialOrder(nodes=[
    site, permit, community, modular,
    climate, nutrient, pest, lighting, water,
    energy, sensor, seeding, monitor,
    analysis, harvest, waste, delivery
])

# Site Survey precedes permitting, community engagement, and modular design
root.order.add_edge(site, permit)
root.order.add_edge(site, community)
root.order.add_edge(site, modular)

# Permit Review and Community Meet must complete before Modular Design
root.order.add_edge(permit, modular)
root.order.add_edge(community, modular)

# After Modular Design, configure all subsystems in parallel
root.order.add_edge(modular, climate)
root.order.add_edge(modular, nutrient)
root.order.add_edge(modular, pest)
root.order.add_edge(modular, lighting)
root.order.add_edge(modular, water)

# All subsystems feed into an Energy Audit
for step in [climate, nutrient, pest, lighting, water]:
    root.order.add_edge(step, energy)

# Then install sensors and proceed to crop seeding
root.order.add_edge(energy, sensor)
root.order.add_edge(sensor, seeding)

# Follow the crop lifecycle: planting, monitoring, analysis
root.order.add_edge(seeding, monitor)
root.order.add_edge(monitor, analysis)

# Post-harvest workflow
root.order.add_edge(analysis, harvest)
root.order.add_edge(harvest, waste)
root.order.add_edge(waste, delivery)