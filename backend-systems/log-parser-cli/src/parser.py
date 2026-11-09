import sys
import re
from pathlib import Path
from collections import Counter
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

LOG_PATTERN = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>INFO|WARNING|ERROR)\s+"
    r"\[(?P<module>\w+)\]\s+"
    r"(?P<message>.*?)"
    r"(?: - status: (?P<status>\d+))?$"
)

def parse_log_file(file_path: str):
    path = Path(file_path)

    if not path.is_file():
        console.print(f"[bold red]Erro:[/bold red] O arquivo '{file_path}' não foi encontrado.")
        sys.exit(1)

    errors = []
    modules_counter = Counter()

    with open(path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, 1):
            match = LOG_PATTERN.search(line.strip())
            if match:
                data = match.groupdict()
                level = data["level"]
                status = data["status"]

                if level in ["ERROR", "WARNING"]:
                    modules_counter[data["module"]] += 1

                if level == "ERROR" or (status and status.startswith(("4", "5"))):
                    data["line_number"] = line_number
                    errors.append(data)

    console.print(Panel.fit("[bold blue]DIAGNÓSTICO DE INCIDENTES - LOG PARSER CLI[/bold blue]"))
    console.print(f"Arquivo analisado: [bold yellow]{path.name}[/bold yellow]\n")

    table = Table(title="Ocorrências Críticas Detectadas", show_lines=True)
    table.add_column("Linha", justify="center", style="cyan")
    table.add_column("Data/Hora", style="dim")
    table.add_column("Nível", justify="center")
    table.add_column("Módulo", style="bold magenta")
    table.add_column("Mensagem de Erro", style="white")
    table.add_column("Status", justify="center", style="bold yellow")

    for err in errors:
        level_color = "red" if err["level"] == "ERROR" else "yellow"
        table.add_row(
            str(err["line_number"]),
            err["timestamp"],
            f"[{level_color}]{err['level']}[/{level_color}]",
            err["module"],
            err["message"],
            err["status"] or "N/A"
        )

    console.print(table)

    console.print("\n[bold]Resumo de Afetados por Módulo:[/bold]")
    for mod, count in modules_counter.items():
        console.print(f" • [cyan]{mod}[/cyan]: {count} falhas")

if __name__ == "__main__":
    target_file = sys.argv[1] if len(sys.argv) > 1 else "../data/sample.log"
    parse_log_file(target_file)
