# Generated from: cda6171e-e73b-451f-b871-de0145446484.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It involves site analysis, structural modifications, environmental control installations, hydroponic system setup, nutrient solution preparation, seed selection, automated planting, growth monitoring via IoT sensors, pest control using integrated biological methods, energy optimization through smart grid integration, water recycling implementation, harvesting automation, packaging with minimal waste materials, distribution logistics coordination, and post-harvest data analysis to improve yield efficiency. Each step requires cross-disciplinary collaboration among architects, agronomists, engineers, and supply chain specialists to adapt traditional farming techniques to a compact, sustainable, and tech-driven urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
sa      = Transition(label="Site Analysis")
sc      = Transition(label="Structure Check")
ml      = Transition(label="Modify Layout")
hvac    = Transition(label="Install HVAC")
hydro   = Transition(label="Setup Hydroponics")
nut     = Transition(label="Prepare Nutrients")
seeds   = Transition(label="Select Seeds")
plant   = Transition(label="Automate Planting")
sensors = Transition(label="Deploy Sensors")
pest    = Transition(label="Pest Control")
energy  = Transition(label="Optimize Energy")
water   = Transition(label="Recycle Water")
harv    = Transition(label="Automate Harvest")
pack    = Transition(label="Package Crops")
coord   = Transition(label="Coordinate Delivery")
analyze = Transition(label="Analyze Data")

# Build the loop body for ongoing monitoring & interventions: pest control, energy optimization, water recycling
monitor_body = StrictPartialOrder(
    nodes=[pest, energy, water]
    # no ordering → all three can happen in any interleaving
)

# LOOP node: first deploy sensors, then repeatedly do monitor_body before re-checking/continuing
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sensors, monitor_body]
)

# Root partial order
root = StrictPartialOrder(
    nodes=[
        sa, sc, ml, hvac,
        hydro, nut, seeds,
        plant, monitor_loop,
        harv, pack, coord, analyze
    ]
)

# Define the control‐flow edges
root.order.add_edge(sa, sc)
root.order.add_edge(sc, ml)
root.order.add_edge(ml, hvac)
root.order.add_edge(hvac, hydro)

# After hydroponics is set up, nutrients & seed‐selection can run in parallel
root.order.add_edge(hydro, nut)
root.order.add_edge(hydro, seeds)

# Both nutrient prep & seed selection must finish before planting
root.order.add_edge(nut, plant)
root.order.add_edge(seeds, plant)

# Planting precedes sensor deployment & the monitoring loop
root.order.add_edge(plant, monitor_loop)

# Once the loop exits, proceed to harvest, then packaging, delivery, and analysis
root.order.add_edge(monitor_loop, harv)
root.order.add_edge(harv, pack)
root.order.add_edge(pack, coord)
root.order.add_edge(coord, analyze)