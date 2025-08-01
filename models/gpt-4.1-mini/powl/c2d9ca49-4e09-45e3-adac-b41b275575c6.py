# Generated from: c2d9ca49-4e09-45e3-adac-b41b275575c6.json
# Description: This process outlines the establishment of an urban vertical farming facility integrating advanced hydroponics and AI-driven climate control systems. The workflow begins with site analysis and structural adaptation, followed by nutrient solution formulation and seed selection tailored for urban microclimates. It involves iterative sensor calibration, data-driven growth optimization, automated pest detection, and energy consumption balancing. The process also includes continuous staff training on biosecurity protocols and sustainability metrics evaluation, culminating in the integration of a consumer subscription model for fresh produce delivery, ensuring a closed-loop urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Structure_Adapt = Transition(label='Structure Adapt')
Seed_Choose = Transition(label='Seed Choose')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Calibrate = Transition(label='Sensor Calibrate')
Climate_Setup = Transition(label='Climate Setup')
Planting_Cycle = Transition(label='Planting Cycle')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Detect = Transition(label='Pest Detect')
Data_Analyze = Transition(label='Data Analyze')
Energy_Balance = Transition(label='Energy Balance')
Staff_Train = Transition(label='Staff Train')
Biosecurity_Check = Transition(label='Biosecurity Check')
Yield_Forecast = Transition(label='Yield Forecast')
Subscription_Setup = Transition(label='Subscription Setup')
Delivery_Plan = Transition(label='Delivery Plan')
Sustainability_Audit = Transition(label='Sustainability Audit')

# Loop for iterative Sensor Calibrate and Data Analyze to optimize Growth Monitor
calibration_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Growth_Monitor, OperatorPOWL(operator=Operator.XOR, children=[Sensor_Calibrate, Data_Analyze])]
)

# Partial order for initial site and structure preparation, and nutrient / seed selection
initial_po = StrictPartialOrder(
    nodes=[Site_Survey, Structure_Adapt, Nutrient_Mix, Seed_Choose]
)
initial_po.order.add_edge(Site_Survey, Structure_Adapt)
initial_po.order.add_edge(Structure_Adapt, Nutrient_Mix)
initial_po.order.add_edge(Structure_Adapt, Seed_Choose)

# Partial order for climate setup after initial and before planting
climate_po = StrictPartialOrder(
    nodes=[Climate_Setup]
)
# Will be connected after initial_po

# Partial order for Planting Cycle onwards including calibration loop, pest detection, energy balancing
planting_po = StrictPartialOrder(
    nodes=[Planting_Cycle, calibration_loop, Pest_Detect, Energy_Balance]
)
planting_po.order.add_edge(Planting_Cycle, calibration_loop)
planting_po.order.add_edge(calibration_loop, Pest_Detect)
planting_po.order.add_edge(Pest_Detect, Energy_Balance)

# Staff training and biosecurity checking run concurrently but before yield forecast
staff_bio_po = StrictPartialOrder(
    nodes=[Staff_Train, Biosecurity_Check]
)
# No order between staff and biosecurity - concurrent

# Yield forecast after staff/biosecurity completed
yield_po = StrictPartialOrder(
    nodes=[Yield_Forecast]
)

# Sustainability audit concurrent with staff/biosecurity and before subscription setup
sustainability_po = StrictPartialOrder(
    nodes=[Sustainability_Audit]
)

# Subscription setup and delivery plan follow yield forecast and sustainability audit
subscription_po = StrictPartialOrder(
    nodes=[Subscription_Setup, Delivery_Plan]
)
subscription_po.order.add_edge(Subscription_Setup, Delivery_Plan)

# Compose staff, biosecurity, sustainability, yield, subscription into one PO
mid_po = StrictPartialOrder(
    nodes=[staff_bio_po, sustainability_po, yield_po, subscription_po]
)
# staff_bio_po and sustainability_po concurrent (no order edges)
mid_po.order.add_edge(staff_bio_po, yield_po)
mid_po.order.add_edge(sustainability_po, yield_po)
mid_po.order.add_edge(yield_po, subscription_po)

# Compose full PO with initial_po -> climate_po -> planting_po -> mid_po
root = StrictPartialOrder(
    nodes=[initial_po, climate_po, planting_po, mid_po]
)
root.order.add_edge(initial_po, climate_po)
root.order.add_edge(climate_po, planting_po)
root.order.add_edge(planting_po, mid_po)