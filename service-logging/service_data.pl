service_mon(acpid,active).
service_mon(bluetooth,active).

service(acpid).
service(bluetooth).

ser_state(active).
ser_state(inactive).

ser_provided(acpid,[active]).
ser_provided(bluetooth,[inactive]).

ser_check(X,[X|_]).
ser_check(X,[_|Tail]):- ser_check(X,Tail).

ser_granted(X,Y):- ser_provided(X,Z),ser_check(Y,Z).

check(X,Y):-service(X),ser_state(Y),ser_granted(X,Y).

sla():- forall(service_mon(X,Y),check(X,Y)).

