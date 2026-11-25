% PROGRAM
planet(mercury, 1, 0, terrestrial).
planet(venus, 2, 0, terrestrial).
planet(earth, 3, 1, terrestrial).
planet(mars, 4, 2, terrestrial).
planet(jupiter, 5, 95, gas_giant).
planet(saturn, 6, 146, gas_giant).
planet(uranus, 7, 28, ice_giant).
planet(neptune, 8, 16, ice_giant).

position(Name, P) :- planet(Name, P, _, _).
type_of(Name, T) :- planet(Name, _, _, T).
has_moons(Name) :- planet(Name, _, M, _), M > 0.
inner_planet(Name) :- planet(Name, P, _, _), P =< 4.

% OUTPUT (SWI-Prolog queries)
% ?- position(earth, P).
% P = 3.
%
% ?- type_of(jupiter, T).
% T = gas_giant.
%
% ?- has_moons(X).
% X = earth ;
% X = mars ;
% X = jupiter ;
% X = saturn ;
% X = uranus ;
% X = neptune.
%
% ?- inner_planet(X).
% X = mercury ;
% X = venus ;
% X = earth ;
% X = mars.
