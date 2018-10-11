service_check(acpid,active,vm2).
service_check(bluetooth,active,vm2).

service_req(acpid,active,[vm2]).
service_req(bluetooth,active,[vm2,vm1]).

vms(X,[X|_]).
vms(X,[_|Tail]):- vms(X,Tail).

service(X,Y,V):- service_req(X,Y,K),vms(V,K).

sla():- forall(service(X,Y,V),service_check(X,Y,V)).
