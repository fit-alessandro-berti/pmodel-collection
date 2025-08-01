# Generated from: 683af796-cce1-4480-9133-6226ba95b043.json
# Description: This process outlines the establishment of a sustainable urban vertical farm within a repurposed industrial building. It involves site assessment, structural retrofitting, climate control system installation, hydroponic setup, nutrient solution calibration, crop selection based on urban demand, automation integration, pest monitoring via AI sensors, energy consumption optimization, staff training on novel farming techniques, regulatory compliance verification, market distribution planning, and continuous yield monitoring to ensure maximal efficiency and minimal environmental impact throughout the farm's operational lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
t_sa   = Transition(label='Site Assessment')
t_sr   = Transition(label='Structural Retrofit')
t_cs   = Transition(label='Climate Setup')
t_hi   = Transition(label='Hydroponic Install')
t_nc   = Transition(label='Nutrient Calibrate')
t_csel = Transition(label='Crop Selection')
t_ai   = Transition(label='Automation Integrate')
t_pm   = Transition(label='Pest Monitoring')
t_eo   = Transition(label='Energy Optimize')
t_st   = Transition(label='Staff Training')
t_rc   = Transition(label='Regulatory Check')
t_mp   = Transition(label='Market Planning')

# Define loop body activities
t_ym = Transition(label='Yield Monitoring')
t_wr = Transition(label='Waste Recycling')
t_da = Transition(label='Data Analysis')

# Silent transition to start/exit the loop
skip = SilentTransition()

# Body of the continuous cycle: yield monitoring, waste recycling, data analysis (concurrent)
body = StrictPartialOrder(nodes=[t_ym, t_wr, t_da])
# no order edges => fully concurrent

# Loop: execute skip, then either exit or run body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[skip, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    t_sa, t_sr, t_cs, t_hi, t_nc, t_csel, t_ai, t_pm, t_eo, t_st, t_rc, t_mp, loop
])

# Sequential workflow up to market planning, then enter the continuous loop
root.order.add_edge(t_sa,   t_sr)
root.order.add_edge(t_sr,   t_cs)
root.order.add_edge(t_cs,   t_hi)
root.order.add_edge(t_hi,   t_nc)
root.order.add_edge(t_nc,   t_csel)
root.order.add_edge(t_csel, t_ai)
root.order.add_edge(t_ai,   t_pm)
root.order.add_edge(t_pm,   t_eo)
root.order.add_edge(t_eo,   t_st)
root.order.add_edge(t_st,   t_rc)
root.order.add_edge(t_rc,   t_mp)
root.order.add_edge(t_mp,   loop)