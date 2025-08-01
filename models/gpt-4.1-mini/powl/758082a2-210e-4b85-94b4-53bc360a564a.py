# Generated from: 758082a2-210e-4b85-94b4-53bc360a564a.json
# Description: This process involves transforming underutilized urban rooftop spaces into productive agricultural environments. It includes assessing structural integrity, designing modular planting systems, sourcing sustainable materials, integrating automated irrigation and nutrient delivery, and coordinating with local regulations. The process also covers community workshops, environmental impact assessments, pest management, and harvesting logistics to ensure a thriving, eco-friendly rooftop farm that supports local food production and urban biodiversity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
load_testing = Transition(label='Load Testing')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
system_assembly = Transition(label='System Assembly')
irrigation_setup = Transition(label='Irrigation Setup')
nutrient_mixing = Transition(label='Nutrient Mixing')
plant_selection = Transition(label='Plant Selection')
soil_preparation = Transition(label='Soil Preparation')
pest_monitoring = Transition(label='Pest Monitoring')
regulation_check = Transition(label='Regulation Check')
community_training = Transition(label='Community Training')
harvest_planning = Transition(label='Harvest Planning')
waste_recycling = Transition(label='Waste Recycling')
performance_review = Transition(label='Performance Review')

# Structural assessment PO
structural_assess = StrictPartialOrder(nodes=[site_survey, load_testing, design_layout])
structural_assess.order.add_edge(site_survey, load_testing)
structural_assess.order.add_edge(load_testing, design_layout)

# Material and system setup PO
material_system_setup = StrictPartialOrder(nodes=[material_sourcing, system_assembly])
material_system_setup.order.add_edge(material_sourcing, system_assembly)

# Agricultural system setup PO (some concurrent activities)
agri_setup = StrictPartialOrder(nodes=[irrigation_setup, nutrient_mixing, plant_selection, soil_preparation])
# irrigation_setup and nutrient_mixing can be done before plant_selection and soil_preparation
agri_setup.order.add_edge(irrigation_setup, plant_selection)
agri_setup.order.add_edge(nutrient_mixing, plant_selection)
agri_setup.order.add_edge(irrigation_setup, soil_preparation)
agri_setup.order.add_edge(nutrient_mixing, soil_preparation)

# Regulatory and community PO (regulation check before community training)
reg_comm = StrictPartialOrder(nodes=[regulation_check, community_training])
reg_comm.order.add_edge(regulation_check, community_training)

# Maintenance and harvest PO, pest monitoring before harvest planning
maint_harvest = StrictPartialOrder(nodes=[pest_monitoring, harvest_planning, waste_recycling, performance_review])
maint_harvest.order.add_edge(pest_monitoring, harvest_planning)
maint_harvest.order.add_edge(harvest_planning, waste_recycling)
maint_harvest.order.add_edge(waste_recycling, performance_review)

# Compose the full process partial order
root = StrictPartialOrder(nodes=[
    structural_assess,
    material_system_setup,
    agri_setup,
    reg_comm,
    maint_harvest
])

# Add order edges between phases
root.order.add_edge(structural_assess, material_system_setup)
root.order.add_edge(material_system_setup, agri_setup)
root.order.add_edge(agri_setup, reg_comm)
root.order.add_edge(reg_comm, maint_harvest)