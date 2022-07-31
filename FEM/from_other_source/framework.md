# framework of pyFEM
1. read structure form file
2. test_struc=Structure.create_structure()
3. test_struc.create_elements()
4. test_struc.create_nodes()
5. define loads
6. define cases
7. create solver
    - condense
    - assemble
8. solve
    - sovle system
    - solve inner dof
9. create resutls object
10. output to file or graphic


<!--
```flow
st=>start: kaish
op=>operation: My Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
```
-->

