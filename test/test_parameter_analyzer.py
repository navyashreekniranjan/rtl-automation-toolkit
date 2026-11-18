from rtl_toolkit.parameter_analyzer import analyze_parameters

def test_parameter_extraction(tmp_path):
    rtl_file = tmp_path / "counter.v"
    rtl_file.write_text("""
    module counter #( 
        parameter WIDTH = 8,
        parameter MAX_COUNT = 100
    )(
        input clk);
    endmodule
    """)

    result = analyze_parameters(rtl_file)

    assert result == [
        {"name": "WIDTH", "value": "8"},
        {"name": "MAX_COUNT", "value": "100"}
    ]


def test_parameter_inside_module_body(tmp_path):
    rtl_file = tmp_path /"counter.v"
    rtl_file.write_text("""
    module counter(
        input clk
        );

        parameter WIDTH = 8;

    endmodule
    """)

    result = analyze_parameters(rtl_file)

    assert result == [
        {"name": "WIDTH", "value":"8"}
    ]

def test_multiple_parameters_without_repeated_keyword(tmp_path):
    rtl_file = tmp_path / "counter.v"
    rtl_file.write_text("""
        module counter(
            input clk
            );
            
            parameter WIDTH = 8, DEPTH = 16;
        """)
    result = analyze_parameters(rtl_file)

    assert result == [
        {"name":"WIDTH" , "value":"8"},
        {"name":"DEPTH", "value": "16"}
    ]