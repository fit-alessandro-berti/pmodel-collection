# Generated from: 5568f432-baa5-4bc0-b5c7-33d7e6beb14b.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming system within a repurposed industrial building. It includes site evaluation, environmental control integration, hydroponic system installation, and multi-tiered crop planning. The process requires coordination between architects, agricultural scientists, IoT specialists, and supply chain managers to ensure optimal crop yield, energy efficiency, and sustainability. Continuous monitoring, pest control, and harvest scheduling are critical activities, alongside waste recycling and community engagement initiatives to promote local food production and reduce carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site = Transition(label="Site Survey")
design = Transition(label="Design Layout")
audit = Transition(label="Structural Audit")
enviro = Transition(label="Enviro Setup")
hydro = Transition(label="Hydro Install")
light = Transition(label="Lighting Config")
sensor = Transition(label="Sensor Deploy")
crop = Transition(label="Crop Selection")
seed = Transition(label="Seed Planting")
water = Transition(label="Water Cycling")
nutrient = Transition(label="Nutrient Mix")
pest = Transition(label="Pest Monitor")
yieldt = Transition(label="Yield Tracking")
data = Transition(label="Data Analysis")
waste = Transition(label="Waste Recycle")
market = Transition(label="Market Launch")
community = Transition(label="Community Meet")
energy = Transition(label="Energy Audit")

# Monitoring sequence: Pest Monitor -> Yield Tracking -> Data Analysis
mon_seq = StrictPartialOrder(nodes=[pest, yieldt, data])
mon_seq.order.add_edge(pest, yieldt)
mon_seq.order.add_edge(yieldt, data)

# Loop: continuous monitoring until exit
loop_mon = OperatorPOWL(operator=Operator.LOOP, children=[mon_seq, mon_seq])

# Build the full partial order
root = StrictPartialOrder(
    nodes=[
        site, design, audit, enviro,
        hydro, light, sensor,
        crop, seed, water, nutrient,
        loop_mon,
        waste, market, community, energy
    ]
)

# Site evaluation → design & audit in parallel
root.order.add_edge(site, design)
root.order.add_edge(site, audit)

# Design & audit → environmental setup
root.order.add_edge(design, enviro)
root.order.add_edge(audit, enviro)

# Enviro setup → hydroponics, lighting, sensors in parallel
root.order.add_edge(enviro, hydro)
root.order.add_edge(enviro, light)
root.order.add_edge(enviro, sensor)

# Hydro/lighting/sensors → crop planning
root.order.add_edge(hydro, crop)
root.order.add_edge(light, crop)
root.order.add_edge(sensor, crop)

# Crop selection → seeding
root.order.add_edge(crop, seed)

# Seeding → water cycling & nutrient mixing in parallel
root.order.add_edge(seed, water)
root.order.add_edge(seed, nutrient)

# After water & nutrients → enter monitoring loop
root.order.add_edge(water, loop_mon)
root.order.add_edge(nutrient, loop_mon)

# After monitoring loop → waste recycle, market launch, community meet, energy audit
root.order.add_edge(loop_mon, waste)
root.order.add_edge(loop_mon, market)
root.order.add_edge(loop_mon, community)
root.order.add_edge(loop_mon, energy)