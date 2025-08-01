# Generated from: caf2784b-5fe2-4a65-b0f5-6d36f16fcc7a.json
# Description: This process outlines the complex and multifaceted steps involved in establishing an urban vertical farm inside a repurposed industrial building. It includes initial site assessment, environmental impact evaluation, modular system design, and the integration of IoT sensors for real-time monitoring. The process continues with hydroponic system installation, nutrient calibration, and automated lighting setup tailored for optimal plant growth. It further encompasses staff training on sustainable farming techniques, ongoing data analytics for yield optimization, pest management protocols, and finally, the distribution logistics for delivering fresh produce directly to local markets. This atypical yet realistic business process requires cross-disciplinary coordination between architects, engineers, agronomists, and supply chain experts to ensure profitability and sustainability in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_audit = Transition(label='Site Audit')
impact_study = Transition(label='Impact Study')
design_modules = Transition(label='Design Modules')
sensor_setup = Transition(label='Sensor Setup')
hydroponics_install = Transition(label='Hydroponics Install')
nutrient_test = Transition(label='Nutrient Test')
lighting_config = Transition(label='Lighting Config')
staff_training = Transition(label='Staff Training')
data_collection = Transition(label='Data Collection')
yield_analysis = Transition(label='Yield Analysis')
pest_control = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')
packaging_prep = Transition(label='Packaging Prep')
market_delivery = Transition(label='Market Delivery')
feedback_loop = Transition(label='Feedback Loop')

# First partial order: Initial site assessment and design
po_initial = StrictPartialOrder(nodes=[
    site_audit,
    impact_study,
    design_modules,
    sensor_setup
])
po_initial.order.add_edge(site_audit, impact_study)
po_initial.order.add_edge(impact_study, design_modules)
po_initial.order.add_edge(design_modules, sensor_setup)

# Second partial order: Installation and calibration
po_install = StrictPartialOrder(nodes=[
    hydroponics_install,
    nutrient_test,
    lighting_config
])
po_install.order.add_edge(hydroponics_install, nutrient_test)
po_install.order.add_edge(nutrient_test, lighting_config)

# Third partial order: Training and ongoing monitoring (data collection & yield analysis)
po_training_monitoring = StrictPartialOrder(nodes=[
    staff_training,
    data_collection,
    yield_analysis
])
po_training_monitoring.order.add_edge(staff_training, data_collection)
po_training_monitoring.order.add_edge(data_collection, yield_analysis)

# Fourth partial order: Pest control and harvest planning
po_pest_harvest = StrictPartialOrder(nodes=[
    pest_control,
    harvest_plan
])
po_pest_harvest.order.add_edge(pest_control, harvest_plan)

# Fifth partial order: Packaging and delivery
po_pack_deliver = StrictPartialOrder(nodes=[
    packaging_prep,
    market_delivery
])
po_pack_deliver.order.add_edge(packaging_prep, market_delivery)

# Define the feedback loop (loop on feedback_loop and data_collection with yield_analysis)
# Model feedback_loop as a LOOP:
# loop = *(body=A (feedback_loop), redo=B (data_collection + yield_analysis + pest_control + harvest_plan))
# Actually per description, Feedback Loop implies repeated analysis and pest control phases,
# so feedback will likely loop after packaging or market delivery back to monitoring/controls.

# We'll create a loop:
# loop body: feedback_loop activity
# loop redo: partial order covering data_collection, yield_analysis, pest_control, harvest_plan

po_feedback_work = StrictPartialOrder(nodes=[
    data_collection,
    yield_analysis,
    pest_control,
    harvest_plan
])
po_feedback_work.order.add_edge(data_collection, yield_analysis)
po_feedback_work.order.add_edge(yield_analysis, pest_control)
po_feedback_work.order.add_edge(pest_control, harvest_plan)

loop_feedback = OperatorPOWL(
    operator=Operator.LOOP,
    children=[feedback_loop, po_feedback_work]
)

# Now compose the root partial order integrating all parts
# Order:
# po_initial -> po_install -> po_training_monitoring -> loop_feedback -> po_pack_deliver

root = StrictPartialOrder(nodes=[
    po_initial,
    po_install,
    po_training_monitoring,
    loop_feedback,
    po_pack_deliver
])
root.order.add_edge(po_initial, po_install)
root.order.add_edge(po_install, po_training_monitoring)
root.order.add_edge(po_training_monitoring, loop_feedback)
root.order.add_edge(loop_feedback, po_pack_deliver)