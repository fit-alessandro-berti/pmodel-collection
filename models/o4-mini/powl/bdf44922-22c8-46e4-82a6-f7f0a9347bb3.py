# Generated from: bdf44922-22c8-46e4-82a6-f7f0a9347bb3.json
# Description: This process outlines the establishment of an urban vertical farming system within a repurposed industrial building. It involves site evaluation, structural modifications for weight support, installation of hydroponic and aeroponic systems, integration of automated climate control, and implementation of AI-driven nutrient delivery. The process also includes staff training on system maintenance, daily crop monitoring, pest management with minimal chemicals, and data analysis for yield optimization. Finally, it covers packaging logistics and coordination with local markets to ensure fresh produce distribution, emphasizing sustainability and resource efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey    = Transition(label='Site Survey')
load_testing   = Transition(label='Load Testing')
struct_mod     = Transition(label='Structural Mod')
system_install = Transition(label='System Install')
sensor_setup   = Transition(label='Sensor Setup')
climate_setup  = Transition(label='Climate Setup')
ai_integration = Transition(label='AI Integration')
nutrient_mix   = Transition(label='Nutrient Mix')
staff_training = Transition(label='Staff Training')
crop_planting  = Transition(label='Crop Planting')
growth_monitor = Transition(label='Growth Monitor')
pest_control   = Transition(label='Pest Control')
data_analysis  = Transition(label='Data Analysis')
packaging_prep = Transition(label='Packaging Prep')
market_sync    = Transition(label='Market Sync')

# Silent transition for loop redo
skip = SilentTransition()

# Define the daily operations group: monitor -> pest control -> data analysis
daily_group = StrictPartialOrder(nodes=[growth_monitor, pest_control, data_analysis])
daily_group.order.add_edge(growth_monitor, pest_control)
daily_group.order.add_edge(pest_control, data_analysis)

# Loop: repeat daily_group until exit
loop_daily = OperatorPOWL(operator=Operator.LOOP, children=[daily_group, skip])

# Build the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    load_testing,
    struct_mod,
    system_install,
    sensor_setup,
    climate_setup,
    ai_integration,
    nutrient_mix,
    staff_training,
    crop_planting,
    loop_daily,
    packaging_prep,
    market_sync
])

# Define the control-flow/order dependencies
root.order.add_edge(site_survey,    load_testing)
root.order.add_edge(load_testing,   struct_mod)
root.order.add_edge(struct_mod,     system_install)
root.order.add_edge(system_install, sensor_setup)
root.order.add_edge(sensor_setup,   climate_setup)
root.order.add_edge(climate_setup,  ai_integration)
root.order.add_edge(ai_integration, nutrient_mix)
root.order.add_edge(nutrient_mix,   staff_training)
root.order.add_edge(staff_training, crop_planting)
root.order.add_edge(crop_planting,  loop_daily)
root.order.add_edge(loop_daily,     packaging_prep)
root.order.add_edge(packaging_prep, market_sync)