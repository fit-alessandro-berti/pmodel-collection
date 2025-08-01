# Generated from: 96686db1-0a80-44e0-9978-d3231dba3c8e.json
# Description: This process describes the complex establishment of an urban vertical farm within a repurposed multi-story building. It involves integrating advanced hydroponic systems, optimizing artificial lighting, and implementing automated nutrient delivery tailored to diverse plant species. The process ensures sustainable water recycling, climate control, and pest management without chemicals. Coordination with local authorities for zoning and energy compliance is required. Post-installation, continuous monitoring through IoT sensors enables adaptive growth adjustments. The integration of AI-driven analytics supports yield forecasting and resource optimization, ensuring economic viability within urban agriculture constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Zoning_Approval = Transition(label='Zoning Approval')
Structural_Audit = Transition(label='Structural Audit')

Hydroponic_Design = Transition(label='Hydroponic Design')
Lighting_Setup = Transition(label='Lighting Setup')
Nutrient_Plan = Transition(label='Nutrient Plan')

Water_Recycling = Transition(label='Water Recycling')
Climate_Control = Transition(label='Climate Control')
Pest_Monitoring = Transition(label='Pest Monitoring')

Sensor_Install = Transition(label='Sensor Install')
IoT_Network = Transition(label='IoT Network')

AI_Integration = Transition(label='AI Integration')

Staff_Training = Transition(label='Staff Training')
Growth_Testing = Transition(label='Growth Testing')
Yield_Forecast = Transition(label='Yield Forecast')

# Partial order for Initial phase: Site Survey --> (Zoning Approval & Structural Audit concurrent)
initial_phase = StrictPartialOrder(nodes=[Site_Survey, Zoning_Approval, Structural_Audit])
initial_phase.order.add_edge(Site_Survey, Zoning_Approval)
initial_phase.order.add_edge(Site_Survey, Structural_Audit)

# Partial order for Design phase: Hydroponic Design, Lighting Setup, Nutrient Plan concurrent
design_phase = StrictPartialOrder(
    nodes=[Hydroponic_Design, Lighting_Setup, Nutrient_Plan]
)
# all concurrent, no edges

# Partial order for Environmental systems installation: Water Recycling --> Climate Control --> Pest Monitoring
env_systems = StrictPartialOrder(
    nodes=[Water_Recycling, Climate_Control, Pest_Monitoring]
)
env_systems.order.add_edge(Water_Recycling, Climate_Control)
env_systems.order.add_edge(Climate_Control, Pest_Monitoring)

# Partial order for Sensor and Network setup: Sensor Install --> IoT Network
sensor_phase = StrictPartialOrder(
    nodes=[Sensor_Install, IoT_Network]
)
sensor_phase.order.add_edge(Sensor_Install, IoT_Network)

# Partial order for AI integration and training: AI Integration --> Staff Training
ai_training = StrictPartialOrder(nodes=[AI_Integration, Staff_Training])
ai_training.order.add_edge(AI_Integration, Staff_Training)

# Partial order for Testing and Forecast (concurrent)
test_forecast = StrictPartialOrder(nodes=[Growth_Testing, Yield_Forecast])
# no edges, concurrent

# Compose Installation phase: design_phase must finish before env_systems which must finish before sensor_phase
installation_phase = StrictPartialOrder(
    nodes=[design_phase, env_systems, sensor_phase]
)
installation_phase.order.add_edge(design_phase, env_systems)
installation_phase.order.add_edge(env_systems, sensor_phase)

# Compose Post-installation phase: ai_training --> test_forecast
post_installation = StrictPartialOrder(
    nodes=[ai_training, test_forecast]
)
post_installation.order.add_edge(ai_training, test_forecast)

# Compose Overall process: 
# initial_phase --> installation_phase --> post_installation
root = StrictPartialOrder(
    nodes=[initial_phase, installation_phase, post_installation]
)
root.order.add_edge(initial_phase, installation_phase)
root.order.add_edge(installation_phase, post_installation)