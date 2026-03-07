# Git Avancado: Funcionamento Interno e Pratica - EaD

<p align="center">
  <img alt="USP IMECC" src="https://img.shields.io/badge/USP-IMECC-8C1515?style=for-the-badge&logo=google-scholar&logoColor=white">
  <img alt="Extensao" src="https://img.shields.io/badge/Curso%20de%20Extensao-Difusao-0A66C2?style=for-the-badge">
  <img alt="Periodo" src="https://img.shields.io/badge/Periodo-12%20a%2030%20jan%202026-444444?style=for-the-badge">
  <img alt="Carga horaria" src="https://img.shields.io/badge/Carga%20horaria-13h30-2E7D32?style=for-the-badge">
</p>

<p align="center">
  <img alt="Git" src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white">
  <img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
  <img alt="GitLab" src="https://img.shields.io/badge/GitLab-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white">
  <img alt="Version Control" src="https://img.shields.io/badge/Version%20Control-Git%20Internals-1F4B99?style=for-the-badge">
</p>

---

## Resumo

Curso de extensao universitaria realizado na Universidade de Sao Paulo, com foco no funcionamento interno do Git e no uso pratico de recursos avancados de versionamento. O curso foi alem do uso cotidiano de `clone`, `pull`, `commit` e `push`, aprofundando a estrutura de objetos, referencias, merges, reescrita de historico, recuperacao de dados e estrategias de colaboracao.

Para mim, o valor principal deste curso foi transformar um uso bastante frequente de Git, GitHub e GitLab em entendimento estrutural. Em vez de operar o Git apenas como ferramenta de rotina, passei a enxergar com mais clareza o banco de objetos, o papel das referencias, os limites da reescrita de historico e os mecanismos que tornam possiveis recuperacao, auditoria, merge e investigacao de problemas.

---

## Certificado

| Recurso | Acesso |
| --- | --- |
| Certificado local | [Visualizar PDF](./certificado.pdf) |
| Certificado para download | [Baixar PDF](https://raw.githubusercontent.com/Edamas/Edamas/main/assets/certificados/USP/usp-git-avancado-2026/certificado.pdf) |
| Certificado oficial USP | [Baixar pelo Apolo](http://uspdigital.usp.br/apolo/extDiplomaBaixar.jsp?codpubmtr=A1BB3AFBE0BA&nomsis=Apolo&codund=45&codcurceu=450400304&codedicurceu=25001&numseqofeedi=1) |
| Programa oficial | [Visualizar PDF](./programa-oficial.pdf) |
| Programa para download | [Baixar PDF](https://raw.githubusercontent.com/Edamas/Edamas/main/assets/certificados/USP/usp-git-avancado-2026/programa-oficial.pdf) |
| Verificacao de autenticidade | [USP WebDoc](http://uspdigital.usp.br/webdoc) |

> Codigo de controle do certificado: `MV68-JUYY-1NUS-XZUF`
>
> Frequencia registrada: `100%`
>
> Area de conhecimento: `Ciencia da Computacao`

---

## Dados do Curso

| Campo | Informacao |
| --- | --- |
| Instituicao | Universidade de Sao Paulo (USP) |
| Unidade | Instituto de Matematica, Estatistica e Ciencia da Computacao |
| Modalidade | Curso de Extensao Universitaria em Difusao |
| Periodo | 12/01/2026 a 30/01/2026 |
| Carga horaria | 13 horas e 30 minutos |
| Situacao | Aprovado |
| Documento emitido em | 23/02/2026 |

---

## Conteudo Programatico Oficial

- historia do Git
- revisao de conceitos basicos
- plumbing e porcelain
- hash
- objetos
- referencias
- three-way merge
- estrategias de merge
- cherry-pick
- rebase basico
- tags anotadas
- packfile
- reflog
- diff
- stash
- remotes
- boas praticas de commit
- reescrita de historico
- pathspecs
- Git como ferramenta de debug e busca
- submodulos
- subtrees
- ferramentas para grandes repositorios
- `.gitignore`
- atributos
- hooks

### Topicos que se destacaram no estudo pratico

- banco de objetos do Git: `blob`, `tree`, `commit` e `tag`
- referencias e ponteiros como `HEAD`, branches e tags
- diferenca entre comandos de alto nivel e baixo nivel
- `merge`, `rebase`, `cherry-pick` e suas implicacoes no historico
- `reflog`, `fsck`, `bisect`, `blame`, `grep` e `log` como apoio a recuperacao e investigacao
- organizacao de repositorios maiores com `submodules`, `subtrees`, `packfile` e configuracoes

---

## Aplicacao Pratica

Este curso nao gerou um repositorio publico ou uma aplicacao publicada especifica, como ocorreu em outros cursos. Ainda assim, o impacto pratico foi direto no meu fluxo de trabalho com versionamento.

### Onde esse aprendizado se aplica

- uso mais consciente de `Git`, `GitHub` e `GitLab`
- leitura mais precisa do historico e da integridade dos commits
- melhor tomada de decisao entre `merge`, `rebase`, `reset`, `restore` e `revert`
- maior seguranca para recuperar trabalho perdido com `reflog` e `fsck`
- mais criterio para organizar repositorios, commits, tags e remotes
- melhor capacidade de investigar bugs, regressões e mudancas no codigo com `bisect`, `blame`, `grep` e `log`

### Evidencia de estudo

Ao longo do curso, mantive material de estudo proprio e exercicios locais sobre objetos, referencias, busca, debug, configuracoes, merge, rebase e recuperacao de dados. Embora esse material nao tenha sido publicado como projeto independente, ele serviu como base concreta de fixacao tecnica.

---

## Meu Parecer

Na minha avaliacao, este curso foi especialmente valioso porque aprofundou aquilo que costuma ficar invisivel no uso cotidiano do Git. Mesmo para quem ja trabalha bastante com Git, GitHub e GitLab, entender melhor o funcionamento interno muda a qualidade das decisoes tecnicas e reduz bastante o uso mecanico da ferramenta.

O aspecto mais forte do curso foi mostrar que Git nao e apenas um conjunto de comandos, mas uma estrutura consistente de objetos, referencias e operacoes sobre historico. Isso ajuda a compreender melhor quando usar determinado fluxo, quando uma reescrita de historico e aceitavel, como recuperar estados perdidos e como depurar alteracoes de forma mais inteligente.

Tambem considero muito relevante o equilibrio entre teoria e pratica. O curso nao ficou restrito a decoracao de comandos: ele deu contexto conceitual para integridade, rastreabilidade, colaboracao, recuperacao e organizacao de historico. Para meu portifolio, isso fortalece uma competencia transversal importante, porque versionamento bem compreendido melhora a qualidade do trabalho em praticamente qualquer projeto de software, dados ou automacao.

### Possiveis "ahas" deste curso

- o Git nao guarda apenas diferencas entre arquivos; ele constroi uma base de objetos enderecada por conteudo
- o historico nao e uma simples lista linear: ele e uma estrutura de referencias e grafos de commits
- perder uma branch ou um commit nem sempre significa perder o trabalho, porque o Git registra muito mais rastros do que parece a primeira vista
- comandos aparentemente semelhantes carregam filosofias e riscos bem diferentes, como `merge`, `rebase`, `reset`, `restore` e `revert`

---

## Referencias

- [Programa oficial do curso](./programa-oficial.pdf)
- [Certificado emitido pela USP](./certificado.pdf)
- [Pro Git](https://git-scm.com/book/en/v2)
- [Documentacao oficial do Git](https://git-scm.com/docs)
