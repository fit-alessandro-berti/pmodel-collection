# Generated from: c8c032aa-a34a-426c-9fe9-3e749590bab8.json
# Description: This process describes the complex and atypical supply chain management for a vertical farming business that integrates urban agriculture with high-tech systems. It involves sourcing specialized LED lights, hydroponic nutrients, and climate control components, coordinating with local urban suppliers, scheduling growth cycles based on predictive analytics, managing energy consumption through smart grids, conducting quality inspections at multiple growth stages, and orchestrating last-mile delivery to urban retailers and direct consumers. The process also includes handling unexpected events such as equipment failure, pest outbreaks, and fluctuating market demands, requiring real-time adjustments and cross-functional collaboration between agronomists, logistics teams, and IT specialists to maintain product quality and optimize sustainability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define basic activities
light_sourcing = Transition(label='Light Sourcing')
nutrient_order = Transition(label='Nutrient Order')
climate_setup = Transition(label='Climate Setup')
growth_planning = Transition(label='Growth Planning')
seed_planting = Transition(label='Seed Planting')
irrigation_check = Transition(label='Irrigation Check')
pest_monitoring = Transition(label='Pest Monitoring')
energy_tracking = Transition(label='Energy Tracking')
quality_testing = Transition(label='Quality Testing')
data_analysis = Transition(label='Data Analysis')
equipment_repair = Transition(label='Equipment Repair')
packaging_prep = Transition(label='Packaging Prep')
inventory_update = Transition(label='Inventory Update')
market_forecast = Transition(label='Market Forecast')
delivery_scheduling = Transition(label='Delivery Scheduling')
customer_feedback = Transition(label='Customer Feedback')

# Silent transitions for looping and optional repair
skip_equipment = SilentTransition()
skip_loop = SilentTransition()

# Choice: either perform equipment repair or skip
equip_choice = OperatorPOWL(operator=Operator.XOR, children=[equipment_repair, skip_equipment])

# One cycle of growth monitoring and testing
cycle = StrictPartialOrder(nodes=[
    irrigation_check,
    pest_monitoring,
    energy_tracking,
    equip_choice,
    quality_testing,
    data_analysis
])
cycle.order.add_edge(irrigation_check, pest_monitoring)
cycle.order.add_edge(pest_monitoring, energy_tracking)
cycle.order.add_edge(energy_tracking, equip_choice)
cycle.order.add_edge(equip_choice, quality_testing)
cycle.order.add_edge(quality_testing, data_analysis)

# Loop the cycle until the growth phase is complete
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, skip_loop])

# Top‐level partial order of the entire process
root = StrictPartialOrder(nodes=[
    light_sourcing,
    nutrient_order,
    climate_setup,
    growth_planning,
    seed_planting,
    growth_loop,
    packaging_prep,
    inventory_update,
    market_forecast,
    delivery_scheduling,
    customer_feedback
])
# Dependencies
root.order.add_edge(light_sourcing, growth_planning)
root.order.add_edge(nutrient_order, growth_planning)
root.order.add_edge(climate_setup, growth_planning)
root.order.add_edge(growth_planning, seed_planting)
root.order.add_edge(seed_planting, growth_loop)
root.order.add_edge(growth_loop, packaging_prep)
root.order.add_edge(packaging_prep, inventory_update)
root.order.add_edge(inventory_update, delivery_scheduling)
root.order.add_edge(market_forecast, delivery_scheduling)
root.order.add_edge(delivery_scheduling, customer_feedback)