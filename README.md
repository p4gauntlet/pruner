# Usage

# To prune without a config 

`p4pruner --compiler-bin [PATH_TO_COMPILER_BIN] --validation-bin [PATH_TO_VALIDATION_BIN] [P4_PROG] `

# To prune with a config 

`p4pruner --config [P4_CONFIG] [P4_PROG] `

Note : A sample config is provided at the root of the repo. 


---

# Pruning passes

## Statement pruning

### Required preceding passes 

- None

### Parameters 
- `PRUNE_STMT_MAX`  : The initial size of the bank of statements that we start pruning, later this might become a function of the initial size of the given p4 program.   
- `PRUNE_ITERS`     : The number of times the statement pruner would run through the program.
- `NO_CHNG_ITERS`   : If the program remains the same for this number of iterations then we assume the phase is completed and move to the next pass.
- `AIDM_INCREASE`   : The additive increasing factor for the bank of statements.
- `AIDM_DECREASE`   : The multiplicative decresing factor for the bank of statements.
  
### Description

This pass tries to prune statements from the program. A certain number of statements are chosen at random by a `Collector` which is a subclass of an `Inspector`. Then these are fed to a `Pruner` which is a subclass of a `Transform`, which actually prunes the statements from the program tree. We start with a very large number of statements to prune, and then follow a AIMD, if we were successful in our attempt, i.e the exit code of the program remained the same, i.e the bug still exists in the program, we increase the bank by 2 statements otherwise we half the size of the bank.



## Expression pruning

### Required preceding passes 

- None

### Parameters 
- `PRUNE_ITERS`     : The number of times the expressions pruner would run through the program.
- `NO_CHNG_ITERS`   : If the program remains the same for this number of iterations then we assume the phase is completed and move to the next pass.

### Description

This pass now tries to prune the individual expressions inside the statements. We have defined how the pass would handle and prune different type of expressions, for example, given a operator, we try to randomly pick a side and see if the bug remains. Given a shift, we simplify it to the lvalue. There are still many expressions that we haven't looked at yet, for example a `Range` or a `Slice`.


## Boolean pruning

### Required preceding passes 

- None

### Parameters 
- `PRUNE_ITERS`     : The number of times the boolean pruner would run through the program.
- `NO_CHNG_ITERS`   : If the program remains the same for this number of iterations then we assume the phase is completed and move to the next pass.

### Description

This pass now tries to prune and simplify boolean expressions. Given a boolean expression we try to replace it with a random boolean literal and see if the bug remains.

# Compiler pruning

These passes require some generic passes : 

```
ResolveReferences,
ConstantFolding,
InstantiateDirectCalls,
TypeInference
```

## Replace variables

### Required preceding passes 

- Generic Passes once
- `ResolveReferences and TypeInference` every pass

### Parameters 
- None

### Description

This pass tries to replace each variable with a literal and checks if the bug remained, for example it might turn the expressions `aVar + bVar` to `16w0 + 10w0` depending upon the bitwidth of the variables. We do this to aid the subsquent pass (i.e Extended unused declarations) which tries to remove all unused decelarations from the program, so this pass frees up more variables to be removed by the next pass.

## Extended remove unused declarations 

### Required preceding passes 

- Generic Passes once
- Replace variables

### Parameters 
- None

### Description

This is a subclass of `P4::RemoveUnusedDeclarations` where we try to agressively remove all unused declarations as opposed to the conserative approach followed by p4c since we don't care about semantic preserving but rather only about saving the bug. 

--- 

## Current Order of the applied passes 



- Statement pruning
- Expression pruning
- Boolean expression pruning
- Generic passes // this starts the compiler pruning phase
- Replace variables
- Extended remove unused declarations

