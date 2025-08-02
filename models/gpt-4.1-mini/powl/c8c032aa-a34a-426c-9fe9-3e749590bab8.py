# Generated from: c8c032aa-a34a-426c-9fe9-3e749590bab8.json
# Description: This process describes the complex and atypical supply chain management for a vertical farming business that integrates urban agriculture with high-tech systems. It involves sourcing specialized LED lights, hydroponic nutrients, and climate control components, coordinating with local urban suppliers, scheduling growth cycles based on predictive analytics, managing energy consumption through smart grids, conducting quality inspections at multiple growth stages, and orchestrating last-mile delivery to urban retailers and direct consumers. The process also includes handling unexpected events such as equipment failure, pest outbreaks, and fluctuating market demands, requiring real-time adjustments and cross-functional collaboration between agronomists, logistics teams, and IT specialists to maintain product quality and optimize sustainability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Light_Sourcing = Transition(label='Light Sourcing')
Nutrient_Order = Transition(label='Nutrient Order')
Climate_Setup = Transition(label='Climate Setup')
Growth_Planning = Transition(label='Growth Planning')
Seed_Planting = Transition(label='Seed Planting')
Irrigation_Check = Transition(label='Irrigation Check')
Pest_Monitoring = Transition(label='Pest Monitoring')
Energy_Tracking = Transition(label='Energy Tracking')
Quality_Testing = Transition(label='Quality Testing')
Data_Analysis = Transition(label='Data Analysis')
Equipment_Repair = Transition(label='Equipment Repair')
Packaging_Prep = Transition(label='Packaging Prep')
Inventory_Update = Transition(label='Inventory Update')
Delivery_Scheduling = Transition(label='Delivery Scheduling')
Customer_Feedback = Transition(label='Customer Feedback')
Market_Forecast = Transition(label='Market Forecast')

skip = SilentTransition()

# Initial sourcing and setup partial order (LED lights, nutrients, climate control parallel sourcing)
sourcing_po = StrictPartialOrder(nodes=[Light_Sourcing, Nutrient_Order, Climate_Setup])

# Growth planning flows after sourcing
planning_po = StrictPartialOrder(nodes=[Growth_Planning, sourcing_po])
planning_po.order.add_edge(sourcing_po, Growth_Planning)

# Seed planting after planning
planting_po = StrictPartialOrder(nodes=[Seed_Planting, planning_po])
planting_po.order.add_edge(planning_po, Seed_Planting)

# Concurrent monitoring activities during growth: Irrigation_Check, Pest_Monitoring, Energy_Tracking
monitoring_po = StrictPartialOrder(nodes=[Irrigation_Check, Pest_Monitoring, Energy_Tracking])

# Quality testing after monitoring
quality_po = StrictPartialOrder(nodes=[Quality_Testing, monitoring_po])
quality_po.order.add_edge(monitoring_po, Quality_Testing)

# Data Analysis supports scheduling future growth cycles and adjustments
data_and_forecast_po = StrictPartialOrder(nodes=[Data_Analysis, Market_Forecast])

# Equipment failure and pest outbreak handled as a loop with repair and monitoring repeating until exit
# Loop body: [Pest_Monitoring], repair: Equipment_Repair

# We model a LOOP: body = Equipment_Repair, redo = Pest_Monitoring
repair_loop = OperatorPOWL(operator=Operator.LOOP, children=[Equipment_Repair, Pest_Monitoring])

# Packaging, inventory, delivery sequencing after quality test
packaging_delivery_po = StrictPartialOrder(nodes=[Packaging_Prep, Inventory_Update, Delivery_Scheduling])
packaging_delivery_po.order.add_edge(Packaging_Prep, Inventory_Update)
packaging_delivery_po.order.add_edge(Inventory_Update, Delivery_Scheduling)

# Customer feedback leads to data analysis again or ends
feedback_loop = OperatorPOWL(operator=Operator.XOR, children=[Customer_Feedback, skip])

# Connect customer feedback to data analysis and market forecast node
feedback_and_data_po = StrictPartialOrder(nodes=[feedback_loop, Data_Analysis, Market_Forecast])
feedback_and_data_po.order.add_edge(feedback_loop, Data_Analysis)
feedback_and_data_po.order.add_edge(feedback_loop, Market_Forecast)

# Assemble the main order connecting all parts

# top-level partial order includes:
# sourcing_po -> planning_po -> planting_po -> monitoring_po -> quality_po -> repair_loop -> packaging_delivery_po -> feedback_and_data_po

root = StrictPartialOrder(nodes=[
    sourcing_po,
    planning_po,
    planting_po,
    monitoring_po,
    quality_po,
    repair_loop,
    packaging_delivery_po,
    feedback_and_data_po
])

root.order.add_edge(sourcing_po, planning_po)
root.order.add_edge(planning_po, planting_po)
root.order.add_edge(planting_po, monitoring_po)
root.order.add_edge(monitoring_po, quality_po)
root.order.add_edge(quality_po, repair_loop)
root.order.add_edge(repair_loop, packaging_delivery_po)
root.order.add_edge(packaging_delivery_po, feedback_and_data_po)