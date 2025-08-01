# Generated from: 9cc12842-5f5e-40bb-bde3-8852a9154108.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed commercial building. It involves site analysis, modular rack installation, hydroponic system integration, nutrient cycling optimization, environmental control calibration, automated pest detection, crop scheduling, data-driven yield forecasting, waste recycling, energy consumption monitoring, and community engagement to ensure sustainability and profitability in a constrained urban environment. The process balances technology deployment with ecological principles and local regulations to create a scalable food production model that addresses urban food deserts and reduces supply chain emissions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site = Transition(label='Site Survey')
design = Transition(label='Design Layout')
rack = Transition(label='Rack Setup')
hydro = Transition(label='Install Hydroponics')
calibrate = Transition(label='Calibrate Sensors')
optimize = Transition(label='Optimize Nutrients')
lighting = Transition(label='Configure Lighting')
pest = Transition(label='Pest Detection')
schedule = Transition(label='Crop Scheduling')
analysis = Transition(label='Data Analysis')
waste = Transition(label='Waste Processing')
energy = Transition(label='Energy Monitoring')
training = Transition(label='Staff Training')
quality = Transition(label='Quality Check')
community = Transition(label='Community Outreach')

# Build the partial‐order structure
root = StrictPartialOrder(nodes=[
    site, design, rack, hydro, calibrate,
    optimize, lighting, pest, schedule,
    analysis, waste, energy, training,
    quality, community
])

# Add the control‐flow edges representing dependencies
root.order.add_edge(site, design)
root.order.add_edge(design, rack)
root.order.add_edge(design, hydro)
root.order.add_edge(rack, calibrate)
root.order.add_edge(hydro, calibrate)
root.order.add_edge(calibrate, optimize)
root.order.add_edge(calibrate, lighting)
root.order.add_edge(optimize, pest)
root.order.add_edge(optimize, schedule)
root.order.add_edge(lighting, pest)
root.order.add_edge(lighting, schedule)
root.order.add_edge(pest, analysis)
root.order.add_edge(schedule, analysis)
root.order.add_edge(analysis, waste)
root.order.add_edge(analysis, energy)
root.order.add_edge(waste, training)
root.order.add_edge(energy, training)
root.order.add_edge(training, quality)
root.order.add_edge(quality, community)