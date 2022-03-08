import pytest
from demo_user import demo_database1

class TestEmployee:
    @classmethod
    def setup_class(cls):
        print("\nSetting Up Class")

    @classmethod
    def teardown_class(cls):
        print("\nTearing Down Class")

    @pytest.fixture
    def setup(self):
        obj = demo_database1()
        return obj

    def test_db_connection(self):
        with pytest.raises(Exception):
            self.setup.get_connection()

    def test_engine(self):
        with pytest.raises(Exception):
            self.setup.get_engine()


