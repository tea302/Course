import pytest

from Course.utils import *

class TestGetPostByPk:
    def test_get_post_by_pk_1(self):
        assert get_post_by_pk(1) == 1, "Ошибка для поста № 1"

    def test_get_post_by_pk_2(self):
        assert get_post_by_pk(2) == 2, "Ошибка для поста № 2"