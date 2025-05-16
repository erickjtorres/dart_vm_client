def test_import():
    """Test that the package can be imported without errors."""
    try:
        import dart_vm_client
        from dart_vm_client import DartVmClient
        assert True
    except ImportError:
        assert False, "Failed to import dart_vm_client package" 