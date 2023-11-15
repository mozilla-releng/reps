from typing import Any, Callable, Dict


CookiecutterContext = Dict[str, Any]
HookFn = Callable[[CookiecutterContext], None]
