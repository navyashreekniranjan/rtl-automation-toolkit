module ports_example (
    input [7:0] data_a,
    input [7:0] data_b,
    output [7:0] result
);

    

    assign result = data_a ^ data_b;

endmodule
