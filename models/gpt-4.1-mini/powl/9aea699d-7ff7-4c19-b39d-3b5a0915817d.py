# Generated from: 9aea699d-7ff7-4c19-b39d-3b5a0915817d.json
# Description: This process outlines the comprehensive steps involved in establishing an urban rooftop farming operation on a commercial building. It begins with structural assessments to ensure load capacity, followed by microclimate analysis to optimize plant selection and layout. Procurement of sustainable materials and soil substrates occurs next, alongside installation of automated irrigation systems and solar-powered lighting. Continuous integration of sensor networks allows real-time monitoring of moisture, temperature, and nutrient levels. Staff training in urban agriculture techniques and safety protocols ensures efficient daily operations. Finally, the process includes marketing strategies targeting local restaurants and community programs to promote farm-to-table initiatives, ensuring economic viability and social impact within urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Load_Check = Transition(label='Load Check')
Climate_Scan = Transition(label='Climate Scan')
Material_Buy = Transition(label='Material Buy')
Soil_Prep = Transition(label='Soil Prep')
Irrigation_Fit = Transition(label='Irrigation Fit')
Lighting_Setup = Transition(label='Lighting Setup')
Sensor_Install = Transition(label='Sensor Install')
Data_Sync = Transition(label='Data Sync')
Crop_Select = Transition(label='Crop Select')
Staff_Train = Transition(label='Staff Train')
Safety_Drill = Transition(label='Safety Drill')
Harvest_Plan = Transition(label='Harvest Plan')
Market_Outreach = Transition(label='Market Outreach')
Community_Engage = Transition(label='Community Engage')
Waste_Manage = Transition(label='Waste Manage')
Energy_Audit = Transition(label='Energy Audit')
Yield_Assess = Transition(label='Yield Assess')

# Procurement: Material Buy and Soil Prep in parallel
procurement = StrictPartialOrder(nodes=[Material_Buy, Soil_Prep])
# no order edges - concurrent

# Install: Irrigation Fit and Lighting Setup in parallel
install = StrictPartialOrder(nodes=[Irrigation_Fit, Lighting_Setup])
# no order edges - concurrent

# Data processing chain: Sensor Install -> Data Sync -> Crop Select
data_chain = StrictPartialOrder(nodes=[Sensor_Install, Data_Sync, Crop_Select])
data_chain.order.add_edge(Sensor_Install, Data_Sync)
data_chain.order.add_edge(Data_Sync, Crop_Select)

# Staff training sequence: Staff Train -> Safety Drill
training = StrictPartialOrder(nodes=[Staff_Train, Safety_Drill])
training.order.add_edge(Staff_Train, Safety_Drill)

# Marketing parallel: Market Outreach and Community Engage
marketing = StrictPartialOrder(nodes=[Market_Outreach, Community_Engage])
# no order edges - concurrent

# Final assessment sequence: Waste Manage -> Energy Audit -> Yield Assess
final_assess = StrictPartialOrder(nodes=[Waste_Manage, Energy_Audit, Yield_Assess])
final_assess.order.add_edge(Waste_Manage, Energy_Audit)
final_assess.order.add_edge(Energy_Audit, Yield_Assess)

# Compose procurement and install in parallel (these both after climate scan)
procure_install = StrictPartialOrder(nodes=[procurement, install])
# no order edges - concurrent

# After Load Check -> Climate Scan
start = StrictPartialOrder(nodes=[Load_Check, Climate_Scan])
start.order.add_edge(Load_Check, Climate_Scan)

# After climate scan, procurement and install in parallel
after_climate = procure_install

# Define the whole workflow partial orders and their causal relations:

# Step1: Load Check -> Climate Scan done (start)
# Step2: Climate Scan -> procurement and install (in parallel)
# Step3: procurement and install must both complete before Sensor Install starts
# Step4: data chain (Sensor Install -> Data Sync -> Crop Select)
# Step5: after crop select, staff training (Staff Train->Safety Drill) and marketing (Market Outreach & Community Engage) run in parallel
# Step6: finally, Harvest Plan starts after training and marketing are done
# Step7: Harvest Plan -> final assessment (Waste Manage -> Energy Audit -> Yield Assess)

# Define Harvest Plan separately
harvest_plan = Harvest_Plan

# Merge training and marketing as parallel
train_marketing = StrictPartialOrder(nodes=[training, marketing])
# no edges between training and marketing

# Now build the root with all nodes:
root = StrictPartialOrder(nodes=[
    start,
    after_climate,
    data_chain,
    train_marketing,
    harvest_plan,
    final_assess
])

# Add ordering edges according to above description

# start: Load Check -> Climate Scan
# already done inside start

# start -> after_climate (by Climate Scan -> procurement and install)
root.order.add_edge(start, after_climate)  # start completes before procurement/install start

# after_climate -> data_chain (both procurement and install must complete before Sensor Install)
root.order.add_edge(after_climate, data_chain)

# data_chain ends with Crop Select, start train_marketing after data_chain
root.order.add_edge(data_chain, train_marketing)

# train_marketing -> harvest_plan
root.order.add_edge(train_marketing, harvest_plan)

# harvest_plan -> final_assess
root.order.add_edge(harvest_plan, final_assess)