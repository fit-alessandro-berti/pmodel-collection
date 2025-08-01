# Generated from: c827453b-fb6a-408e-912a-586fdfd11b6b.json
# Description: This process involves managing an adaptive urban farming system that integrates IoT sensors, real-time data analytics, and community feedback to optimize crop yield and sustainability in limited spaces. Activities include monitoring environmental variables, adjusting nutrient delivery dynamically, rotating crops based on predictive models, and coordinating local volunteer schedules. The system also incorporates waste recycling from nearby restaurants into composting units, and uses autonomous drones for pollination and pest control. Continuous improvement is driven by machine learning algorithms analyzing historical and current data, ensuring responsiveness to seasonal changes and urban microclimates while maximizing resource efficiency and community engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
SensorSetup = Transition(label='Sensor Setup')
DataCapture = Transition(label='Data Capture')
NutrientMix = Transition(label='Nutrient Mix')
CropRotate = Transition(label='Crop Rotate')
WasteCollect = Transition(label='Waste Collect')
CompostProcess = Transition(label='Compost Process')
DroneDispatch = Transition(label='Drone Dispatch')
PestControl = Transition(label='Pest Control')
PollinationRun = Transition(label='Pollination Run')
VolunteerAssign = Transition(label='Volunteer Assign')
FeedbackGather = Transition(label='Feedback Gather')
ModelUpdate = Transition(label='Model Update')
YieldForecast = Transition(label='Yield Forecast')
WaterAdjust = Transition(label='Water Adjust')
ReportGenerate = Transition(label='Report Generate')
ResourceAudit = Transition(label='Resource Audit')
ScheduleSync = Transition(label='Schedule Sync')

# 1. Monitoring environmental variables: Sensor Setup --> Data Capture
monitoring_po = StrictPartialOrder(nodes=[SensorSetup, DataCapture])
monitoring_po.order.add_edge(SensorSetup, DataCapture)

# 2. Adjusting nutrient delivery dynamically: Nutrient Mix --> Water Adjust
nutrient_po = StrictPartialOrder(nodes=[NutrientMix, WaterAdjust])
nutrient_po.order.add_edge(NutrientMix, WaterAdjust)

# 3. Rotating crops based on predictive models:
# Crop Rotate --> Yield Forecast
# Yield Forecast --> Model Update
crop_rotation_po = StrictPartialOrder(nodes=[CropRotate, YieldForecast, ModelUpdate])
crop_rotation_po.order.add_edge(CropRotate, YieldForecast)
crop_rotation_po.order.add_edge(YieldForecast, ModelUpdate)

# 4. Waste recycling from nearby restaurants into composting:
# Waste Collect --> Compost Process
waste_po = StrictPartialOrder(nodes=[WasteCollect, CompostProcess])
waste_po.order.add_edge(WasteCollect, CompostProcess)

# 5. Autonomous drones for pollination and pest control:
# Drone Dispatch --> Split choice (Pest Control XOR Pollination Run)
drone_choice = OperatorPOWL(operator=Operator.XOR, children=[PestControl, PollinationRun])
drone_po = StrictPartialOrder(nodes=[DroneDispatch, drone_choice])
drone_po.order.add_edge(DroneDispatch, drone_choice)

# 6. Coordinating local volunteer schedules and gathering feedback:
# Volunteer Assign --> Feedback Gather
volunteer_po = StrictPartialOrder(nodes=[VolunteerAssign, FeedbackGather])
volunteer_po.order.add_edge(VolunteerAssign, FeedbackGather)

# 7. Continuous improvement loop:
# Loop with body: (Model Update --> Schedule Sync)
# followed by choice to exit or do (Resource Audit --> Report Generate) then back to Model Update

loop_body = StrictPartialOrder(nodes=[ModelUpdate, ScheduleSync])
loop_body.order.add_edge(ModelUpdate, ScheduleSync)

# Post-body loop sequence
post_loop = StrictPartialOrder(nodes=[ResourceAudit, ReportGenerate])
post_loop.order.add_edge(ResourceAudit, ReportGenerate)

continuous_improvement = OperatorPOWL(
    operator=Operator.LOOP,
    children=[loop_body, post_loop]
)

# Linking crop_rotation_po's ModelUpdate with continuous_improvement's loop_body ModelUpdate:
# We can unify ModelUpdate nodes by reusing the same Transition instance to reflect this

# Compose partial orders to reflect the overall workflow
# Combine monitoring, nutrient delivery, crop rotation, waste recycling, drones, volunteer coordination:

# These sub-processes largely proceed concurrently except where dependencies exist.

root = StrictPartialOrder(
    nodes=[
        monitoring_po,
        nutrient_po,
        crop_rotation_po,
        waste_po,
        drone_po,
        volunteer_po,
        continuous_improvement
    ]
)

# Define dependencies among main components to reflect likely control flow:
# Environmental monitoring and data capture (monitoring_po) influences nutrient and crop rotation
root.order.add_edge(monitoring_po, nutrient_po)
root.order.add_edge(monitoring_po, crop_rotation_po)

# Nutrient and crop rotation might be prerequisites to drip irrigation adjustment and improvements
root.order.add_edge(nutrient_po, continuous_improvement)
root.order.add_edge(crop_rotation_po, continuous_improvement)

# Waste recycling is concurrent but suppose it precedes drone dispatch (using composting may affect drone operations)
root.order.add_edge(waste_po, drone_po)

# Drone operations and volunteer coordination likely happen concurrently with continuous improvements,
# but volunteer feedback probably informs continuous improvements too:
root.order.add_edge(volunteer_po, continuous_improvement)

# Drone operations and volunteer coordination can run in parallel
# No edge needed between drone_po and volunteer_po for concurrency

# Final ordering summary:
# monitoring_po -> nutrient_po, crop_rotation_po
# nutrient_po -> continuous_improvement
# crop_rotation_po -> continuous_improvement
# waste_po -> drone_po
# volunteer_po -> continuous_improvement

# The final model is saved in root