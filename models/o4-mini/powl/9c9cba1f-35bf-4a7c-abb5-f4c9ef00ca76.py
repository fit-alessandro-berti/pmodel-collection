# Generated from: 9c9cba1f-35bf-4a7c-abb5-f4c9ef00ca76.json
# Description: This process outlines the establishment of an urban vertical farming system that integrates hydroponics, renewable energy, and AI-driven environmental controls to optimize crop yield in limited city spaces. It involves site analysis, modular assembly, nutrient calibration, system integration, continuous monitoring, predictive maintenance, and adaptive harvesting schedules to ensure sustainable, high-efficiency food production within urban environments. The process also includes community engagement and regulatory compliance to align with local policies and promote urban agricultural awareness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
site = Transition(label='Site Survey')
design = Transition(label='Design Layout')
fab = Transition(label='Module Fabrication')
hydro = Transition(label='Hydro Setup')
energy = Transition(label='Energy Install')
sensor = Transition(label='Sensor Deploy')
ai = Transition(label='AI Configuration')
nutrient = Transition(label='Nutrient Mix')
water = Transition(label='Water Testing')
lighting = Transition(label='Lighting Adjust')
plant = Transition(label='Crop Planting')

monitor = Transition(label='Growth Monitor')
analysis = Transition(label='Data Analysis')
maint = Transition(label='Maintenance Check')

harvest = Transition(label='Harvest Plan')
waste = Transition(label='Waste Manage')

community = Transition(label='Community Meet')
compliance = Transition(label='Compliance Audit')

# Define the loop body: Analysis -> Maintenance
seq_analysis_maint = StrictPartialOrder(nodes=[analysis, maint])
seq_analysis_maint.order.add_edge(analysis, maint)

# Loop: after each Growth Monitor, optionally repeat Analysis->Maintenance then another Growth Monitor
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor, seq_analysis_maint]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site, design, fab,
    hydro, energy, sensor, ai,
    nutrient, water, lighting,
    plant, loop, harvest, waste,
    community, compliance
])

# Main construction flow
root.order.add_edge(site, design)
root.order.add_edge(design, fab)

root.order.add_edge(fab, hydro)
root.order.add_edge(fab, energy)
root.order.add_edge(fab, sensor)
root.order.add_edge(fab, ai)

root.order.add_edge(hydro, nutrient)
root.order.add_edge(hydro, water)
root.order.add_edge(hydro, lighting)

# All setup/calibration and installations complete before planting
for pre in [nutrient, water, lighting, energy, sensor, ai]:
    root.order.add_edge(pre, plant)

# After planting, enter the monitoring/maintenance loop
root.order.add_edge(plant, loop)

# After exiting the loop, plan harvest and then manage waste
root.order.add_edge(loop, harvest)
root.order.add_edge(harvest, waste)

# Community engagement and compliance can start after the site survey, in parallel
root.order.add_edge(site, community)
root.order.add_edge(site, compliance)