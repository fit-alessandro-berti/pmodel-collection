# Generated from: 16f13f47-998c-49ac-9e09-5f8c4fc7747d.json
# Description: This process details the complex steps involved in establishing an urban vertical farm within a repurposed industrial building. It integrates architectural redesign, advanced hydroponic system installation, environmental control calibration, and supply chain coordination. The workflow encompasses site analysis, regulatory compliance, modular assembly, nutrient solution formulation, automation programming, and staff training. Emphasis is placed on sustainability through energy-efficient lighting, water recycling, and waste management. The process concludes with quality assurance testing and market launch preparation to ensure consistent crop production and profitability in an unconventional urban agriculture setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Activities
tsurvey = Transition(label='Site Survey')
dlayout = Transition(label='Design Layout')
rcheck = Transition(label='Regulatory Check')
sreinforce = Transition(label='Structural Reinforce')
hsetup = Transition(label='Hydroponic Setup')
lighting = Transition(label='Lighting Install')
climate = Transition(label='Climate Control')
waterrec = Transition(label='Water Recycling')
nutrient = Transition(label='Nutrient Mix')
automation = Transition(label='Automation Config')
sensor = Transition(label='Sensor Calibrate')
testing = Transition(label='System Testing')
staff = Transition(label='Staff Training')
waste = Transition(label='Waste Disposal')
launch = Transition(label='Market Launch')

# Phase 1: Site analysis & compliance
ph1 = StrictPartialOrder(nodes=[tsurvey, dlayout, rcheck, sreinforce])
ph1.order.add_edge(tsurvey, dlayout)
ph1.order.add_edge(dlayout, rcheck)
ph1.order.add_edge(rcheck, sreinforce)

# Phase 2: Hydroponic & sustainability setup
ph2 = StrictPartialOrder(nodes=[hsetup, lighting, climate, waterrec])
ph2.order.add_edge(hsetup, lighting)
ph2.order.add_edge(hsetup, climate)
ph2.order.add_edge(hsetup, waterrec)

# Phase 3: Nutrient & automation configuration
ph3 = StrictPartialOrder(nodes=[nutrient, automation, sensor])
ph3.order.add_edge(nutrient, automation)
ph3.order.add_edge(automation, sensor)

# Phase 4: Testing, training, waste disposal
ph4 = StrictPartialOrder(nodes=[testing, staff, waste])
ph4.order.add_edge(testing, staff)
ph4.order.add_edge(testing, waste)

# Root: end-to-end process
root = StrictPartialOrder(nodes=[ph1, ph2, ph3, ph4, launch])
root.order.add_edge(ph1, ph2)
root.order.add_edge(ph2, ph3)
root.order.add_edge(ph3, ph4)
root.order.add_edge(ph4, launch)