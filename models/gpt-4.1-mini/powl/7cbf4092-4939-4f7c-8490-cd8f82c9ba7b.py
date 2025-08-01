# Generated from: 7cbf4092-4939-4f7c-8490-cd8f82c9ba7b.json
# Description: This process details the establishment of a vertical farming operation within an urban environment, integrating sustainable agricultural practices with advanced technology. It involves site analysis, modular construction, environmental controls calibration, nutrient solution management, and crop cycle optimization. The procedure also includes stakeholder coordination, regulatory compliance checks, energy use monitoring, and waste recycling strategies to maximize yield and minimize footprint in a confined city space. Continuous data collection and adaptive growth algorithms ensure efficient resource use and crop quality throughout multiple harvest cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Material_Sourcing = Transition(label='Material Sourcing')
Module_Assembly = Transition(label='Module Assembly')
Irrigation_Setup = Transition(label='Irrigation Setup')
Lighting_Install = Transition(label='Lighting Install')
Climate_Control = Transition(label='Climate Control')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Planting = Transition(label='Seed Planting')
Growth_Monitoring = Transition(label='Growth Monitoring')
Pest_Screening = Transition(label='Pest Screening')
Harvest_Planning = Transition(label='Harvest Planning')
Yield_Analysis = Transition(label='Yield Analysis')
Waste_Handling = Transition(label='Waste Handling')
Energy_Tracking = Transition(label='Energy Tracking')
Regulation_Check = Transition(label='Regulation Check')
Stakeholder_Meet = Transition(label='Stakeholder Meet')

# Define initial partial order for construction steps:
# Site Survey -> Design Layout -> Material Sourcing -> Module Assembly
construction_po = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, Material_Sourcing, Module_Assembly])
construction_po.order.add_edge(Site_Survey, Design_Layout)
construction_po.order.add_edge(Design_Layout, Material_Sourcing)
construction_po.order.add_edge(Material_Sourcing, Module_Assembly)

# Environmental controls calibration:
env_controls_po = StrictPartialOrder(nodes=[Irrigation_Setup, Lighting_Install, Climate_Control])
# They can be done concurrently (no order edges)

# Nutrient solution management steps:
nutrient_po = StrictPartialOrder(nodes=[Nutrient_Mix, Seed_Planting])
nutrient_po.order.add_edge(Nutrient_Mix, Seed_Planting)

# Crop cycle repeated *loop*:
# The crop cycle sequence:
# Growth Monitoring -> Pest Screening -> Harvest Planning -> Yield Analysis
crop_cycle_seq = StrictPartialOrder(nodes=[Growth_Monitoring, Pest_Screening, Harvest_Planning, Yield_Analysis])
crop_cycle_seq.order.add_edge(Growth_Monitoring, Pest_Screening)
crop_cycle_seq.order.add_edge(Pest_Screening, Harvest_Planning)
crop_cycle_seq.order.add_edge(Harvest_Planning, Yield_Analysis)

# Looping crop cycle: after Yield Analysis, decide to repeat or exit
# According to * (A,B): execute A then choose exit or perform B then A again.
# Here A = crop_cycle_seq, B = SilentTransition() indicating "continue"
continue_silent = SilentTransition()
crop_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_cycle_seq, continue_silent])

# Operations for sustainability and administrative tasks:
# Waste Handling, Energy Tracking, Regulation Check, Stakeholder Meet
# Let's assume Waste Handling and Energy Tracking can be done concurrently, then followed by Reg Check and Stakeholder Meet in order.

sustain_po = StrictPartialOrder(
    nodes=[Waste_Handling, Energy_Tracking, Regulation_Check, Stakeholder_Meet]
)
# Waste Handling and Energy Tracking concurrent (no edge between)
sustain_po.order.add_edge(Waste_Handling, Regulation_Check)
sustain_po.order.add_edge(Energy_Tracking, Regulation_Check)
sustain_po.order.add_edge(Regulation_Check, Stakeholder_Meet)

# Now combine environmental controls calibration and nutrient management concurrently (both independent)
env_nutrient_po = StrictPartialOrder(nodes=[env_controls_po, nutrient_po])

# Because env_controls_po and nutrient_po are PO objects, include them as nodes in a PO:
env_nutrient_po = StrictPartialOrder(nodes=[Irrigation_Setup, Lighting_Install, Climate_Control, Nutrient_Mix, Seed_Planting])
# Irrigation_Setup, Lighting_Install, Climate_Control concurrent (no order edges)
# Nutrient_Mix -> Seed_Planting
env_nutrient_po.order.add_edge(Nutrient_Mix, Seed_Planting)

# Combine all main parts:
# construction_po -> env_nutrient_po -> crop_loop -> sustain_po
root = StrictPartialOrder(
    nodes=[construction_po, env_nutrient_po, crop_loop, sustain_po]
)
root.order.add_edge(construction_po, env_nutrient_po)
root.order.add_edge(env_nutrient_po, crop_loop)
root.order.add_edge(crop_loop, sustain_po)