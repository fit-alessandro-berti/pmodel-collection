# Generated from: c827453b-fb6a-408e-912a-586fdfd11b6b.json
# Description: This process involves managing an adaptive urban farming system that integrates IoT sensors, real-time data analytics, and community feedback to optimize crop yield and sustainability in limited spaces. Activities include monitoring environmental variables, adjusting nutrient delivery dynamically, rotating crops based on predictive models, and coordinating local volunteer schedules. The system also incorporates waste recycling from nearby restaurants into composting units, and uses autonomous drones for pollination and pest control. Continuous improvement is driven by machine learning algorithms analyzing historical and current data, ensuring responsiveness to seasonal changes and urban microclimates while maximizing resource efficiency and community engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
SensorSetup     = Transition(label='Sensor Setup')
DataCapture     = Transition(label='Data Capture')
YieldForecast   = Transition(label='Yield Forecast')
ModelUpdate     = Transition(label='Model Update')
NutrientMix     = Transition(label='Nutrient Mix')
WaterAdjust     = Transition(label='Water Adjust')
CropRotate      = Transition(label='Crop Rotate')
WasteCollect    = Transition(label='Waste Collect')
CompostProcess  = Transition(label='Compost Process')
DroneDispatch   = Transition(label='Drone Dispatch')
PollinationRun  = Transition(label='Pollination Run')
PestControl     = Transition(label='Pest Control')
VolunteerAssign = Transition(label='Volunteer Assign')
ScheduleSync    = Transition(label='Schedule Sync')
FeedbackGather  = Transition(label='Feedback Gather')
ReportGenerate  = Transition(label='Report Generate')
ResourceAudit   = Transition(label='Resource Audit')

# Exclusive choice of adjustment actions
adjust_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[NutrientMix, WaterAdjust, CropRotate]
)

# Parallel drone activities: pollination and pest control
drone_tasks = StrictPartialOrder(
    nodes=[PollinationRun, PestControl]
)
# no order edges => concurrent execution

# Waste recycling subprocess
waste_subproc = StrictPartialOrder(
    nodes=[WasteCollect, CompostProcess]
)
waste_subproc.order.add_edge(WasteCollect, CompostProcess)

# Volunteer & feedback subprocess
volunteer_flow = StrictPartialOrder(
    nodes=[VolunteerAssign, ScheduleSync, FeedbackGather, ReportGenerate, ResourceAudit]
)
volunteer_flow.order.add_edge(VolunteerAssign, ScheduleSync)
volunteer_flow.order.add_edge(ScheduleSync, FeedbackGather)
volunteer_flow.order.add_edge(FeedbackGather, ReportGenerate)
volunteer_flow.order.add_edge(ReportGenerate, ResourceAudit)

# Main monitoring‐action cycle (to be looped)
main_cycle = StrictPartialOrder(
    nodes=[DataCapture, YieldForecast, ModelUpdate, adjust_choice,
           DroneDispatch, drone_tasks, waste_subproc]
)
main_cycle.order.add_edge(DataCapture,     YieldForecast)
main_cycle.order.add_edge(YieldForecast,   ModelUpdate)
main_cycle.order.add_edge(ModelUpdate,     adjust_choice)
main_cycle.order.add_edge(adjust_choice,   DroneDispatch)
main_cycle.order.add_edge(DroneDispatch,   drone_tasks)
main_cycle.order.add_edge(drone_tasks,     waste_subproc)

# Loop: repeat monitoring & action, exit via volunteer & feedback
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_cycle, volunteer_flow]
)

# Assemble full process: setup then loop
root = StrictPartialOrder(nodes=[SensorSetup, loop])
root.order.add_edge(SensorSetup, loop)