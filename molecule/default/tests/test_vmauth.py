def test_account_present(host):
    group = host.group("vmauth")
    user = host.user("vmauth")
    assert group.exists
    assert user.exists

def test_directory(host):
    dirs = [
        "/etc/vmauth",
        "/var/lib/vmauth",
    ]

    for folder in dirs:
        d = host.file(folder)
        assert d.is_directory
        assert d.user == "vmauth"
        assert d.group == "vmauth"
        assert oct(d.mode) == "0o755"

def test_config_file(host):
    config = host.file("/etc/vmauth/config.yml")
    assert config.exists
    assert config.user == "vmauth"
    assert config.group == "vmauth"
    assert oct(config.mode) == "0o644"

def test_service_file(host):
    service_file = host.file("/etc/systemd/system/vmauth.service")
    assert service_file.exists

def test_service(host):
    service = host.service("vmauth")
    assert service.is_enabled
    assert service.is_running

def test_socket(host):
    socket = host.socket("tcp://0.0.0.0:8429")  # Todo change port
    assert socket.is_listening
