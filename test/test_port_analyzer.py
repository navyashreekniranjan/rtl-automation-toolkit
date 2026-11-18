from rtl_toolkit.port_analyzer import analyze_ports

def test_single_bit_ports(tmp_path):
    rtl_file = tmp_path / "example.v"
    rtl_file.write_text("""
    module example(
        input clk,
        output ready
    );
    endmodule
    """)

    result = analyze_ports(rtl_file)

    assert result == [
        {"name": "clk", "direction": "input", "width": 1},
        {"name": "ready", "direction": "output", "width": 1}
    ]

def test_vector_port_width(tmp_path):
    rtl_file = tmp_path / "example.v"
    rtl_file.write_text("""
    module example(
        input [7:0] data_a, data_b,
        input[3:0] data,
        output[7:0] result
    );
    endmodule
    """)

    result = analyze_ports(rtl_file)

    assert result == [
            {"name": "data_a", "direction": "input", "width": 8},
            {"name": "data_b", "direction": "input", "width": 8},
            {"name": "data", "direction": "input", "width": 4},
            {"name": "result", "direction": "output", "width": 8}
        ]

def test_inout_port(tmp_path):
    rtl_file = tmp_path / "example.v"
    rtl_file.write_text("""
    module example(
        inout[7:0] data,
    );
    endmodule
    """)

    result = analyze_ports(rtl_file)

    assert result == [
            {"name": "data", "direction": "inout", "width": 8}
        ]

def test_inherited_directions(tmp_path):
    rtl_file = tmp_path / "example.v"
    rtl_file.write_text("""
    module example(
        input clk, reset,
        output ready, valid
    );
    endmodule
    """)

    result = analyze_ports(rtl_file)

    assert result == [
            {"name": "clk", "direction": "input", "width": 1},
            {"name": "reset", "direction": "input", "width": 1},
            {"name": "ready", "direction": "output", "width": 1},
            {"name": "valid", "direction": "output", "width": 1}
        ]


def test_empty_module(tmp_path):
    rtl_file = tmp_path / "example.v"
    rtl_file.write_text("""
    module example;
    endmodule
    """)

    result = analyze_ports(rtl_file)

    assert result == []

def test_range_does_not_carry_over(tmp_path):
    rtl_file = tmp_path / "example.v"
    rtl_file.write_text("""
    module example(
        input [7:0] data_a, data_b,
        input ready
    );
    endmodule
    """)

    result = analyze_ports(rtl_file)

    assert result == [
        {"name": "data_a", "direction": "input", "width": 8},
        {"name": "data_b", "direction": "input", "width": 8},
        {"name": "ready", "direction": "input", "width": 1}
    ]