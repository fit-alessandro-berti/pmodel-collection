# Generated from: 7f788fc5-115c-4554-adc1-e39c82d12ab1.json
# Description: This process details the comprehensive steps involved in establishing an urban rooftop farm on a commercial building. It includes assessing structural integrity, navigating local regulations, designing modular planting systems, sourcing sustainable materials, installing irrigation and solar-powered monitoring devices, training staff on urban agriculture techniques, implementing pest management strategies, and setting up a direct-to-consumer sales platform. The process ensures environmental compliance, maximizes crop yield in limited space, and integrates technology for efficient farm management while fostering community engagement through workshops and events.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site = Transition(label='Site Assess')
reg = Transition(label='Regulation Check')
struct = Transition(label='Structural Survey')
design = Transition(label='Design Layout')
material = Transition(label='Material Sourcing')
irrig = Transition(label='Irrigation Setup')
solar = Transition(label='Solar Install')
monitor = Transition(label='Monitoring Setup')
soil = Transition(label='Soil Prep')
seed = Transition(label='Seed Selection')
plant = Transition(label='Planting Phase')
pest = Transition(label='Pest Control')
training = Transition(label='Staff Training')
harvest = Transition(label='Harvest Plan')
sales = Transition(label='Sales Launch')
event = Transition(label='Community Event')
waste = Transition(label='Waste Manage')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site, reg, struct, design, material,
    irrig, solar, monitor, training,
    soil, seed, plant, pest,
    harvest, sales, event, waste
])

# Structural assessment and regulatory check in parallel after site assessment
root.order.add_edge(site, reg)
root.order.add_edge(site, struct)

# Design follows both regulation check and structural survey
root.order.add_edge(reg, design)
root.order.add_edge(struct, design)

# Material sourcing follows design
root.order.add_edge(design, material)

# Infrastructure setups after materials are available
root.order.add_edge(material, irrig)
root.order.add_edge(material, solar)
root.order.add_edge(material, monitor)

# Staff training once infrastructure is in place
root.order.add_edge(irrig, training)
root.order.add_edge(solar, training)
root.order.add_edge(monitor, training)

# Agricultural operations follow training
root.order.add_edge(training, soil)
root.order.add_edge(soil, seed)
root.order.add_edge(seed, plant)
root.order.add_edge(plant, pest)

# Harvest planning and execution
root.order.add_edge(pest, harvest)

# Sales and community engagement after harvest
root.order.add_edge(harvest, sales)
root.order.add_edge(sales, event)

# Waste management after harvest
root.order.add_edge(harvest, waste)