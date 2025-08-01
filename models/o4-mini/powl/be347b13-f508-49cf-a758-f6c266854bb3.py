# Generated from: be347b13-f508-49cf-a758-f6c266854bb3.json
# Description: This process outlines the establishment of a fully automated urban vertical farm within a repurposed industrial building. It involves site assessment, modular system installation, nutrient solution calibration, environmental control programming, crop selection based on market trends, integration of robotics for planting and harvesting, real-time data monitoring for growth optimization, waste recycling protocols, and supply chain coordination for distribution. The process ensures sustainability, maximizes yield in limited space, and adapts dynamically to urban agricultural demands while complying with city regulations and minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site        = Transition(label="Site Survey")
design      = Transition(label="System Design")
module      = Transition(label="Module Setup")
nutrient    = Transition(label="Nutrient Prep")
env         = Transition(label="Env Control")
sensor      = Transition(label="Sensor Install")
robot       = Transition(label="Robot Config")
crop        = Transition(label="Crop Selection")

seeding     = Transition(label="Plant Seeding")
monitor     = Transition(label="Growth Monitor")
waste       = Transition(label="Waste Recycle")
analysis    = Transition(label="Data Analysis")
quality     = Transition(label="Quality Check")
harvest     = Transition(label="Harvest Plan")
logistics   = Transition(label="Logistics Prep")
market      = Transition(label="Market Sync")

# 1. Initial setup phase: site survey through crop selection
setup = StrictPartialOrder(nodes=[
    site, design, module,
    nutrient, env, sensor, robot,
    crop
])
setup.order.add_edge(site, design)
setup.order.add_edge(design, module)
setup.order.add_edge(module, nutrient)
setup.order.add_edge(module, env)
setup.order.add_edge(module, sensor)
setup.order.add_edge(module, robot)
setup.order.add_edge(nutrient, crop)
setup.order.add_edge(env, crop)

# 2. One production cycle: seeding → (monitor ∥ waste) → analysis → quality → harvest → logistics → market
cycle = StrictPartialOrder(nodes=[
    seeding, monitor, waste,
    analysis, quality,
    harvest, logistics, market
])
cycle.order.add_edge(seeding, monitor)
cycle.order.add_edge(seeding, waste)
cycle.order.add_edge(monitor, analysis)
cycle.order.add_edge(analysis, quality)
cycle.order.add_edge(quality, harvest)
cycle.order.add_edge(harvest, logistics)
cycle.order.add_edge(logistics, market)

# 3. Loop over production cycles until exit
skip = SilentTransition()
production_loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, skip])

# 4. Root partial order: perform setup, then enter the production loop
root = StrictPartialOrder(nodes=[setup, production_loop])
root.order.add_edge(setup, production_loop)