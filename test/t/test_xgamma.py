import pytest


class Test(object):

    @pytest.mark.complete("xgamma -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("xgamma -gam")
    def test_gam(self, completion):
        assert completion.list == ["-gamma"]
        assert completion.line.endswith(" ")
