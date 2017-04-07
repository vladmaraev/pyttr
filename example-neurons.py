from neurons import Neuron, Network, Synapse, InhibitorySynapse, ActivityPattern

n = Neuron()
print(n.state.dendrites)

n.update()
print(n.state.axon)

n.excite()
print(n.state.axon)

n.inhibit()
print(n.state.axon)

N = Network()
N.add_neuron()
N.add_neuron()
print(N.neurons[0].state.axon)
print(N.neurons[1].state.axon)

N = Network()
n1 = N.add_neuron()

print(N.history)

N.ntrace()
print(N.history)

n1.excite()
print(N.history)

n1.inhibit()
print(N.history)

n1.spike()
print(N.history)

N.nontrace()

n2 = N.add_neuron()

N.ntrace()
n1.excite()
n2.excite()
print(N.history)

N.nontrace()

n1.inhibit()
n2.inhibit()

s1 = Synapse(n1,n2)

N.ntrace()
n1.excite()
N.run()
print(N.history)

n1.inhibit() #n2 still active
print(N.history)

n1.excite()
print(N.history)



n1.inhibit('notick')
n2.inhibit()
print(N.history)

N.nontrace()

n3 = N.add_neuron()

N.ntrace()
N.excite()
print(N.history)

N.inhibit()
print(N.history)

N.excite([1,2])
print(N.history)

N.inhibit([1])
print(N.history)

N.nontrace()
N.inhibit()
N.ntrace()
h = ActivityPattern([[2]])
N.realize_apat(h)
print(N.history)

N.nontrace()
N.inhibit()
N.ntrace()
h = ActivityPattern([[2],[1]])
N.realize_apat(h)
print(N.history)

N.nontrace()
N.inhibit()
N.ntrace()
h = ActivityPattern([[2],[1],[1,2]],[[1],[1],[0,0]])
N.realize_apat(h)
print(N.history)


N.nontrace()
N.inhibit()
N.ntrace()
h = ActivityPattern([[0]])
N.realize_apat(h)
N.run()
print(N.history)
#Both 0 and 1 are activated because of the synapse connecting 0 to 1

print(N.match_apat(h))

N = Network()
n = N.add_neuron('n')
n1 = N.add_neuron('n1')
n2 = N.add_neuron('n2')
n3 = N.add_neuron('n3')
d1 = N.add_delay_neuron(0,'d1')
d2 = N.add_delay_neuron(1,'d2')
s1 = Synapse(n,n1)
s2 = Synapse(n,d1)
s3 = Synapse(n,d2)
s4 = Synapse(d1,n2)
s5 = Synapse(d2,n3)
s6 = InhibitorySynapse(d1,n1)
s7 = InhibitorySynapse(d2,n2)
N.ntrace()
n.excite()
N.run()
N.display_history()
