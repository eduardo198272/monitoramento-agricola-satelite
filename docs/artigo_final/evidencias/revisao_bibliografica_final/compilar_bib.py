from pathlib import Path
import json, shutil, subprocess
root=Path.cwd()
base=root/"docs/artigo_final"
tmp=Path("/tmp/opencode/auditoria-bibliografica")
project=tmp/"projeto"
build=tmp/"build_entrega"
project.mkdir(exist_ok=True)
build.mkdir(exist_ok=True)
manifest=json.loads((root/"docs/envio_professor/projeto_latex/MANIFESTO_SHA256.json").read_text())
for name in manifest:
    dst=project/name
    dst.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(base/name,dst)
result=subprocess.run(
    ["/tmp/opencode/tectonic","-X","compile","Relatorio_Final.tex",
     "--outdir",str(build),"--keep-logs","--keep-intermediates"],
    cwd=project,capture_output=True,text=True)
(build/"console.txt").write_text(result.stdout+result.stderr)
print(result.stdout+result.stderr)
raise SystemExit(result.returncode)
