# Generated from: e425f41a-416a-491d-8642-2f5bf6427ce6.json
# Description: This process outlines the creation of bespoke artisanal perfumes combining traditional crafting techniques with modern sensory analysis. It begins with ingredient sourcing from rare botanicals, followed by extraction and initial blending. Multiple rounds of sensory evaluation and chemical refinement ensure a balanced, unique scent profile. Packaging is customized per client preferences, including hand-labeling and bespoke containers. Throughout, quality control and regulatory compliance are maintained, culminating in limited edition releases that blend craftsmanship with innovation for luxury markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ing_src = Transition(label='Ingredient Sourcing')
bot_ext = Transition(label='Botanical Extraction')
init_blend = Transition(label='Initial Blending')
sens_test = Transition(label='Sensory Testing')
chem_anal = Transition(label='Chemical Analysis')
recipe_refine = Transition(label='Recipe Refinement')
stab_check = Transition(label='Stability Check')
client_samp = Transition(label='Client Sampling')
feedback = Transition(label='Feedback Review')
final_adj = Transition(label='Final Adjustment')
cust_pack = Transition(label='Custom Packaging')
label_design = Transition(label='Label Design')
hand_labeling = Transition(label='Hand Labeling')
reg_audit = Transition(label='Regulatory Audit')
batch_doc = Transition(label='Batch Documentation')
limited_release = Transition(label='Limited Release')
market_launch = Transition(label='Market Launch')

# Build the loop for multiple rounds of sensory testing & chemical refinement
sens_chem_seq = StrictPartialOrder(nodes=[sens_test, chem_anal])
sens_chem_seq.order.add_edge(sens_test, chem_anal)

loop_cycle = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sens_chem_seq, recipe_refine]
)

# Assemble the overall workflow as a partial order
root = StrictPartialOrder(nodes=[
    ing_src,
    bot_ext,
    init_blend,
    loop_cycle,
    stab_check,
    client_samp,
    feedback,
    final_adj,
    cust_pack,
    label_design,
    hand_labeling,
    limited_release,
    market_launch,
    reg_audit,
    batch_doc
])

# Sequencing edges
root.order.add_edge(ing_src, bot_ext)
root.order.add_edge(bot_ext, init_blend)
root.order.add_edge(init_blend, loop_cycle)
root.order.add_edge(loop_cycle, stab_check)
root.order.add_edge(stab_check, client_samp)
root.order.add_edge(client_samp, feedback)
root.order.add_edge(feedback, final_adj)
root.order.add_edge(final_adj, cust_pack)
root.order.add_edge(cust_pack, label_design)
root.order.add_edge(label_design, hand_labeling)
root.order.add_edge(hand_labeling, limited_release)
root.order.add_edge(limited_release, market_launch)

# 'reg_audit' and 'batch_doc' remain unconnected to model their ongoing, concurrent nature