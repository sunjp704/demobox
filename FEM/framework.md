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



```flow
s=>start: initiate
op1=>operation: create structure
op2=>operation: create load
op3=>operation: apply load to structure to create case
op4=>operation: generate a solver
op5=>operation: create result
e=>end
s->op1->op2->op3->op4->op5->end
```

