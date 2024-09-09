"""

 Pseudoinstruction Handler

 Helper functions for the CSSE232 Assembler. 
 Processes assembly code to replace pseudoinstructions with 
 core instructions.

 VVV Put your name here VVV

 Author: Robert J Williamson, 2024

"""

import assembler

def get_pseudoinstruction_defs():
    """Returns a dictionary mapping pseudoinstruction names to methods 
        that will translate a given pseudoinstruction call to a list of 
        core instructions. Each of these function should have the 
        signature: `func(inst_string, line_num)`"""
    pseudo_dict = {"double":double,
                   "diffsums":diffsums,
                   "push":push,
                   "li":li,
                   "beqz":beqz,
                   "jalif":jalif}

    return pseudo_dict

##############
#
# Individual definitions for pseudoinstructions
#
# Each of these functions should take in a string (e.g. "double t0, t1")
# and the line number from the original code that is being translated.
# The line number is mostly for error tracing, but you may find it
# useful for some pseudoinstructions.
##############

def double(inst, num):
    """Takes a string representing a call to the `double` pseudoinstruction. 
        Returns a list of strings containing the calls for the core instructions 
        which implement this pseudoinstruction.

        Behavior:
            `double r1, r2 -> Reg[r1] = 2 * r2`
        """

    #TODO: Lab 2 - implement this

    raise NotImplementedError

def diffsums(inst, num):
    """Takes a string representing a call to the `diffsums` pseudoinstruction. 
        Returns a list of strings containing the calls for the core instructions 
        which implement this pseudoinstruction.

        Behavior:
            `diffsums r1, r2, r3, r4, r5 -> Reg[r1] = (r2 + r3) - (r4 + r5)`

        Note: the same register may be used multiple times in this instruction, e.g.:
            `diffsums t0, t0, t1, t0, t2`
        """

    #TODO: Lab 2 - implement this

    raise NotImplementedError

def push(inst, num):
    """Takes a string representing a call to the `push` pseudoinstruction. 
        Returns a list of strings containing the calls for the core instructions 
        which implement this pseudoinstruction.

        Behavior:
            `push r1 -> sp = sp-4 ; Mem[sp] = r1`
        """

    #TODO: Lab 2 - implement this

    raise NotImplementedError

def li(inst, num):
    """Takes a string representing a call to the `li` pseudoinstruction. 
        Returns a list of strings containing the calls for the core instructions 
        which implement this pseudoinstruction.

        Behavior:
            `li rd, imm -> rd = imm`

        You should assume that imm can be up to 32 bits.

        Recall that the assembler assumes all immediates are in decimal.
        """

    #TODO: Lab 2 - implement this

    raise NotImplementedError


def beqz(inst, num):
    """Takes a string representing a call to the `beqz` pseudoinstruction. 
        Returns a list of strings containing the calls for the core instructions 
        which implement this pseudoinstruction.

        Behavior:
            `beqz r1, LABEL -> if(r1 == 0) PC = LABEL`

        You can assume LABEL should fit into 12 bits.
        """

    #TODO: Lab 2 - implement this

    raise NotImplementedError

def jalif(inst, num):
    """Takes a string representing a call to the `jalif` pseudoinstruction. 
        Returns a list of strings containing the calls for the core instructions 
        which implement this pseudoinstruction.

        Behavior:
            `jalif r1, r2, LABEL -> if(r1 == r2) {ra = PC+4; PC=LABEL}`

        You can assume LABEL should fit into 20 bits.

        Note: Make sure this code works if a program has multiple `jalif` instructions...
        """

    #TODO: Lab 2 - implement this

    raise NotImplementedError

##############
#
# Helper methods
#
##############

def replace_all(sym, val, slist):
    """Replaces all instances of `sym` with `val` in each string in the list `slist`."""
    new_slist = []
    for s in slist:
        new_slist.append(s.replace(sym, str(val)))
    return new_slist
