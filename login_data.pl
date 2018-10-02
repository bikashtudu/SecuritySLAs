user_login(prasad,vm2).
user_login(root,vm2).
user_login(gdm,vm2).
user_login(prasad,vm1).


users(root).
users(prasad).
users(gdm).

vm(vm1).
vm(vm2).
vm(vm3).

access(root,[vm1,vm2]).
access(prasad,[vm2,vm1]).
access(gdm,[vm2]).

access_check(X,[X|_]).
access_check(X,[_|Tail]):- access_check(X,Tail).

check(X,Y):-users(X),vm(Y),access_granted(X,Y).

access_granted(X,Y):- access(X,Z),access_check(Y,Z).
sla():- user_login(X,Y),check(X,Y).



