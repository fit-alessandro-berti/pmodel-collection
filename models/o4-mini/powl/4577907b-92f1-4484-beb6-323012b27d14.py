# Generated from: 4577907b-92f1-4484-beb6-323012b27d14.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming operation within a metropolitan building. It includes site assessment for structural capacity and sunlight optimization, integration of automated hydroponic systems, IoT sensor deployment for real-time monitoring, nutrient solution calibration, and climate control setup. The workflow further involves workforce training on system maintenance, scheduling crop cycles for maximum yield, implementing pest management protocols without pesticides, and coordinating logistics for local distribution. Continuous data analysis and iterative adjustment of environmental parameters ensure sustainable growth and energy efficiency. The process culminates in certification compliance and marketing launch to promote locally grown produce in urban communities, providing a scalable model for future expansion.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey    = Transition(label='Site Survey')
load_test      = Transition(label='Load Test')
light_mapping  = Transition(label='Light Mapping')
system_design  = Transition(label='System Design')
hydro_setup    = Transition(label='Hydro Setup')
sensor_install = Transition(label='Sensor Install')
nutrient_mix   = Transition(label='Nutrient Mix')
climate_control= Transition(label='Climate Control')
staff_training = Transition(label='Staff Training')
crop_planning  = Transition(label='Crop Planning')
pest_control   = Transition(label='Pest Control')
data_monitoring= Transition(label='Data Monitoring')
yield_analysis = Transition(label='Yield Analysis')
compliance_check = Transition(label='Compliance Check')
market_launch    = Transition(label='Market Launch')

# Loop for continuous monitoring & analysis
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_monitoring, yield_analysis]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    load_test,
    light_mapping,
    system_design,
    hydro_setup,
    sensor_install,
    nutrient_mix,
    climate_control,
    staff_training,
    crop_planning,
    pest_control,
    monitoring_loop,
    compliance_check,
    market_launch
])

# Define the sequential dependencies
root.order.add_edge(site_survey,    load_test)
root.order.add_edge(load_test,      light_mapping)
root.order.add_edge(light_mapping,  system_design)
root.order.add_edge(system_design,  hydro_setup)
root.order.add_edge(hydro_setup,    sensor_install)
root.order.add_edge(sensor_install, nutrient_mix)
root.order.add_edge(nutrient_mix,   climate_control)
root.order.add_edge(climate_control,staff_training)
root.order.add_edge(staff_training, crop_planning)
root.order.add_edge(crop_planning,  pest_control)
root.order.add_edge(pest_control,   monitoring_loop)
root.order.add_edge(monitoring_loop, compliance_check)
root.order.add_edge(compliance_check, market_launch)