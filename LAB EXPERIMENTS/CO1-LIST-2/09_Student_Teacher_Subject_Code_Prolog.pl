% PROGRAM
teacher(ramesh, ai, csa1717).
teacher(lakshmi, dbms, csa1501).
teacher(suresh, os, csa1620).

student(anitha, ai).
student(bala, dbms).
student(charan, ai).
student(deepa, os).

subject_code(Sub, Code) :- teacher(_, Sub, Code).
taught_by(Student, Teacher) :- student(Student, Sub), teacher(Teacher, Sub, _).
student_details(Student, Sub, Code, Teacher) :-
    student(Student, Sub),
    teacher(Teacher, Sub, Code).

% OUTPUT (SWI-Prolog queries)
% ?- subject_code(ai, Code).
% Code = csa1717.
%
% ?- taught_by(bala, T).
% T = lakshmi.
%
% ?- student_details(anitha, Sub, Code, Teacher).
% Sub = ai,
% Code = csa1717,
% Teacher = ramesh.
%
% ?- taught_by(Student, ramesh).
% Student = anitha ;
% Student = charan.
