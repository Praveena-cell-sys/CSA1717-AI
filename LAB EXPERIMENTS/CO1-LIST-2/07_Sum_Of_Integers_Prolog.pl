% PROGRAM
sum(0, 0).
sum(N, S) :-
    N > 0,
    N1 is N - 1,
    sum(N1, S1),
    S is S1 + N.

% OUTPUT (SWI-Prolog queries)
% ?- sum(5, S).
% S = 15.
%
% ?- sum(10, S).
% S = 55.
%
% ?- sum(100, S).
% S = 5050.
