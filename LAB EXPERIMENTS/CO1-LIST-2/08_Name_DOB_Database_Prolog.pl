% PROGRAM
person(arun, dob(12, 5, 2003)).
person(priya, dob(23, 8, 2004)).
person(karthik, dob(7, 1, 2003)).
person(divya, dob(30, 11, 2004)).

dob_of(Name, D, M, Y) :- person(Name, dob(D, M, Y)).
born_in_year(Year, Name) :- person(Name, dob(_, _, Year)).

% OUTPUT (SWI-Prolog queries)
% ?- dob_of(priya, D, M, Y).
% D = 23,
% M = 8,
% Y = 2004.
%
% ?- born_in_year(2003, Name).
% Name = arun ;
% Name = karthik.
%
% ?- person(Name, dob(_, 11, _)).
% Name = divya.
