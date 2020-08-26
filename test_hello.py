from hello import marco
from click.testing import CliRunner
from hellocli import callmarco

def test_marco():
    assert "Polo" == marco("Marco")

def test_search():
    runner = CliRunner()
    result = runner.invoke(callmarco, ['--name', 'Marcos'])
    assert result.ext_code == 0
    assert 'No!' in result.output
