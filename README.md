# SERPRO

Integração para consultas no servidor da `SERPRO` Brasil

Inicialmente será possível fazer consulta de `CPF's` e  `CNPJ's` nas bases federais. As consultasa base da `SERPRO` são pagas e você precisará comprar uma licença mensal para consulta.

Este pacote não é oficial, mas visa facilitar as consultas de `CPF` e `CNPJ` para os desenvolvedores brasileiros.

Sinta-se a vontade para ajudar abrindo `issues` e `pull requests` com melhorias e sugestões.

---

Você precisará configurar os dados básicos de conexão.

```python
{
    "consumer_key": "JT8.....c6a",
    "consumer_secret": "MOy...K1r"
}
```

---
## Dependências

Este pacote usa um validador de `CPF` e `CNPJ` a fim de evitar mandar para consulta na `SERPRO` qualquer dado inválido, evitando pagamento de valores desnecessários.

```txt
requests==2.19.1
pycpfcnpj==1.5
```