# Generated from: c884c0ad-4b6c-478e-8553-2c8264c78c4d.json
# Description: This process manages the end-to-end supply chain for an urban vertical farming enterprise specializing in locally grown produce using hydroponic systems. It begins with seed sourcing from specialized suppliers and continues through germination monitoring, nutrient solution preparation, automated planting, and environmental condition adjustment. The process includes continuous crop health scanning with IoT sensors, integrated pest management without pesticides, and dynamic growth rate analysis to optimize yield. Harvesting is automated with robotic arms, followed by sorting and quality verification based on size and freshness. Packaging uses biodegradable materials and is tracked via blockchain for transparency. The distribution phase coordinates with last-mile delivery partners using AI route optimization to ensure freshness upon arrival. Customer feedback is collected digitally to improve future crop cycles, and waste is minimized through composting and recycling programs integrated into the system. Data analytics drive predictive maintenance of equipment and forecast demand to adjust planting schedules dynamically, ensuring sustainability and profitability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed = Transition(label='Seed Sourcing')
germ = Transition(label='Germination Check')
nutrient = Transition(label='Nutrient Mix')
planting = Transition(label='Automated Planting')
climate = Transition(label='Climate Control')
scanning = Transition(label='Crop Scanning')
pest = Transition(label='Pest Monitoring')
analysis = Transition(label='Growth Analysis')
harvest = Transition(label='Robotic Harvest')
sort = Transition(label='Quality Sort')
packaging = Transition(label='Eco Packaging')
tracking = Transition(label='Blockchain Track')
routing = Transition(label='Route Planning')
feedback = Transition(label='Feedback Collect')
recycling = Transition(label='Waste Recycling')
data_analytics = Transition(label='Data Analytics')
demand = Transition(label='Demand Forecast')
maintenance = Transition(label='Maintenance Alert')

# Loop for continuous analytics → forecasting → maintenance
forecast_maintenance = StrictPartialOrder(nodes=[demand, maintenance])
forecast_maintenance.order.add_edge(demand, maintenance)
analytics_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analytics, forecast_maintenance])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    seed, germ, nutrient, planting, climate,
    scanning, pest, analysis,
    harvest, sort, packaging, tracking, routing,
    feedback, recycling, analytics_loop
])

# Sequential supply‐chain ordering
root.order.add_edge(seed, germ)
root.order.add_edge(germ, nutrient)
root.order.add_edge(nutrient, planting)
root.order.add_edge(planting, climate)

# Concurrent monitoring after climate control
root.order.add_edge(climate, scanning)
root.order.add_edge(climate, pest)
root.order.add_edge(climate, analysis)

# Join before harvesting
root.order.add_edge(scanning, harvest)
root.order.add_edge(pest, harvest)
root.order.add_edge(analysis, harvest)

# Post‐harvest workflow
root.order.add_edge(harvest, sort)
root.order.add_edge(sort, packaging)
root.order.add_edge(packaging, tracking)
root.order.add_edge(tracking, routing)
root.order.add_edge(routing, feedback)

# After feedback, run recycling and analytics loop in parallel
root.order.add_edge(feedback, recycling)
root.order.add_edge(feedback, analytics_loop)