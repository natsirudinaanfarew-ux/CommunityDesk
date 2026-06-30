# === Stage 32: Add pagination helpers for long console output ===
# Project: CommunityDesk
def paginate_output(text, max_lines=15):
    """Yields chunks of text limited by line count."""
    lines = text.splitlines()
    for i in range(0, len(lines), max_lines):
        yield '\n'.join(lines[i:i+max_lines]) + ('\n' if i + max_lines < len(lines) else '')

def format_table(headers, rows, width=80):
    """Renders a simple ASCII table from headers and list of row lists."""
    col_widths = [min(len(str(h)), 15) for h in headers]
    for r in rows:
        if len(r) < len(headers): r.extend([''] * (len(headers) - len(r)))
        elif len(r) > len(headers): col_widths[:len(headers)] = [max(cw, len(str(v))) for cw, v in zip(col_widths, r)]
    sep = '+' + '+'.join('-' * w for w in col_widths) + '+'
    header_line = '|' + '| '.join(h.ljust(w) for h, w in zip(headers, col_widths)) + '|'
    row_lines = ['|'] + [('| ' + str(v).ljust(w) if v is not None else ('  ').ljust(w)) for v, w in zip(r, col_widths)] + ['|']
    return sep + '\n' + header_line + '\n' + sep + '\n'.join(row_lines) + '\n' + sep

def limit_output(text, max_chars=200):
    """Truncates text with ellipsis if it exceeds character limit."""
    if len(text) <= max_chars: return text
    end = text.rfind(' ', 0, max_chars - 3)
    return text[:end] + '...'

def chunk_list(lst, size=10):
    """Yields sublists of fixed size from the input list."""
    for i in range(0, len(lst), size): yield lst[i:i+size]
