Virtual Environment Notes — pip vs uv

Steps Followed

Created a virtual environment with ` python -m venv venv`
Activated it with source  `venv/bin/activate`
Installed requests using ` pip install requests`
Deleted the environment with  `rm -rf venv`
Recreated it using `uv venv` and activated with `source .venv/bin/activate`
Installed the same package using `uv pip install` requests
Generated requirements.txt using `uv pip freeze > requirements.txt`

pip vs uv — Comparison
Environment creation

pip → `python -m venv venv`
uv → `uv venv`

Install command

pip → `pip install requests`
uv → `uv pip install requests`

Speed

pip → noticeably slower
uv → much faster

Built into Python

pip → yes, no extra install needed
uv → no, requires `pip install uv` first

Folder created

pip → `venv/`
uv → `.venv/`

Command compatibility

pip → standard
uv → same syntax as pip, just prefixed with `uv`