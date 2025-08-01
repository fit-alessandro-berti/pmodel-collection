# Generated from: 2938294c-a1ca-4013-8751-9cd5bd84024e.json
# Description: This process outlines the intricate and atypical steps involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It combines elements of architectural retrofit, hydroponic system integration, climate control calibration, and sustainable resource management. The process begins with structural assessments and zoning clearances, followed by modular rack installation and nutrient solution formulation. Specialized tasks include LED spectrum tuning for various plant species, automated pest detection, and real-time data analytics for yield optimization. The workflow integrates cross-disciplinary teams coordinating logistics, technology deployment, and regulatory compliance to ensure a high-efficiency, eco-friendly urban agricultural production system that maximizes space utilization and minimizes environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
assess           = Transition(label='Assess Structure')
permits         = Transition(label='Obtain Permits')
layout          = Transition(label='Design Layout')
racks           = Transition(label='Install Racks')
hydro           = Transition(label='Setup Hydroponics')
lighting        = Transition(label='Configure Lighting')
sensors         = Transition(label='Calibrate Sensors')
inspections     = Transition(label='Conduct Inspections')
mix_nutrients   = Transition(label='Mix Nutrients')
test_irrigation = Transition(label='Test Irrigation')
seeding         = Transition(label='Plant Seeding')
automation      = Transition(label='Implement Automation')
analytics       = Transition(label='Deploy Analytics')
monitor         = Transition(label='Monitor Growth')
adjust          = Transition(label='Adjust Environment')
waste           = Transition(label='Manage Waste')
training        = Transition(label='Train Staff')
launch_ops      = Transition(label='Launch Operations')

# Define the loop body for growth monitoring and environment adjustment + waste management
# B is a small partial order with adjust and waste done in parallel
B = StrictPartialOrder(nodes=[adjust, waste])
# The LOOP operator: first 'monitor', then either exit or do B (adjust+waste) then monitor again
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor, B])

# Build the top‐level strict partial order
root = StrictPartialOrder(nodes=[
    assess, permits, layout, racks,
    hydro, lighting, sensors, inspections,
    mix_nutrients, test_irrigation, seeding,
    automation, analytics,
    growth_loop, training, launch_ops
])

# Add the control‐flow (partial‐order) edges
root.order.add_edge(assess, permits)
root.order.add_edge(permits, layout)
root.order.add_edge(layout, racks)

# After racks, four tasks can start in parallel
root.order.add_edge(racks, hydro)
root.order.add_edge(racks, lighting)
root.order.add_edge(racks, sensors)
root.order.add_edge(racks, inspections)

# Hydroponics branch
root.order.add_edge(hydro, mix_nutrients)
root.order.add_edge(hydro, test_irrigation)

# Seeding waits for nutrients, irrigation test, lighting, sensors, and inspections
root.order.add_edge(mix_nutrients, seeding)
root.order.add_edge(test_irrigation, seeding)
root.order.add_edge(lighting, seeding)
root.order.add_edge(sensors, seeding)
root.order.add_edge(inspections, seeding)

# After seeding: automation -> analytics
root.order.add_edge(seeding, automation)
root.order.add_edge(automation, analytics)

# Analytics spawns the growth loop and staff training in parallel
root.order.add_edge(analytics, growth_loop)
root.order.add_edge(analytics, training)

# Both the loop and training must finish before launch
root.order.add_edge(growth_loop, launch_ops)
root.order.add_edge(training, launch_ops)