# Es mejor ejecutarlo desde Linux

Sí, en Linux **Whisper** debería funcionar sin problemas, ya que sus dependencias suelen estar mejor soportadas en este sistema operativo. Linux proporciona soporte nativo para `libc`, que es la biblioteca estándar de C que Whisper utiliza y que suele estar ausente o ser incompatible en algunas configuraciones de Windows.

### Pasos para Usar Whisper en Linux

1. **Configurar Whisper en Linux**:
   - Instala Whisper ejecutando:
     ```bash
     pip install git+https://github.com/openai/whisper.git
     ```

2. **Instalar FFmpeg** (si no lo tienes instalado):
   Whisper utiliza FFmpeg para manejar archivos de audio y video, así que asegúrate de instalarlo:
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

3. **Ejecutar el Código**:
   Una vez configurado Whisper y FFmpeg en Linux, puedes utilizar el mismo código que ya tienes para procesar el archivo de video en tu sistema Linux. 

### Ejemplo de Comando para Ejecutar el Script

Si tu archivo está en una unidad montada en `/media`, el comando sería algo como:

```bash
python genera-from-file.py "/media/Usuario/YoutubeVideos/ActualizaciónGATrueNAS.mp4"
```

Esta configuración debería funcionar sin problemas en Linux y podrás transcribir tus videos locales usando Whisper.
