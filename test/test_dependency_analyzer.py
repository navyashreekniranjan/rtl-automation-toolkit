from rtl_toolkit.dependency_analyzer import analyze_dependencies

def test_simple_dependency(tmp_path):
    adder_file = tmp_path / "adder.v"
    adder_file.write_text("module adder; endmodule")

    register_file = tmp_path / "register.v"
    register_file.write_text("module register; endmodule")

    top_file = tmp_path / "top.v"
    top_file.write_text("""
        module top; 
            adder u_adder();
            register u_register();
            fifo u_fifo();
        endmodule
        """)

    dependencies = analyze_dependencies([
        adder_file,
        register_file,
        top_file
    ])

    assert dependencies["dependencies"] == {
        "adder": [],
        "register": [],
        "top": ["adder", "register", "fifo"]
    }

    assert dependencies["unresolved_modules"] == ["fifo"]