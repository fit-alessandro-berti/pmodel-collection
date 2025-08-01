# Generated from: bfcd7eaa-48c6-4314-a378-693b32ea1a95.json
# Description: This process involves the complex orchestration of establishing an urban vertical farm within a repurposed industrial building. It includes site assessment, modular structure design, climate control integration, hydroponic system installation, nutrient solution calibration, automated lighting setup, crop selection, growth monitoring, pest management, yield forecasting, energy optimization, waste recycling, market analysis, and finally, distribution logistics to ensure fresh produce reaches local markets efficiently. Each step requires coordination across engineering, agricultural science, and logistics teams to maximize space utilization and sustainability in a densely populated environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Structure_Build = Transition(label='Structure Build')
Climate_Setup = Transition(label='Climate Setup')
Hydroponics_Install = Transition(label='Hydroponics Install')
Nutrient_Prep = Transition(label='Nutrient Prep')
Lighting_Config = Transition(label='Lighting Config')
Crop_Select = Transition(label='Crop Select')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Yield_Forecast = Transition(label='Yield Forecast')
Energy_Audit = Transition(label='Energy Audit')
Waste_Manage = Transition(label='Waste Manage')
Market_Study = Transition(label='Market Study')
Logistics_Plan = Transition(label='Logistics Plan')

# Construct the workflow as a partial order representing topological dependencies:
# From the description:
# Start with 'Site Survey'
# Then 'Design Layout'
# Then 'Structure Build'
# Then parallel tasks: 'Climate Setup', 'Hydroponics Install', 'Nutrient Prep', 'Lighting Config' (all depend on Structure Build)
# Then 'Crop Select' depends on all above
# Then 'Growth Monitor' depends on 'Crop Select'
# Then 'Pest Control' and 'Yield Forecast' depend on 'Growth Monitor'
# Then 'Energy Audit' and 'Waste Manage' depend on 'Yield Forecast' and 'Pest Control' (assumed)
# Then 'Market Study' depends on 'Energy Audit' and 'Waste Manage'
# Then finally 'Logistics Plan' depends on 'Market Study'

nodes = [
    Site_Survey,
    Design_Layout,
    Structure_Build,
    Climate_Setup,
    Hydroponics_Install,
    Nutrient_Prep,
    Lighting_Config,
    Crop_Select,
    Growth_Monitor,
    Pest_Control,
    Yield_Forecast,
    Energy_Audit,
    Waste_Manage,
    Market_Study,
    Logistics_Plan,
]

root = StrictPartialOrder(nodes=nodes)

# Define order edges based on dependencies

root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Structure_Build)

# Parallel tasks depend on Structure Build
root.order.add_edge(Structure_Build, Climate_Setup)
root.order.add_edge(Structure_Build, Hydroponics_Install)
root.order.add_edge(Structure_Build, Nutrient_Prep)
root.order.add_edge(Structure_Build, Lighting_Config)

# Crop Select depends on all four parallel tasks
root.order.add_edge(Climate_Setup, Crop_Select)
root.order.add_edge(Hydroponics_Install, Crop_Select)
root.order.add_edge(Nutrient_Prep, Crop_Select)
root.order.add_edge(Lighting_Config, Crop_Select)

root.order.add_edge(Crop_Select, Growth_Monitor)

root.order.add_edge(Growth_Monitor, Pest_Control)
root.order.add_edge(Growth_Monitor, Yield_Forecast)

root.order.add_edge(Pest_Control, Energy_Audit)
root.order.add_edge(Pest_Control, Waste_Manage)
root.order.add_edge(Yield_Forecast, Energy_Audit)
root.order.add_edge(Yield_Forecast, Waste_Manage)

root.order.add_edge(Energy_Audit, Market_Study)
root.order.add_edge(Waste_Manage, Market_Study)

root.order.add_edge(Market_Study, Logistics_Plan)