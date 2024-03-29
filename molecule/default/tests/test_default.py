def test_binaries(host):
    binaries = [
        "/usr/local/bin/vmagent-prod",
        "/usr/local/bin/vmalert-prod",
        "/usr/local/bin/vmalert-tool-prod",
        "/usr/local/bin/vmbackup-prod",
        "/usr/local/bin/vmctl-prod",
        "/usr/local/bin/vmrestore-prod",
    ]
    for binary in binaries:
        assert host.file(binary).exists
        assert host.file(binary).is_file
        assert host.file(binary).mode == 0o755

def test_tarball(host):
    tarball = host.file("/tmp/vmutils-linux.tar.gz")
    extract = host.file("/tmp/vmutils")
    assert not tarball.exists
    assert not extract.exists
