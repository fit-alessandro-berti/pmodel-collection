# Generated from: 69989004-cfba-496b-aa7b-808747236ae8.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farm within a densely populated city environment. It includes site assessment, modular infrastructure assembly, climate control calibration, nutrient delivery optimization, and automated harvesting integration. Special attention is given to sustainable energy use, waste recycling loops, pest management without chemicals, and real-time crop monitoring through IoT devices. Collaborative coordination with city planners, local suppliers, and technology vendors ensures compliance with urban regulations and maximizes resource efficiency. The process concludes with staff training and community engagement to promote urban agriculture awareness and long-term operational success.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Permit_Acquire = Transition(label='Permit Acquire')
Modular_Build = Transition(label='Modular Build')
Climate_Setup = Transition(label='Climate Setup')
Water_Install = Transition(label='Water Install')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Deploy = Transition(label='Sensor Deploy')
Lighting_Adjust = Transition(label='Lighting Adjust')
Pest_Inspect = Transition(label='Pest Inspect')
Waste_Cycle = Transition(label='Waste Cycle')
Energy_Sync = Transition(label='Energy Sync')
Harvest_Plan = Transition(label='Harvest Plan')
Staff_Train = Transition(label='Staff Train')
Community_Meet = Transition(label='Community Meet')

# Step 1: Initial planning partial order with Site Survey, Design Layout, Permit Acquire
planning = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, Permit_Acquire])
planning.order.add_edge(Site_Survey, Design_Layout)
planning.order.add_edge(Design_Layout, Permit_Acquire)

# Step 2: Modular infrastructure assembly and climate control calibration partial order
# Build modular structure before Climate Setup
infrastructure = StrictPartialOrder(nodes=[Modular_Build, Climate_Setup])
infrastructure.order.add_edge(Modular_Build, Climate_Setup)

# Step 3: Nutrient delivery optimization and water install concurrently with sensor deploy and lighting adjust
# We model nutrient delivery (Water Install, Nutrient Mix) before sensor deploy and lighting adjust since these depend on setup
nutrient_phase = StrictPartialOrder(nodes=[Water_Install, Nutrient_Mix])
nutrient_phase.order.add_edge(Water_Install, Nutrient_Mix)

sensor_lighting = StrictPartialOrder(nodes=[Sensor_Deploy, Lighting_Adjust])

# Step 4: Pest management (without chemicals) and waste recycling loop
# Waste cycle is a loop with possible repeated pest inspections and energy syncs
# Model pest inspect and energy sync concurrently
pest_energy = StrictPartialOrder(nodes=[Pest_Inspect, Energy_Sync])

# Loop: execute Waste Cycle, then choose to exit or do pest_energy then Waste Cycle again
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[Waste_Cycle, pest_energy])

# Step 5: Harvest planning after above
# Harvest plan depends on the end of infrastructure, nutrient phase, sensor lighting, waste loop
# We'll compose a partial order that depends on the completion of those phases before Harvest Plan

# combinational partial order of infrastructure, nutrient_phase, sensor_lighting, waste_loop (concurrent except the dependencies)
pre_harvest = StrictPartialOrder(nodes=[infrastructure, nutrient_phase, sensor_lighting, waste_loop])
# No explicit edges between these phases, meaning they can occur concurrently

# Harvest plan after all:
harvest = StrictPartialOrder(nodes=[pre_harvest, Harvest_Plan])
harvest.order.add_edge(pre_harvest, Harvest_Plan)

# Step 6: Final staff training and community meeting in parallel, both after harvest plan
final_events = StrictPartialOrder(nodes=[Staff_Train, Community_Meet])
# Both depend on Harvest_Plan
final = StrictPartialOrder(nodes=[harvest, final_events])
final.order.add_edge(harvest, final_events)

# Final root model including all phases
root = StrictPartialOrder(
    nodes=[
        planning,
        infrastructure,
        nutrient_phase,
        sensor_lighting,
        waste_loop,
        harvest,
        final_events
    ]
)

# Define edges to respect dependencies between phases
# Planning finishes before infrastructure begins
root.order.add_edge(planning, infrastructure)

# Infrastructure precedes nutrient phase and sensor_lighting (these occur after modular build & climate)
root.order.add_edge(infrastructure, nutrient_phase)
root.order.add_edge(infrastructure, sensor_lighting)

# Nutrient phase and sensor_lighting may occur concurrently, both must precede waste_loop and harvest
root.order.add_edge(nutrient_phase, waste_loop)
root.order.add_edge(sensor_lighting, waste_loop)

# Waste loop must complete before harvest (modeled inside harvest but also add order here for clarity)
root.order.add_edge(waste_loop, harvest)

# Harvest precedes final staff training and community meeting (final_events)
root.order.add_edge(harvest, final_events)