# Generated from: 126f4a85-812c-4f5f-9fe5-8acf676abf46.json
# Description: This process outlines the establishment of an urban rooftop farm, integrating architectural assessments, environmental impact studies, and community engagement. It involves selecting suitable crops, designing modular planting systems, installing irrigation and lighting technologies, and coordinating with local authorities for compliance. The process also includes soil preparation using recycled materials, pest management through natural predators, and setting up data collection for crop monitoring. Post-installation, it emphasizes training staff, marketing the farm produce to local markets, and evaluating sustainability metrics to ensure long-term viability and community benefits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Survey = Transition(label='Site Survey')
Permit_Review = Transition(label='Permit Review')
Crop_Selection = Transition(label='Crop Selection')
System_Design = Transition(label='System Design')
Material_Sourcing = Transition(label='Material Sourcing')
Soil_Prep = Transition(label='Soil Prep')
Irrigation_Setup = Transition(label='Irrigation Setup')
Lighting_Install = Transition(label='Lighting Install')
Pest_Control = Transition(label='Pest Control')
Monitoring_Setup = Transition(label='Monitoring Setup')
Staff_Training = Transition(label='Staff Training')
Community_Outreach = Transition(label='Community Outreach')
Market_Analysis = Transition(label='Market Analysis')
Harvest_Planning = Transition(label='Harvest Planning')
Sustainability_Audit = Transition(label='Sustainability Audit')

# Model 1: Initial assessments that can be done concurrently:
# 'Site Survey' and 'Permit Review' in parallel, both needed before 'Crop Selection'
init_assessments = StrictPartialOrder(nodes=[Site_Survey, Permit_Review, Crop_Selection])
init_assessments.order.add_edge(Site_Survey, Crop_Selection)
init_assessments.order.add_edge(Permit_Review, Crop_Selection)

# Model 2: Crop Selection followed by design and sourcing (design then sourcing in parallel with soil prep)
# Design + Soil Prep + Material Sourcing after Crop_Selection

# System_Design must be done before Material_Sourcing
design_and_sourcing = StrictPartialOrder(
    nodes=[System_Design, Material_Sourcing, Soil_Prep]
)
design_and_sourcing.order.add_edge(System_Design, Material_Sourcing)
# Soil_Prep can be concurrent with Material_Sourcing (no edge)

# Crop_Selection before design_and_sourcing
crop_to_design = StrictPartialOrder(
    nodes=[Crop_Selection, design_and_sourcing]
)
crop_to_design.order.add_edge(Crop_Selection, design_and_sourcing)

# Model 3: Installation Stage
# Irrigation_Setup, Lighting_Install, Pest_Control, Monitoring_Setup are concurrently done after design_and_sourcing and Soil_Prep
installation = StrictPartialOrder(
    nodes=[Irrigation_Setup, Lighting_Install, Pest_Control, Monitoring_Setup]
)
# installation depends on design_and_sourcing and Soil_Prep
# Since Soil_Prep is inside design_and_sourcing node as concurrent node,
# to model this clearly, let's create a joint node for join condition

# The activities Soil_Prep and Material_Sourcing are both inside design_and_sourcing,
# but Soil_Prep is parallel with Material_Sourcing, and Material_Sourcing is after System_Design.
# To ensure all finishes before installation, we'll create a PO structure as:

# We'll create a PO with nodes design_and_sourcing and installation and add edge design_and_sourcing --> installation

post_design_install = StrictPartialOrder(
    nodes=[design_and_sourcing, installation]
)
post_design_install.order.add_edge(design_and_sourcing, installation)

# Model 4: Post-installation activities, in sequence:
# Staff Training -> Community Outreach -> Market Analysis -> Harvest Planning -> Sustainability Audit
post_install = StrictPartialOrder(
    nodes=[
        Staff_Training,
        Community_Outreach,
        Market_Analysis,
        Harvest_Planning,
        Sustainability_Audit,
    ]
)
post_install.order.add_edge(Staff_Training, Community_Outreach)
post_install.order.add_edge(Community_Outreach, Market_Analysis)
post_install.order.add_edge(Market_Analysis, Harvest_Planning)
post_install.order.add_edge(Harvest_Planning, Sustainability_Audit)

# Connect installation to post_install in sequence
install_to_post = StrictPartialOrder(
    nodes=[installation, post_install]
)
install_to_post.order.add_edge(installation, post_install)

# Now combine all main parts in sequence:
# init_assessments -> crop_to_design -> installation -> post_install
root = StrictPartialOrder(
    nodes=[init_assessments, crop_to_design, installation, post_install]
)
root.order.add_edge(init_assessments, crop_to_design)
root.order.add_edge(crop_to_design, installation)
root.order.add_edge(installation, post_install)