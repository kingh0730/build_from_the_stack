# Verilog

Design me a digital circuit in Verilog that takes in a 4-bit number and outputs
a 4-bit number that is the 2's complement of the input number.

```verilog
module twos_complement(
    input [3:0] a,
    output [3:0] b
    );
    assign b = ~a + 1;
endmodule
```
