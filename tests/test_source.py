import pytest

# Тестирование Source

# Получение верного типа Source при указании URL

# Exception при указании не валидного URL

# Скачивание источника

# Удаление файлов после использования

# Получение дескриптора на файл

# gitsource regexp
from source import GitSource
from tests.parametrize_set import GIT_URLS


@pytest.mark.parametrize('url,result', GIT_URLS)
def test_gitsouce_regexp(url, result):
    assert GitSource.match_source_url(url) is result

