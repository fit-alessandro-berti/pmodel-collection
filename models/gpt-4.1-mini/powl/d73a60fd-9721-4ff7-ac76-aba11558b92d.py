# Generated from: d73a60fd-9721-4ff7-ac76-aba11558b92d.json
# Description: This process outlines the establishment of an urban vertical farm integrating hydroponic and aeroponic systems within a multi-story building. It involves site analysis, structural adaptation, environmental control installation, nutrient cycling optimization, crop scheduling, energy management, pest monitoring, data analytics, waste recycling, and community engagement. The aim is to maximize crop yield in limited urban space while minimizing resource consumption and environmental impact, requiring coordination across engineering, agriculture, and sustainability teams.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Survey = Transition(label='Site Survey')
Structural_Audit = Transition(label='Structural Audit')
System_Design = Transition(label='System Design')
Permit_Filing = Transition(label='Permit Filing')
Foundation_Prep = Transition(label='Foundation Prep')
Frame_Build = Transition(label='Frame Build')
Irrigation_Setup = Transition(label='Irrigation Setup')
Lighting_Install = Transition(label='Lighting Install')
Climate_Control = Transition(label='Climate Control')
Nutrient_Mix = Transition(label='Nutrient Mix')
Crop_Planting = Transition(label='Crop Planting')
Pest_Scouting = Transition(label='Pest Scouting')
Data_Monitoring = Transition(label='Data Monitoring')
Waste_Sorting = Transition(label='Waste Sorting')
Energy_Audit = Transition(label='Energy Audit')
Community_Meet = Transition(label='Community Meet')
Yield_Analysis = Transition(label='Yield Analysis')

# Site analysis and structural steps (mostly sequential)
site_structural_po = StrictPartialOrder(nodes=[
    Site_Survey,
    Structural_Audit,
    System_Design,
    Permit_Filing,
    Foundation_Prep,
    Frame_Build
])
site_structural_po.order.add_edge(Site_Survey, Structural_Audit)
site_structural_po.order.add_edge(Structural_Audit, System_Design)
site_structural_po.order.add_edge(System_Design, Permit_Filing)
site_structural_po.order.add_edge(Permit_Filing, Foundation_Prep)
site_structural_po.order.add_edge(Foundation_Prep, Frame_Build)

# Environmental and systems installation (some concurrency between irrigation, lighting, climate)
env_setup_po = StrictPartialOrder(nodes=[
    Irrigation_Setup,
    Lighting_Install,
    Climate_Control
])
# No order edges = concurrent installation of these systems

# Nutrient cycling and crop scheduling - Crop_Planting after Nutrient_Mix
nutrient_crop_po = StrictPartialOrder(nodes=[
    Nutrient_Mix,
    Crop_Planting
])
nutrient_crop_po.order.add_edge(Nutrient_Mix, Crop_Planting)

# Monitoring, pest scouting, data collection: Pest_Scouting and Data_Monitoring can be concurrent
monitoring_po = StrictPartialOrder(nodes=[
    Pest_Scouting,
    Data_Monitoring
])
# no edges = concurrent

# Waste sorting and energy audit are also concurrent sustainability activities
sustainability_po = StrictPartialOrder(nodes=[
    Waste_Sorting,
    Energy_Audit
])
# no edges = concurrent

# Community engagement and yield analysis: Yield_Analysis after Community_Meet
community_yield_po = StrictPartialOrder(nodes=[
    Community_Meet,
    Yield_Analysis
])
community_yield_po.order.add_edge(Community_Meet, Yield_Analysis)

# Combine environmental installation with nutrient & crop scheduling as partial order (these can overlap)
env_nutrient_po = StrictPartialOrder(nodes=[
    env_setup_po,
    nutrient_crop_po
])
env_nutrient_po.order.add_edge(env_setup_po, nutrient_crop_po)  # Installation before crop planting after nutrient mix

# Combine monitoring and sustainability as parallel
monitor_sustain_po = StrictPartialOrder(nodes=[
    monitoring_po,
    sustainability_po
])
# no edges, concurrent

# Combine monitoring+sustainability with community_yield, but community_yield last
ms_cy_po = StrictPartialOrder(nodes=[
    monitor_sustain_po,
    community_yield_po
])
ms_cy_po.order.add_edge(monitor_sustain_po, community_yield_po)

# Combine environmental/nutrient with monitoring+sustainability+community_yield
whole_second_phase_po = StrictPartialOrder(nodes=[
    env_nutrient_po,
    ms_cy_po
])
whole_second_phase_po.order.add_edge(env_nutrient_po, ms_cy_po)

# Finally, full model: site_structural before whole_second_phase_po
root = StrictPartialOrder(nodes=[
    site_structural_po,
    whole_second_phase_po
])
root.order.add_edge(site_structural_po, whole_second_phase_po)