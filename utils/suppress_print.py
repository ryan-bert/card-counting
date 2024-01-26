import sys
import os


class SuppressPrint:
    """
    A context manager to suppress print output.

    Redirects sys.stdout to a file that discards all written data (os.devnull),
    effectively silencing print statements within its context. Restores
    the original stdout on exit.
    """

    def __enter__(self):
        """
        Enter the runtime context related to this object.

        The with statement will bind this method’s return value
        to the target(s) specified in the as clause of the statement,
        if any.

        Here, it redirects sys.stdout to null device (os.devnull) to suppress print statements.
        """
        self._original_stdout = sys.stdout  # Save the original stdout
        sys.stdout = open(os.devnull, 'w')  # Redirect stdout to null
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the runtime context and restore the original stdout.

        Parameters:
        - exc_type: Exception type (if any occurred)
        - exc_val: Exception value (if any occurred)
        - exc_tb: Exception traceback (if any occurred)
        """
        sys.stdout.close()  # Close the stream redirecting to null
        sys.stdout = self._original_stdout  # Restore the original stdout
