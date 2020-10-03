#ifndef _PRUNER_H
#define _PRUNER_H

#include "ir/ir.h"


namespace PRUNER{

    class Pruner : public Transform{
    public: 
        Pruner(){
            setName("Pruner");
        }

        IR::Node* preorder(IR::AssignmentStatement *s);

    };
}

#endif