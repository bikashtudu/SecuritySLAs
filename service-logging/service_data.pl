service_mon(acpid,active,vm1).
service_mon(bluetooth,active,vm2).

service(acpid).
service(bluetooth).

ser_state(active).
ser_state(inactive).

ser_provided(acpid,[active],[vm1]).
ser_provided(bluetooth,[active],[vm1,vm2]).

ser_check(X,[X|_]).
ser_check(X,[_|Tail]):- ser_check(X,Tail).

vm_check(X,[X|_]).
vm_check(X,[_|Tail]):- ser_check(X,Tail).

ser_granted(X,Y,V):- ser_provided(X,Z,K),ser_check(Y,Z),vm_check(V,K).

check(X,Y,V):-service(X),ser_state(Y),ser_granted(X,Y,V).

sla():- forall(service_mon(X,Y,V),check(X,Y,V)).
