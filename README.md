---
description: Integração com API federal para consulta de CPF e CNPJ
---

# SERPRO

Inicialmente será possível fazer consulta de `CPF's` e  `CNPJ's` nas bases federais. As consultas a base da `SERPRO` são pagas e você precisará comprar uma licença mensal para consulta.

Este pacote não é oficial, mas visa facilitar as consultas de `CPF` e `CNPJ` para os desenvolvedores brasileiros.

[Ir para o respositório](https://github.com/rfschubert/schubert_serpro)

Sinta-se a vontade para ajudar abrindo `issues` e `pull requests` com melhorias e sugestões.

Você precisará configurar os dados básicos de conexão.

```python
{
    "consumer_key": "JT8.....c6a",
    "consumer_secret": "MOy...K1r"
}
```

### Dependências

Este pacote usa um validador de `CPF` e `CNPJ` a fim de evitar mandar para consulta na `SERPRO` qualquer dado inválido, evitando pagamento de valores desnecessários.

> {% code-tabs %}
> {% code-tabs-item title="requirements.txt" %}
> ```text
> requests==2.19.1
> pycpfcnpj==1.5
> ```
> {% endcode-tabs-item %}
> {% endcode-tabs %}

