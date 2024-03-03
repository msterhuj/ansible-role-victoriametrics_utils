def test_account_present(host):
    group = host.group("vmagent")
    user = host.user("vmagent")
    assert group.exists
    assert user.exists

def test_directory(host):
    # check owner and permission 0755
    dirs = [
        "/etc/vmagent",
        "/var/lib/vmagent",
    ]

    for folder in dirs:
        d = host.file(folder)
        assert d.is_directory
        assert d.user == "vmagent"
        assert d.group == "vmagent"
        assert oct(d.mode) == "0o755"

def test_config_file(host):
    config = host.file("/etc/vmagent/vmagent.yml")
    assert config.exists
    assert config.user == "vmagent"
    assert config.group == "vmagent"
    assert oct(config.mode) == "0o644"

def test_service_file(host):
    service_file = host.file("/etc/systemd/system/vmagent.service")
    assert service_file.exists

def test_service(host):
    service = host.service("vmagent")
    assert service.is_enabled
    assert service.is_running

def test_socket(host):
    socket = host.socket("tcp://0.0.0.0:8429")
    assert socket.is_listening
