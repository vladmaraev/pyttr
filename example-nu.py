from pprint import pprint
from nu import Type, BType, PType, DepType, Pred, MeetType_n, FunType, InhibitType_n, StringType_n, Ty, iota, gensym_n, nu, and_n, MeetType, or_n, JoinType, labels, Rec, RecType
from neurons import Network, Neuron, Synapse, ActivityPattern
from utils import show, example

example(1)
#Types in general correspond to a pattern of activation on a given network.
T = Type('MyType')
print(show(nu(T)))

N = Network()
n1 = N.add_neuron()
h1 = ActivityPattern([[0]])
Tn = nu(T)
Tn.add_apat(N,h1)
N.ntrace()
Tn.create_n(N)
N.display_history()

print(Tn.query_n(N))

example(2)
#We can do the same for a basic type. In this example T corresponds to the
#activation of two neurons.
T = BType('MyBasicType')
print(show(nu(T)))

N = Network()
n1 = N.add_neuron()
n2 = N.add_neuron()
h1 = ActivityPattern([[0],[1]])
Tn = nu(T)
Tn.add_apat(N,h1)
N.ntrace()
Tn.create_n(N)
N.display_history()

print(Tn.query_n(N))

example(3)
Ind = Type('Ind')
Ind.judge('a')
Ind.judge('b')
hug = Pred('hug',[Ind,Ind])

N = Network()
iota.add_grandmother('a',N)
iota.add_grandmother('b',N)
hug_n = nu(hug)
hug_n.add_grandmother(N)
N.ntrace()
hug_a_b_n = nu(PType(hug,['a','b']))
hug_a_b_n.create_n(N)
N.display_history()

N.nontrace()


Ind.judge('c')
believe = Pred('believe',[Ind,Ty])
iota.add_grandmother('c',N)
believe_n = nu(believe)
believe_n.add_grandmother(N)

N.ntrace()
nu(PType(believe, ['c', PType(hug,['a','b'])])).create_n(N)
N.display_history()





example(4)
# N.nontrace()
# N.inhibit()
# # gensym_n.add_function_levels(N,2)
# # print(gensym_n.num_function_levels(N))

# N.ntrace()
# #print(N.history)
# N.display_history()

# PType(hug,['a','b']).nu.create_n(N)
# #print(N.history)
# N.display_history()

N.nontrace()
Ind_n = nu(Ind)
Ind_n.add_grandmother(N)
N.ntrace()
T = DepType('v',Ind,PType(hug,['v','b']))
Tn = nu(T)
Tn.create_n(N)
#print(N.history)
N.display_history()
pprint(Tn.show_apat(N))

N.nontrace()
N.ntrace()
T= DepType('x',Ind,DepType('y',Ind,PType(hug,['x','y'])))
Tn = nu(T)
Tn.create_n(N)
N.display_history()
pprint(Tn.show_apat(N))



example(5)
Ppty = FunType(Ind,Ty)
every = Pred('every',[Ppty,Ppty])
every_n = nu(every)
N = Network()
every_n.add_grandmother(N)

dog = Pred('dog',[Ind])
dog_n = nu(dog)
dog_n.add_grandmother(N)

run = Pred('run',[Ind])
run_n = nu(run)
run_n.add_grandmother(N)

Ind_n.add_grandmother(N)
dog_ppty = DepType('x',Ind,PType(dog,['x']))
run_ppty = DepType('x',Ind,PType(run,['x']))

Tedr = PType(every,[dog_ppty,run_ppty])
Tedr_n = nu(Tedr)
N.ntrace()
Tedr_n.create_n(N)
N.display_history()
pprint(Tedr_n.show_apat(N))



N.nontrace()
m = N.memorize_type(Tedr_n,'every dog runs')
N.ntrace()
m.excite()
N.run()
N.display_history()



example(6)
N = Network()
Ind_n.add_grandmother(N)
iota.add_grandmother('a',N)
iota.add_grandmother('b',N)
a_n = nu('a')
pprint(Ind_n.show_apat(N))
pprint(a_n.show_apat(N))
pprint(Ind_n.judgmnt_type_n(a_n).show_apat(N))

m = N.memorize_judgmnt(Ind_n,a_n,'a:Ind')
N.ntrace()
m.excite()
N.run()
N.display_history()

example(7)
# uses variables from example 5
N = Network()
every_n.add_grandmother(N)
dog_n.add_grandmother(N)
run_n.add_grandmother(N)
Ind_n.add_grandmother(N)
T = PType(every,[dog_ppty,run_ppty])
T_n = nu(T)
iota.add_grandmother('e',N)
e_n = nu('e')
m = N.memorize_judgmnt(T_n,e_n, 'e:every(dog,run)')
N.ntrace()
m.excite()
N.run()
N.display_history()



example(8)
N = Network()
T1 = Type('T1')
T2 = Type('T2')
T1_n = nu(T1)
T2_n = nu(T2)
T1_n.add_grandmother(N)
T2_n.add_grandmother(N)
and_n.add_grandmother(N)
iota.add_grandmother('a',N)
T3 = MeetType(T1,T2)
T3_n = nu(T3)
m = N.memorize_judgmnt(T3_n,a_n,'a:T1&T2')
N.ntrace()
m.excite()
N.run()
N.display_history()

print(N.match_apat(T1_n.judgmnt_type_n(a_n).getapat(N)))
print(N.match_apat(T2_n.judgmnt_type_n(a_n).getapat(N)))


example(9)
N = Network()
T1 = Type('T1')
T2 = Type('T2')
T1_n = nu(T1)
T2_n = nu(T2)
T1_n.add_grandmother(N)
T2_n.add_grandmother(N)
or_n.add_grandmother(N)
iota.add_grandmother('a',N)
T3 = JoinType(T1,T2)
T3_n = nu(T3)
m = N.memorize_judgmnt(T3_n,a_n,'a:T1vT2')
N.ntrace()
m.excite()
N.run()
N.display_history()

print(N.match_apat(T1_n.judgmnt_type_n(a_n).getapat(N)))
print(N.match_apat(T2_n.judgmnt_type_n(a_n).getapat(N)))



example(10)
#Subtyping for neural types in terms of a relation on apats on a given network.  Works for these examples...
print(T1_n.judgmnt_type_n(a_n).subtype_of_n(T3_n.judgmnt_type_n(a_n),N))
and_n.add_grandmother(N)
T4 = MeetType(T1,T2)
T4_n = nu(T4)
print(T1_n.judgmnt_type_n(a_n).subtype_of_n(T4_n.judgmnt_type_n(a_n),N))


example(11)
# Since both labels and objects are implemented as strings it is important not
# to use the same string as a label and an object.  Here we use the convention
# that labels always begin with 'l_'.

N = Network()
labels.add_grandmother('l_x',N)
labels.add_grandmother('l_e',N) 
iota.add_grandmother('a',N)
iota.add_grandmother('s',N)
r = Rec({'l_x':'a','l_e':'s'})
r_n = nu(r)
pprint(r_n.show_apat(N))

N.ntrace()
r_n.create_n(N)
N.display_history()


example(12)
N = Network()
labels.add_grandmother('l_x',N)
labels.add_grandmother('l_e',N)
Ind_n.add_grandmother(N)
dog_n.add_grandmother(N)
Dog = DepType('v',Ind,PType(dog,['v']))
T_dog = RecType({'l_x':Ind,
                 'l_e':(Dog,['l_x'])})
T_dog_n = nu(T_dog)
pprint(T_dog_n.show_apat(N))

N.ntrace()
T_dog_n.create_n(N)
N.display_history()
#Problem with two labels at same time in dependent fields
#Now solved: a label neuron is marked as either a label or part of a value

#Random order? np.random.shuffle()


example(13)
#Function application
N = Network()
dog_n.add_grandmother(N)
Ind_n.add_grandmother(N)
Dog = DepType('v',Ind,PType(dog,['v']))
iota.add_grandmother('a',N)
print(show(Dog.app('a')))
print('\n')
Dog_n = nu(Dog)
a_n = nu('a')
Dog_a_n = nu(Dog.app('a'))
pprint(Dog_n.show_apat(N))
print('\n')
pprint(a_n.show_apat(N))
print('\n')
pprint(Dog_a_n.show_apat(N))



example(14)
#Substitution in records
N = Network()
labels.add_grandmother('l_x',N)
labels.add_grandmother('l_e',N) 
iota.add_grandmother('a',N)
iota.add_grandmother('s',N)
r = Rec({'l_x':'a','l_e':'s'})
iota.add_grandmother('s1',N)
r1 = r.subst('s','s1')
r1_n = nu(r1)
pprint(r1_n.show_apat(N))




example(15) #Substitution of dependent types in record types
N = Network()
labels.add_grandmother('l_x',N)
labels.add_grandmother('l_e',N)
Ind_n.add_grandmother(N)
dog_n.add_grandmother(N)
cat = Pred('cat',[Ind])
cat_n = nu(cat)
cat_n.add_grandmother(N)
Dog = DepType('v',Ind,PType(dog,['v']))
Cat = DepType('v',Ind,PType(cat,['v']))
T_dog = RecType({'l_x':Ind,
                 'l_e':(Dog,['l_x'])})
T_cat = T_dog.subst(Dog,Cat)
print(show(T_dog))
print(show(T_cat))
T_dog_n = nu(T_dog)
T_cat_n = nu(T_cat)
pprint(T_dog_n.show_apat(N))
print('\n')
pprint(T_cat_n.show_apat(N))


example(16)
N = Network()
labels.add_grandmother('l_x',N)
labels.add_grandmother('l_e',N) 
iota.add_grandmother('a',N)
iota.add_grandmother('s',N)
Ind_n.add_grandmother(N)
r = Rec({'l_x':'a','l_e':'s'})
r_n = nu(r)
dog_n.add_grandmother(N)
Dog = DepType('v',Ind,PType(dog,['v']))
T_dog = RecType({'l_x':Ind,
                 'l_e':(Dog,['l_x'])})
T_dog_n = nu(T_dog)
pprint(T_dog_n.resolve(r_n).show_apat(N))
print('\n')
j_n = T_dog_n.judgmnt_type_n(r_n)
pprint(j_n.show_apat(N))
print('\n')



N.ntrace()
j_n.create_n(N)
N.display_history()



labels.add_grandmother('l_type',N)
labels.add_grandmother('l_obj',N)
j_n = nu(T_dog.aus_prop(r))
pprint(j_n.show_apat(N))
N.nontrace()
N.ntrace()
j_n.create_n(N)
N.display_history()

# See ausprop.pdf for an annotated version of the last example


