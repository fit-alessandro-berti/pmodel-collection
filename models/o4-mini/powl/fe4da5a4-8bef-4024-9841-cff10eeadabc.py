# Generated from: fe4da5a4-8bef-4024-9841-cff10eeadabc.json
# Description: This process describes the complex and atypical business workflow for establishing an urban rooftop farm on commercial buildings. It includes securing permits, structural assessments, soil and water testing, sourcing sustainable materials, installing modular planters, integrating IoT sensors for environmental monitoring, setting up automated irrigation systems, coordinating with local vendors for organic seeds, training staff on urban agriculture practices, implementing pest control measures, marketing fresh produce to local restaurants, managing seasonal crop rotation, ensuring compliance with city health regulations, and establishing waste composting protocols to maintain environmental sustainability and maximize yield within limited urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
permit = Transition(label='Permit Securing')
structure = Transition(label='Structure Check')
soil = Transition(label='Soil Testing')
water = Transition(label='Water Analysis')
material = Transition(label='Material Sourcing')
vendor = Transition(label='Vendor Liaison')
planter = Transition(label='Planter Setup')
sensor = Transition(label='Sensor Install')
irrigation = Transition(label='Irrigation Setup')
training = Transition(label='Staff Training')
pest = Transition(label='Pest Control')
crop = Transition(label='Crop Rotation')
marketing = Transition(label='Produce Marketing')
health = Transition(label='Health Audit')
compost = Transition(label='Waste Composting')

# Define the loop over seasonal crop rotation + pest control
skip = SilentTransition()
cycle_body = StrictPartialOrder(nodes=[crop, pest])
cycle_body.order.add_edge(crop, pest)
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle_body, skip])

# Build the root partial order
root = StrictPartialOrder(
    nodes=[
        permit, structure,
        soil, water,
        material, vendor,
        planter,
        sensor, irrigation, training,
        loop,
        marketing, health, compost
    ]
)

# Add control-flow dependencies
root.order.add_edge(permit, structure)

# After structure check, do testing and sourcing in parallel
root.order.add_edge(structure, soil)
root.order.add_edge(structure, water)
root.order.add_edge(structure, material)
root.order.add_edge(structure, vendor)

# Planter setup waits for tests and sourcing/vendor liaison
root.order.add_edge(soil, planter)
root.order.add_edge(water, planter)
root.order.add_edge(material, planter)
root.order.add_edge(vendor, planter)

# After planter is in place, install sensors, irrigation, and train staff (concurrent)
root.order.add_edge(planter, sensor)
root.order.add_edge(planter, irrigation)
root.order.add_edge(planter, training)

# After setup and training, enter the seasonal loop
root.order.add_edge(sensor, loop)
root.order.add_edge(irrigation, loop)
root.order.add_edge(training, loop)

# Once the loop finishes, carry out final activities in sequence
root.order.add_edge(loop, marketing)
root.order.add_edge(marketing, health)
root.order.add_edge(health, compost)