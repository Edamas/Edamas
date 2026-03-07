# Git Avançado: Funcionamento Interno e Prática - EaD

<p align="center">
  <img alt="USP IMECC" src="https://img.shields.io/badge/USP-IMECC-8C1515?style=for-the-badge&logo=google-scholar&logoColor=white">
  <img alt="Extensão" src="https://img.shields.io/badge/Curso%20de%20Extens%C3%A3o-Difus%C3%A3o-0A66C2?style=for-the-badge">
  <img alt="Período" src="https://img.shields.io/badge/Per%C3%ADodo-12%20a%2030%20jan%202026-444444?style=for-the-badge">
  <img alt="Carga horária" src="https://img.shields.io/badge/Carga%20hor%C3%A1ria-13h30-2E7D32?style=for-the-badge">
</p>

<p align="center">
  <img alt="Git" src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white">
  <img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
  <img alt="GitLab" src="https://img.shields.io/badge/GitLab-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white">
  <img alt="Version Control" src="https://img.shields.io/badge/Version%20Control-Git%20Internals-1F4B99?style=for-the-badge">
</p>

---

## Resumo

Curso de extensão universitária realizado na Universidade de São Paulo, com foco no funcionamento interno do Git e no uso prático de recursos avançados de versionamento. O curso foi além do uso cotidiano de `clone`, `pull`, `commit` e `push`, aprofundando a estrutura de objetos, referências, merges, reescrita de histórico, recuperação de dados e estratégias de colaboração.

Para mim, o valor principal deste curso foi transformar um uso bastante frequente de Git, GitHub e GitLab em entendimento estrutural. Em vez de operar o Git apenas como ferramenta de rotina, passei a enxergar com mais clareza o banco de objetos, o papel das referências, os limites da reescrita de histórico e os mecanismos que tornam possíveis recuperação, auditoria, merge e investigação de problemas.

---

## Certificado

| Recurso | Acesso |
| --- | --- |
| Certificado local | [Visualizar PDF](./certificado.pdf) |
| Certificado para download | [Baixar PDF](https://raw.githubusercontent.com/Edamas/Edamas/main/assets/certificados/USP/usp-git-avancado-2026/certificado.pdf) |
| Certificado oficial USP | [Baixar pelo Apolo](http://uspdigital.usp.br/apolo/extDiplomaBaixar.jsp?codpubmtr=A1BB3AFBE0BA&nomsis=Apolo&codund=45&codcurceu=450400304&codedicurceu=25001&numseqofeedi=1) |
| Programa oficial | [Visualizar PDF](./programa-oficial.pdf) |
| Programa para download | [Baixar PDF](https://raw.githubusercontent.com/Edamas/Edamas/main/assets/certificados/USP/usp-git-avancado-2026/programa-oficial.pdf) |
| Verificação de autenticidade | [USP WebDoc](http://uspdigital.usp.br/webdoc) |

> Código de controle do certificado: `MV68-JUYY-1NUS-XZUF`
>
> Frequência registrada: `100%`
>
> Área de conhecimento: `Ciência da Computação`

---

## Dados do Curso

| Campo | Informação |
| --- | --- |
| Instituição | Universidade de São Paulo (USP) |
| Unidade | Instituto de Matemática, Estatística e Ciência da Computação |
| Modalidade | Curso de Extensão Universitária em Difusão |
| Período | 12/01/2026 a 30/01/2026 |
| Carga horária | 13 horas e 30 minutos |
| Situação | Aprovado |
| Documento emitido em | 23/02/2026 |

---

## Conteúdo Programático Oficial

- história do Git
- revisão de conceitos básicos
- plumbing e porcelain
- hash
- objetos
- referências
- three-way merge
- estratégias de merge
- cherry-pick
- rebase básico
- tags anotadas
- packfile
- reflog
- diff
- stash
- remotes
- boas práticas de commit
- reescrita de histórico
- pathspecs
- Git como ferramenta de debug e busca
- submódulos
- subtrees
- ferramentas para grandes repositórios
- `.gitignore`
- atributos
- hooks

### Tópicos que se destacaram no estudo prático

- banco de objetos do Git: `blob`, `tree`, `commit` e `tag`
- referências e ponteiros como `HEAD`, branches e tags
- diferença entre comandos de alto nível e baixo nível
- `merge`, `rebase`, `cherry-pick` e suas implicações no histórico
- `reflog`, `fsck`, `bisect`, `blame`, `grep` e `log` como apoio à recuperação e investigação
- organização de repositórios maiores com `submodules`, `subtrees`, `packfile` e configurações

---

## Aplicação Prática

Este curso não gerou um repositório público ou uma aplicação publicada específica, como ocorreu em outros cursos. Ainda assim, o impacto prático foi direto no meu fluxo de trabalho com versionamento.

### Onde esse aprendizado se aplica

- uso mais consciente de `Git`, `GitHub` e `GitLab`
- leitura mais precisa do histórico e da integridade dos commits
- melhor tomada de decisão entre `merge`, `rebase`, `reset`, `restore` e `revert`
- maior segurança para recuperar trabalho perdido com `reflog` e `fsck`
- mais critério para organizar repositórios, commits, tags e remotes
- melhor capacidade de investigar bugs, regressões e mudanças no código com `bisect`, `blame`, `grep` e `log`

### Evidência de estudo

Ao longo do curso, mantive material de estudo próprio e exercícios locais sobre objetos, referências, busca, debug, configurações, merge, rebase e recuperação de dados. Embora esse material não tenha sido publicado como projeto independente, ele serviu como base concreta de fixação técnica.

---

## Meu Parecer

Na minha avaliação, este curso foi especialmente valioso porque aprofundou aquilo que costuma ficar invisível no uso cotidiano do Git. Mesmo para quem já trabalha bastante com Git, GitHub e GitLab, entender melhor o funcionamento interno muda a qualidade das decisões técnicas e reduz bastante o uso mecânico da ferramenta.

O aspecto mais forte do curso foi mostrar que Git não é apenas um conjunto de comandos, mas uma estrutura consistente de objetos, referências e operações sobre histórico. Isso ajuda a compreender melhor quando usar determinado fluxo, quando uma reescrita de histórico é aceitável, como recuperar estados perdidos e como depurar alterações de forma mais inteligente.

Também considero muito relevante o equilíbrio entre teoria e prática. O curso não ficou restrito à decoração de comandos: ele deu contexto conceitual para integridade, rastreabilidade, colaboração, recuperação e organização de histórico. Para meu portfólio, isso fortalece uma competência transversal importante, porque versionamento bem compreendido melhora a qualidade do trabalho em praticamente qualquer projeto de software, dados ou automação.

### Possíveis "ahás" deste curso

- o Git não guarda apenas diferenças entre arquivos; ele constrói uma base de objetos endereçada por conteúdo
- o histórico não é uma simples lista linear: ele é uma estrutura de referências e grafos de commits
- perder uma branch ou um commit nem sempre significa perder o trabalho, porque o Git registra muito mais rastros do que parece à primeira vista
- comandos aparentemente semelhantes carregam filosofias e riscos bem diferentes, como `merge`, `rebase`, `reset`, `restore` e `revert`

---

## Referências

- [Programa oficial do curso](./programa-oficial.pdf)
- [Certificado emitido pela USP](./certificado.pdf)
- [Pro Git](https://git-scm.com/book/en/v2)
- [Documentação oficial do Git](https://git-scm.com/docs)
