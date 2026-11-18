from rtl_toolkit.duplicate_checker import duplicate_checker

def test_duplicate_module(tmp_path):
    rtl_file = tmp_path / "counter.v"
    rtl_file.write_text("module counter; endmodule")

    rtl_file_2 = tmp_path / "counter_copy.v"
    rtl_file_2.write_text("module counter; endmodule")

    duplicates = duplicate_checker([rtl_file, rtl_file_2])

    assert "counter" in duplicates
    assert len(duplicates["counter"]) == 2


def test_no_duplicate_module(tmp_path):
    rtl_file = tmp_path / "adder.v"
    rtl_file.write_text("module adder; endmodule")

    duplicates = duplicate_checker([rtl_file])

    assert duplicates == {} 