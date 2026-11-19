module invalid_example(
    input clk,
    input reset,
    output reg data
);
always@(posedge clk or posedge reset)begin
    if(reset)
        data <= 1'b0;
    else
         data <= 1'b1;
end
endmodule
