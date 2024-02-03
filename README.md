# Python Web Scraping Script

Este script Python foi desenvolvido para realizar scraping em um site específico e capturar informações da página, incluindo o código-fonte e uma captura de tela. Antes de executar o script, é altamente recomendável utilizar uma VPN para proteger sua identidade online.

## Requisitos

- Biblioteca Selenium
- Driver do Chrome

```bash
pip install selenium requests
```

Certifique-se de ter o driver do Chrome instalado e configurado corretamente. Você pode baixar o driver em [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/).

## Utilização

1. Execute o script `web_scraping.py` em um ambiente Python.
2. Certifique-se de estar utilizando uma VPN para ocultar seu IP durante as solicitações.
3. O script fará uma solicitação GET para a URL especificada e salvará o código-fonte da página em um arquivo chamado `source_code.txt`.
4. Em seguida, o script iniciará um navegador Chrome em modo headless, acessará a URL (mesmo que não seja válida) e capturará uma screenshot, salvando-a como `screenshot.png`.

**Atenção**: O uso indevido deste script para scraping de sites pode violar os termos de serviço do site-alvo. Certifique-se de ter permissão adequada antes de usar este script em qualquer site.

## Notas Importantes

- Utilizar uma VPN é altamente recomendado para preservar a privacidade do usuário.
- Este script é fornecido apenas para fins educacionais e não deve ser usado para atividades maliciosas.
- Respeite os termos de serviço do site que você está acessando e certifique-se de ter permissão para realizar scraping.

**Autor:** Pit

**Contato:** devpit@proton.me
