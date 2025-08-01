# Generated from: e210eac0-39ba-4b3c-bf5e-ef253a5bd431.json
# Description: This process outlines the intricate steps involved in establishing a fully operational urban vertical farm within a constrained city environment. It includes site analysis, environmental compliance, modular system design, nutrient cycling optimization, integration of renewable energy sources, automated climate control calibration, and continuous yield monitoring. The process also covers community engagement to ensure local support, waste management strategies to minimize footprint, data analytics for crop optimization, and iterative feedback loops for system improvements. This atypical yet highly sustainable business model requires cross-disciplinary coordination between agriculture, technology, and urban planning sectors, aiming to revolutionize food production in dense metropolitan areas while maintaining ecological balance and economic viability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey       = Transition(label='Site Survey')
regulation_check  = Transition(label='Regulation Check')
modular_design    = Transition(label='Modular Design')
material_sourcing = Transition(label='Material Sourcing')
system_assembly   = Transition(label='System Assembly')
energy_integration= Transition(label='Energy Integration')
climate_setup     = Transition(label='Climate Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
automation_config = Transition(label='Automation Config')
crop_seeding      = Transition(label='Crop Seeding')
growth_monitoring = Transition(label='Growth Monitoring')
waste_handling    = Transition(label='Waste Handling')
community_meet    = Transition(label='Community Meet')
data_analysis     = Transition(label='Data Analysis')
feedback_loop     = Transition(label='Feedback Loop')
yield_forecast    = Transition(label='Yield Forecast')

# Loop: Data Analysis (A), then optionally Feedback Loop (B) repeatedly, then exit
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_analysis, feedback_loop]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    regulation_check,
    modular_design,
    material_sourcing,
    system_assembly,
    energy_integration,
    climate_setup,
    nutrient_mix,
    automation_config,
    crop_seeding,
    growth_monitoring,
    waste_handling,
    community_meet,
    loop,
    yield_forecast
])

# Add control‐flow edges
root.order.add_edge(site_survey,       regulation_check)
root.order.add_edge(regulation_check,  modular_design)
root.order.add_edge(modular_design,    material_sourcing)
root.order.add_edge(material_sourcing, system_assembly)

# After assembly, integrate all subsystems in parallel
root.order.add_edge(system_assembly, energy_integration)
root.order.add_edge(system_assembly, climate_setup)
root.order.add_edge(system_assembly, nutrient_mix)
root.order.add_edge(system_assembly, automation_config)

# All integrations must finish before seeding
root.order.add_edge(energy_integration,  crop_seeding)
root.order.add_edge(climate_setup,       crop_seeding)
root.order.add_edge(nutrient_mix,        crop_seeding)
root.order.add_edge(automation_config,   crop_seeding)

# Seeding -> Growth Monitoring
root.order.add_edge(crop_seeding, growth_monitoring)

# After monitoring: waste handling, community meeting, and enter the analysis‐feedback loop
root.order.add_edge(growth_monitoring, waste_handling)
root.order.add_edge(growth_monitoring, community_meet)
root.order.add_edge(growth_monitoring, loop)

# After loop exit, produce the yield forecast
root.order.add_edge(loop, yield_forecast)