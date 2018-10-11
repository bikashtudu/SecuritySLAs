service_mon(acpid,active,prasad,vm2).
service_mon(bluetooth,active,prasad,vm2).

service(acpid).
service(bluetooth).

ser_state(active).
ser_state(inactive).

ser_provided(acpid,[active],[prasad],[vm2]).
ser_provided(bluetooth,[active],[prasad],[vm1,vm2]).

ser_check(X,[X|_]).
ser_check(X,[_|Tail]):- ser_check(X,Tail).

vm_check(X,[X|_]).
vm_check(X,[_|Tail]):- ser_check(X,Tail).

user_check(X,[X|_]).
user_check(X,[_|Tail]):- ser_check(X,Tail).

ser_granted(X,Y,U,V):- ser_provided(X,Z,A,K),ser_check(Y,Z),user_check(U,A),vm_check(V,K).

check(X,Y,U,V):-service(X),ser_state(Y),ser_granted(X,Y,U,V).

sla():- forall(service_mon(X,Y,U,V),check(X,Y,U,V)).
