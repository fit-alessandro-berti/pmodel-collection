# Generated from: 364b1d23-9879-4d9e-b1c1-f4c97afc9cd6.json
# Description: This process outlines the complex and innovative steps involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It includes site assessment, climate control system design, modular planting structure assembly, nutrient recycling setup, automation integration for irrigation and lighting, pest management protocols, and real-time data analytics deployment. The workflow ensures sustainability through energy efficiency, waste minimization, and crop yield optimization, while addressing urban zoning regulations and community engagement for local produce distribution. This atypical but realistic process requires multidisciplinary coordination among architects, agronomists, engineers, and IT specialists to successfully create a scalable vertical farming ecosystem in a constrained urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Survey = Transition(label='Site Survey')
Zoning_Check = Transition(label='Zoning Check')
Design_Layout = Transition(label='Design Layout')
Climate_Setup = Transition(label='Climate Setup')
Structure_Build = Transition(label='Structure Build')
Irrigation_Install = Transition(label='Irrigation Install')
Lighting_Setup = Transition(label='Lighting Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automation_Config = Transition(label='Automation Config')
Pest_Control = Transition(label='Pest Control')
Data_Analytics = Transition(label='Data Analytics')
Energy_Audit = Transition(label='Energy Audit')
Waste_Manage = Transition(label='Waste Manage')
Staff_Training = Transition(label='Staff Training')
Launch_Crop = Transition(label='Launch Crop')
Market_Setup = Transition(label='Market Setup')
Community_Meet = Transition(label='Community Meet')

# Define partial orders to model concurrency where applicable and sequencing where required

# Site assessment branch: Site Survey -> Zoning Check
site_assessment = StrictPartialOrder(nodes=[Site_Survey, Zoning_Check])
site_assessment.order.add_edge(Site_Survey, Zoning_Check)

# Design branch after site assessment: Design Layout -> Climate Setup
design_branch = StrictPartialOrder(nodes=[Design_Layout, Climate_Setup])
design_branch.order.add_edge(Design_Layout, Climate_Setup)

# Structure build branch depends on Climate Setup: Structure Build (after Climate Setup)
structure_build = StrictPartialOrder(nodes=[Structure_Build])
# will add order edge from Climate_Setup later

# Installations which can be partially concurrent: Irrigation Install, Lighting Setup, Nutrient Mix
installations = StrictPartialOrder(nodes=[Irrigation_Install, Lighting_Setup, Nutrient_Mix])
# no edges => concurrent tasks

# Automation config depends on installations completed
automation = StrictPartialOrder(nodes=[Automation_Config])
# edges from installations finish to here later

# Pest Control starts after Automation Config
pest_control = StrictPartialOrder(nodes=[Pest_Control])
# edge from Automation_Config -> Pest_Control later

# Data Analytics, Energy Audit and Waste Manage run concurrently after Pest Control
analytics_energy_waste = StrictPartialOrder(
    nodes=[Data_Analytics, Energy_Audit, Waste_Manage]
)
# no order edges => concurrent

# Staff Training depends on Data Analytics, Energy Audit, Waste Manage (all)
staff_training = StrictPartialOrder(nodes=[Staff_Training])
# edges from all three to Staff Training later

# Crop launch depends on Staff Training
launch_crop = StrictPartialOrder(nodes=[Launch_Crop])
# edge from Staff Training to Launch Crop later

# Marketing and Community Meet run concurrently after Launch Crop
market_community = StrictPartialOrder(nodes=[Market_Setup, Community_Meet])
# no order edges, edges from Launch Crop later

# Now build the top-level partial order 
# Start with all nodes referenced
nodes = [
    site_assessment,
    design_branch,
    structure_build,
    installations,
    automation,
    pest_control,
    analytics_energy_waste,
    staff_training,
    launch_crop,
    market_community
]

root = StrictPartialOrder(nodes=nodes)

# Add edges between partial orders to represent dependencies

# site_assessment -> design_branch (Zoning_Check -> Design_Layout)
root.order.add_edge(site_assessment, design_branch)

# design_branch -> structure_build (Climate_Setup -> Structure_Build)
root.order.add_edge(design_branch, structure_build)

# structure_build -> installations
root.order.add_edge(structure_build, installations)

# installations -> automation
root.order.add_edge(installations, automation)

# automation -> pest_control
root.order.add_edge(automation, pest_control)

# pest_control -> analytics_energy_waste
root.order.add_edge(pest_control, analytics_energy_waste)

# analytics_energy_waste -> staff_training
root.order.add_edge(analytics_energy_waste, staff_training)

# staff_training -> launch_crop
root.order.add_edge(staff_training, launch_crop)

# launch_crop -> market_community
root.order.add_edge(launch_crop, market_community)