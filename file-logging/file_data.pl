
file(syslog).
file(sys).

file_cmd(sys_read).
file_cmd(sys_write).

file_provided(syslog,[sys_read],[prasad],[vm2]).
file_provided(sys,[sys_read,sys_write],[prasad],[vm1,vm2]).

file_check(X,[X|_]).
file_check(X,[_|Tail]):- file_check(X,Tail).

vm_check(X,[X|_]).
vm_check(X,[_|Tail]):- file_check(X,Tail).

user_check(X,[X|_]).
user_check(X,[_|Tail]):- file_check(X,Tail).

file_granted(X,Y,U,V):- file_provided(X,Z,A,K),file_check(Y,Z),user_check(U,A),vm_check(V,K).

check(X,Y,U,V):-file(X),file_cmd(Y),file_granted(X,Y,U,V).

sla():- forall(file_mon(X,Y,U,V),check(X,Y,U,V)).
