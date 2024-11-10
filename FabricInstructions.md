## Fabric Project
https://github.com/WeiJiHsiao/pbwsl

## Fabric Installation
### Source
https://github.com/danielmiessler/fabric
### Install Fabric directly from the repo
go install github.com/danielmiessler/fabric@latest
### Run the setup to set up your directories and keys
fabric --setup

## Alternatives for pbpaste
My own go version for all platforms: https://github.com/Taikun/pbpaste
pbcopy / pbpaste en Windows WSL: https://github.com/WeiJiHsiao/pbwsl
pbcopy | pbpaste en Linux: https://superuser.com/questions/28832...
### Alternartives using Aliases
On Windows, you can use the PowerShell command Get-Clipboard from a PowerShell command prompt. If you like, you can also alias it to pbpaste. If you are using classic PowerShell, edit the file ~\Documents\WindowsPowerShell\.profile.ps1, or if you are using PowerShell Core, edit ~\Documents\PowerShell\.profile.ps1 and add the alias,
```poweshell
Set-Alias pbpaste Get-Clipboard
```
On Linux, you can use xclip -selection clipboard -o to paste from the clipboard. You will likely need to install xclip with your package manager. For Debian based systems including Ubuntu,

```bash
sudo apt update
sudo apt install xclip -y
```
You can also create an alias by editing ~/.bashrc or ~/.zshrc and adding the alias,

```bash
alias pbpaste='xclip -selection clipboard -o'
```

## Configurar fabric
```bash
./fabric --setup
```

## Aquí están los ficheros de configuración
```bash
/home/taikun/.config/fabric
```

## PAra extraer la sabíduria de un vídeo:
```bash
./fabric -y "https://www.youtube.com/watch?v=pVo8RNGr0hc" --stream --pattern extract_wisdom -g es
```

## Resumen:
```bash
./fabric -y "https://www.youtube.com/watch?v=pVo8RNGr0hc" --stream --pattern summarize -g es
```

## Ver los patterns:
```bash
./fabric -l
```

## Escribe tweet largo:
```bash
pbpaste | ./fabric -p tweet -g es
```

## Mejorar un prompt
```bash
echo "Para que me genere la información de Youtube" | fabric -sp improve_prompt
```

```bash
./fabric -y "https://youtu.be/V-62gAoEWqw"--stream --pattern extract_wisdom -g es
```