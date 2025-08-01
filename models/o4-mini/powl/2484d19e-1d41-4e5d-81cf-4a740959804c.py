# Generated from: 2484d19e-1d41-4e5d-81cf-4a740959804c.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban vertical farm within a densely populated city. It includes site analysis, modular design, environmental control calibration, nutrient cycling optimization, and integration of AI-driven monitoring systems. The process ensures minimal resource consumption by recycling water and organic waste, supports continuous crop growth through automated lighting schedules, and involves community engagement for local produce distribution. Additionally, it addresses regulatory compliance, supply chain logistics, and scalability assessment to adapt to changing urban demands, making it an atypical yet highly realistic business model in modern agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
material_src    = Transition(label='Material Sourcing')
module_assembly = Transition(label='Module Assembly')
system_wiring   = Transition(label='System Wiring')
climate_setup   = Transition(label='Climate Setup')
sensor_install  = Transition(label='Sensor Install')
ai_integration  = Transition(label='AI Integration')
lighting_sched  = Transition(label='Lighting Schedule')
crop_seeding    = Transition(label='Crop Seeding')
water_recycle   = Transition(label='Water Recycling')
nutrient_mix    = Transition(label='Nutrient Mix')
waste_proc      = Transition(label='Waste Processing')
growth_mon      = Transition(label='Growth Monitoring')
yield_analysis  = Transition(label='Yield Analysis')
regulation_chk  = Transition(label='Regulation Check')
market_setup    = Transition(label='Market Setup')

# 1) Initial setup & installation in strict order
init = StrictPartialOrder(nodes=[
    site_survey, design_layout, material_src,
    module_assembly, system_wiring,
    climate_setup, sensor_install,
    ai_integration, lighting_sched, crop_seeding
])
init.order.add_edge(site_survey,     design_layout)
init.order.add_edge(design_layout,   material_src)
init.order.add_edge(material_src,    module_assembly)
init.order.add_edge(module_assembly, system_wiring)
init.order.add_edge(system_wiring,   climate_setup)
init.order.add_edge(system_wiring,   sensor_install)
init.order.add_edge(climate_setup,   lighting_sched)
init.order.add_edge(sensor_install,  ai_integration)
init.order.add_edge(lighting_sched,  crop_seeding)
init.order.add_edge(ai_integration,  crop_seeding)

# 2) Nutrient‐cycling loop: Water Recycling -> Nutrient Mix -> Waste Processing
cycle = StrictPartialOrder(nodes=[water_recycle, nutrient_mix, waste_proc])
cycle.order.add_edge(water_recycle, nutrient_mix)
cycle.order.add_edge(nutrient_mix,  waste_proc)
skip_cycle = SilentTransition()
recycling_loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, skip_cycle])

# 3) Growth‐monitoring loop (continuous checks)
skip_gm = SilentTransition()
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_mon, skip_gm])

# 4) Finalization: Yield Analysis -> Regulation Check -> Market Setup
#    Both loops must complete before we proceed
root = StrictPartialOrder(nodes=[
    init, recycling_loop, growth_loop,
    yield_analysis, regulation_chk, market_setup
])
# dependencies
root.order.add_edge(init,            recycling_loop)
root.order.add_edge(init,            growth_loop)
root.order.add_edge(recycling_loop,  yield_analysis)
root.order.add_edge(growth_loop,     yield_analysis)
root.order.add_edge(yield_analysis,  regulation_chk)
root.order.add_edge(regulation_chk,  market_setup)