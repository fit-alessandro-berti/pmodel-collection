# Generated from: 2cb8a47a-f03f-4646-9e7a-78e5d3cb0bc9.json
# Description: This process outlines the establishment of an urban vertical farm that integrates advanced hydroponic systems with AI-driven environmental controls. It involves site evaluation in dense metropolitan areas, modular infrastructure assembly, nutrient solution formulation, and real-time sensor calibration. The process also includes labor scheduling for crop monitoring, pest management using biocontrol agents, and dynamic yield forecasting. Additionally, it covers regulatory compliance for urban agriculture, marketing to local retailers, harvesting automation, and waste recycling protocols to ensure sustainability and profitability in constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site       = Transition(label='Site Survey')
design     = Transition(label='Design Layout')
permits    = Transition(label='Permits Obtain')
structure  = Transition(label='Structure Build')
hydro      = Transition(label='Hydro Setup')
sensor     = Transition(label='Sensor Install')
nutrient   = Transition(label='Nutrient Mix')
ai         = Transition(label='AI Config')
plant      = Transition(label='Crop Planting')
labor      = Transition(label='Labor Assign')
monitor    = Transition(label='Growth Monitor')
pest       = Transition(label='Pest Control')
yieldf     = Transition(label='Yield Forecast')
harvest    = Transition(label='Harvest Automate')
waste      = Transition(label='Waste Recycle')
market     = Transition(label='Market Engage')

# Loop body: pest control and yield forecasting can happen concurrently
body = StrictPartialOrder(nodes=[pest, yieldf])
# Define the monitoring loop: do Growth Monitor, then either exit or do (Pest Control || Yield Forecast) then Growth Monitor again
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor, body])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site, design, permits, structure, hydro, sensor,
    nutrient, ai, plant, labor, monitoring_loop,
    harvest, waste, market
])

# Define the control‐flow edges
root.order.add_edge(site, design)
root.order.add_edge(design, permits)
root.order.add_edge(permits, structure)
root.order.add_edge(structure, hydro)
root.order.add_edge(hydro, sensor)
root.order.add_edge(sensor, nutrient)
root.order.add_edge(nutrient, ai)
root.order.add_edge(ai, plant)
root.order.add_edge(plant, labor)
root.order.add_edge(labor, monitoring_loop)
root.order.add_edge(monitoring_loop, harvest)
root.order.add_edge(harvest, waste)
root.order.add_edge(waste, market)