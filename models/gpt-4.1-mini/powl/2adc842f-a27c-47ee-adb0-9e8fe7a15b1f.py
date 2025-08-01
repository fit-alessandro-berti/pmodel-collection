# Generated from: 2adc842f-a27c-47ee-adb0-9e8fe7a15b1f.json
# Description: This process describes the sourcing, production, and distribution of artisanal cheese from rare breeds of goats. It involves selective breeding coordination, specialized feeding schedules, milk quality testing, traditional curdling methods, precise aging conditions, and custom packaging. The process ensures traceable origin, seasonal variation adjustments, and direct delivery to niche markets and exclusive retailers, maintaining exceptional quality and artisanal integrity throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
Breed_Selection = Transition(label='Breed Selection')
Feed_Planning = Transition(label='Feed Planning')
Milk_Collection = Transition(label='Milk Collection')
Quality_Testing = Transition(label='Quality Testing')
Curd_Preparation = Transition(label='Curd Preparation')
Mold_Inoculation = Transition(label='Mold Inoculation')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salting_Process = Transition(label='Salting Process')
Controlled_Aging = Transition(label='Controlled Aging')
Humidity_Check = Transition(label='Humidity Check')
Texture_Sampling = Transition(label='Texture Sampling')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Order_Processing = Transition(label='Order Processing')
Retail_Delivery = Transition(label='Retail Delivery')
Feedback_Gathering = Transition(label='Feedback Gathering')

# Partial order modeling the main flow with some concurrency where logically appropriate

# Sourcing & preparation partial order
sourcing_preparation = StrictPartialOrder(nodes=[
    Breed_Selection,
    Feed_Planning,
    Milk_Collection,
    Quality_Testing,
    Curd_Preparation,
    Mold_Inoculation,
    Pressing_Cheese,
    Salting_Process,
])

# Define order in sourcing_preparation
sourcing_preparation.order.add_edge(Breed_Selection, Feed_Planning)
sourcing_preparation.order.add_edge(Feed_Planning, Milk_Collection)
sourcing_preparation.order.add_edge(Milk_Collection, Quality_Testing)
sourcing_preparation.order.add_edge(Quality_Testing, Curd_Preparation)
sourcing_preparation.order.add_edge(Curd_Preparation, Mold_Inoculation)
sourcing_preparation.order.add_edge(Mold_Inoculation, Pressing_Cheese)
sourcing_preparation.order.add_edge(Pressing_Cheese, Salting_Process)

# Aging partial order with loops to reflect checks and sampling until done
aging_body = StrictPartialOrder(nodes=[Controlled_Aging, Humidity_Check, Texture_Sampling])
aging_body.order.add_edge(Controlled_Aging, Humidity_Check)
aging_body.order.add_edge(Humidity_Check, Texture_Sampling)

# Loop: After aging, either finish or repeat checking and sampling aging
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[Controlled_Aging, StrictPartialOrder(nodes=[Humidity_Check, Texture_Sampling])])

# Packaging partial order (Packaging Design and Label Printing can be concurrent)
packaging = StrictPartialOrder(nodes=[Packaging_Design, Label_Printing])
# no order edges between packaging design and label printing => concurrent

# Distribution partial order
distribution = StrictPartialOrder(nodes=[Order_Processing, Retail_Delivery, Feedback_Gathering])
distribution.order.add_edge(Order_Processing, Retail_Delivery)
distribution.order.add_edge(Retail_Delivery, Feedback_Gathering)

# Assemble all parts in main PO in order:
#  sourcing_preparation --> aging_loop --> packaging --> distribution

root = StrictPartialOrder(nodes=[sourcing_preparation, aging_loop, packaging, distribution])
root.order.add_edge(sourcing_preparation, aging_loop)
root.order.add_edge(aging_loop, packaging)
root.order.add_edge(packaging, distribution)