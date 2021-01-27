# Pruner passes

## Statement pruning

### Required preceding passes 

- None

### Parameters 
- `PRUNE_STMT_MAX`  : The initial size of the bank of statements that we start pruning, later this might become a function of the initial size of the given p4 program.   
- `PRUNE_ITERS`     : The number of times the statement pruner would run through the program.
- `NO_CHNG_ITERS`   : If the program remains the same for this number of iterations then we assume the phase is completed and move to the next pass.

### Description

This pass tries to prune statements from the program. A certain number of statements are chosen at random by a `Collector` which is a subclass of an `Inspector`. Then these are fed to a `Pruner` which is a subclass of a `Transform`, which actually prunes the statements from the program tree. We start with a very large number of statements to prune, and then follow a AIMD, if we were successful in our attempt, i.e the exit code of the program remained the same, i.e the bug still exists in the program, we increase the bank by 2 statements otherwise we half the size of the bank.


