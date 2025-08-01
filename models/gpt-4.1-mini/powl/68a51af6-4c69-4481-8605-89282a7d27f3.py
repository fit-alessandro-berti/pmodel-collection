# Generated from: 68a51af6-4c69-4481-8605-89282a7d27f3.json
# Description: This process outlines the complex and atypical procedure of establishing an urban vertical farm within a repurposed high-rise building. It involves multiple stages including site evaluation, environmental control design, modular system integration, crop selection, nutrient delivery setup, and waste recycling methods. The process requires coordination between architects, agricultural scientists, engineers, and logistics teams to ensure optimal crop yield and sustainability. Additionally, it addresses regulatory compliance, energy efficiency optimization, and community engagement to incorporate local needs and reduce environmental impact. Continuous monitoring and iterative adjustments are essential to adapt to urban constraints and maximize productivity in a non-traditional farming environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Regulation_Check = Transition(label='Regulation Check')
Layout_Plan = Transition(label='Layout Plan')
Climate_Setup = Transition(label='Climate Setup')
Modular_Install = Transition(label='Modular Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Crop_Select = Transition(label='Crop Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Lighting_Config = Transition(label='Lighting Config')
Waste_System = Transition(label='Waste System')
Energy_Audit = Transition(label='Energy Audit')
Staff_Train = Transition(label='Staff Train')
Yield_Monitor = Transition(label='Yield Monitor')
Pest_Control = Transition(label='Pest Control')
Community_Meet = Transition(label='Community Meet')
Data_Analysis = Transition(label='Data Analysis')
Maintenance_Plan = Transition(label='Maintenance Plan')

# Define logical substructures based on the description

# Initial evaluations and plans: Site Survey -> Regulation Check -> Layout Plan
initial_PO = StrictPartialOrder(
    nodes=[Site_Survey, Regulation_Check, Layout_Plan]
)
initial_PO.order.add_edge(Site_Survey, Regulation_Check)
initial_PO.order.add_edge(Regulation_Check, Layout_Plan)

# Environment & modular system setup (can run some concurrently after Layout Plan)
# Climate Setup and Modular Install can be concurrent but both must follow Layout Plan
environment_PO = StrictPartialOrder(
    nodes=[Climate_Setup, Modular_Install, Layout_Plan]
)
environment_PO.order.add_edge(Layout_Plan, Climate_Setup)
environment_PO.order.add_edge(Layout_Plan, Modular_Install)

# Irrigation setup depends on Modular Install
irrigation_PO = StrictPartialOrder(
    nodes=[Irrigation_Setup, Modular_Install]
)
irrigation_PO.order.add_edge(Modular_Install, Irrigation_Setup)

# Crop Select depends on Site Survey and Regulation Check done (earlier) and after Layout Plan as well,
# but for simplicity assume after Layout Plan
crop_select_PO = StrictPartialOrder(
    nodes=[Crop_Select, Layout_Plan]
)
crop_select_PO.order.add_edge(Layout_Plan, Crop_Select)

# Nutrient Mix and Lighting Config depend on Crop Select and Climate Setup
nutrient_lighting_PO = StrictPartialOrder(
    nodes=[Nutrient_Mix, Lighting_Config, Crop_Select, Climate_Setup]
)
nutrient_lighting_PO.order.add_edge(Crop_Select, Nutrient_Mix)
nutrient_lighting_PO.order.add_edge(Crop_Select, Lighting_Config)
nutrient_lighting_PO.order.add_edge(Climate_Setup, Nutrient_Mix)
nutrient_lighting_PO.order.add_edge(Climate_Setup, Lighting_Config)

# Waste System and Energy Audit depend on Modular Install
waste_energy_PO = StrictPartialOrder(
    nodes=[Waste_System, Energy_Audit, Modular_Install]
)
waste_energy_PO.order.add_edge(Modular_Install, Waste_System)
waste_energy_PO.order.add_edge(Modular_Install, Energy_Audit)

# Staff Training can start after Irrigation Setup and Energy Audit done
staff_train_PO = StrictPartialOrder(
    nodes=[Staff_Train, Irrigation_Setup, Energy_Audit]
)
staff_train_PO.order.add_edge(Irrigation_Setup, Staff_Train)
staff_train_PO.order.add_edge(Energy_Audit, Staff_Train)

# Yield Monitor, Pest Control, Community Meet after Staff Train and Crop Select
monitoring_PO = StrictPartialOrder(
    nodes=[Yield_Monitor, Pest_Control, Community_Meet, Staff_Train, Crop_Select]
)
monitoring_PO.order.add_edge(Staff_Train, Yield_Monitor)
monitoring_PO.order.add_edge(Staff_Train, Pest_Control)
monitoring_PO.order.add_edge(Staff_Train, Community_Meet)
monitoring_PO.order.add_edge(Crop_Select, Yield_Monitor)
monitoring_PO.order.add_edge(Crop_Select, Pest_Control)
monitoring_PO.order.add_edge(Crop_Select, Community_Meet)

# Data Analysis depends on Yield Monitor and Pest Control
data_analysis_PO = StrictPartialOrder(
    nodes=[Data_Analysis, Yield_Monitor, Pest_Control]
)
data_analysis_PO.order.add_edge(Yield_Monitor, Data_Analysis)
data_analysis_PO.order.add_edge(Pest_Control, Data_Analysis)

# Maintenance Plan depends on Data Analysis and Community Meet
maintenance_PO = StrictPartialOrder(
    nodes=[Maintenance_Plan, Data_Analysis, Community_Meet]
)
maintenance_PO.order.add_edge(Data_Analysis, Maintenance_Plan)
maintenance_PO.order.add_edge(Community_Meet, Maintenance_Plan)

# Loop: Continuous monitoring and iterative adjustments
# Loop node: execute monitoring_PO then choose to exit or execute data_analysis_PO + maintenance_PO then monitoring_PO again
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring_PO, StrictPartialOrder(
    nodes=[data_analysis_PO, maintenance_PO]
)])

# However, data_analysis_PO and maintenance_PO have nodes in common with monitoring_PO
# To build the body of the loop, combine data_analysis_PO and maintenance_PO in a PO (order between them)
analysis_maint_PO = StrictPartialOrder(
    nodes=[Data_Analysis, Community_Meet, Maintenance_Plan]
)
analysis_maint_PO.order.add_edge(Data_Analysis, Maintenance_Plan)
analysis_maint_PO.order.add_edge(Community_Meet, Maintenance_Plan)

loop_body = StrictPartialOrder(
    nodes=[data_analysis_PO, analysis_maint_PO]
)
# The above is problematic since we cannot nest POWL inside POWL nodes arbitrarily
# better construct a hierarchy:
# Loop children[0] = monitoring_PO
# Loop children[1] = PO of data_analysis_PO + maintenance_PO

# We'll unify data_analysis_PO and maintenance_PO nodes:
loop_body = StrictPartialOrder(
    nodes=[Yield_Monitor, Pest_Control, Data_Analysis, Community_Meet, Maintenance_Plan]
)
loop_body.order.add_edge(Yield_Monitor, Data_Analysis)
loop_body.order.add_edge(Pest_Control, Data_Analysis)
loop_body.order.add_edge(Data_Analysis, Maintenance_Plan)
loop_body.order.add_edge(Community_Meet, Maintenance_Plan)

monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring_PO, loop_body])

# Compose all partial orders in order:

# Partial order of all before loop
before_loop_PO_nodes = [initial_PO, environment_PO, irrigation_PO, crop_select_PO, nutrient_lighting_PO, waste_energy_PO, staff_train_PO]

# We cannot directly add a POWL node as a node inside another POWL PO;
# So we compose the big model as a StrictPartialOrder of all these nodes plus the monitoring_loop

root_nodes = before_loop_PO_nodes + [monitoring_loop]

root = StrictPartialOrder(nodes=root_nodes)

# Define edge dependencies between these composite nodes:

# initial_PO -> environment_PO
root.order.add_edge(initial_PO, environment_PO)
# environment_PO -> irrigation_PO and crop_select_PO and waste_energy_PO
root.order.add_edge(environment_PO, irrigation_PO)
root.order.add_edge(environment_PO, crop_select_PO)
root.order.add_edge(environment_PO, waste_energy_PO)
# irrigation_PO -> staff_train_PO
root.order.add_edge(irrigation_PO, staff_train_PO)
# waste_energy_PO -> staff_train_PO
root.order.add_edge(waste_energy_PO, staff_train_PO)
# crop_select_PO -> nutrient_lighting_PO and monitoring_PO (monitoring embedded in loop so:
# connect crop_select_PO -> monitoring_loop)
root.order.add_edge(crop_select_PO, nutrient_lighting_PO)
root.order.add_edge(crop_select_PO, monitoring_loop)
# nutrient_lighting_PO, staff_train_PO -> monitoring_loop
root.order.add_edge(nutrient_lighting_PO, monitoring_loop)
root.order.add_edge(staff_train_PO, monitoring_loop)