# Generated from: 281cc54d-69b1-4b3d-a186-a4fd59d38bff.json
# Description: This process describes the end-to-end operational cycle of an urban vertical farming system that integrates automated environmental controls, crop monitoring, nutrient delivery, and waste recycling. The system starts with seed selection and ends with packaging and distribution, incorporating real-time data analysis to optimize growth conditions. The process also includes preventive maintenance of hydroponic equipment, pest detection via AI imaging, and energy consumption balancing to ensure sustainability in dense urban environments. Each step involves coordination between IoT devices, human operators, and cloud-based analytics platforms to maximize crop yield and minimize resource use, representing a cutting-edge approach to urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Seed_Selection = Transition(label='Seed Selection')
Germination_Start = Transition(label='Germination Start')
Nutrient_Mix = Transition(label='Nutrient Mix')
Planting_Setup = Transition(label='Planting Setup')
Light_Adjustment = Transition(label='Light Adjustment')
Humidity_Control = Transition(label='Humidity Control')
Growth_Monitoring = Transition(label='Growth Monitoring')
Pest_Detection = Transition(label='Pest Detection')
Water_Recycling = Transition(label='Water Recycling')
Air_Circulation = Transition(label='Air Circulation')
Data_Analysis = Transition(label='Data Analysis')
Equipment_Check = Transition(label='Equipment Check')
Harvest_Timing = Transition(label='Harvest Timing')
Crop_Packaging = Transition(label='Crop Packaging')
Distribution_Prep = Transition(label='Distribution Prep')
Waste_Processing = Transition(label='Waste Processing')
Energy_Audit = Transition(label='Energy Audit')

# Preventive maintenance loop for equipment check and energy audit (loop: Equipment_Check, Energy_Audit)
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[Equipment_Check, Energy_Audit])

# Pest detection step: modeled as a choice between performing pest detection or silently skipping it (optional)
skip = SilentTransition()
pest_detection_choice = OperatorPOWL(operator=Operator.XOR, children=[Pest_Detection, skip])

# Parallel environmental controls:
# Light Adjustment and Humidity Control can be concurrent partial order nodes
environment_controls = StrictPartialOrder(
    nodes=[Light_Adjustment, Humidity_Control]
)  # concurrent, no order edges

# Water Recycling and Air Circulation can also be concurrent
environment_maintenance = StrictPartialOrder(
    nodes=[Water_Recycling, Air_Circulation]
)  # concurrent

# Data analysis typically follows monitoring and environmental controls
# So define a partial order for Growth Monitoring, environment controls, and environmental maintenance
gm_env = StrictPartialOrder(
    nodes=[Growth_Monitoring, environment_controls, environment_maintenance]
)
# define order edges for GM to environment controls and environment controls to environment maintenance

# For partial orders, edges are between nodes; since environment_controls and environment_maintenance are StrictPartialOrders (complex nodes),
# we'll use them directly as nodes (nested allowed).

gm_env.order.add_edge(Growth_Monitoring, environment_controls)
gm_env.order.add_edge(environment_controls, environment_maintenance)

# Data Analysis follows these
data_analysis_partial = StrictPartialOrder(
    nodes=[gm_env, Data_Analysis]
)
data_analysis_partial.order.add_edge(gm_env, Data_Analysis)

# Now build the main flow in order:
# Seed Selection --> Germination Start --> Nutrient Mix --> Planting Setup --> maintenance_loop parallel OR before Planting Setup?
# According to typical cycle, maintenance can run as a loop during process. Here we position it after Planting Setup but before environment monitoring.

# Build the first partial order for start activities
start_to_planting = StrictPartialOrder(
    nodes=[Seed_Selection, Germination_Start, Nutrient_Mix, Planting_Setup]
)
start_to_planting.order.add_edge(Seed_Selection, Germination_Start)
start_to_planting.order.add_edge(Germination_Start, Nutrient_Mix)
start_to_planting.order.add_edge(Nutrient_Mix, Planting_Setup)

# Define partial order with maintenance_loop and pest_detection_choice after Planting Setup, possibly concurrent to environment steps

post_planting = StrictPartialOrder(
    nodes=[maintenance_loop, pest_detection_choice, data_analysis_partial]
)
# pest_detection_choice and maintenance_loop probably occur before data analysis (data analysis aggregates results)
# Let's order maintenance_loop and pest_detection_choice before data analysis_partial

post_planting.order.add_edge(maintenance_loop, data_analysis_partial)
post_planting.order.add_edge(pest_detection_choice, data_analysis_partial)

# Create parallel after planting: maintenance_loop, pest_detection_choice, and environment monitoring/data analysis

# We incorporate gm_env inside data_analysis_partial, so it follows the above.

# Now final activities after data analysis:
# Harvest Timing --> Crop Packaging --> Distribution Prep --> Waste Processing (which relates to recycling and sustainability)
final_sequence = StrictPartialOrder(
    nodes=[Harvest_Timing, Crop_Packaging, Distribution_Prep, Waste_Processing]
)
final_sequence.order.add_edge(Harvest_Timing, Crop_Packaging)
final_sequence.order.add_edge(Crop_Packaging, Distribution_Prep)
final_sequence.order.add_edge(Distribution_Prep, Waste_Processing)

# Waste Processing relates to Water Recycling and possibly Energy Audit from maintenance_loop.
# But Energy Audit is inside maintenance_loop already; Water Recycling in environment_maintenance.
# We can keep Waste Processing at the end.

# Define overall partial order of whole process:
# start_to_planting --> post_planting --> final_sequence

root = StrictPartialOrder(
    nodes=[start_to_planting, post_planting, final_sequence]
)
root.order.add_edge(start_to_planting, post_planting)
root.order.add_edge(post_planting, final_sequence)