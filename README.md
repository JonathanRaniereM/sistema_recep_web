# Sistema de Recepção Web Integrado com Terminal Eletrônico de Assinatura

<img width="800" src="https://raw.githubusercontent.com/JonathanRaniereM/sistema_recep_web/main/sistema_recep_front/src/views/assets/images/demonstrativo.gif">

## Sobre o Projeto

Este projeto apresenta uma solução inovadora de sistema de recepção web, desenvolvido com o foco em eficiência, segurança e conformidade com a legislação vigente. A principal funcionalidade do sistema é sua integração com o terminal eletrônico de assinatura da Topaz Systems, proporcionando uma experiência de uso ágil e segura para os usuários.

### Características Principais

- **Integração com Terminal Eletrônico de Assinatura**: O sistema incorpora a avançada tecnologia de assinatura eletrônica da Topaz Systems, garantindo autenticação robusta e segura das assinaturas. Esse processo não apenas otimiza a eficácia da coleta de assinaturas mas também assegura a integridade e a verificabilidade dos dados assinados, essenciais para transações e consentimentos digitais.
- 
- **Rigorosa Adesão à LGPD**: A arquitetura e operação do sistema são meticulosamente alinhadas com as disposições da Lei Geral de Proteção de Dados (LGPD), garantindo uma governança de dados impecável. Desde a coleta até o tratamento de dados pessoais, o sistema adota padrões de segurança de primeira linha para proteger as informações dos usuários, assegurando tanto a conformidade legal quanto a confiança dos usuários.
  
- **Segurança de Dados Através de Armazenamento MySQL**: Utilizamos um repositório de dados MySQL, configurado com protocolos de segurança avançados, incluindo criptografia de dados em repouso e em trânsito, bem como autenticação em duas etapas. Essas medidas são projetadas para fornecer uma camada robusta de proteção contra acessos não autorizados, mitigando riscos de violações de dados e garantindo a integridade e a confidencialidade dos dados armazenados.
  
- **Sincronização em Tempo Real com Redis Server e Django Channels**: O emprego do Redis Server, em sinergia com Django Channels, permite uma comunicação em tempo real eficiente através de WebSockets. Essa configuração assegura que quaisquer atualizações de dados sejam imediatamente propagadas por todas as instâncias conectadas, garantindo uma experiência de usuário contínua e uma sincronização de dados impecável entre os terminais de serviço.

- **Geração de Termo de Consentimento em PDF com Assinatura Eletrônica**: Como parte do nosso compromisso com a conformidade legislativa e segurança dos dados, o sistema automaticamente gera um termo de consentimento em PDF, incorporando as informações e a assinatura eletrônica do visitante. Esta funcionalidade não só simplifica o processo de obtenção e registro do consentimento em conformidade com a LGPD, mas também fornece um documento legalmente admissível que reforça a transparência e a segurança jurídica no armazenamento de dados dos visitantes.

## Motivação

Portanto, a concepção deste sistema transcende a simples automação de processos; trata-se de uma resposta estratégica para modernizar a gestão de visitantes em uma instituição governamental, assegurando que ela possa cumprir suas funções de maneira segura, eficiente e transparente



## Como Utilizar

[Inclua instruções específicas sobre como utilizar o sistema, como configurá-lo, quais são os requisitos, etc.]

## Contribuição

Sua contribuição é bem-vinda! Se você tem interesse em contribuir para o projeto, por favor, leia o arquivo CONTRIBUTING.md para mais informações sobre como proceder.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE.md para mais detalhes.

---

Para mais informações, por favor, entre em contato conosco através de [inserir meio de contato].

Agradecemos seu interesse e apoio ao nosso projeto!
