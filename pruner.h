#ifndef _P4PRUNER_H
#define _P4PRUNER_H

#include "ir/ir.h"


namespace P4PRUNER{

    class Pruner : public Transform{
    public:
        Pruner(){
            setName("Pruner");
        }

        IR::Node* preorder(IR::AssignmentStatement *s);

    };
}

#endif /* _P4PRUNER_H */
