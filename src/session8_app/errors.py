"""Custom exceptions for the application."""


class AppError(Exception):
    """Base application error."""


class ValidationError(AppError):
    """Raised when user input is invalid."""


class DataAccessError(AppError):
    """Raised when data cannot be loaded from external sources."""
