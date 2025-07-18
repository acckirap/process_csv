class CSVProcessingError(Exception):
    """Базовая ошибка при обработке CSV."""


class InvalidFilterSyntax(CSVProcessingError):
    """Ошибка в синтаксисе фильтрации."""


class InvalidAggregationSyntax(CSVProcessingError):
    """Ошибка в синтаксисе агрегации."""


class NonNumericAggregationError(CSVProcessingError):
    """Аггрегация поддерживается только для числовых полей."""


class FileOpenError(CSVProcessingError):
    """Ошибка при открытии файла."""
