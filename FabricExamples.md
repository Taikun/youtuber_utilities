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